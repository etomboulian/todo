from flask import Blueprint

bp = Blueprint("api", __name__, url_prefix="/api/")

import server.api.people as people

bp.register_blueprint(people.bp)