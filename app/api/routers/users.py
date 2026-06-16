from fastapi import APIRouter, HTTPException
from datetime import datetime
from zoneinfo import ZoneInfo
from pydantic import BaseModel, Field



router = APIRouter(prefix="/users", tags=["users"])

class CreateStructure(BaseModel):
    name: str = Field(minlength=3)
    password: str = Field(minlength=4)



#so we need fake data ! 
fake_users = [
    {
        "id": 1,
        "username": "andrew",
        "email": "test@test.com",
        "created_at": "2026-06-16T00:00:00+09:00",
    }
]


@router.get("")
def get_users():
    return fake_users 





def new_user_id():
    if not fake_users:
        return 1 
    
    largest_user_id = 0 
    
    for user in fake_users:
        if user["id"] > largest_user_id:
            largest_user_id = user["id"]

        
    return largest_user_id + 1 





JAPAN_TIMEZONE = ZoneInfo("Asia/Tokyo")

def current_japan_time():
    return datetime.now(JAPAN_TIMEZONE).isoformat()


@router.post("")
def create_user():
    new_id = new_user_id()

    new_user = {
        "id": new_id,
        "name": "andrew",
        "password": "15267252",
        "created_at": current_japan_time()

    }

    fake_users.append(new_user)

    return new_user



@router.post("/login")
def login(request: CreateStructure):
    return {"message": "login successful!"}