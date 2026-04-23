from fastapi import FastAPI

from app.routes import health, auth, users, projects, tasks

app = FastAPI()

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)