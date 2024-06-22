import datetime
from flask import Blueprint, Response, abort, jsonify, request
from model import Broadcast, FoodService, ServiceType
from geoalchemy2 import functions as func

###
# File containing all the routes relating to operations by generic users.
#
# All routes in this file should have a url prefix of /api
###

main_bp = Blueprint("main", import_name=__name__, url_prefix="/api")

@main_bp.route("/", methods=["GET"])
def index() -> Response:
    '''
    Template route
    '''
    return jsonify({"main_api_version": "1.0.0"})

@main_bp.route("/foodService/getAll", methods=["GET"])
def get_food_services():
    '''
    Get all the food services in the database.
    Returns a list of all food services in the database.
    '''
    food_services = FoodService.query.all()
    if not food_services:
        return jsonify([]), 200

    food_service_list = []
    for food_service in food_services:
        food_service_list.append({
            'name': food_service.name,
            'lastContacted': food_service.lastContacted,
            'notes': food_service.notes,
            'type': food_service.type,
            'halalStatus': food_service.halalStatus
        })
    return jsonify(food_service_list), 200


@main_bp.route("/restaurant/getAll", methods=["GET"])
def get_restaurants():
    '''
    Get all the restaurants in the database.
    Returns a list of all restaurants in the database.
    '''
    serviceType = ServiceType.query.filter_by(name='Restaurant').first()
    if not serviceType:
        return abort(404, description="Restaurant food service does not exist in the database. Check with system admin.")

    food_services: list[FoodService] = FoodService.query.filter_by(type=serviceType.id).all()

    # Serialise the food services
    response_restaurants = [
        {
            'name': food_service.name,
            'lastContacted': food_service.lastContacted,
            'notes': food_service.notes,
            'type': food_service.type,
            'halalStatus': food_service.halalStatus
        }
        for food_service in food_services
    ]

    return jsonify(response_restaurants), 200


@main_bp.route("/restaurant/getNearby", methods=["GET"])
def get_restaurants_nearby():
    '''
    Get all the restaurants in the database that are nearby.
    Returns a list of all restaurants in the database that are nearby.

    Query Parameters:
    location: The location of the user.
    distance: The distance in meters from the user's location.
    '''

    # Parse args
    distance = request.args.get('distance', type=float)
    if not distance:
        return abort(400, description="Distance query parameter is required.")
    user_lat = request.args.get('lat', type=float)
    user_lon = request.args.get('lon', type=float)
    if not user_lat or not user_lon:
        return abort(400, description="Latitude and longitude query parameters are required.")
    
    # Get restaurant service type
    serviceType = ServiceType.query.filter_by(name='Restaurant').first()
    if not serviceType:
        return abort(404, description="Restaurant food service does not exist in the database. Check with system admin.")

    # Query for nearby locations
    user_point = func.ST_SetSRID(func.ST_MakePoint(user_lon, user_lat), 4326)
    nearby_locations = FoodService.query.filter(func.ST_DWithin(FoodService.location.geom, user_point, distance)).filter_by(type=serviceType.id).all()

    # Build response
    response_locations = [
        {
            'name': location.name,
            'lastContacted': location.lastContacted,
            'notes': location.notes,
            'type': location.type,
            'halalStatus': location.halalStatus
        }
        for location in nearby_locations
    ]

    # Return nearby locations
    return jsonify(response_locations), 200


@main_bp.route("/butcher/getAll", methods=["GET"])
def get_butchers():
    '''
    Get all the butchers in the database.
    Returns a list of all butchers in the database.
    '''
    serviceType = ServiceType.query.filter_by(name='Butcher').first()
    if not serviceType:
        return abort(404, description="Butcher food service does not exist in the database. Check with system admin.")

    food_services: list[FoodService] = FoodService.query.filter_by(type=serviceType.id).all()

    response_butchers = [
        {
            'name': food_service.name,
            'lastContacted': food_service.lastContacted,
            'notes': food_service.notes,
            'type': food_service.type,
            'halalStatus': food_service.halalStatus
        }
        for food_service in food_services
    ]

    return jsonify(response_butchers), 200


@main_bp.route("/butcher/getNearby", methods=["GET"])
def get_butchers_nearby():
    '''
    Get all the butchers in the database that are nearby.
    Returns a list of all butchers in the database that are nearby.

    Query Parameters:
    location: The location of the user.
    distance: The distance in meters from the user's location.
    '''
    # Parse args
    distance = request.args.get('distance', type=float)
    if not distance:
        return abort(400, description="Distance query parameter is required.")
    user_lat = request.args.get('lat', type=float)
    user_lon = request.args.get('lon', type=float)
    if not user_lat or not user_lon:
        return abort(400, description="Latitude and longitude query parameters are required.")
    
    # Get restaurant service type
    serviceType = ServiceType.query.filter_by(name='Butcher').first()
    if not serviceType:
        return abort(404, description="Restaurant food service does not exist in the database. Check with system admin.")

    # Query for nearby locations
    user_point = func.ST_SetSRID(func.ST_MakePoint(user_lon, user_lat), 4326)
    nearby_locations = FoodService.query.filter(func.ST_DWithin(FoodService.location.geom, user_point, distance)).filter_by(type=serviceType.id).all()

    # Build response
    response_locations = [
        {
            'name': location.name,
            'lastContacted': location.lastContacted,
            'notes': location.notes,
            'type': location.type,
            'halalStatus': location.halalStatus
        }
        for location in nearby_locations
    ]

    # Return nearby locations
    return jsonify(response_locations), 200


@main_bp.route("/broadcast/getMessages", methods=["GET"])
def get_broadcasts():
    '''
    Get all the broadcasts in the database.
    Returns a list of all broadcasts in the database.
    '''
    broadcasts = Broadcast.query.all()
    broadcast_list = []
    for broadcast in broadcasts:
        broadcast_list.append({
            'title': broadcast.title,
            'message': broadcast.message,
            'startDate': broadcast.startDate,
            'startTime': broadcast.startTime,
            'endDate': broadcast.endDate,
            'endTime': broadcast.endTime,
            'isImportant': broadcast.isImportant
        })
    return jsonify(broadcast_list), 200


@main_bp.route("/broadcast/getCurrentMessages", methods=["GET"])
def get_current_broadcasts():
    '''
    Get all the broadcasts in the database that are currently active.
    Returns a list of all broadcasts in the database that are currently active.
    '''
    current_datetime = datetime.datetime.now()
    broadcasts = Broadcast.query.filter(Broadcast.startDate <= current_datetime.date(), Broadcast.endDate >= current_datetime.date()).all()
    broadcast_list = []
    for broadcast in broadcasts:
        broadcast_list.append({
            'title': broadcast.title,
            'message': broadcast.message,
            'startDate': broadcast.startDate,
            'startTime': broadcast.startTime,
            'endDate': broadcast.endDate,
            'endTime': broadcast.endTime,
            'isImportant': broadcast.isImportant
        })
    return jsonify(broadcast_list), 200

