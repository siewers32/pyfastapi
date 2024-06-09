from pydantic import BaseModel
class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str
    correct: bool

class QuestionAnswerPayload(BaseModel):
    question: Question
    answer: Answer
    