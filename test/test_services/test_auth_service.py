from unittest.mock import MagicMock, patch

from src.constants.messages import (
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_NOT_VALID_MATCH_PASSWORD,
    MESSAGE_NOT_VALID_PASSWORD,
    MESSAGE_SUCCESS_LOGIN,
    MESSAGE_SUCCESS_REGISTER,
    MESSAGE_USER_NOT_EXISTS,
    MESSAGE_USERNAME_ALREADY_EXISTS,
)
from src.models.user_model import UserModel
from src.services.auth_service import AuthService


class TestAuthServiceLogin:
    def test_returns_none_when_username_is_empty(self, valid_credentials: dict[str, str]) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog:
            mock_dialog.return_value = MagicMock()
            result: UserModel | None = AuthService.login(username="", password=valid_credentials["password"])
        assert result is None

    def test_returns_none_when_password_is_empty(self, valid_credentials: dict[str, str]) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog:
            mock_dialog.return_value = MagicMock()
            result: UserModel | None = AuthService.login(username=valid_credentials["username"], password="")
        assert result is None

    def test_returns_none_when_username_is_whitespace(self, valid_credentials: dict[str, str]) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog:
            mock_dialog.return_value = MagicMock()
            result: UserModel | None = AuthService.login(username="   ", password=valid_credentials["password"])
        assert result is None

    def test_returns_none_when_password_is_whitespace(self, valid_credentials: dict[str, str]) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog:
            mock_dialog.return_value = MagicMock()
            result: UserModel | None = AuthService.login(username=valid_credentials["username"], password="   ")
        assert result is None

    def test_validation_dialog_called_when_fields_are_empty(self) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog_class:
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            AuthService.login(username="", password="")

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_FIELDS)
        mock_dialog.dialog.assert_called_once()

    def test_returns_none_when_user_not_found(self, invalid_credentials: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.NotFoundDialogError") as mock_dialog,
        ):
            mock_dao_class.return_value.get_by_username.return_value = None
            mock_dialog.return_value = MagicMock()
            result: UserModel | None = AuthService.login(
                username=invalid_credentials["username"],
                password=invalid_credentials["password"],
            )
        assert result is None

    def test_not_found_dialog_called_when_user_does_not_exist(self, invalid_credentials: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.NotFoundDialogError") as mock_dialog_class,
        ):
            mock_dao_class.return_value.get_by_username.return_value = None
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            AuthService.login(
                username=invalid_credentials["username"],
                password=invalid_credentials["password"],
            )

        mock_dialog_class.assert_called_once_with(message=MESSAGE_USER_NOT_EXISTS)
        mock_dialog.dialog.assert_called_once()

    def test_returns_none_when_password_does_not_match(self, sample_user: UserModel, invalid_credentials: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.HashService.verify", return_value=False),
            patch("src.services.auth_service.ValidationDialogError") as mock_dialog,
        ):
            mock_dao_class.return_value.get_by_username.return_value = sample_user
            mock_dialog.return_value = MagicMock()
            result: UserModel | None = AuthService.login(
                username=sample_user.username,
                password=invalid_credentials["password"],
            )
        assert result is None

    def test_validation_dialog_called_when_password_wrong(self, sample_user: UserModel, invalid_credentials: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.HashService.verify", return_value=False),
            patch("src.services.auth_service.ValidationDialogError") as mock_dialog_class,
        ):
            mock_dao_class.return_value.get_by_username.return_value = sample_user
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            AuthService.login(username=sample_user.username, password=invalid_credentials["password"])

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_PASSWORD)
        mock_dialog.dialog.assert_called_once()

    def test_returns_user_on_successful_login(self, sample_user: UserModel, valid_credentials: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.HashService.verify", return_value=True),
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog,
        ):
            mock_dao_class.return_value.get_by_username.return_value = sample_user
            mock_dialog.return_value = MagicMock()
            result: UserModel | None = AuthService.login(
                username=valid_credentials["username"],
                password=valid_credentials["password"],
            )
        assert result == sample_user

    def test_success_dialog_called_on_login(self, sample_user: UserModel, valid_credentials: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.HashService.verify", return_value=True),
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class,
        ):
            mock_dao_class.return_value.get_by_username.return_value = sample_user
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            AuthService.login(
                username=valid_credentials["username"],
                password=valid_credentials["password"],
            )

        mock_dialog_class.assert_called_once_with(message=MESSAGE_SUCCESS_LOGIN)
        mock_dialog.dialog.assert_called_once()


class TestAuthServiceRegister:
    def test_returns_false_when_username_is_empty(self, registration_data: dict[str, str]) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog:
            mock_dialog.return_value = MagicMock()
            result: bool = AuthService.register(
                username="",
                password=registration_data["password"],
                confirm_password=registration_data["confirm_password"],
            )
        assert result is False

    def test_returns_false_when_password_is_empty(self, registration_data: dict[str, str]) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog:
            mock_dialog.return_value = MagicMock()
            result: bool = AuthService.register(
                username=registration_data["username"],
                password="",
                confirm_password="",
            )
        assert result is False

    def test_returns_false_when_username_is_whitespace(self, registration_data: dict[str, str]) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog:
            mock_dialog.return_value = MagicMock()
            result: bool = AuthService.register(
                username="   ",
                password=registration_data["password"],
                confirm_password=registration_data["confirm_password"],
            )
        assert result is False

    def test_validation_dialog_called_when_fields_are_empty(self) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog_class:
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            AuthService.register(username="", password="", confirm_password="")

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_FIELDS)
        mock_dialog.dialog.assert_called_once()

    def test_returns_false_when_passwords_do_not_match(self, registration_data: dict[str, str]) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog:
            mock_dialog.return_value = MagicMock()
            result: bool = AuthService.register(
                username=registration_data["username"],
                password=registration_data["password"],
                confirm_password="different_password",
            )
        assert result is False

    def test_validation_dialog_called_when_passwords_do_not_match(self, registration_data: dict[str, str]) -> None:
        with patch("src.services.auth_service.ValidationDialogError") as mock_dialog_class:
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            AuthService.register(
                username=registration_data["username"],
                password=registration_data["password"],
                confirm_password="different_password",
            )

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_MATCH_PASSWORD)
        mock_dialog.dialog.assert_called_once()

    def test_returns_false_when_username_already_exists(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.ConflictDialogError") as mock_dialog,
        ):
            mock_dao_class.return_value.exists.return_value = True
            mock_dialog.return_value = MagicMock()
            result: bool = AuthService.register(
                username=registration_data["username"],
                password=registration_data["password"],
                confirm_password=registration_data["confirm_password"],
            )
        assert result is False

    def test_conflict_dialog_called_when_username_exists(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.ConflictDialogError") as mock_dialog_class,
        ):
            mock_dao_class.return_value.exists.return_value = True
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            AuthService.register(
                username=registration_data["username"],
                password=registration_data["password"],
                confirm_password=registration_data["confirm_password"],
            )

        mock_dialog_class.assert_called_once_with(message=MESSAGE_USERNAME_ALREADY_EXISTS)
        mock_dialog.dialog.assert_called_once()

    def test_returns_true_on_successful_register(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.HashService.hash", return_value="hashed"),
            patch("src.services.auth_service.UserModel"),
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog,
        ):
            mock_dao_class.return_value.exists.return_value = False
            mock_dialog.return_value = MagicMock()
            result: bool = AuthService.register(
                username=registration_data["username"],
                password=registration_data["password"],
                confirm_password=registration_data["confirm_password"],
            )
        assert result is True

    def test_user_is_saved_on_successful_register(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.HashService.hash", return_value="hashed"),
            patch("src.services.auth_service.UserModel"),
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog,
        ):
            mock_dao: MagicMock = MagicMock()
            mock_dao.exists.return_value = False
            mock_dao_class.return_value = mock_dao
            mock_dialog.return_value = MagicMock()
            AuthService.register(
                username=registration_data["username"],
                password=registration_data["password"],
                confirm_password=registration_data["confirm_password"],
            )

        mock_dao.save.assert_called_once()

    def test_password_is_hashed_on_register(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.HashService.hash") as mock_hash,
            patch("src.services.auth_service.UserModel"),
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog,
        ):
            mock_dao_class.return_value.exists.return_value = False
            mock_hash.return_value = "hashed"
            mock_dialog.return_value = MagicMock()
            AuthService.register(
                username=registration_data["username"],
                password=registration_data["password"],
                confirm_password=registration_data["confirm_password"],
            )

        mock_hash.assert_called_once_with(registration_data["password"])

    def test_success_dialog_called_on_register(self, registration_data: dict[str, str]) -> None:
        with (
            patch("src.services.auth_service.UserDAO") as mock_dao_class,
            patch("src.services.auth_service.HashService.hash", return_value="hashed"),
            patch("src.services.auth_service.UserModel"),
            patch("src.services.auth_service.SuccessDialogInformation") as mock_dialog_class,
        ):
            mock_dao_class.return_value.exists.return_value = False
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            AuthService.register(
                username=registration_data["username"],
                password=registration_data["password"],
                confirm_password=registration_data["confirm_password"],
            )

        mock_dialog_class.assert_called_once_with(message=MESSAGE_SUCCESS_REGISTER)
        mock_dialog.dialog.assert_called_once()
