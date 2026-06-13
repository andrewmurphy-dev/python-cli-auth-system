from fastapi import APIRouter 
from datetime import datetime
from zoneinfo import ZoneInfo 


router = APIRouter(prefix="/users", tags=["users"])



#so we need fake data ! 
fake_users = {
    "id": 1,
    "name": "Andrew",
    "password": 454563378,
    "created_at": 
}



@router.get("")
def get_users():
    return fake_users 





def new_user_id():
    if not fake_users:
        return 1 
    
    largest_user_id = 0 
    
    for user in fake_users:
        if fake_users["id"] > largest_user_id:
            largest_user_id = fake_users["id"]

        
    return largest_user_id + 1 





JAPAN_TIMEZONE = ZoneInfo("Asia/Tokyo")

def current_japan_time():
    return datetime.now(JAPAN_TIMEZONE).isoformat()


@router.post("")
def create_user():
    new_id = new_user_id()

    new_user = {
        "id": new_id,
        "name": "andrew"
        "password": "15267252"
        "created_at": current_japan_time()

    }

    fake_users.appemd(new_user)

    return new_user 