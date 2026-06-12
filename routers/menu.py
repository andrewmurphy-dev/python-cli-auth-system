from fastapi import APIRouter 


router = APIRouter(prefix="/menu", tags=["menu"])



#so we need fake data ! 
fake_users = {

    "name": "Andrew",
    "password": 454563378
}



@router.get("")
def menu():
    return fake_users 