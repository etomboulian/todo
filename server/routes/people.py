from flask import Blueprint, request, jsonify

bp = Blueprint("api", __name__)

@bp.route("/people", methods=["GET"])
def get_people():
    return "Get People Endpoint"

@bp.route("/people", methods=["POST"])
def create_person():
    return "Create Person Endpoint"

@bp.route("/people/{id:int}", methods=["GET"])
def get_person():
    return "Get Person Endpoint"

@bp.route("/people/{id:int}", methods=["PUT"])
def update_person():
    return "Update Person Endpoint"

@bp.route("/people/{id:int}", methods=["DELETE"])
def delete_person():
    return "Delete Person Endpoint"