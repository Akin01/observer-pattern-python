from pydantic import BaseModel
from typing import Generic, TypeVar
from datetime import datetime

T = TypeVar("T")
TaskId = str | list[str]


class EventPayload(BaseModel, Generic[T]):
    task_id: TaskId
    timestamp: datetime = datetime.now()
    data: T


class User(BaseModel):
    user_id: int
    name: str
    age: int
    job: str
    address: str | None
