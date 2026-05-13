from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BaseDialogNotification,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class TestBaseDialog:
    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message_equals_error_app_constant(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.message == MESSAGE_ERROR_APP

    def test_custom_message_overrides_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message="custom message")

        assert dialog.message == "custom message"

    def test_title_returns_error_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.title == "Error"

    def test_to_dict_contains_required_keys(self) -> None:
        dialog: BaseDialog = BaseDialog()

        result: dict[str, Any] = dialog.to_dict()

        assert "dialog_type" in result
        assert "title" in result
        assert "message" in result

    def test_to_dict_message_matches_instance_message(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test msg")

        result: dict[str, Any] = dialog.to_dict()

        assert result["message"] == "test msg"

    def test_open_calls_showerror_for_error_dialog_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once()


class TestBaseDialogError:
    def test_is_exception(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert isinstance(error, Exception)

    def test_is_base_dialog(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert isinstance(error, BaseDialog)

    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert error.dialog_type == BaseDialog.ERROR

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError(message="test error")


class TestValidationDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert isinstance(ValidationDialogError(), BaseDialogError)

    def test_custom_message_is_stored(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="invalid input")

        assert error.message == "invalid input"

    def test_can_be_caught_as_base_dialog_error(self) -> None:
        with pytest.raises(BaseDialogError):
            raise ValidationDialogError()


class TestNotFoundDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert isinstance(NotFoundDialogError(), BaseDialogError)

    def test_custom_message_is_stored(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError(message="not found")

        assert error.message == "not found"


class TestConflictDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert isinstance(ConflictDialogError(), BaseDialogError)

    def test_custom_message_is_stored(self) -> None:
        error: ConflictDialogError = ConflictDialogError(message="already exists")

        assert error.message == "already exists"


class TestAuthenticationDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert isinstance(AuthenticationDialogError(), BaseDialogError)


class TestBusinessDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert isinstance(BusinessDialogError(), BaseDialogError)


class TestInternalDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert isinstance(InternalDialogError(), BaseDialogError)

    def test_custom_message_is_stored(self) -> None:
        error: InternalDialogError = InternalDialogError(message="internal failure")

        assert error.message == "internal failure"


class TestSuccessDialogInformation:
    def test_is_base_dialog_notification(self) -> None:
        assert isinstance(SuccessDialogInformation(), BaseDialogNotification)

    def test_dialog_type_is_info(self) -> None:
        notification: SuccessDialogInformation = SuccessDialogInformation()

        assert notification.dialog_type == BaseDialog.INFO

    def test_title_returns_information(self) -> None:
        notification: SuccessDialogInformation = SuccessDialogInformation()

        assert notification.title == "Information"

    def test_custom_message_is_stored(self) -> None:
        notification: SuccessDialogInformation = SuccessDialogInformation(message="done")

        assert notification.message == "done"

    def test_open_calls_showinfo(self) -> None:
        notification: SuccessDialogInformation = SuccessDialogInformation()
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_handler}):
            notification.open()

        mock_handler.assert_called_once()


class TestDeprecatedDialogWarning:
    def test_is_base_dialog_notification(self) -> None:
        assert isinstance(DeprecatedDialogWarning(), BaseDialogNotification)

    def test_dialog_type_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert warning.dialog_type == BaseDialog.WARNING

    def test_open_calls_showwarning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_handler}):
            warning.open()

        mock_handler.assert_called_once()
