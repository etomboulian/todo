from flask import Blueprint, render_template, abort, request, redirect, url_for
import core.repository as repository
import core.schemas as schemas
from core.db import SessionLocal

bp = Blueprint("web", __name__, template_folder="templates")

@bp.route("/", methods=["GET"])
def home_page():
    return render_template("home.html")

@bp.route("/todo/", methods=["GET", "POST"])
def list_todos():
    db = SessionLocal()
    todo_list = repository.todo.list(db)
    return render_template("todo_list.html", todo_list=todo_list)

@bp.route("/todo/create", methods=["GET", "POST"])
def create_todo():
    db = SessionLocal()

    # Handle Create on POST
    if request.method == "POST":

        new_todo_data = request.form.to_dict()
        new_todo = schemas.TodoCreate(**new_todo_data)
        new_db_todo = repository.todo.create(db, new_todo)
        if new_db_todo:
            return redirect(url_for("web.list_todos"))
    
    return render_template("todo_edit.html", todo=None)

@bp.route("/todo/<int:id>", methods=["GET", "POST"])
def edit_todo(id: int):
    db = SessionLocal()
    # Handle updates on POST
    if request.method == "POST":
        data = request.form.to_dict()
        new_todo_data = schemas.TodoUpdate(**data)
        repository.todo.update(db, new_todo_data, id)
        return redirect(url_for("web.list_todos"))
    
    # Handle the edit form on a GET
    todo = repository.todo.get(db, id)
    if todo:
        return render_template("todo_edit.html", todo=todo)
    # Return a 401 if we cannot find a todo to edit
    return abort(401)

@bp.route("/todo/<int:id>/delete", methods=["POST"])
def delete_todo(id: int):
    db = SessionLocal()
    repository.todo.delete(db, id)
    return redirect(url_for("web.list_todos"))
    
