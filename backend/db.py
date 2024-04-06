from pathlib import Path
from typing import List, Dict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

DB_FILE = "sqlite:///queries.db"
engine = create_engine(DB_FILE)

Base = declarative_base()


class Query(Base):
    __tablename__ = 'queries'

    id = Column(Integer, primary_key=True)
    query = Column(String, unique=True)
    steps = relationship("Step", back_populates="query")


class Step(Base):
    __tablename__ = "steps"

    id = Column(Integer, primary_key=True)
    step_order = Column(Integer)
    text = Column(String)
    query_id = Column(Integer, ForeignKey('queries.id'))

    query = relationship("Query", back_populates="steps")


class DBControl:
    def __init__(self):
        self.path = Path(DB_FILE)
        self.engine = create_engine(DB_FILE)
        if not self.path.exists():
            Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def add_query(self, prompt: str, steps: List) -> None:
        query = Query(query=prompt)
        self.session.add(query)
        self.session.commit()

        for step in steps:
            order_num, step_text, _ = step.split(".")  # it will end with a full stop sign
            step_text = step_text.strip()
            order_num = int(order_num)
            _step = Step(step_order=order_num, text=step_text, query_id=query.id)
            self.session.add(_step)

        self.session.commit()

    def show_steps(self, query_id: int) -> List:
        steps = self.session.query(Step).filter(Step.query_id == query_id).all()
        steps = [f"{step.step_order}. {step.text}." for step in steps]

        return steps

    def show_queries(self) -> Dict:
        queries = self.session.query(Query).all()
        results = {}

        for query in queries:
            steps = query.steps
            results[query.query] = [(i.step_order, i.text) for i in steps]

        return results

    def __del__(self):
        self.session.close()


if __name__ == '__main__':
    db = DBControl()
