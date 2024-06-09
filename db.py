from sqlalchemy.orm import registry, relationship
from sqlalchemy import Column, String, Integer, Boolean, create_engine, ForeignKey

engine = create_engine(
    'mysql+mysqlconnector://web:230mod@localhost:3306/quiz', echo=True
)

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Question(Base):
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True)
    question = Column(String(length=255))
    
    def __repr__(self):
        return "<Question(question_id='{0}', question='{1}')>" \
            .format(self.question_id, self.question)

class Answer(Base):
    __tablename__ = 'answers'
    answer_id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.question_id'))
    answer = Column(String(length=255))
    correct = Column(Boolean, unique=False, default=False)
    
    question = relationship("Question")

    def __repr__(self):
        return "<Answer(answer_id='{0}', question_id='{1}', answer='{2}'), correct='{3}'>" \
            .format(self.answer_id, self.question_id, self.answer, self.correct)

Base.metadata.create_all(engine)

# def add_answer(question:Question, answer:Answer):
#     with Session(engine) as session:
#         existing_book = session