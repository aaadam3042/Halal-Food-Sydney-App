from dotenv import dotenv_values
from flask import Flask, Blueprint, Response, abort, jsonify, request
from flask_migrate import Migrate
from os import getenv, path
from typing import Tuple

from admin.routes import admin_bp
from main.routes import main_bp
from model import db, User

###
# Backend entrypoint
# Contains routes to do with the API itself. In general don't edit this file 
# as routes for the application should be in a blueprint else where.
#
# Routes in this file have the url prefix of /api
###

currentDir = path.dirname(path.abspath(__file__))
envPath = path.join(currentDir, '.env')
env = dotenv_values(envPath)

# Set up the flask app 
app = Flask(__name__)
db_url = env["DATABASE_URL"]
print(db_url)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


api_bp = Blueprint("api", __name__, url_prefix="/api")

# Base route
@api_bp.route("/", methods=["GET"])
def index() -> Response:
    return jsonify({"api_version": "1.0.0"})

    
@api_bp.route("/users", methods=["GET"])
def getUser() -> Response:

    # Get id given as query string
    userID = request.args.get('userID')

    if (userID == None):
        # If no ID was given
        users = User.query.all()
        userList = []
        for user in users:
            userList.append({"id": user.id,
                            "email": user.email,
                            "isAdmin": user.isAdmin})
        userJson = {"users": userList}
        return jsonify(userJson)
    else:
        # If ID was given
        user = User.query.get(userID)
        if (user == None):
            abort(404, "User of given userID could not be found")
        return jsonify({
            "email": user.email,
            "isAdmin": user.isAdmin
    })

@api_bp.route("/users/new", methods=["PUT"])
def newUser() -> Tuple[Response, int]:
    # Create a new user
    data = request.get_json()
    if (not data or 'email' not in data or 'isAdmin' not in data):
        abort(400, "Bad Request: Missing query parameters")

    email = data['email']
    isAdmin = data['isAdmin']

    try:
        isAdmin = int(isAdmin)
    except:
        abort(400, "Bad Request: Invalid value for 'isAdmin'")
    newUser = User(email=email, isAdmin=isAdmin)
    db.session.add(newUser)
    db.session.commit()
    return jsonify({'message': 'User succesfully created'}), 200


# Register all blueprints
app.register_blueprint(api_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
