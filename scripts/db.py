
from core.db import SessionLocal, Base
import core.repository as repository
import core.schemas as schemas

people = [
    {"first_name": "Admin", "last_name": "Test"}, 
    {"first_name": "New", "last_name": "User"}
]

todos = [
    {"subject": "first todo", "description": "A description of the first todo item"},
    {"subject": "second todo", "description": "A description for the second todo item"}
]

def add_initial_data():
    db = SessionLocal()
    for person in people:
        new_item = schemas.PersonCreate(**person)
        repository.person.create(db, new_item)

    for todo in todos:
        new_item = schemas.TodoCreate(**todo)
        repository.todo.create(db, new_item)


def create_db():
    import core.models
    Base.metadata.create_all()


