import pytest
from pydantic import ValidationError

from src.models.user_model import UserModel


class TestUserModel:
    def test_creates_with_valid_data(self) -> None:
        user: UserModel = UserModel(username="alice", password="secret")

        assert user.username == "alice"
        assert user.password == "secret"

    def test_username_is_stripped_of_whitespace(self) -> None:
        user: UserModel = UserModel(username="  alice  ", password="secret")

        assert user.username == "alice"

    def test_password_is_stripped_of_whitespace(self) -> None:
        user: UserModel = UserModel(username="alice", password="  secret  ")

        assert user.password == "secret"

    def test_empty_username_raises_validation_error(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="", password="secret")

    def test_empty_password_raises_validation_error(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="alice", password="")

    def test_whitespace_only_username_raises_validation_error(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="   ", password="secret")

    def test_whitespace_only_password_raises_validation_error(self) -> None:
        with pytest.raises(ValidationError):
            UserModel(username="alice", password="   ")
