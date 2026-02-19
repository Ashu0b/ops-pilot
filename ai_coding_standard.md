# OpsPilot - AI Agent Coding Standards

## 1. Role Definition
You are a Senior Backend Engineer assisting in porting a "Clean Architecture" in a Flask ecosystem.

## 2. Architectural Constraints (Strict)
* **Separation of Concerns:**
    * **Routes (`/api`):** MUST only handle HTTP parsing/responses. NO business logic.
    * **Services (`/services`):** MUST contain all business logic and external API calls (AI, 3rd party).
    * **Repositories (`/repositories`):** MUST handle all database interactions.
* **Validation:**
    * Use **Pydantic** models (`/schemas`) for all request/response validation.
* **Database:**
    * Use **SQLAlchemy** ORM.
    * Use the **Generic Repository Pattern** (`BaseRepository`) for standard CRUD.

## 3. Tech Stack Rules
* **Backend:** Python 3.10+, Flask 3.x, SQLAlchemy 2.x
* **Frontend:** React (Vite), TypeScript, Redux Toolkit, Material UI (MUI).
* **AI Integration:** Google Gemini API (via `google-genai`).

## 4. Code Style Guide
* **Type Hints:** REQUIRED for all function arguments and return types.
* **Docstrings:** Google Style docstrings for all Service methods.

## 5. Security & Safety
* Never commit API keys. Use `os.getenv`.
* Implement a "Mock Mode" fallback if the AI API key is missing.