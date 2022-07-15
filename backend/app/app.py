from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Union
from sqlalchemy.orm import Session
from .internal import admin
from .dependencies import get_query_token, get_token_header
from .routers import pages, profile, settings
from .database.database import SessionLocal, engine
from .database import crud, models, schemas

models.Base.metadata.create_all(bind=engine)
#app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

origins = ['http://localhost:8080']

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=['*'],
   allow_headers=['*']
)

app.include_router(pages.router)
app.include_router(profile.router)
app.include_router(settings.router)
app.include_router(
    admin.router,
    prefix='/admin',
    tags=['admin'],
    dependencies=[Depends(get_token_header)],
    responses={418: {'description': 'I\'m a teapot'}}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def root():
    return {}
