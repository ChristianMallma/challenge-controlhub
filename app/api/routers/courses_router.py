from fastapi import APIRouter, HTTPException
from typing import List

from app.api.dbs import fake_course_db
from app.models.course import Course

router = APIRouter()


@router.get("/courses", response_model=List[Course])
def get_courses():
    return fake_course_db


@router.post("/courses", response_model=Course)
def create_course(new_course: Course):
    new_id = max(course.get('id') for course in fake_course_db) + 1
    new_course = new_course.dict()
    new_course['id'] = new_id
    fake_course_db.append(new_course)
    return new_course


@router.put("/courses/{course_id}", response_model=Course)
def update_course(course_id: int, new_course_data: Course):
    for idx, existing_course in enumerate(fake_course_db):
        if existing_course["id"] == course_id:
            updated_existing_course = {**existing_course, **new_course_data.dict(), "id": course_id}
            fake_course_db[idx] = updated_existing_course
            return updated_existing_course
    raise HTTPException(status_code=404, detail="Course not found")


@router.delete("/courses/{course_id}", response_model=Course)
def delete_course(course_id: int):
    for idx, existing_course in enumerate(fake_course_db):
        if existing_course["id"] == course_id:
            removed_course = fake_course_db.pop(idx)
            return removed_course
    raise HTTPException(status_code=404, detail="Course not found")

