from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas.question import Question
from app.schemas.answer import Answer
from app.schemas.lesson import Lesson
from app.services.questions_service import create_new_question, update_existing_question, delete_existing_question, \
    get_questions_by_lesson_id, get_lesson_details_by_lesson_id, submit_answers

router = APIRouter()


@router.post("/lessons/{lesson_id}/questions", response_model=Question, tags=["Question"])
def create_question(lesson_id: int, question: Question):
    """
    Create a new question
    """
    new_question = create_new_question(lesson_id, question)

    if not new_question:
        raise HTTPException(status_code=404, detail="Lesson not found")

    return new_question


@router.put("/lessons/{lesson_id}/questions/{question_id}", response_model=Question, tags=["Question"])
def update_question(lesson_id: int, question_id: int, question: Question):
    """
    Update a question by question id
    """
    updated_question = update_existing_question(lesson_id, question_id, question)

    if not updated_question:
        raise HTTPException(status_code=404, detail="Question not found")

    return updated_question


@router.delete("/lessons/{lesson_id}/questions/{question_id}", response_model=Question, tags=["Question"])
def delete_question(lesson_id: int, question_id: int):
    """
    Delete question by question id
    """
    removed_question = delete_existing_question(lesson_id, question_id)

    if not removed_question:
        raise HTTPException(status_code=404, detail="Question not found")

    return removed_question


@router.get("/lessons/{lesson_id}/questions", response_model=List[Question], tags=["Question"])
def get_questions(lesson_id: int):
    """
    Get all questions by lesson id
    """
    questions = get_questions_by_lesson_id(lesson_id)
    return questions


# LESSONS DETAILS - TAKE LESSON

@router.get("/lessons/{lesson_id}", response_model=Lesson, tags=["Question"])
def get_lesson_details(lesson_id: int):
    """
    Get lesson details:
    - Show questions by lesson
    """
    lesson_details = get_lesson_details_by_lesson_id(lesson_id)

    if not lesson_details:
        raise HTTPException(status_code=404, detail="Lesson not found")

    return lesson_details


@router.post("/lessons/{lesson_id}/take", tags=["Submit Answer"])
async def take_lesson(lesson_id: int, answers: List[Answer]):
    """
    Submit answers to a lesson

    Assuming the aprobation umbral is 60% (APROBATION_UMBRAL=0.6)
    """
    submit_answer = submit_answers(lesson_id, answers)

    if not submit_answer:
        raise HTTPException(status_code=404, detail=f"No question found for some question id")

    return submit_answer
