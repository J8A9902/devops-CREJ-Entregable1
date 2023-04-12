from database import db
from sqlalchemy import asc, desc

class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    @classmethod
    def find_by_id(cls, id: int):
        return cls.query.filter_by(id=id).first()
