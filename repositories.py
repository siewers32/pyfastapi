from sqlalchemy.orm import Session

from . import models, schemas

class AnswerRepo:
    
    async def create (db: Session, answer:schemas.AnswerCreate):
        db_answer = models.Answer(answer=answer.answer)
        db.add(db_answer)
        db.commit()
        db.refresh()
        return db_answer
    
    def fetch_by_id(db: Session, _id):
        return db.query(models.Answer).filter(models.Answer.id == _id).first()
    
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Answer).offset(skip).limit(limit).all()

    async def delete(db: Session, answer_id):
        db_item = db.query(models.Answer).filter_by(id=answer_id).first()
        db.delete(db_item)
        db.commit()
        
class QuestionRepo:
    
    async def create (db: Session, question:schemas.QuestionCreate):
        db_question = models.Question(question=question.question)
        db.add(db_question)
        db.commit()
        db.refresh()
        return db_question
    
    def fetch_by_id(db: Session, _id):
        return db.query(models.Question).filter(models.Question.id == _id).first()
    
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Question).offset(skip).limit(limit).all()

    async def delete(db: Session, question_id):
        db_item = db.query(models.Question).filter_by(id=question_id).first()
        db.delete(db_item)
        db.commit()