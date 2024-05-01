from app.repositories.dbs import fake_question_db, fake_lesson_db
from app.schemas.question import Question
from app.schemas.answer import Answer


def create_new_question(lesson_id: int, question: Question):
    if not any(lesson['id'] == lesson_id for lesson in fake_lesson_db):
        return None

    new_id = max((q['id'] for q in fake_question_db if q['lesson_id'] == lesson_id), default=0) + 1
    new_question = question.dict()
    new_question['id'] = new_id
    new_question['lesson_id'] = lesson_id
    fake_question_db.append(new_question)

    return new_question


def update_existing_question(lesson_id: int, question_id: int, question: Question):
    for idx, existing_question in enumerate(fake_question_db):
        if existing_question['id'] == question_id and existing_question['lesson_id'] == lesson_id:
            updated_question = {**existing_question, **question.dict(), "id": question_id, "lesson_id": lesson_id}
            fake_question_db[idx] = updated_question
            return updated_question

    return None


def delete_existing_question(lesson_id: int, question_id: int):
    for idx, existing_question in enumerate(fake_question_db):
        if existing_question['id'] == question_id and existing_question['lesson_id'] == lesson_id:
            removed_question = fake_question_db.pop(idx)
            return removed_question

    return None


def get_questions_by_lesson_id(lesson_id: int):
    return [question for question in fake_question_db if question['lesson_id'] == lesson_id]


def get_lesson_details_by_lesson_id(lesson_id: int):
    lesson = next((lesson for lesson in fake_lesson_db if lesson["id"] == lesson_id), None)

    if not lesson:
        return None

    questions = [Question(**question) for question in fake_question_db if question["lesson_id"] == lesson_id]
    return {**lesson, "questions": questions}


def submit_answers(lesson_id: int, answers: [Answer]):
    correct_count = 0
    APROBATION_UMBRAL = 0.6

    for answer in answers:
        correct_answer = next((q['correct_answer'] for q in fake_question_db if q['id'] == answer.question_id), None)

        if correct_answer is None:
            return None

        if set(answer.selected_options) == set(correct_answer):
            correct_count += 1

    total_questions = len([q for q in fake_question_db if q['lesson_id'] == lesson_id])
    is_passed = correct_count >= (total_questions * APROBATION_UMBRAL)

    return {"total_questions": total_questions, "correct_answers": correct_count, "passed": is_passed}
