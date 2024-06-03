from flask import Blueprint, render_template

bp = Blueprint("customer", __name__, url_prefix='/customers/')

@bp.route('/')
def customer_list():
    return render_template("customers.html")