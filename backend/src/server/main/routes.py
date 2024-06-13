import datetime
from flask import Blueprint, Response, jsonify
from model import Broadcast

###
# File containing all the routes relating to operations by generic users.
#
# All routes in this file should have a url prefix of /api/main
###

main_bp = Blueprint("main", import_name=__name__, url_prefix="/api/main")

@main_bp.route("/", methods=["GET"])
def index() -> Response:
    '''
    Template route
    '''
    return jsonify({"main_api_version": "1.0.0"})

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

