from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from database import create_db
from models import Note
from service import NotesService

app = FastAPI()
service = NotesService()


@app.on_event("startup")
def on_startup():
    create_db()


@app.post("/notes", status_code=201)
def create_note(payload: Note):
    return service.create_note(payload)


@app.get("/notes")
def list_notes():
    return service.list_notes()


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    note = service.get_note(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.put("/notes/{note_id}/content")
def update_note(note_id, payload: Note):
    note = service.update_note(payload)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    if not service.delete_note(note_id):
        raise HTTPException(status_code=404, detail="Note not found")
