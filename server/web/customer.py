from flask import Blueprint

bp = Blueprint("customer", __name__, url_prefix='/customers/')

@bp.route('/')
def customer_list():
    ...