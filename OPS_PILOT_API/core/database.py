import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
logger = logging.getLogger(__name__)


def init_db(app):
    app.config.setdefault(
        "SQLALCHEMY_ENGINE_OPTIONS",
        {
            "pool_size": 20,
            "max_overflow": 5,
            "pool_timeout": 30,
            "pool_recycle": 300,
            "pool_pre_ping": True,
            "connect_args": {"connect_timeout": 30},
        },
    )

    db.init_app(app)
