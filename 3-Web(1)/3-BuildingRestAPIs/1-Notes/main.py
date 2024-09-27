from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


# Create a FastAPI instance
app = FastAPI()

# Create a "path operation function"
# path = "/"
# operation = HTTP GET method
# function = read_root
@app.get("/")
def read_root():
    return {"message": "Hello DE28, happy monday!"}

# item_id is a path parameter
# q is an optional query parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str]=None):
    return {"item_id": item_id, "optional_query": q}

# Create a Item object (type alias) using BaseModel
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}

# Example: circle.py, poor man's Wolfram Alpha

from circle import Circle

@app.get("/circumference/{radius}")
def read_circumference(radius: float):
    my_circle = Circle(radius)
    return {"circumference": my_circle.circumference()}

# Mini-ex: Create path operation function for area
@app.get("/area/{radius}")
def read_area(radius: float):
    my_circle = Circle(radius)
    return {"area": my_circle.area()}

# Example: Employee database

# My dummy database
employee_database = {
    "Einstein": {"role": "Genius", "age": 143},
    "Marie Curie": {"role": "Double Genius", "age": 154}
}

# Employee type
class Employee(BaseModel):
    name: str
    role: str
    age: Optional[int] = None

@app.get("/get_employee/{name}")
def get_employee(name: str):
    return employee_database.get(name)

# Mini-ex: Make name an optional path argument, and if not provided return the entire employee db,
# if provided just return employee information.

# Note: To get db by name, we need to call: http://localhost:8000/get_employee/?name=Einstein
@app.get("/get_employee/") # When arguments are optional, we don't provide them in the path
def get_employee(name: Optional[str]=None): # We can get optional path arguments with 'Optional'
    if name is None:
        return employee_database
    return employee_database.get(name)

@app.post("/add_employee/")
def add_employee(employee: Employee):
    # Done some action to the database
    employee_database[employee.name] = {"role": employee.role, "age": employee.age}
    return {"Message": f"Successfully added {employee.name}"} # response body

# Exercise: Make the above employee database example persitant by writing it to a json file.
# You will want to use the json module and the .load() and .dump() methods.
# See employee_db/ dir for solution