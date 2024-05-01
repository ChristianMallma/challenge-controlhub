from app.repositories.dbs import fake_lesson_db, fake_course_db
from app.schemas.lesson import Lesson


def get_lessons_by_course(course_id: int):
    lessons = [lesson for lesson in fake_lesson_db if lesson["course_id"] == course_id]

    return lessons


def create_new_lesson(course_id: int, lesson: Lesson):
    if not any(course['id'] == course_id for course in fake_course_db):
        return None

    new_id = max((l['id'] for l in fake_lesson_db if l['course_id'] == course_id), default=0) + 1
    new_lesson = lesson.dict()
    new_lesson['id'] = new_id
    new_lesson['course_id'] = course_id
    fake_lesson_db.append(new_lesson)

    return new_lesson


def update_existing_lesson(course_id: int, lesson_id: int, lesson: Lesson):
    for idx, existing_lesson in enumerate(fake_lesson_db):
        if existing_lesson['id'] == lesson_id and existing_lesson['course_id'] == course_id:
            updated_lesson = {**existing_lesson, **lesson.dict(), "id": lesson_id, "course_id": course_id}
            fake_lesson_db[idx] = updated_lesson
            return updated_lesson

    return None


def delete_existing_lesson(course_id: int, lesson_id: int):
    for idx, existing_lesson in enumerate(fake_lesson_db):
        if existing_lesson['id'] == lesson_id and existing_lesson['course_id'] == course_id:
            removed_lesson = fake_lesson_db.pop(idx)
            return removed_lesson

    return None
