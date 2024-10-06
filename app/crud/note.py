from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from models import Note, Tag
from schemas.note import NoteCreate


async def read_notes(session: AsyncSession) -> list[Note]:
    state = select(Note).order_by('created_at')
    result: Result = await session.execute(state)
    notes = result.scalars().all()
    return list(notes)


async def read_note(session: AsyncSession, note_id: int) -> Note | None:
    return await session.get(Note, note_id)


async def note_create(session: AsyncSession, note_in: NoteCreate) -> Note:
    tag_names = [tag.name for tag in note_in.tags]
    print(tag_names)
    existing_tags_query = select(Tag).where(Tag.name.in_(tag_names))
    print('1', existing_tags_query)
    existing_tags_result = await session.execute(existing_tags_query)
    existing_tags = existing_tags_result.scalars().all()
    print('2', existing_tags)

    tags = []
    for tag_name in note_in.tags:
        if tag_name in existing_tags:
            tags.append(existing_tags[tag_name])
        else:
            new_tag = Tag(name=tag_name)
            session.add(new_tag)
            tags.append(new_tag)
    note = Note(
        title=note_in.title,
        description=note_in.description,
        tags=tags
    )
    session.add(note)
    await session.commit()
    await session.refresh(note)
    return note

