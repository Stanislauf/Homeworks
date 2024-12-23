from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def add_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Введите имя пользователя", example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Введите возраст", example=24)]
):
    new_id = str(max(map(int, users.keys()), default=0) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: int,
    username: Annotated[str, Path(min_length=5, max_length=20, description="Введите имя пользователя", example="UrbanProfi")],
    age: Annotated[int, Path(ge=18, le=120, description="Введите возраст", example=28)]
):
    if str(user_id) in users:
        users[str(user_id)] = f'Имя: {username}, возраст: {age}'
        return f"User {user_id} has been updated"
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if str(user_id) in users:
        del users[str(user_id)]
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
