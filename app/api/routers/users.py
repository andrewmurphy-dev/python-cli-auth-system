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





#signup - user 

@router.post("")
def create_user(request: CreateStructure, db: Session = Depends(get_db)):
    result = db.execute(text("""INSERT INTO users (name, pasword)
                             VALUES (:name, :password)
                             RETURNING id, name, password, created_at,
"""),
{
    "name": request.name,
    "password": request.password,
},

)


    db.commit()

    row = result.mappings().one()

    return {
        "message": "Signed up successfully",
        "user": {
            "id": row["id"],
            "name": row["name"],
            "password": row["password"],
            "created_at": int(row["created_at"].timestamp()),
        },
    }



@router.post("/login")
def login(request: CreateStructure, db: Session = Depends(get_db)):
    result = db.execute(
        text("""
            SELECT id, name, password, created_at
            FROM users
            WHERE name = :name AND password = :password
        """),
        {
            "name": request.name,
            "password": request.password,
        },
    )

    user = result.mappings().first()

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": "login successful!"}




