from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import (
    MESSAGE_ALREADY_EXISTS_USERNAME,
    MESSAGE_NOT_EXISTS_USER,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_NOT_VALID_MATCH_PASSWORD,
    MESSAGE_NOT_VALID_PASSWORD,
    MESSAGE_SUCCESS_LOGIN,
    MESSAGE_SUCCESS_REGISTER,
)
from src.models.user_model import UserModel
from src.services.auth_service import AuthService
from src.utils.dialogs import ConflictDialogError, NotFoundDialogError, ValidationDialogError


@pytest.fixture
def mock_dao() -> MagicMock:
    return MagicMock()


@pytest.fixture
def auth_service(mock_dao: MagicMock) -> AuthService:
    return AuthService(dao=mock_dao)


class TestAuthServiceLogin:
    def test_raises_validation_error_when_username_is_empty(self, auth_service: AuthService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.login(username="", password="pass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_password_is_empty(self, auth_service: AuthService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.login(username="user", password="")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_username_is_whitespace(self, auth_service: AuthService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.login(username="   ", password="pass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_password_is_whitespace(self, auth_service: AuthService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.login(username="user", password="   ")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_not_found_error_when_user_does_not_exist(self, auth_service: AuthService, mock_dao: MagicMock, invalid_credentials: dict[str, str]) -> None:
        mock_dao.get_by_username.return_value = None
        with pytest.raises(NotFoundDialogError) as exc_info:
            auth_service.login(**invalid_credentials)
        assert exc_info.value.message == MESSAGE_NOT_EXISTS_USER

    def test_raises_validation_error_when_password_is_wrong(self, auth_service: AuthService, mock_dao: MagicMock, sample_user: UserModel) -> None:
        mock_dao.get_by_username.return_value = sample_user
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.login(username="testuser", password="wrongpass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_PASSWORD

    def test_returns_user_on_success(self, auth_service: AuthService, mock_dao: MagicMock, sample_user: UserModel) -> None:
        mock_dao.get_by_username.return_value = sample_user
        with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            result: UserModel = auth_service.login(username="testuser", password="testpass")

        assert result is sample_user

    def test_success_dialog_opened_on_login(self, auth_service: AuthService, mock_dao: MagicMock, sample_user: UserModel) -> None:
        mock_dao.get_by_username.return_value = sample_user
        with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class:
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            auth_service.login(username="testuser", password="testpass")

        mock_dialog_class.assert_called_once_with(message=MESSAGE_SUCCESS_LOGIN)
        mock_dialog.open.assert_called_once()

    def test_get_by_username_called_with_correct_username(self, auth_service: AuthService, mock_dao: MagicMock) -> None:
        mock_dao.get_by_username.return_value = None
        try:
            auth_service.login(username="testuser", password="pass")
        except NotFoundDialogError:
            pass

        mock_dao.get_by_username.assert_called_once_with("testuser")


class TestAuthServiceRegister:
    def test_raises_validation_error_when_username_is_empty(self, auth_service: AuthService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.register(username="", password="pass", confirm_password="pass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_password_is_empty(self, auth_service: AuthService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.register(username="user", password="", confirm_password="pass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_confirm_password_is_empty(self, auth_service: AuthService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.register(username="user", password="pass", confirm_password="")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_username_is_whitespace(self, auth_service: AuthService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.register(username="   ", password="pass", confirm_password="pass")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_password_is_whitespace(self, auth_service: AuthService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.register(username="user", password="   ", confirm_password="   ")
        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_raises_validation_error_when_passwords_do_not_match(self, auth_service: AuthService) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            auth_service.register(username="user", password="pass1", confirm_password="pass2")
        assert exc_info.value.message == MESSAGE_NOT_VALID_MATCH_PASSWORD

    def test_raises_conflict_error_when_username_already_exists(
        self, auth_service: AuthService, mock_dao: MagicMock, registration_data: dict[str, str]
    ) -> None:
        mock_dao.exists.return_value = True
        with pytest.raises(ConflictDialogError) as exc_info:
            auth_service.register(**registration_data)
        assert exc_info.value.message == MESSAGE_ALREADY_EXISTS_USERNAME

    def test_returns_true_on_success(self, auth_service: AuthService, mock_dao: MagicMock, registration_data: dict[str, str]) -> None:
        mock_dao.exists.return_value = False
        with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            result: bool = auth_service.register(**registration_data)

        assert result is True

    def test_user_is_saved_on_success(self, auth_service: AuthService, mock_dao: MagicMock, registration_data: dict[str, str]) -> None:
        mock_dao.exists.return_value = False
        with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            auth_service.register(**registration_data)

        mock_dao.save.assert_called_once()

    def test_saved_user_has_correct_username(self, auth_service: AuthService, mock_dao: MagicMock, registration_data: dict[str, str]) -> None:
        mock_dao.exists.return_value = False
        with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            auth_service.register(**registration_data)

        saved_user: UserModel = mock_dao.save.call_args[0][0]
        assert saved_user.username == registration_data["username"]

    def test_saved_user_has_hashed_password(self, auth_service: AuthService, mock_dao: MagicMock, registration_data: dict[str, str]) -> None:
        mock_dao.exists.return_value = False
        with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            auth_service.register(**registration_data)

        saved_user: UserModel = mock_dao.save.call_args[0][0]
        assert saved_user.password != registration_data["password"]

    def test_success_dialog_opened_on_register(self, auth_service: AuthService, mock_dao: MagicMock, registration_data: dict[str, str]) -> None:
        mock_dao.exists.return_value = False
        with patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class:
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            auth_service.register(**registration_data)

        mock_dialog_class.assert_called_once_with(message=MESSAGE_SUCCESS_REGISTER)
        mock_dialog.open.assert_called_once()
