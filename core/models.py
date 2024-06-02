from core.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Todo(Base):
    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    date_created: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
    date_updated: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now, onupdate=datetime.now)

    def model_dump(self):
        dump = {}
        for field in self.__dict__:
            if(not field.startswith("_")):
                dump[field] = self.__dict__[field]
        return dump
      

class Person(Base):
    __tablename__ = "person"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False, default=datetime.now)
    date_created: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now, onupdate=datetime.now)

    def model_dump(self):
        dump = {}
        for field in self.__dict__:
            if(not field.startswith("_")):
                dump[field] = self.__dict__[field]
        return dump