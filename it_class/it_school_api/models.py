from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GreetResponse(BaseModel):

    greet_msg: str
    name: str

class Course(BaseModel):

    id: int
    name: str
    description: str
    listed_date: Optional[datetime] = datetime.now() 
    start_date: datetime
    trainer: str
    seats: int

# class CoursePath(BaseModel):

