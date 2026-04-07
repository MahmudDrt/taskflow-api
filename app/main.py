from fastapi import FastAPI

from app.routes import health, auth, users, projects, tasks
from app.database.database import Base, engine
from app.models.user import User
from app.models.project import Project
from app.models.task import Task

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)