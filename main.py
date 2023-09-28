from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from db import database

app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(user.router, tags=['users'])

app.include_router(user.router, tags=['orders'])
app.include_router(user.router, tags=['products'])



if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
