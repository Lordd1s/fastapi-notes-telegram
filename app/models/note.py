from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DATETIME, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.db.base import Base

note_tag_association = Table(
    'note_tag_association', Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id')),
)


class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True)

    notes = relationship("Note", secondary=note_tag_association, back_populates="tags")


class Note(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String)
    tags_id = relationship("Note", secondary=note_tag_association, back_pop='notes')
    created_at = Column(DATETIME, default=datetime.now(timezone.utc), index=True)
    last_changed_at = Column(DATETIME, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), index=True)

    tags = relationship(Tags, secondary=note_tag_association, back_populates="notes")