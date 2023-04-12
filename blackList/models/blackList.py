from sqlalchemy import Sequence

from models.base_model import BaseModel
from database import db

TRAYECTO_ID_SEQ = Sequence('trayecto_id_seq')

class Trayecto(BaseModel):
    id = db.Column(db.Integer, TRAYECTO_ID_SEQ, primary_key=True, autoincrement=True)
    sourceAirportCode = db.Column(db.String, unique=False, nullable=False)
    sourceCountry = db.Column(db.String, unique=False, nullable=False)
    destinyAirportCode = db.Column(db.String, unique=False, nullable=False)
    destinyCountry = db.Column(db.String, unique=False, nullable=False)
    bagCost = db.Column(db.Integer, unique=False, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=True, default= db.func.now())


    def __init__(self, sourceAirportCode: str, sourceCountry: str, destinyAirportCode: str, destinyCountry: str, bagCost: int):
        self.sourceAirportCode = sourceAirportCode
        self.sourceCountry = sourceCountry
        self.destinyAirportCode = destinyAirportCode
        self.destinyCountry = destinyCountry
        self.bagCost = bagCost

