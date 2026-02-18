from core.database import db
from sqlalchemy import func
from enums.common_enums import PriorityEnum, EventStatusEnum
from .base_model import BaseModel


class Event(BaseModel):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority_id = db.Column(db.Integer, db.ForeignKey(
        "priority.id"), nullable=True, default=PriorityEnum.MEDIUM.value)
    status_id = db.Column(db.Integer, db.ForeignKey(
        "event_status.id"), nullable=False, default=EventStatusEnum.OPEN.value)
    raw_logs = db.Column(db.Text, nullable=True)
    ai_analysis = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, server_default=func.now())