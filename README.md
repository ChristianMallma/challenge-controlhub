# Request:
Our Frontend dev specifically asked for these endpoints for the students to use: 
- Get a list of all courses, telling which ones the student can access 
- Get lessons for a course, telling which ones the student can access 
- Get lesson details for answering its questions Take a lesson (to avoid several requests, they asked to send all answers in one go) 
- Basic CRUD for courses, lessons and questions 

# Considerations
 This project has the following considerations:
- Simulate the data using a static data
- Developed up to CRUD of courses (lessons and questions are missing)


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
uvicorn app.main:app --reload
```