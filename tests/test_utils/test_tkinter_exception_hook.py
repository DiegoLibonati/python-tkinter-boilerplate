from unittest.mock import MagicMock, patch

from src.utils.dialogs import ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


class TestTkinterExceptionHook:
    def test_calls_open_when_exc_value_is_base_dialog(self) -> None:
        dialog: ValidationDialogError = ValidationDialogError(message="test error")
        dialog.open = MagicMock()

        tkinter_exception_hook(ValidationDialogError, dialog, None)

        dialog.open.assert_called_once()

    def test_creates_internal_error_for_non_dialog_exception(self) -> None:
        exc: ValueError = ValueError("something broke")
        mock_instance: MagicMock = MagicMock()

        with patch(
            "src.utils.tkinter_exception_hook.InternalDialogError", return_value=mock_instance
        ) as mock_cls:
            tkinter_exception_hook(ValueError, exc, None)

        mock_cls.assert_called_once_with(message="something broke")
        mock_instance.open.assert_called_once()
