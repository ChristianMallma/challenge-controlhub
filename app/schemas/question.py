from pydantic import BaseModel, Field
from typing import List


class Question(BaseModel):
    id: int = Field(None, description="The question id.")
    text: str = Field(..., description="The text of the question.")
    lesson_id: int = Field(None, description="The id of the lesson.")
    options: List[str] = Field(..., description="A list of possible answers from which the user can choose.")
    correct_answer: List[str] = Field(..., description="A list of correct answers.")
