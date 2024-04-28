# /app/main.py

from fastapi import FastAPI

from app.api.routers.courses_router import router as courses_router
from app.api.routers.lessons_router import router as lessons_router

app = FastAPI()

app.include_router(courses_router)
app.include_router(lessons_router)
