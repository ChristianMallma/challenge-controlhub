from fastapi import APIRouter, HTTPException
from typing import List

from app.api.dbs import fake_lesson_db, fake_course_db
from app.models.lesson import Lesson

router = APIRouter()


# Get lessons by id course
@router.get("/courses/{course_id}/lessons", response_model=List[Lesson])
def get_lessons_for_course(course_id: int):
    lessons = [lesson for lesson in fake_lesson_db if lesson["course_id"] == course_id]
    if not lessons:
        raise HTTPException(status_code=404, detail="Course not found or no lessons available")
    return lessons


# Create lesson
@router.post("/courses/{course_id}/lessons", response_model=Lesson)
def create_lesson(course_id: int, lesson: Lesson):
    if not any(course['id'] == course_id for course in fake_course_db):
        raise HTTPException(status_code=404, detail="Course not found")
    new_id = max((l['id'] for l in fake_lesson_db if l['course_id'] == course_id), default=0) + 1
    new_lesson = lesson.dict()
    new_lesson['id'] = new_id
    new_lesson['course_id'] = course_id
    fake_lesson_db.append(new_lesson)
    return new_lesson


# Update lesson
@router.put("/courses/{course_id}/lessons/{lesson_id}", response_model=Lesson)
def update_lesson(course_id: int, lesson_id: int, lesson: Lesson):
    for idx, existing_lesson in enumerate(fake_lesson_db):
        if existing_lesson['id'] == lesson_id and existing_lesson['course_id'] == course_id:
            updated_lesson = {**existing_lesson, **lesson.dict(), "id": lesson_id, "course_id": course_id}
            fake_lesson_db[idx] = updated_lesson
            return updated_lesson
    raise HTTPException(status_code=404, detail="Lesson not found")


# Delete lesson
@router.delete("/courses/{course_id}/lessons/{lesson_id}", response_model=Lesson)
def delete_lesson(course_id: int, lesson_id: int):
    for idx, existing_lesson in enumerate(fake_lesson_db):
        if existing_lesson['id'] == lesson_id and existing_lesson['course_id'] == course_id:
            removed_lesson = fake_lesson_db.pop(idx)
            return removed_lesson
    raise HTTPException(status_code=404, detail="Lesson not found")
