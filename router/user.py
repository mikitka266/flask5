from fastapi import APIRouter

from db import users

router = APIRouter()


@router.get('/fake_users/{count}')
async def create_note(count int):
    for i in range(count):
        query = users.insert().values(first_name=f'user{i}',
        last_name=f'family{i}',
        email=f'mail{i}@mail.ru',
        password=f'password{i}')
        await database.execute(query)
        return {'message': f'{count} fake users create'}


@router.post('/user', response_model = UserIn)
async def create_user(user: UserIn):
    users.insert().values(first_name=user.first_name,
                          last_name=user.last_name, email=user.email,
                          password=user.password)
    return user


@router.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    for i in await database.fetch_all(query):
        print(i)
    return await database.fetch_all(query)



@router.put('/users/', response_model=User)
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


@router.delete('/users/', response_model=User)
async def delete_user(id: int, users=None):
    for i in range(0, len(users)):
        if users[i].id == id:
            users.remove(users[i])
            return {"message": "User was deleted successfully"}
        raise HTTPException(status_code=404, detail='User not found')
