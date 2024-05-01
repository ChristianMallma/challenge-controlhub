from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas.lesson import Lesson
from app.services.lessons_service import get_lessons_by_course, create_new_lesson, update_existing_lesson, \
    delete_existing_lesson

router = APIRouter()


@router.get("/courses/{course_id}/lessons", response_model=List[Lesson], tags=["Lesson"])
def get_lessons_for_course(course_id: int):
    """
    Get lessons by course id
    """
    lessons = get_lessons_by_course(course_id)
    if not lessons:
        raise HTTPException(status_code=404, detail="Course not found or no lessons available")
    return lessons


@router.post("/courses/{course_id}/lessons", response_model=Lesson, tags=["Lesson"])
def create_lesson(course_id: int, lesson: Lesson):
    """
    Create a new lesson
    """
    new_lesson = create_new_lesson(course_id, lesson)

    if not new_lesson:
        raise HTTPException(status_code=404, detail="Course not found")

    return new_lesson


@router.put("/courses/{course_id}/lessons/{lesson_id}", response_model=Lesson, tags=["Lesson"])
def update_lesson(course_id: int, lesson_id: int, lesson: Lesson):
    """
    Update lesson by lesson id
    """
    updated_lesson = update_existing_lesson(course_id, lesson_id, lesson)

    if not updated_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    return updated_lesson


@router.delete("/courses/{course_id}/lessons/{lesson_id}", response_model=Lesson, tags=["Lesson"])
def delete_lesson(course_id: int, lesson_id: int):
    """
    Delete lesson by lesson id
    """
    removed_lesson = delete_existing_lesson(course_id, lesson_id)

    if not removed_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    return removed_lesson
