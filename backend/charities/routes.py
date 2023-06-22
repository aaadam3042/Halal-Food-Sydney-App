from flask import Blueprint, Response, jsonify

###
# File containing all the routes relating to operations by generic users.
#
# All routes in this file should have a url prefix of /api/charities
###

charities_bp = Blueprint("charities", import_name=__name__, url_prefix="/api/charities")

@charities_bp.route("/", methods=["GET"])
def index() -> Response:
    '''
    Template route
    '''
    return jsonify({"charities_api_version": "1.0.0"})
