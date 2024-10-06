from typing import Optional

from pydantic import BaseModel, ConfigDict


class NoteBase(BaseModel):
    title: str
    description: str
    tags: list['TagBase']


class NoteCreate(NoteBase):
    pass


class NoteResponse(NoteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class TagResponse(TagBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
