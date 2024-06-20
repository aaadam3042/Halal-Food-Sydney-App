import datetime
import os
import binascii
import csv
from flask_bcrypt import Bcrypt
from flask import Blueprint, Response, abort, jsonify, request
from flask_httpauth import HTTPBasicAuth
from io import TextIOWrapper, BytesIO, StringIO
from geoalchemy2 import functions as func
from model import Broadcast, db, User, FoodService, ServiceType, HalalStatus, Location, Contact, StatusHistory, ServiceSupplier, FoodServiceTagJunction, ServiceTag, Supplier

###
# File containing all the routes relating to operations by admins. Ensure that
# all routes have been implemented with security in mind.
#
# All routes in this file should have a url prefix of /api/admin
#
# Authentication details are sent in an auth field
###

auth = HTTPBasicAuth()
bcrypt = Bcrypt()

admin_bp = Blueprint("admin", import_name=__name__, url_prefix="/api/admin")


def init_bcyrpt(app):
    '''
    Initialise the bcrypt object
    '''
    bcrypt.init_app(app)


@auth.verify_password
def verify_password(email, password):
    '''
    Verify the password of the user
    '''
    db_user = User.query.filter_by(email=email).first()
    if (db_user == None):
        return False
    
    salted_password = password + db_user.salt
   
    if ( bcrypt.check_password_hash(db_user.password, salted_password)):
        return True
    return False


@admin_bp.route("/user/create", methods=["POST"])
@auth.login_required
def createAdmin():
    '''
    Add a new admin

    Request body:
    {
        "email": "
        "password": "
    }
    '''

    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return abort(400, "Bad Request: Missing query parameters")

    salt = binascii.hexlify(os.urandom(64)).decode()
    salted_password = password + salt  
    hashed_password = bcrypt.generate_password_hash(salted_password).decode('utf-8') 

    newUser = User()
    newUser.email = email
    newUser.password = hashed_password
    newUser.salt = salt
    newUser.isAdmin = True

    db.session.add(newUser)
    db.session.commit()

    return jsonify({'message': 'Admin succesfully created'}), 200


@admin_bp.route("/broadcast/addMessage", methods=["PUT"])
@auth.login_required
def set_broadcast():
    '''
    Sets the broadcast message in the database

    Request body:
    {
        "title": "String- Title of the broadcast",
        "message": "String- Message to broadcast",
        "broadcast_datetime": "String- Date and time to broadcast the message in the form of HH:MM DD/MM/YYYY",
        "endBroadcast_datetime": "String- Date and time to broadcast the message in the form of HH:MM DD/MM/YYYY",
        "[isImportant]": "Boolean- Is the message important - defaults to false"
    }
    '''
    title = request.form.get("title")
    message = request.form.get("message")
    broadcast_datetime = request.form.get("broadcast_datetime")
    endBroadcast_datetime = request.form.get("endBroadcast_datetime")
    isImportant = request.form.get("isImportant")

    if not title or not message or not broadcast_datetime or not endBroadcast_datetime:
        return abort(400, "Bad Request: Missing query parameters")
    
    if title.strip() == "":
        return abort(400, "Bad Request: Title cannot be empty")

    # Parse isImportant
    importantBool = None
    if isImportant == None or isImportant.strip() == "" or isImportant.strip().lower() == "false":
        importantBool = False
    elif isImportant.strip().lower() == "true":
        importantBool = True
    if importantBool == None:
        return abort(400, "Bad Request: isImportant should be a bool")
    
    # Parse the datetime
    try:
        broadcast_datetime = datetime.datetime.strptime(broadcast_datetime, "%H:%M %d/%m/%Y")
        boradcast_date = broadcast_datetime.date()
        broadcast_time = broadcast_datetime.time()
        endBroadcast_datetime = datetime.datetime.strptime(endBroadcast_datetime, "%H:%M %d/%m/%Y")
        end_broadcast_date = endBroadcast_datetime.date()
        end_broadcast_time = endBroadcast_datetime.time()
    except ValueError:
        return abort(400, "Bad Request: Invalid date format")
    
    # Make sure the title is unique
    if Broadcast.query.filter_by(title=title).first():
        return abort(400, "Bad Request: Title already exists")

    # Add the broadcast to the database
    newBroadcast = Broadcast()
    newBroadcast.title = title
    newBroadcast.message = message
    newBroadcast.startDate = boradcast_date
    newBroadcast.startTime = broadcast_time
    newBroadcast.endDate = end_broadcast_date
    newBroadcast.endTime = end_broadcast_time
    newBroadcast.isImportant = importantBool

    db.session.add(newBroadcast)
    db.session.commit()

    # Question is whether date and time should be used as a the time when the message gets broadcasted or the time it was created
    # Also hard to make auto close messages as stateless
    return jsonify({'message': 'Broadcast message succesfully added'}), 200


@admin_bp.route("/broadcast/deleteMessage", methods=["DELETE"])
@auth.login_required
def delete_broadcast():
    '''
    Delete a broadcast message from the database

    Request body:
    {
        "title": "String- Title of the broadcast"
    }
    '''
    title = request.form.get("title")

    if not title:
        return abort(400, "Bad Request: Missing query parameters")

    broadcast = Broadcast.query.filter_by(title=title).first()
    if not broadcast:
        return abort(404, "Not Found: Broadcast message not found")

    db.session.delete(broadcast)
    db.session.commit()

    return jsonify({'message': 'Broadcast message succesfully deleted'}), 200


@admin_bp.route("/generateGeometry", methods=["PUT"])
@auth.login_required
def generate_geometry():
    '''
    Generate the geometry for all the locations in the database. One off function ideally.
    Shouldn't need to use it in future as geom is now non nullable.
    '''
    locations = Location.query.all()
    for location in locations:
        if location.latitude and location.longitude:
            location.geom = func.ST_SetSRID(func.ST_MakePoint(location.longitude, location.latitude), 4326)
            db.session.add(location)    
    db.session.commit()

    return jsonify({'message': 'Geometry succesfully generated'}), 200


@admin_bp.route("/loadFoodLog", methods=["PUT"])
@auth.login_required
def loadFoodLog():
    '''
    Load a food log csv file into the database.

    Note: Extremely fragile code and will break if headers of csv change, etc.
    Only designed to be used once or twice for initial data loading.
    Sincerest apologies to the person who has to use this code later, probably myself in the future.
    Things just don't work but they work enough. Data from logs has to be cleaned before manually. Also this code
    may add unnamed suppliers to the database.

    Request body:
    {
        "foodlog": csv file
    }
    
    Query parameters:
    {
        "type": restaraunt | butcher
    }
    '''

    # Arguments parsing
    csvfile = request.files.get("foodlog")
    serviceType = request.args.get("type")

    if not csvfile:
        return abort(400, "Bad Request: Missing csv file")
    
    if not serviceType:
        return abort(400, "Bad Request: Missing service type query parameter")
    
    serviceType = serviceType.title()

    if serviceType != "Restaurant" and serviceType != "Butcher":
        return abort(400, "Bad Request: Invalid service type - " + serviceType)

    # Convert the file to a useable file type
    csvfile = BytesIO(csvfile.read())
    csvfile = TextIOWrapper(csvfile, encoding='utf-8')

    # Skip the read me
    lines = csvfile.readlines()
    for i, line in enumerate(lines):
        if line.strip().startswith('Butcher Name') or line.strip().startswith('Restaurant Name'):
            csvfile = StringIO(''.join(lines[i:]))
            break

    # Read the CSV file
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Butcher Name'] if serviceType == "Butcher" else row['Restaurant Name']
        # Initialise variables
        phone = None
        website = None
        if serviceType == 'Butcher':
            contact_details = row['Contact Details\n(Address, Phone, Website)'].split('\n')
            address = contact_details[0]
            phone = contact_details[1] if len(contact_details) > 1 else None
            website = contact_details[2] if len(contact_details) > 2 else None
        elif serviceType == 'Restaurant':
            address = row['Address']
        else:
            return abort(400, "Bad Request: Invalid service type - " + serviceType)
        status = row['Status'].title()
        suppliers = row['Supplier']
        last_contacted = row['Last Contacted']
        notes = row['Notes & other enquiry details']
        coordinates = row['Coordinates']

        if name.strip() == '':
            continue
        if status.strip() == '':
            return abort(400, "Bad Request: Issue with file, status is empty for some entries.")


        # If exists use the existing food service otherwise create a new one
        foodService = FoodService.query.filter(FoodService.name.ilike(name)).first()
        new_service = False
        if not foodService:
            foodService = FoodService()
            new_service = True 

        # Add food service table attribute
        foodService.name = name
        if last_contacted != '':
            last_contacted = datetime.datetime.strptime(last_contacted, '%d/%m/%Y').date()
        else: 
            last_contacted = None
        foodService.lastContacted = last_contacted
        foodService.notes = notes

        # Add many-to-one attributes
        foodServiceType = ServiceType.query.filter(ServiceType.name.ilike(serviceType)).first()
        if (foodServiceType == None):
            foodServiceType = ServiceType()
            foodServiceType.name = serviceType
            db.session.add(foodServiceType)
            db.session.flush()
            db.session.refresh(foodServiceType)
        foodService.type = foodServiceType.id

        halalStatus = HalalStatus.query.filter(HalalStatus.name.ilike(status)).first()
        if (halalStatus == None):
            halalStatus = HalalStatus()
            halalStatus.name = status
            db.session.add(halalStatus)
            db.session.flush()
            db.session.refresh(halalStatus)
        foodService.halalStatus = halalStatus.id

        # Add new food service once main attributes are added
        if new_service:
            db.session.add(foodService)
            db.session.flush()

            # Allows us to grab id
            db.session.refresh(foodService)

        # Add the many-to-many attributes
        # Add suppliers
        # NOTE: Suppliers are hard because they are not formatted well in the csv
        # A bit of hard coding involved
        suppliersList = suppliers.split(',')
        for supplier in suppliersList:
            supplier = supplier.strip()

            # NOTE: Here comes the fragile bit
            supplierName = ""
            if supplier in ['Fresh Poultry', 'Giglios', 'Self-Sourced', 'Cordina', 'MAM 100% Halaal', 'Apni Dukaan Australia', 'Sydney Kebabs', 'Steggles']:
                supplierName = supplier

            if supplierName == "":
                continue

            supplierTable = Supplier.query.filter(Supplier.name.ilike(supplierName)).first()
            if (supplierTable == None):
                supplierTable = Supplier()
                supplierTable.name = supplierName
                db.session.add(supplierTable)
            # Find if service supplier already exists
            serviceSupplier = ServiceSupplier.query.filter_by(supplierID=supplierTable.id, serviceID=foodService.id).first()
            if serviceSupplier == None:
                serviceSupplier = ServiceSupplier()
                db.session.flush()
                db.session.refresh(supplierTable)
                serviceSupplier.supplierID = supplierTable.id
                serviceSupplier.serviceID = foodService.id
                db.session.add(serviceSupplier)

        # Tags are not in the csv file so no actual data added


        # Add the one-to-many attributes
        # Add history
        newHistory = StatusHistory()
        newHistory.serviceID = foodService.id
        newHistory.halalStatus = halalStatus.id
        if last_contacted != None:
            newHistory.date = last_contacted
        else:
            newHistory.date = datetime.date.today()
        db.session.add(newHistory)

        # Add new location even if it already exists. Treated as a seperate location
        if address.strip() == '':
            return abort(400, "Bad Request: Issue with file, address is empty for some entries.")

        newLocation  = Location()

        address = address.split(',') 
        streetLine = address[0]
        suburb = address[1].split(' ')[:-3] # Accounts for multiple word suburbs
        state = address[1].split(' ')[-2]
        postcode = address[1].split(' ')[-1]

        newLocation.street = streetLine
        newLocation.city = 'Sydney' 
        newLocation.state = state
        newLocation.postCode = postcode
        newLocation.country = 'Australia'

        if (coordinates != '' and coordinates != None and coordinates != ' '):
            coordinates = coordinates.split(',')
            newLocation.latitude = coordinates[0][1:]
            newLocation.longitude = coordinates[1].strip()[:-1]
        newLocation.serviceID = foodService.id
        db.session.add(newLocation)

        # Add contact details
        # Add phone if exists
        if phone != None and serviceType=="Butcher" and phone.strip() != '':
            phoneContact = Contact.query.filter_by(type='phone', value=phone).first()
            if phoneContact == None:
                phoneContact = Contact()
                phoneContact.type = 'phone'
                phoneContact.value = phone
                db.session.add(phoneContact)
            phoneContact.serviceID = foodService.id
            db.session.add(phoneContact)

        # Add website if exists
        if website != None and serviceType=="Butcher" and website.strip() != '':
            websiteContact = Contact.query.filter_by(type='website', value=website).first()
            if websiteContact == None:
                websiteContact = Contact()
                websiteContact.type = 'website'
                websiteContact.value = website
                db.session.add(websiteContact)
            websiteContact.serviceID = foodService.id
            db.session.add(websiteContact)



        db.session.commit()

    return jsonify({'message': 'Loadsheet succesfully loaded'}), 200

def index() -> Response:
    '''
    Template route
    '''
    return jsonify({"admin_api_version": "1.0.0"})
