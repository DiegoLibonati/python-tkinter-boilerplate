import pytest

from src.models.user_model import UserModel
from src.utils.dialogs import ValidationDialogError
from src.utils.exceptions_decorator import exceptions_decorator


class TestExceptionsDecorator:
    def test_passes_through_return_value(self) -> None:
        @exceptions_decorator
        def add(a: int, b: int) -> int:
            return a + b

        result: int = add(2, 3)

        assert result == 5

    def test_preserves_wrapped_function_name(self) -> None:
        @exceptions_decorator
        def my_function() -> None:
            pass

        assert my_function.__name__ == "my_function"

    def test_reraises_pydantic_validation_error_as_validation_dialog_error(self) -> None:
        @exceptions_decorator
        def create_invalid_user() -> None:
            UserModel(username="", password="secret")

        with pytest.raises(ValidationDialogError):
            create_invalid_user()

    def test_does_not_catch_non_pydantic_exceptions(self) -> None:
        @exceptions_decorator
        def raise_runtime() -> None:
            raise RuntimeError("not handled")

        with pytest.raises(RuntimeError):
            raise_runtime()
