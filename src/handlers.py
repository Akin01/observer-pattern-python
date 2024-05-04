from schema import User
import logging

logger = logging.getLogger(__name__)


class QueryError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


users_db: list[User] = []

USER_CREATE_TASK_ID = "USER_CREATE_TASK"
USER_REMOVE_TASK_ID = "USER_REMOVE_TASK"


def create_user(data: User | list[User]) -> None:
    if isinstance(data, User):
        logger.info("User has been saved")
        users_db.append(data)
    elif isinstance(data, list):
        logger.info("Users has been saved")
        users_db.extend(data)
    else:
        logging.error("Failed to save user data")
        raise ValueError("User should be a User | list[User] types")


def remove_user(user: User | int) -> None:
    user_found: User | None = None
    user_id: int = 0

    if isinstance(user, int):
        user_id = user
        user_filtered = list(filter(lambda x: x.user_id == user_id, users_db))
        user_found = user_filtered[0] if user_filtered else None
    elif isinstance(user, User):
        user_id = user.user_id
        user_index = users_db.index(user)
        user_found = users_db[user_index]

    if user_found is None:
        raise QueryError(f"User with id: {user_id} doesn't exist")

    users_db.remove(user_found)
    logger.info(f"User with id: {user_id} has been deleted")


def get_user(user_id: int) -> User:
    user = list(filter(lambda x: x.user_id == user_id, users_db))

    if not user:
        logger.error(f"User with id: {user_id} doesn't exist")
        raise QueryError("User doesn't exist")

    return user[0]


def get_all_users() -> list[User]:
    return users_db
