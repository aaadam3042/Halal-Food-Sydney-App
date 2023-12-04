import os
import binascii
from flask_bcrypt import Bcrypt
from flask import Blueprint, Response, jsonify
from flask_httpauth import HTTPBasicAuth

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
@admin_bp.route("/admin/create", methods=["POST"])
def createAdmin():
    '''
    Add a new admin

    Requires authentication via auth header
    '''

    salt = binascii.hexlify(os.urandom(64)).decode()
    salted_password = password + salt   # TODO: put in actual password from auth header
    hashed_password = bcrypt.generate_password_hash(salted_password).decode('utf-8') 

    # TODO: store salt and hashed password in database
    return "Not implemented"

@admin_bp.route("/", methods=["GET"])
def index() -> Response:
    '''
    Template route
    '''
    return jsonify({"admin_api_version": "1.0.0"})
