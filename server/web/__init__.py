from flask import Blueprint, render_template
from .customer import bp as cust_bp
from .todos import bp as todos_bp

bp = Blueprint("web", __name__)
bp.register_blueprint(cust_bp)
bp.register_blueprint(todos_bp)

@bp.route("/", methods=["GET"])
def home():
    return render_template("home.html")

