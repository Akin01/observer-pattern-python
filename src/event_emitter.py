from typing import Callable
from schema import TaskId, EventPayload
import logging
from decorators import singleton

logger = logging.getLogger(__name__)


class EventBrokerError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


@singleton
class EventEmitter:
    event_cache: dict[str, list[Callable]] = {}

    def __init__(self, predefined_task: TaskId | None = None) -> None:
        if predefined_task:
            for task in predefined_task:
                self.event_cache[task] = []

    def register_event(self, task_id: TaskId, handler: Callable) -> None:
        event = self.event_cache.get(task_id)

        if event is None:
            self.event_cache[task_id] = [handler]
            logger.info(f"Event <{task_id}> with handler <{handler.__name__}> has been registered")
        else:
            self.event_cache[task_id].append(handler)
            logger.info(f"Handler <{handler.__name__}> has been added to existing event <{task_id}>")

    def remove_event(self, task_id: TaskId) -> None:
        event = self.event_cache.get(task_id)

        if event is None:
            raise EventBrokerError(f"Event <{task_id}> doesn't exist")
        else:
            del self.event_cache[task_id]
            logger.info(f"Event <{task_id}> has been deleted")

    def dispatch_event(self, task_id: TaskId, payload: EventPayload) -> None:
        event = self.event_cache.get(task_id)

        if event is None:
            raise EventBrokerError(f"Event <{task_id}> doesn't exist")

        for handler in event:
            handler(payload.data)

        logger.info(f"Event with task_id: {payload.task_id} has been executed")
        logger.info(f"Payload: {payload.data}")
        logger.info(f"Created at: {payload.timestamp.strftime('%m-%d-%Y %H:%M:%S')}")
