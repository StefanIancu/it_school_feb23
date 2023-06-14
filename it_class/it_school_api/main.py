from typing import Union, Dict, List
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from models import GreetResponse, Course
from datetime import datetime

app = FastAPI()

external_data = [
    Course(name="Python Online", description="Learn Python 3", 
           start_date=datetime(2023, 12, 1), trainer="Mihai Dinu", seats=16, id=1),
    Course(name="Java Online", description="Learn Java and Spring", 
           start_date=datetime(2023, 12, 11), trainer="Ionut Dobre", seats=24, id=2),

]

@app.get("/hello")
def read_root():
    return {"greet_msg": "Hello",
            "name": "George"
            }

@app.get("/hello/{name}")
def greet_user(name: str) -> GreetResponse:
    """Get a greeting message and user name."""
    return GreetResponse(greet_msg="Hello", name=name.title())

@app.get("/courses")
def list_courses() -> List[Course]:
    return external_data

@app.get("/course/{id}")
def course_detail(id: int) -> Course:
    for i in external_data:
        if i.id == id:
            return i
    raise HTTPException(status_code=404, detail="Course not found.")

@app.post("/courses", status_code=201)
def create_course(course: Course) -> Course:
    external_data.append(course)
    return course 

@app.put("/courses/{id}")
def update_course(id: int, course: Course) -> Course:
    for i, v in enumerate(external_data):
        if v.id == id:
            external_data[i] = course
            return external_data[i]
    raise HTTPException(status_code=404, detail="Edit not found")

# @app.patch("/courses/{id}")
# def update_course_seat(id: int, course: CoursePath) -> Course:
#     for i, v in enumerate(external_data):
#         if v.id == id:
#             external_data[i].seats = course
#             return external_data[i]
#     raise HTTPException(status_code=404, detail="Edit not found")

@app.delete("/courses/{id}")
def delete_course(id: int):
    pass
