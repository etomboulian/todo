import pytest

import core.repository as repository
import core.schemas as schemas
from core.db import SessionLocal

db = SessionLocal()

data = {
    "subject": "Test Todo Item",
    "description": "This is a test of the Todo application to ensure that it works"
}

class TestCrudTodo:

    def test_crud_todo(self):
        # Create Test
        new_item = schemas.TodoCreate(**data)
        db_item = repository.todo.create(db, new_item)
        assert(db_item is not None)
        assert(db_item.id > 0)

        # Read Test
        read_item = repository.todo.get(db, db_item.id)
        assert(read_item is not None)
        assert(read_item.id == db_item.id)

        # Update Test
        data["subject"] = data["subject"] + " updated"
        update_item = schemas.TodoUpdate(**data)
        db_item = repository.todo.update(db, update_item, db_item.id)
        assert(db_item is not None)
        assert(db_item.subject == data["subject"])
        
        # Delete Test
        deleted_item = repository.todo.delete(db, db_item.id)
        assert(deleted_item is not None)
        check_deleted = repository.todo.get(db, deleted_item.id)
        assert(check_deleted is None)
        