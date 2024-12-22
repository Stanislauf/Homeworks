from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conint
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

class User(BaseModel):
    username: str
    age: conint(ge=0)

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def add_user(username: str, age: Annotated[int, conint(ge=0)]):
    new_id = str(max(map(int, users.keys()), default=0) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: Annotated[int, conint(ge=0)]):
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f"The user {user_id} has been updated"
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
