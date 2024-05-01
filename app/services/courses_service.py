from app.repositories.dbs import fake_course_db
from app.schemas.course import Course


def get_all_courses():
    return fake_course_db


def create_new_course(new_course: Course):
    new_id = max(course.get('id') for course in fake_course_db) + 1
    new_course = new_course.dict()
    new_course['id'] = new_id
    fake_course_db.append(new_course)

    return new_course


def update_existing_course(course_id: int, new_course_data: Course):
    for idx, existing_course in enumerate(fake_course_db):
        if existing_course["id"] == course_id:
            updated_existing_course = {**existing_course, **new_course_data.dict(), "id": course_id}
            fake_course_db[idx] = updated_existing_course
            return updated_existing_course

    return None


def delete_existing_course(course_id: int):
    for idx, existing_course in enumerate(fake_course_db):
        if existing_course["id"] == course_id:
            removed_course = fake_course_db.pop(idx)
            return removed_course

    return None
