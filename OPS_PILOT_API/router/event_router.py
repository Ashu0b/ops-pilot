import logging
from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from core.database import db
from repositories.event_repository import EventRepo
from schemas.event_schema import EventCreateSchema
from models.event_models import Event
from services.ai_service import analyze_log

logger = logging.getLogger(__name__)

event_router = Blueprint('events', __name__)


@event_router.route('/events', methods=['GET'])
def get_events():
    try:
        events = EventRepo.get_all(db.session)
    except SQLAlchemyError as e:
        logger.error("Failed to fetch events: %s", e, exc_info=True)
        return jsonify({"error": "Failed to fetch events"}), 500

    return jsonify([e.to_dict() for e in events]), 200

@event_router.route('/create-event', methods=['POST'])
def create_event():
    json_data = request.get_json(silent=True)
    if not json_data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    try:
        data = EventCreateSchema(**json_data)
    except ValidationError as e:
        logger.warning("Validation error: %s", e.errors())
        return jsonify({"error": "Validation failed", "details": e.errors()}), 422

    try:
        ai_result = analyze_log(data.raw_logs)
    except Exception as e:
        logger.error("AI analysis failed: %s", e, exc_info=True)
        return jsonify({"error": "AI analysis failed. Please try again later."}), 502

    try:
        new_event = Event(**data.model_dump())
        saved_event = EventRepo.create(
            session=db.session,
            instance=new_event,
            commit_immediately=True,
        )
    except Exception as e:
        logger.error("DB error creating event: %s", e, exc_info=True)
        return jsonify({"error": "Failed to save event. Please try again later."}), 500

    logger.info("Event created: id=%s", saved_event.id)
    return jsonify(saved_event.to_dict()), 201