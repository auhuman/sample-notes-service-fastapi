from sqlalchemy import table
from sqlmodel import SQLModel, Field
from typing import Optional
import time

class Note(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    content: str = ""
    created_at: float = Field(default_factory=time.time)
    updated_at: float = Field(default_factory=time.time)