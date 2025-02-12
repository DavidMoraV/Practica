from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Endpoint GET
@app.get("/get-user/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "username": "test_user"}

# Endpoint POST
class User(BaseModel):
    username: str
    email: str

@app.post("/create-user")
async def create_user(user: User):
    return {"message": f"User {user.username} created with email {user.email}"}

