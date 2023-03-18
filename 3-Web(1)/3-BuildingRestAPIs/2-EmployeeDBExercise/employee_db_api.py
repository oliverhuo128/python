# Exercise: Make the above employee database example persitant by writing it to a json file.
# You will want to use the json module and the .load() and .dump() methods.
# get_employee
# add_employee
import json
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

db_app = FastAPI()

class Employee(BaseModel):
    name: str
    role: str
    age: Optional[int] = None

@db_app.get("/")
def read_root():
    return {"Message": "Welcome to the employee database"}

@db_app.get("/get_employee/")
def get_employee(name: Optional[str] = None):
    # Load the DB into memory
    # 'with' will automatically close the file once the code block as run
    with open("employee_database.json", "r") as db_file:
        employee_database = json.load(db_file)

    if name is None:
        return employee_database

    return employee_database.get(name)

@db_app.post("/add_employee/")
def add_employee(employee: Employee):
    # Load DB into memory
    with open("employee_database.json", "r") as db_file:
        employee_database = json.load(db_file)

    # Add employee to DB dict
    employee_database[employee.name] = {"role": employee.role, "age": employee.age}

    # Write DB to file to persist it
    with open("employee_database.json", "w") as db_file:
        json.dump(employee_database, db_file)

    return {"Message": f"Successfully added {employee.name}"}


    
