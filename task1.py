from http.client import HTTPException

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class UserIn(BaseModel):
    name: str
    email: str
    password: str


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.post('/users/', response_model=list[User])
async def create_user(new_user: UserIn, users=None):
    users.append(
        User(id=len(users) + 1, name=new_user.name, email=new_user.email, password=new_user.password)
    )
    return users


@app.put('/users/', response_model=User)
async def edit_user(id: int, new_user: UserIn, users=None):
    for i in range(0, len(users)):
        if users[i].id == id:
            current_user = users[id - 1]
    if current_user:
        current_user.name = new_user.name
        current_user.email = new_user.email
        current_user.password = new_user.password
    else:
        raise HTTPException(status_code=404, detail='User not found')
    return current_user


@app.delete('/users/', response_model=User)
async def delete_user(id: int, users=None):
    for i in range(0, len(users)):
        if users[i].id == id:
            users.remove(users[i])
            return {"message": "User was deleted successfully"}
        raise HTTPException(status_code=404, detail='User not found')

if __name__ == '__main__':
    uvicorn.run(
        'task1:app',
        host='127.0.0.1',
        port=8000,
        reload=True
    )
