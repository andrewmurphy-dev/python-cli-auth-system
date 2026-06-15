from fastapi import FastAPI
from app.api.router import api_router 



app = FastAPI(tags= "CLI system authentification!")
 

app.include_router(api_router)



