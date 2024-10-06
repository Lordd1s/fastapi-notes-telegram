from fastapi import FastAPI
from api.note import router_note, router_tags


app = FastAPI()
app.include_router(router_note)
app.include_router(router_tags)

@app.get('/')
async def root():
    return {"message": "Hello, World!"}
