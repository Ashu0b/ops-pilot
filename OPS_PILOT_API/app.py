import os
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS
from core.database import init_db, db
from router import register_routers
import models

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(
        app,
        resources={r"/*": {"origins": os.getenv("FRONTEND_URL")}},
        supports_credentials=True
    )
    init_db(app)
    Migrate(app, db)
    register_routers(app)
    return app
