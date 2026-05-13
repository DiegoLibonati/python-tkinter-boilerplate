from src.models.user_model import UserModel
from src.services.hash_service import HashService


class UserDAO:
    def __init__(self) -> None:
        self._users: dict[str, UserModel] = {
            "pepe": UserModel(username="pepe", password=HashService.hash("12345")),
            "ash": UserModel(username="ash", password=HashService.hash("12345")),
            "tom": UserModel(username="tom", password=HashService.hash("12345")),
        }

    def get_by_username(self, username: str) -> UserModel | None:
        return self._users.get(username)

    def exists(self, username: str) -> bool:
        return username in self._users

    def save(self, user: UserModel) -> None:
        self._users[user.username] = user
