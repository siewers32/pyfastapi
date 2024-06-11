from sqlalchemy.orm import registry, relationship, sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, create_engine, ForeignKey

SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://web:230mod@localhost:3306/quiz'
engine = create_engine(
   SQLALCHEMY_DATABASE_URL, echo=True
)

# mapper_registry = registry()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    hashed_password = Column(String(length=255))
    is_active = Column(Boolean, default=True)

    items = relationship("Quiz", back_populates="owner")


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)
    title = Column(String(length=64), index=True)
    description = Column(String(length=255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="quizzes")


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String(length=255))
    
    def __repr__(self):
        return "<Question(id='{0}', question='{1}')>" \
            .format(self.question_id, self.question)

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer = Column(String(length=255))
    correct = Column(Boolean, unique=False, default=False)
    
    question = relationship("Question")

    def __repr__(self):
        return "<Answer(id='{0}', question_id='{1}', answer='{2}'), correct='{3}'>" \
            .format(self.id, self.question_id, self.answer, self.correct)

Base.metadata.create_all(engine)

# def add_answer(question:Question, answer:Answer):
#     with Session(engine) as session:
#         existing_book = session