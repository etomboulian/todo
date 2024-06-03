from flask import Blueprint, render_template, abort, request, redirect, url_for
import core.repository as repository
import core.schemas as schemas
from core.db import SessionLocal

bp = Blueprint("todos", __name__, template_folder="templates", url_prefix="/todo/")

@bp.route("/", methods=["GET", "POST"])
def list():
    db = SessionLocal()
    todo_list = repository.todo.list(db)
    return render_template(
        "todo.html", 
        action="list", 
        todo_list=todo_list
    )

@bp.route("/create", methods=["GET", "POST"])
def create():
    db = SessionLocal()

    # Handle Create on POST
    if request.method == "POST":

        new_todo_data = request.form.to_dict()
        new_todo = schemas.TodoCreate(**new_todo_data)
        new_db_todo = repository.todo.create(db, new_todo)
        if new_db_todo:
            return redirect(url_for("web.todos.list"))
    
    return render_template("todo.html", action="edit", todo=None)

@bp.route("/<int:id>", methods=["GET", "POST"])
def edit(id: int):
    db = SessionLocal()
    # Handle updates on POST
    if request.method == "POST":
        data = request.form.to_dict()
        new_todo_data = schemas.TodoUpdate(**data)
        repository.todo.update(db, new_todo_data, id)
        return redirect(url_for("web.todos.list"))
    
    # Handle the edit form on a GET
    todo = repository.todo.get(db, id)
    if todo:
        return render_template("todo.html", action="edit", todo=todo)
    # Return a 401 if we cannot find a todo to edit
    return abort(401)

@bp.route("/<int:id>/delete", methods=["POST"])
def delete(id: int):
    db = SessionLocal()
    repository.todo.delete(db, id)
    return redirect(url_for("web.todos.list"))
    
