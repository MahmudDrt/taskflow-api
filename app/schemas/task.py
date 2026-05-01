from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class TaskCreate(BaseModel):
    title: str = Field(..., examples=["Implement authentication"])
    description: str | None = Field(
        default=None,
        examples=["Add JWT authentication for users"],
    )
    status: TaskStatus = Field(
        default=TaskStatus.pending,
        description=(
            "Task status. Available values: " "pending, in_progress, completed"
        ),
        examples=["pending"],
    )
    deadline: datetime | None = Field(
        default=None,
        examples=["2026-05-10T12:00:00"],
    )
    project_id: int = Field(..., examples=[1])


class TaskUpdate(BaseModel):
    title: str = Field(..., examples=["Update README"])
    description: str | None = Field(
        default=None,
        examples=["Add Docker launch instructions"],
    )
    status: TaskStatus = Field(
        ...,
        description=(
            "Task status. Available values: " "pending, in_progress, completed"
        ),
        examples=["in_progress"],
    )
    deadline: datetime | None = Field(
        default=None,
        examples=["2026-05-10T12:00:00"],
    )


class TaskPatch(BaseModel):
    title: str | None = Field(
        default=None,
        examples=["Fix task filter"],
    )
    description: str | None = Field(
        default=None,
        examples=["Update only task description"],
    )
    status: TaskStatus | None = Field(
        default=None,
        description=(
            "Task status. Available values: " "pending, in_progress, completed"
        ),
        examples=["completed"],
    )
    deadline: datetime | None = Field(
        default=None,
        examples=["2026-05-10T12:00:00"],
    )


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    status: TaskStatus
    deadline: datetime | None
    project_id: int
    created_at: datetime
