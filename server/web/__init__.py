from flask import Blueprint

bp = Blueprint("web", __name__)

@bp.route("/", methods=["GET"])
def home_page():
    return "<h2> Welcome to the home page </h2>"