from core.database import db


class EventStatusMaster(db.Model):
    __tablename__ = "event_status"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class PriorityMaster(db.Model):
    __tablename__ = "priority"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
