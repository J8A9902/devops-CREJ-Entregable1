from sqlalchemy import Sequence

from models.base_model import BaseModel
from database import db

BLACKLIST_ID_SEQ = Sequence('blackList_id_seq')

class blackList(BaseModel):
    id = db.Column(db.Integer, BLACKLIST_ID_SEQ, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    app_uuid = db.Column(db.String, unique=False, nullable=False)
    blocked_reason = db.Column(db.String(255), unique=False, nullable=False)
    ip = db.Column(db.String, unique=False, nullable=False)
    date = db.Column(db.DateTime, default= db.func.now())


    def __init__(self, email: str, app_uuid: str, blocked_reason: str, ip: str):
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason
        self.ip = ip

