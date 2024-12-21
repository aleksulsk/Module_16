from fastapi import FastAPI, Path
from typing import Annotated
import anyio

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def dict_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user_info(
        user_id: Annotated[str, Path(description='Enter user ID', example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')
async def delete_user_id(
        user_id: Annotated[str, Path(description='Enter user ID', example='2')]) -> str:
    del users[user_id]
    return f'User {user_id} has been deleted'