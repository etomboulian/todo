from flask import Blueprint
from .customer import bp as cust_bp
from .todos import bp as todos_bp

bp = Blueprint("web", __name__)
bp.register_blueprint(cust_bp)
bp.register_blueprint(todos_bp)

