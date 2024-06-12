from dotenv import dotenv_values
from flask import Flask, Blueprint, Response, abort, jsonify, request
from flask_migrate import Migrate
from os import getenv, path
from typing import Tuple

from admin.routes import admin_bp, init_bcyrpt  
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
init_bcyrpt(app)
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

# Register all blueprints
app.register_blueprint(api_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
