from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud import note
from schemas.note import NoteBase, NoteCreate, NoteResponse
from db.session import db_manager

router_note = APIRouter(prefix='/notes', tags=['Notes'])
router_tags = APIRouter(prefix='/tags', tags=['Tags'])

@router_note.get('/', response_model=list[NoteResponse])
async def read_notes(db: AsyncSession = Depends(db_manager.scoped_session_dependency)):
    return await note.read_notes(db)


@router_note.get('/{note_id}', response_model=NoteResponse)
async def read_note(note_id: int, db: AsyncSession = Depends(db_manager.scoped_session_dependency)):
    _note = await note.read_note(session=db, note_id=note_id)
    if _note is not None:
        return _note
    raise HTTPException(status_code=404, detail="Note not found")


@router_note.post('/', response_model=NoteResponse)
async def create_note(note_in: NoteCreate, db: AsyncSession = Depends(db_manager.scoped_session_dependency)):
    return await note.note_create(session=db, note_in=note_in)


