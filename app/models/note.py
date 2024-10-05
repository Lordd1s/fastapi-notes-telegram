from datetime import datetime, timezone

from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base import Base


class Tag(Base):
    name: Mapped[str] = mapped_column(unique=True)
    notes = relationship("Note", secondary="note_tag_association", back_populates="tags")


class Note(Base):
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    last_changed_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    tags = relationship(Tag, secondary="note_tag_association", back_populates="notes")


note_tag_association = Table(
    'note_tag_association', Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True),
)