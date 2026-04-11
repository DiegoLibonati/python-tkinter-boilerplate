from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class TestBaseDialog:
    def test_title_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.ERROR
        assert dialog.title == "Error"

    def test_title_for_warning_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.WARNING
        assert dialog.title == "Warning"

    def test_title_for_info_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.INFO
        assert dialog.title == "Information"

    def test_message_overridden_via_constructor(self) -> None:
        dialog: BaseDialog = BaseDialog(message="Custom message")
        assert dialog.message == "Custom message"

    def test_message_none_keeps_class_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)
        assert dialog.message == MESSAGE_ERROR_APP

    def test_to_dict_contains_required_keys(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert "dialog_type" in result
        assert "title" in result
        assert "message" in result

    def test_to_dict_values_match_instance(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test msg")
        result: dict[str, Any] = dialog.to_dict()
        assert result["dialog_type"] == BaseDialog.ERROR
        assert result["message"] == "test msg"
        assert result["title"] == "Error"

    def test_open_error_calls_showerror(self) -> None:
        mock_fn: MagicMock = MagicMock()
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.ERROR
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_fn}):
            dialog.open()
        mock_fn.assert_called_once()

    def test_open_warning_calls_showwarning(self) -> None:
        mock_fn: MagicMock = MagicMock()
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.WARNING
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_fn}):
            dialog.open()
        mock_fn.assert_called_once()

    def test_open_info_calls_showinfo(self) -> None:
        mock_fn: MagicMock = MagicMock()
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.INFO
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_fn}):
            dialog.open()
        mock_fn.assert_called_once()


class TestBaseDialogError:
    def test_is_exception(self) -> None:
        err: BaseDialogError = BaseDialogError()
        assert isinstance(err, Exception)

    def test_dialog_type_is_error(self) -> None:
        err: BaseDialogError = BaseDialogError()
        assert err.dialog_type == BaseDialog.ERROR

    def test_is_base_dialog_subclass(self) -> None:
        err: BaseDialogError = BaseDialogError()
        assert isinstance(err, BaseDialog)


class TestValidationDialogError:
    def test_custom_message(self) -> None:
        err: ValidationDialogError = ValidationDialogError(message="Invalid input")
        assert err.message == "Invalid input"

    def test_is_base_dialog_error(self) -> None:
        err: ValidationDialogError = ValidationDialogError()
        assert isinstance(err, BaseDialogError)

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError(message="bad")


class TestNotFoundDialogError:
    def test_custom_message(self) -> None:
        err: NotFoundDialogError = NotFoundDialogError(message="Not found")
        assert err.message == "Not found"

    def test_is_base_dialog_error(self) -> None:
        assert isinstance(NotFoundDialogError(), BaseDialogError)


class TestConflictDialogError:
    def test_custom_message(self) -> None:
        err: ConflictDialogError = ConflictDialogError(message="Conflict")
        assert err.message == "Conflict"

    def test_is_base_dialog_error(self) -> None:
        assert isinstance(ConflictDialogError(), BaseDialogError)


class TestAuthenticationDialogError:
    def test_default_message(self) -> None:
        err: AuthenticationDialogError = AuthenticationDialogError()
        assert err.message == "Authentication error"

    def test_is_base_dialog_error(self) -> None:
        assert isinstance(AuthenticationDialogError(), BaseDialogError)


class TestBusinessDialogError:
    def test_default_message(self) -> None:
        err: BusinessDialogError = BusinessDialogError()
        assert err.message == "Business rule violated"


class TestInternalDialogError:
    def test_default_message(self) -> None:
        err: InternalDialogError = InternalDialogError()
        assert err.message == "Internal error"

    def test_custom_message(self) -> None:
        err: InternalDialogError = InternalDialogError(message="Boom")
        assert err.message == "Boom"


class TestSuccessDialogInformation:
    def test_dialog_type_is_info(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation()
        assert dialog.dialog_type == BaseDialog.INFO

    def test_default_message(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation()
        assert dialog.message == "Operation completed successfully"

    def test_custom_message(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation(message="Done!")
        assert dialog.message == "Done!"

    def test_open_calls_showinfo(self) -> None:
        mock_fn: MagicMock = MagicMock()
        dialog: SuccessDialogInformation = SuccessDialogInformation(message="Done")
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_fn}):
            dialog.open()
        mock_fn.assert_called_once()

    def test_is_not_an_exception(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation()
        assert not isinstance(dialog, Exception)


class TestDeprecatedDialogWarning:
    def test_dialog_type_is_warning(self) -> None:
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert dialog.dialog_type == BaseDialog.WARNING

    def test_default_message(self) -> None:
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert dialog.message == "This feature is deprecated"

    def test_open_calls_showwarning(self) -> None:
        mock_fn: MagicMock = MagicMock()
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_fn}):
            dialog.open()
        mock_fn.assert_called_once()
