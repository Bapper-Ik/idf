from fastapi import FastAPI
from app import models
from app.database import engine

from app.api import client, admin, auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get('/')
async def root():
    return {"status": "Server's up and running..."}


app.include_router(client.router)
app.include_router(admin.router)
app.include_router(auth.router)

