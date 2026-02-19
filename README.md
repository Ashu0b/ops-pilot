## OpsPilot: AI-Powered Incident Response Dashboard

Live API Deployment: https://ops-pilot-api.onrender.com

Problem Statement
DevOps teams often waste time manually analyzing repetitive server logs. OpsPilot automates this by using Generative AI to parse raw stack traces, identify root causes, and suggest code fixes immediately.

Key Technical Decisions

1. Architecture: Clean Patterns in Flask
   Generic Repository Pattern: Instead of cluttering routes with DB calls, I implemented a strict Repository pattern. This decouples the database layer from the API logic, making the code testable and cleaner.

Pydantic Validation: I bypassed standard Flask form validation in favor of Pydantic. This ensures strict data contracts (Schemas) for the API.

Enums for Type Safety: To avoid "magic strings" and maintain data integrity, I implemented Python Enum classes for fields like Priority and Status. This prevents invalid states at the code level.

2. Modern Frontend Stack
   Redux Toolkit & TypeScript: State management handles the asynchronous nature of AI analysis (polling/waiting for results), while TypeScript ensures the API contract is strictly respected by the UI.

3. Production-Grade Database & Deployment
   Neon Postgres (Cloud DB): Moved beyond local SQLite to a serverless PostgreSQL instance via Neon, ensuring production-level data persistence.

Flask-Migrate: Database schema changes are managed via Alembic (Flask-Migrate) rather than raw SQL scripts, allowing for safe schema evolution.

Gunicorn vs. Waitress: The application is configured to run on Gunicorn in production (Render) for performance, while supporting Waitress or standard development server for local testing.

4. Resilient AI Integration
   The system uses the Google Gemini API for log analysis.

Fallback Mechanism: A dedicated "Mock Service" activates automatically if no API key is detected, ensuring the application is reviewable without credentials.

API Documentation
The backend exposes the following primary endpoints via the EventRouter:

## GET /events

Retrieves the history of all logged incidents and their AI analysis status.

## POST /create-event

The main ingestion point. Accepts raw logs and metadata, validates them, and triggers the AI analysis service.

Payload: { "title": "...", "raw_logs": "..."}

Setup Instructions

Backend (OPS_PILOT_API)
Prerequisites: Python 3.10+
Bash
cd OPS_PILOT_API

# 1. Create & Activate Virtual Environment

python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

# 2. Install Dependencies

pip install -r requirements.txt

# 3. Apply Database Migrations (Neon/Local)

flask db upgrade

# 4. Run Server

# Option A: Dev Mode

python main.py

# Option B: Production Mode (Local Simulation)

waitress-serve --port=5000 main:app

Frontend (OPS_PILOT_UI)
Prerequisites: Node.js 18+, Yarn
cd OPS_PILOT_UI

# 1. Install Dependencies

yarn install

# 2. Start Development Server

yarn dev

WSGI Server: Gunicorn (gunicorn main:app)
Database: Neon (PostgreSQL)

Environment Variables:
DATABASE_URL: Connection string for Neon Postgres.
GEMINI_API_KEY: Google AI credentials
