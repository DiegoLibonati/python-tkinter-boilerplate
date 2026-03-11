from unittest.mock import MagicMock, patch

import pytest
from pydantic import BaseModel, ValidationError

from src.constants.messages import MESSAGE_ERROR_PYDANTIC
from src.utils.error_handler import handle_exceptions


def make_validation_error() -> ValidationError:
    class DummyModel(BaseModel):
        value: int

    try:
        DummyModel(value="not_an_int")
    except ValidationError as e:
        return e


class TestHandleExceptions:
    def test_returns_result_when_no_exception(self) -> None:
        @handle_exceptions
        def fn() -> str:
            return "ok"

        result: str = fn()
        assert result == "ok"

    def test_passes_args_to_wrapped_function(self) -> None:
        @handle_exceptions
        def fn(a: int, b: int) -> int:
            return a + b

        result: int = fn(2, 3)
        assert result == 5

    def test_passes_kwargs_to_wrapped_function(self) -> None:
        @handle_exceptions
        def fn(value: str) -> str:
            return value.upper()

        result: str = fn(value="hello")
        assert result == "HELLO"

    def test_preserves_function_name(self) -> None:
        @handle_exceptions
        def my_function() -> None:
            pass

        assert my_function.__name__ == "my_function"

    def test_calls_validation_dialog_on_validation_error(self) -> None:
        validation_error: ValidationError = make_validation_error()

        @handle_exceptions
        def fn() -> None:
            raise validation_error

        with patch("src.utils.error_handler.ValidationDialogError") as mock_dialog_class:
            mock_dialog: MagicMock = MagicMock()
            mock_dialog_class.return_value = mock_dialog
            fn()

        mock_dialog_class.assert_called_once()
        mock_dialog.dialog.assert_called_once()

    def test_validation_dialog_called_with_pydantic_message(self) -> None:
        validation_error: ValidationError = make_validation_error()

        @handle_exceptions
        def fn() -> None:
            raise validation_error

        with patch("src.utils.error_handler.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            fn()

        _, kwargs = mock_dialog_class.call_args
        assert kwargs.get("message") == MESSAGE_ERROR_PYDANTIC

    def test_returns_none_on_validation_error(self) -> None:
        validation_error: ValidationError = make_validation_error()

        @handle_exceptions
        def fn() -> str:
            raise validation_error

        with patch("src.utils.error_handler.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            result = fn()

        assert result is None

    def test_does_not_catch_non_validation_errors(self) -> None:
        @handle_exceptions
        def fn() -> None:
            raise RuntimeError("unexpected")

        with pytest.raises(RuntimeError, match="unexpected"):
            fn()
