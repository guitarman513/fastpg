from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()
def build_connection_string():
    user="myuser"
    pw="mypassword"
    host="localhost"
    port="5432"
    name="mydb"
    return f"postgresql://{user}:{pw}@{host}:{port}/{name}"
engine = create_engine(build_connection_string())

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Person(Base):
    __tablename__='person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

@app.get("/")
def read_root():
    return {"Hellp":"World"}

@app.get('/create_table')
def create_table():
    Base.metadata.create_all(engine)
    return{"message":"table added"}

@app.post("add_row")
def add_row(name:str, age:int):
    person = Person(name=name, age=age)
    session.add(person)
    session.commit()
    return {"message":"row (person) added"}

