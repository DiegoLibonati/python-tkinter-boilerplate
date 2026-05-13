from unittest.mock import patch

import pytest

from src.data_access.user_dao import UserDAO
from src.models.user_model import UserModel
from src.services.auth_service import AuthService
from src.utils.dialogs import ConflictDialogError, NotFoundDialogError, ValidationDialogError


class TestAuthService:
    def test_login_raises_validation_error_when_username_empty(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(ValidationDialogError):
            service.login(username="", password="12345")

    def test_login_raises_validation_error_when_password_empty(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(ValidationDialogError):
            service.login(username="pepe", password="")

    def test_login_raises_validation_error_when_username_whitespace(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(ValidationDialogError):
            service.login(username="   ", password="12345")

    def test_login_raises_validation_error_when_password_whitespace(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(ValidationDialogError):
            service.login(username="pepe", password="   ")

    def test_login_raises_not_found_error_when_user_does_not_exist(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(NotFoundDialogError):
            service.login(username="nonexistent", password="12345")

    def test_login_raises_validation_error_when_password_incorrect(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(ValidationDialogError):
            service.login(username="pepe", password="wrongpassword")

    def test_login_returns_user_model_on_valid_credentials(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with patch("src.services.auth_service.SuccessDialogInformation"):
            user: UserModel = service.login(username="pepe", password="12345")

        assert isinstance(user, UserModel)
        assert user.username == "pepe"

    def test_register_raises_validation_error_when_username_empty(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(ValidationDialogError):
            service.register(username="", password="pass", confirm_password="pass")

    def test_register_raises_validation_error_when_password_empty(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(ValidationDialogError):
            service.register(username="newuser", password="", confirm_password="")

    def test_register_raises_validation_error_when_username_whitespace(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(ValidationDialogError):
            service.register(username="   ", password="pass", confirm_password="pass")

    def test_register_raises_validation_error_when_passwords_do_not_match(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(ValidationDialogError):
            service.register(username="newuser", password="pass1", confirm_password="pass2")

    def test_register_raises_conflict_error_when_username_already_exists(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with pytest.raises(ConflictDialogError):
            service.register(username="pepe", password="pass", confirm_password="pass")

    def test_register_returns_true_on_success(self) -> None:
        service: AuthService = AuthService(dao=UserDAO())

        with patch("src.services.auth_service.SuccessDialogInformation"):
            result: bool = service.register(
                username="brandnewuser", password="pass", confirm_password="pass"
            )

        assert result is True

    def test_register_saves_user_in_dao(self) -> None:
        dao: UserDAO = UserDAO()
        service: AuthService = AuthService(dao=dao)

        with patch("src.services.auth_service.SuccessDialogInformation"):
            service.register(username="saveduser", password="pass", confirm_password="pass")

        assert dao.exists("saveduser") is True
