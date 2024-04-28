from fastapi import APIRouter, HTTPException
from typing import List

from app.models.lesson import Lesson
from app.models.question import Question
from app.models.answer import Answer

router = APIRouter()

# Static data
fake_lesson_db = [
    {
        "id": 1,
        "title": "Lesson 1",
        "course_id": 1,
        "description": "Introduction to Python Basics"
    },
    {
        "id": 2,
        "title": "Lesson 2",
        "course_id": 1,
        "description": "Advanced Python Techniques"
    },
]


@router.get("/courses/{course_id}/lessons", response_model=List[Lesson])
def get_lessons_for_course(course_id: int):
    lessons = [lesson for lesson in fake_lesson_db if lesson["course_id"] == course_id]
    if not lessons:
        raise HTTPException(status_code=404, detail="Course not found or no lessons available")
    return lessons


# Stacic data of questions
fake_question_db = [
    {
        "id": 1,
        "text": "What is Python?",
        "lesson_id": 1,
        "options": ["Programming language", "Snake"],
        "correct_answer": ["Programming language"]
    },
    {
        "id": 2,
        "text": "Which data type is mutable in Python?",
        "lesson_id": 1,
        "options": ["list", "tuple"],
        "correct_answer": ["list"]
    }
]


@router.get("/lessons/{lesson_id}", response_model=Lesson)
def get_lesson_details(lesson_id: int):
    lesson = next((lesson for lesson in fake_lesson_db if lesson["id"] == lesson_id), None)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    questions = [Question(**question) for question in fake_question_db if question["lesson_id"] == lesson_id]
    return {**lesson, "questions": questions}


@router.post("/lessons/{lesson_id}/take")
async def take_lesson(lesson_id: int, answers: List[Answer]):
    correct_count = 0
    for answer in answers:
        correct_answer = next((q['correct_answer'] for q in fake_question_db if q['id'] == answer.question_id), None)
        if correct_answer is None:
            raise HTTPException(status_code=404, detail=f"No question found with ID {answer.question_id}")
        if set(answer.selected_options) == set(correct_answer):
            correct_count += 1

    total_questions = len([q for q in fake_question_db if q['lesson_id'] == lesson_id])
    is_passed = correct_count >= (total_questions * 0.7)  # Assuming the aprobation umbral is 70%

    return {"total_questions": total_questions, "correct_answers": correct_count, "passed": is_passed}
