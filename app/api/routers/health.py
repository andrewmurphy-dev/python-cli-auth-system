from fastapi import APIRouter
from app.db import db_test_connection

router = APIRouter()


@router.get("/health")
def health():
    return {"Response": "Server is running"}


@router.get("/db-test")
def db_test():
    result = db_test_connection()

    return {
        "database": "connected",
        "result": result, 
    }








