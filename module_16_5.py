from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.post("/user/{username}/{age}", response_model=User, summary="Post User")
def add_user(username: str, age: int):
    """Добавление нового пользователя."""
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.get("/", response_class=HTMLResponse, summary="Get Main Page")
async def read_users(request: Request):
    """Главная страница со списком пользователей."""
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}", response_class=HTMLResponse, summary="Get Users")
async def get_user(request: Request, user_id: int):
    """Получение пользователя по ID."""
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{user_id}", response_model=User, summary="Delete User")
def delete_user(user_id: int):
    """Удаление пользователя по ID."""
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.put("/user/{user_id}/{username}/{age}", response_model=User, summary="Update User")
def update_user(user_id: int, username: str, age: int):
    """Обновление информации о пользователе."""
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    import uvicorn

    add_user("UrbanUser", 24)
    add_user("UrbanTest", 22)
    add_user("Capybara", 60)

    uvicorn.run(app, host="127.0.0.1", port=8000)