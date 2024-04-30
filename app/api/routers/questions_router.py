from fastapi import APIRouter, HTTPException
from typing import List

from app.api.dbs import fake_lesson_db, fake_question_db
from app.models.question import Question
from app.models.answer import Answer
from app.models.lesson import Lesson

router = APIRouter()


@router.post("/lessons/{lesson_id}/questions", response_model=Question)
def create_question(lesson_id: int, question: Question):
    """
    Create a new question
    """
    if not any(lesson['id'] == lesson_id for lesson in fake_lesson_db):
        raise HTTPException(status_code=404, detail="Lesson not found")
    new_id = max((q['id'] for q in fake_question_db if q['lesson_id'] == lesson_id), default=0) + 1
    new_question = question.dict()
    new_question['id'] = new_id
    new_question['lesson_id'] = lesson_id
    fake_question_db.append(new_question)
    return new_question


@router.put("/lessons/{lesson_id}/questions/{question_id}", response_model=Question)
def update_question(lesson_id: int, question_id: int, question: Question):
    """
    Update a question by question id
    """
    for idx, existing_question in enumerate(fake_question_db):
        if existing_question['id'] == question_id and existing_question['lesson_id'] == lesson_id:
            updated_question = {**existing_question, **question.dict(), "id": question_id, "lesson_id": lesson_id}
            fake_question_db[idx] = updated_question
            return updated_question
    raise HTTPException(status_code=404, detail="Question not found")


@router.delete("/lessons/{lesson_id}/questions/{question_id}", response_model=Question)
def delete_question(lesson_id: int, question_id: int):
    """
    Delete question by question id
    """
    for idx, existing_question in enumerate(fake_question_db):
        if existing_question['id'] == question_id and existing_question['lesson_id'] == lesson_id:
            removed_question = fake_question_db.pop(idx)
            return removed_question
    raise HTTPException(status_code=404, detail="Question not found")


@router.get("/lessons/{lesson_id}/questions", response_model=List[Question])
def get_questions(lesson_id: int):
    """
    Get all questions by lesson id
    """
    return [question for question in fake_question_db if question['lesson_id'] == lesson_id]


# LESSONS DETAILS - TAKE LESSON

@router.get("/lessons/{lesson_id}", response_model=Lesson)
def get_lesson_details(lesson_id: int):
    """
    Get lesson details:
    - Show questions by lesson
    """
    lesson = next((lesson for lesson in fake_lesson_db if lesson["id"] == lesson_id), None)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    questions = [Question(**question) for question in fake_question_db if question["lesson_id"] == lesson_id]
    return {**lesson, "questions": questions}


@router.post("/lessons/{lesson_id}/take")
async def take_lesson(lesson_id: int, answers: List[Answer]):
    """
    Submit answers to a lesson

    Assuming the aprobation umbral is 60% (APROBATION_UMBRAL=0.6)
    """
    correct_count = 0
    APROBATION_UMBRAL = 0.6

    for answer in answers:
        correct_answer = next((q['correct_answer'] for q in fake_question_db if q['id'] == answer.question_id), None)

        if correct_answer is None:
            raise HTTPException(status_code=404, detail=f"No question found with ID {answer.question_id}")

        if set(answer.selected_options) == set(correct_answer):
            correct_count += 1

    total_questions = len([q for q in fake_question_db if q['lesson_id'] == lesson_id])
    is_passed = correct_count >= (total_questions * APROBATION_UMBRAL)

    return {"total_questions": total_questions, "correct_answers": correct_count, "passed": is_passed}
