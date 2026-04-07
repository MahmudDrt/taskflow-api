from datetime import datetime
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: str = "pending"
    deadline: datetime | None = None
    project_id: int


class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    status: str
    deadline: datetime | None = None