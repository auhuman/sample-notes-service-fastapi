from __future__ import annotations
from database import engine
import database
from sqlmodel import Session, select
from models import Note
import time


class NotesService:
    def __init__(self):
        self.db_session = Session(engine)

    def create_note(self, note:Note):
        self.db_session.add(note)
        self.db_session.commit()
        self.db_session.refresh(note)
        return note
    
    def list_notes(self) -> list[Note]:
        statment = select(Note).order_by(Note.updated_at.desc())
        return self.db_session.exec(statment).all()
    
    def get_note(self, note_id: int):
        return self.db_session.get(Note, note_id)

    def update_note(self, note: Note) -> Note | None:
        enote = self.db_session.get(Note, note.id)
        if not enote:
            return None
        enote.content = note.content
        self.db_session.add(enote)
        self.db_session.commit()
        self.db_session.refresh(enote)
        return enote

    def delete_note(self, note_id: int) -> bool:
        note = self.db_session.get(Note, note_id)
        if not note:
            return False
        self.db_session.delete(note)
        self.db_session.commit()
        return True