import pytest

import core.repository as repository
import core.schemas as schemas
from core.db import SessionLocal

db = SessionLocal()

data = {
    "first_name": "Admin",
    "last_name": "Test"
}

class TestCrudPerson:

    def test_crud_person(self):
        # Create Test
        new_item = schemas.PersonCreate(**data)
        db_item = repository.person.create(db, new_item)
        assert(db_item is not None)
        assert(db_item.id > 0)

        # Read Test
        read_item = repository.person.get(db, db_item.id)
        assert(read_item is not None)
        assert(read_item.id == db_item.id)

        # Update Test
        data_read = read_item.model_dump()
        data_read["last_name"] = "Updated"
        
        update_item = schemas.PersonUpdate(**data_read)
        db_item = repository.person.update(db, update_item, db_item.id)
        assert(db_item is not None)
        assert(db_item.last_name == data_read["last_name"])

        # Delete Test
        deleted_item = repository.person.delete(db, db_item.id)
        assert(deleted_item is not None)
        check_deleted = repository.person.get(db, deleted_item.id)
        assert(check_deleted is None)
