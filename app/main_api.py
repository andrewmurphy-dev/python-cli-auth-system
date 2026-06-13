from fastapi import FastAPI
from router.py import api_router




app = FastAPI(tags= "CLI system authentification!")


app.include_router(api_router)



