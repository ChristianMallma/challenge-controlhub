from pydantic import BaseModel, Field
from typing import List


class Answer(BaseModel):
    question_id: int = Field(None, description="The quiestion id.")
    selected_options: List[str] = Field(...,
                                        description="A list of options selected by the user as their answers. "
                                                    "For single-choice questions, this list will contain only one item."
                                        )
