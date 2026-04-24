from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.pending
    deadline: datetime | None = None
    project_id: int


class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus
    deadline: datetime | None = None


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    status: TaskStatus
    deadline: datetime | None
    project_id: int
    created_at: datetime
