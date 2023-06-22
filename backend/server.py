from flask import Flask, Blueprint, Response, jsonify

from admin.routes import admin_bp
from charities.routes import charities_bp

###
# Backend entrypoint
# Contains routes to do with the API itself. In general don't edit this file 
# as routes for the application should be in a blueprint else where.
#
# Routes in this file have the url prefix of /api
###

app = Flask(__name__)
api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/", methods=["GET"])
def index() -> Response:
    return jsonify({"api_version": "1.0.0"})


# Blueprints should be registered after defining routes otherwise
# an assertion error will be raised
app.register_blueprint(api_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(charities_bp)


if __name__ == '__main__':
    app.run(debug=True)
