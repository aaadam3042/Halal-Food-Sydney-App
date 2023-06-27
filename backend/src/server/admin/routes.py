from flask import Blueprint, Response, jsonify

###
# File containing all the routes relating to operations by admins. Ensure that
# all routes have been implemented with security in mind.
#
# All routes in this file should have a url prefix of /api/admin
###

admin_bp = Blueprint("admin", import_name=__name__, url_prefix="/api/admin")

@admin_bp.route("/", methods=["GET"])
def index() -> Response:
    '''
    Template route
    '''
    return jsonify({"admin_api_version": "1.0.0"})
