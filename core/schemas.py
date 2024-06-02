from pydantic import BaseModel
from datetime import datetime

class CreateSchema(BaseModel):
    ...

class UpdateSchema(BaseModel):
    ...

class BaseSchema(BaseModel):
    ...


# Person Schemas
class PersonSchema(BaseSchema):
    id: int
    first_name: str
    last_name: str
    date_created: datetime
    date_updated: datetime


class PersonCreate(CreateSchema):
    first_name: str
    last_name: str


class PersonUpdate(UpdateSchema):
    id: int 
    first_name: str
    last_name: str


# Todo Schemas
class TodoSchema(BaseSchema):
    id: int
    subject: str
    description: str
    date_created: datetime
    date_updated: datetime


class TodoCreate(CreateSchema):
    subject: str
    description: str


class TodoUpdate(UpdateSchema):
    subject: str
    description: str
