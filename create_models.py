# from fastapi import Depends, FastAPI, HTTPException
# from fastapi.responses import JSONResponse
# from typing import Union
from models import models
from schemas import schemas
from fastapi import FastAPI
from pydantic import BaseModel
from db import db
from repositories import repositories
from sqlalchemy.orm import Session
# from fastapi.encoders import jsonable_encoder

app = FastAPI(
        title="Sample FastAPI Application",
        description="Sample FastAPI Application with Swagger and Sqlalchemy",
        version="1.0.0"
    )

engine = db.get_engine()
Base = db.get_base()

models.Base.metadata.create_all(bind=engine)


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None



if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)