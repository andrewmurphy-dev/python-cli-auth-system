from fastapi import APIRouter 


router = APIRouter(prefix="/users", tags=["users"])



#so we need fake data ! 
fake_users = {
    "name": "Andrew",
    "password": 454563378
}



@router.get("")
def get_users():
    return fake_users 