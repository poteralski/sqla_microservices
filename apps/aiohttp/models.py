from apps.aiohttp.extensions import db

from sqlalchemy import Column, Integer


class Example(db.Model):
    __tablename__ = "examples"
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
