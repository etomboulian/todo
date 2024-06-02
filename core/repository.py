from core.db import Session
from core.schemas import BaseSchema, CreateSchema, UpdateSchema
from core.models import Base

# TODO: Rewrite this using Generics instead of inheritance

class BaseRepository():
    def __init__(self, model: Base):
        self.model = model

    def get(self, db: Session, id: int) -> Base:
        return db.query(self.model).filter(self.model.id == id).first()
    
    def list(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db:Session, item_in: CreateSchema):
        item_in = item_in.model_dump()
        db_obj = self.model(**item_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(self, db: Session, item_in: UpdateSchema, item_updating_id: int):
        update_item = self.get(db, item_updating_id)
        new_data = self.model(**item_in.model_dump()).model_dump()
        for field in update_item.model_dump():
            if field in new_data:
                setattr(update_item, field, new_data[field])
        
        db.add(update_item)
        db.commit()
        db.refresh(update_item)
        return update_item

    def delete(self, db: Session, del_item_id: int):
        item = self.get(db, del_item_id)
        db.delete(item)
        db.commit()
        return item
    

# To allow overriding/additional methods
class TodoRepository(BaseRepository):
    ...

# To allow overriding/additional methods
class PersonRepository(BaseRepository):
    ...

from core.models import Todo, Person

todo = TodoRepository(Todo)
person = PersonRepository(Person)
