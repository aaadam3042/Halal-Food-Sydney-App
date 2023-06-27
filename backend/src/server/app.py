from flask import Flask, Blueprint, Response, jsonify
from flask_migrate import Migrate

from server.admin.routes import admin_bp
from server.charities.routes import charities_bp
from server.model import db

###
# Backend entrypoint
# Contains routes to do with the API itself. In general don't edit this file 
# as routes for the application should be in a blueprint else where.
#
# Routes in this file have the url prefix of /api
###

# Set up the flask app 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/aaadam3042'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


# Base route
api_bp = Blueprint("api", __name__, url_prefix="/api")
@api_bp.route("/", methods=["GET"])
def index() -> Response:
    return jsonify({"api_version": "1.0.0"})


# Register all blueprints
app.register_blueprint(api_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(charities_bp)


if __name__ == '__main__':
    app.run(debug=True)
