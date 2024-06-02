from flask import Blueprint, request, jsonify

bp = Blueprint("api", __name__)

import core.repository as repository
import core.schemas as schemas
from core.db import SessionLocal

not_found = {
    "message": "Not found"
}

@bp.route("/people/", methods=["GET"])
def get_people():
    db = SessionLocal()
    people_list = repository.person.list(db)

    response = people_list if people_list else not_found
    return jsonify(response)

@bp.route("/people/", methods=["POST"])
def create_person():
    db = SessionLocal()
    raw_data = request.get_json()
    new_person = schemas.PersonCreate(**raw_data)
    new_db_person = repository.person.create(db, new_person)
    return jsonify(new_db_person)

@bp.route("/people/<int:id>", methods=["GET"])
def get_person(id: int):
    db = SessionLocal()
    person = repository.person.get(db, id)
    response = person if person else not_found
    return jsonify(response)

@bp.route("/people/<int:id>", methods=["PUT"])
def update_person(id: int):
    db = SessionLocal()
    raw_data = request.get_json()
    update_person = schemas.PersonUpdate(**raw_data)
    update_db_person = repository.person.update(db, update_person, id)
    return jsonify(update_db_person)

@bp.route("/people/<int:id>", methods=["DELETE"])
def delete_person(id: int):
    db = SessionLocal()
    deleted_person = repository.person.delete(db, id);
    return jsonify(deleted_person)
