"""
This fake data needs to be changed in the future commits -> replace it with Postgresl
"""

# TODO: Static data for courses
fake_course_db = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "description": "Learn the basics of Python."
    },
    {
        "id": 2,
        "title": "Data Science with Python",
        "description": "Introduction to data science concepts."
    },
]


# TODO: Static data for questions
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


# TODO: Static data for lessons
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
