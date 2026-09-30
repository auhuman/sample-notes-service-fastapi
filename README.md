# Sample Notes Service using FastAPI

A simple REST API for managing notes, built with **FastAPI** and **SQLModel** (SQLite).

## Tech Stack
- **FastAPI** — web framework
- **SQLModel** — ORM (Pydantic + SQLAlchemy)
- **SQLite** — database
- **Uvicorn** — ASGI server

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/notes` | Create a new note |
| `GET` | `/notes` | List all notes (sorted by last updated) |
| `GET` | `/notes/{note_id}` | Get a single note |
| `PUT` | `/notes/{note_id}/content` | Update note content |
| `DELETE` | `/notes/{note_id}` | Delete a note |

## Setup

```bash
pip install fastapi sqlmodel uvicorn
python3 -m fastapi run app.py
```

API docs available at: http://localhost:8000/docs
