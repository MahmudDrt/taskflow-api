from fastapi import FastAPI

from app.routers import health, auth, users, projects, tasks

app = FastAPI(title="TaskFlow API")

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)
