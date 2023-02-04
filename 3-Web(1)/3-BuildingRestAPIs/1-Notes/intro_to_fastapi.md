****# An introduction to building APIs with FastAPI

## Requirements

### Technical Requirements

- A Python installation and optionally your preferred virtual environment manager.
- VS Code or your preferred editor.

### Pre-req Knowledge

- What are APIs and why are they useful.
- How HTTP requests work.
- Python typing and pydantic.

## Why FastAPI?

FastAPI is a modern, fast web framework to build APIs with python. It has excellent [documentation](https://fastapi.tiangolo.com/), so there is no need to duplicate it here.

FastAPI automates a lot of the behind the scenes work that other API frameworks ask to you to deal with yourself, FastAPI provides:

- Automatic data validation (using type-hinting and pydantic)
- Automatic data conversion (between JSON and python types)
- Automatic documentation (built to the OpenAPI standards)
- Documentation that can perform API testing

## Installing FastAPI

1. Navigate to the directory you want to store this in.
2. [Optional] Create a virtual environment and activate it
   - `virtualenv venv`
   - Windows: `venv/Scripts/activate.bat`
   - Mac: `source venv\bin\activate`
3. Install fast api
    `pip install fastapi, uvicorn[standard]`

## Developing with FastAPI

`uvicorn main:app --reload`