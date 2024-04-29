from pydantic import BaseModel, Field
from typing import List, Optional
from .question import Question


class Lesson(BaseModel):
    id: int = Field(None, description="The id of the lesson. Generated in the server.")
    title: str = Field(..., description="The title of the lesson.")
    course_id: int = Field(None, description="The id of the course.")
    description: str = Field(..., description="A lesson description.")
    questions: Optional[List[Question]] = Field(default_factory=list,
                                                description="A list of questions associated with the lesson. "
                                                            "This list may be empty if there are no questions.")
