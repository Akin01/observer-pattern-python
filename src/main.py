from schema import User, EventPayload
from event_emitter import EventEmitter
from handlers import (
    create_user,
    get_all_users,
    get_user, remove_user,
    USER_CREATE_TASK_ID,
    USER_REMOVE_TASK_ID
)
import logging

logging.basicConfig(level=logging.INFO,
                    format="[%(name)s] - [%(levelname)s] -> %(message)s")
logger = logging.getLogger(__name__)

users: list[User] = [
    User(user_id=1, name="Ainul Yaqin", age=23,
         job="Software Engineer", address="Lombok"),
    User(user_id=2, name="Farrel Abyansyah", age=23,
         job="Frontend Engineer", address="Pamulang")
]

william = User(user_id=3, name="William Sitohang",
               age=23, job="IoT Engineer", address="Riau")

event_emitter = EventEmitter()

event_emitter.register_event(USER_CREATE_TASK_ID, create_user)

user_payload_event = EventPayload[list[User]](
    task_id=USER_CREATE_TASK_ID, data=users)
event_emitter.dispatch_event(USER_CREATE_TASK_ID, user_payload_event)

user_from_db = get_all_users()
logger.info(f"Users: {user_from_db}")
logger.info(f"Total users: {len(user_from_db)}")

event_emitter.dispatch_event(USER_CREATE_TASK_ID, EventPayload[User](
    task_id=USER_CREATE_TASK_ID, data=william))

user_from_db = get_all_users()
logger.info(f"Users: {user_from_db}")
logger.info(f"Total users: {len(user_from_db)}")

event_emitter.remove_event(USER_CREATE_TASK_ID)
event_emitter.register_event(USER_REMOVE_TASK_ID, remove_user)

logger.info(f"Remove user: {william.user_id}")
event_emitter.dispatch_event(USER_REMOVE_TASK_ID, EventPayload[int](task_id=USER_REMOVE_TASK_ID, data=william.user_id))

# Cannot retrieve william data because has been removed
logger.info(f"William data: {get_user(william.user_id)}")
