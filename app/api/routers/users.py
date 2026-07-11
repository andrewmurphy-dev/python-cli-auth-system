from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from zoneinfo import ZoneInfo
from pydantic import BaseModel, Field
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db import get_db


router = APIRouter(prefix="/users", tags=["users"])

class CreateStructure(BaseModel):
    name: str = Field(minlength=3)
    password: str = Field(minlength=4)



#so we need fake data ! 
fake_users = [
    {
        "id": 1,
        "name": "andrew",
        "password": "15267252",
        "created_at": "2026-06-16T00:00:00+09:00",
    }
]



@router.get("")
def get_users(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT id, name, password, created_at, FROM users"))
    rows = result.mapping().all()

    users = []

    for row in rows:
        users.append({
            "id": row["id"],
            "name": row["name"],
            "password": row["password"],
            "created_at": int(row["created_at"].timestamp()),
        })

    return users








JAPAN_TIMEZONE = ZoneInfo("Asia/Tokyo")

def current_japan_time():
    return datetime.now(JAPAN_TIMEZONE).isoformat()







@router.post("")
def create_user(request: CreateStructure):
    for user in fake_users:
        if user["name"] == request.name:
            raise HTTPException(status_code=409, detail="Username already exists")

    new_id = new_user_id()

    new_user = {
        "id": new_id,
        "name": request.name,
        "password": request.password,
        "created_at": current_japan_time()

    }

    fake_users.append(new_user)

    return {"message": "Signed up successfully!", "user": new_user}



@router.post("/login")
def login(request: CreateStructure):
    for user in fake_users:
        if user["name"] == request.name and user["password"] == request.password:
            return {"message": "login successful!"}

    raise HTTPException(status_code=401, detail="Invalid username or password")
