from flask import Blueprint, Response, jsonify

###
# File containing all the routes relating to operations by generic users.
#
# All routes in this file should have a url prefix of /api/charities
###

main_bp = Blueprint("charities", import_name=__name__, url_prefix="/api/main")

@main_bp.route("/", methods=["GET"])
def index() -> Response:
    '''
    Template route
    '''
    return jsonify({"main_api_version": "1.0.0"})
