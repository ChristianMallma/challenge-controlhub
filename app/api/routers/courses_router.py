from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas.course import Course
from app.services.courses_service import get_all_courses, create_new_course, update_existing_course, \
    delete_existing_course

router = APIRouter()


@router.get("/courses", response_model=List[Course], tags=["Course"])
def get_courses():
    """
    Get all courses
    """
    courses = get_all_courses()
    return courses


@router.post("/courses", response_model=Course, tags=["Course"])
def create_course(new_course: Course):
    """
    Create a new course
    """
    new_course = create_new_course(new_course)
    return new_course


@router.put("/courses/{course_id}", response_model=Course, tags=["Course"])
def update_course(course_id: int, new_course_data: Course):
    """
    Get course by course id
    """
    updated_existing_course = update_existing_course(course_id, new_course_data)

    if not updated_existing_course:
        raise HTTPException(status_code=404, detail="Course not found")

    return updated_existing_course


@router.delete("/courses/{course_id}", response_model=Course, tags=["Course"])
def delete_course(course_id: int):
    """
    Delete course by course id
    """
    removed_course = delete_existing_course(course_id)

    if not removed_course:
        raise HTTPException(status_code=404, detail="Course not found")

    return removed_course
