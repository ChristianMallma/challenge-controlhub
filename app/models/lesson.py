from pydantic import BaseModel, Field
from typing import List, Optional
from .question import Question


class Lesson(BaseModel):
    id: int = Field(..., description="The id of the lesson.")
    title: str = Field(..., description="The title of the lesson.")
    course_id: int = Field(..., description="The id of the course.")
    description: str = Field(..., description="A lesson description.")
    questions: Optional[List[Question]] = Field(default_factory=list,
                                                description="A list of questions associated with the lesson. "
                                                            "This list may be empty if there are no questions.")
