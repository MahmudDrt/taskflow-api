from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.project import Project
from app.models.user import User
from app.dependencies.auth import get_current_user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    return project