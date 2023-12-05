import os
import binascii
import csv
from flask_bcrypt import Bcrypt
from flask import Blueprint, Response, abort, jsonify, request
from flask_httpauth import HTTPBasicAuth
from io import TextIOWrapper

from app import app
from model import db, User

###
# File containing all the routes relating to operations by admins. Ensure that
# all routes have been implemented with security in mind.
#
# All routes in this file should have a url prefix of /api/admin
###

auth = HTTPBasicAuth()
bcrypt = Bcrypt(app)

admin_bp = Blueprint("admin", import_name=__name__, url_prefix="/api/admin")

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

@auth.login_required
@admin_bp.route("/admin/user/create", methods=["POST"])
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

@auth.login_required
@admin_bp.route("/admin/loadFoodLog", methods=["PUT"])
def loadFoodLog():
    '''
    Load a food log csv file into the database

    Request body:
    {
        "file": csv file
    }
    
    Query parameters:
    {
        "type": restaraunt | butcher
    }
    '''
    csvfile = request.files.get("foodlog")
    serviceType = request.args.get("type")

    if not csvfile or not serviceType:
        return abort(400, "Bad Request: Missing query parameters")
    
    if serviceType != "restaraunt" and serviceType != "butcher":
        return abort(400, "Bad Request: Invalid service type")

    # TODO:
    # Will need to find relevant type and halal status tables
    # build associated location, contact, status history, service supplier, tag junction tables

    # Convert the file to a TextIOWrapper object
    csvfile = TextIOWrapper(csvfile.stream, encoding='utf-8')

    # Skip the read me
    for line in csvfile:
        if line.strip().startswith('Butcher Name') or line.strip().startswith('Restaurant Name'):
            csvfile.seek(csvfile.tell() - len(line))  # rewind to start of line
            break

    # Read the CSV file
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Butcher Name'] if serviceType == "butcher" else row['Restaurant Name']
        contact_details = row['Contact Details'].split('\n')
        address = contact_details[0]
        phone = contact_details[1]
        status = row['Status']
        supplier = row['Supplier']
        last_contacted = row['Last Contacted']
        notes = row['Notes']

        return jsonify({
            "name": name,
            "address": address,
            "phone": phone,
            "status": status,
            "supplier": supplier,
            "last_contacted": last_contacted,
            "notes": notes
        })

    return jsonify({'message': 'Loadsheet succesfully loaded'}), 200

def index() -> Response:
    '''
    Template route
    '''
    return jsonify({"admin_api_version": "1.0.0"})
