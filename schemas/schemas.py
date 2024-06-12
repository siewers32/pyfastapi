from pydantic import BaseModel

class AnswerBase(BaseModel):
    question_id: int
    answer: str
    correct: bool

class AnswerCreate(AnswerBase):
    pass

class Answer(AnswerBase):
    id: int

    class Config:
        from_attributes = True
        
class QuestionBase(BaseModel):
    question: str
    
class QuestionCreate(QuestionBase):
    pass
   
class Question(QuestionBase):
    id: int
    answers: list[Answer] = []
    
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

