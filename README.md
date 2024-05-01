# Request:
Our Frontend dev specifically asked for these endpoints for the students to use: 
- Get a list of all courses, telling which ones the student can access 
- Get lessons for a course, telling which ones the student can access 
- Get lesson details for answering its questions Take a lesson (to avoid several requests, they asked to send all answers in one go) 
- Basic CRUD for courses, lessons and questions 

# Considerations
 This project has the following considerations:
- Simulate the data using a static data
- Add configuration for docker (including postgres, but implementation is missing at this time)


# Steps for run this project

1. Create and environment:
```
python3 -m venv venv
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run project:
```
docker-compose -p controlhub-challenge up
```

# TEST ENDPOINTS -> examples:  

Get courses:
```
GET http://localhost:8000/courses
```

Create course:
```
POST http://localhost:8000/courses

body to send:
{
    "title": "New Python Course",
    "description": "A comprehensive course on Python programming."
}
```

Update course:
```
PUT http://localhost:8000/courses/3

body to send:
{
    "title": "Updated Python Course",
    "description": "An updated comprehensive course on Python programming."
}
```

Update course:
```
DELETE http://localhost:8000/courses/3
```

Get lessons by course:
```
GET http://localhost:8000/courses/1/lessons
```

Create new lesson:
```
POST http://localhost:8000/courses/1/lessons

body to send:
{
  "title": "Lesson on REST APIs",
  "description": "Learn how to create RESTful APIs with FastAPI."
}
```

Update lesson:
```
UPDATE http://localhost:8000/courses/1/lessons/3

body to send:
{
  "title": "Updated Lesson on REST APIs",
  "description": "An updated comprehensive guide on how to create RESTful APIs using FastAPI."
}
```

Delete lesson:
```
DELETE http://localhost:8000/courses/1/lessons/3
```

Questions by lesson id:
```
GET http://localhost:8000/lessons/1/questions
```

Create new question to lesson:
```
POST http://localhost:8000/lessons/1/questions

body to send:
{
  "text": "Which of the following is a mutable data type in Python?",
  "options": ["Tuple", "String", "List", "Integer"],
  "correct_answer": ["list"]
}
```

Update question:
```
UPDATE http://localhost:8000/lessons/1/questions/3

body to send:
{
  "text": "Which of the following data types is mutable in Python updated?",
  "options": ["Tuple", "String", "List", "Frozen Set"],
  "correct_answer": ["List"]
}
```

Delete question:
```
DELETE http://localhost:8000/lessons/1/questions/3
```

Send answer by lesson:
```
POST http://localhost:8000/lessons/1/take

body to send:
[
    {
        "question_id": 1,
        "selected_options": ["Programming language"]
    },
    {
        "question_id": 2,
        "selected_options": ["list"]
    }
]
```