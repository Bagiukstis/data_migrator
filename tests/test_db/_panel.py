from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Panel(Base):
    __tablename__ = "sample"

    id = Column(Integer, primary_key=True)
    category = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    discount = Column(String, nullable=False)

    def __init__(self, category, name, discount):
        self.category = category
        self.name = name
        self.discount = discount

    def __repr__(self):
        return "<Panel('{self.category}', '{self.name}', " "'{self.discount}')>".format(
            self=self
        )
