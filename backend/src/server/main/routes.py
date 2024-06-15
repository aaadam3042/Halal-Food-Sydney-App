import datetime
from flask import Blueprint, Response, abort, jsonify, request
from model import Broadcast, FoodService, ServiceType

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
    return jsonify(food_services), 200


@main_bp.route("/restaurant/getNearby", methods=["GET"])
def get_restaurants_nearby():
    '''
    Get all the restaurants in the database that are nearby.
    Returns a list of all restaurants in the database that are nearby.

    Query Parameters:
    location: The location of the user.
    distance: The distance in meters from the user's location.
    '''
    distance = request.args.get('distance')
    if not distance:
        return abort(400, description="Distance query parameter is required.")
    #TODO: How to get location of user?
    # How to calculate distance between two locations?
    # Should it just be localised to suburbs? coords may not work as db does not force coords to exist

    # Use maps api (Should put a design pattern here but maybe later)
    # User inputs coords    # NOTE: I think we run a db update for coords now and enforce it to exist and be added.
    # Go through db and update coords for each location < --- #TODO: Is this a bad idea? Answer: Yes. Why? Because it's not scalable. What should be done instead? Use a maps api to get coords for each location
    # Use maps api to get coords for each location < --- # TODO: Is there a better way to do this then go through every restaurant in the db?
    # Calculate straight line distance between user and each location
    # Return locations within distance

 
    return jsonify([]), 200


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
    return jsonify(food_services), 200


@main_bp.route("/butcher/getNearby", methods=["GET"])
def get_butchers_nearby():
    '''
    Get all the butchers in the database that are nearby.
    Returns a list of all butchers in the database that are nearby.

    Query Parameters:
    location: The location of the user.
    distance: The distance in meters from the user's location.
    '''
    distance = request.args.get('distance')
    if not distance:
        return abort(400, description="Distance query parameter is required.")
    # TODO: Same issue as restaurants
    # refactor similar code out once done
    return jsonify([]), 200


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

