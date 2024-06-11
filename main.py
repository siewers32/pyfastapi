from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Union
from . import schemas, models
from fastapi import FastAPI
from pydantic import BaseModel
from db import get_db, engine
from repositories import AnswerRepo, QuestionRepo
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_price": item.price, "item_id": item_id}

app = FastAPI(title="Sample FastAPI Application",
    description="Sample FastAPI Application with Swagger and Sqlalchemy",
    version="1.0.0",)

models.Base.metadata.create_all(bind=engine)

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

@app.post("/answer/")
def create_question(request: schemas.QuestionAnswerPayload):
    return "New question added " + request.question.question + " " + request.answer.answer
