from collections.abc import Callable
from functools import wraps
from typing import TypeVar

from pydantic import ValidationError
from typing_extensions import ParamSpec

from src.configs.logger_config import setup_logger
from src.constants.messages import MESSAGE_ERROR_PYDANTIC
from src.utils.dialogs import ValidationDialogError

logger = setup_logger(__name__)

P = ParamSpec("P")
R = TypeVar("R")


def handle_exceptions(fn: Callable[P, R]) -> Callable[P, R]:
    @wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return fn(*args, **kwargs)

        except ValidationError as _e:
            # logger.error("Validation error: %s", e)
            ValidationDialogError(message=MESSAGE_ERROR_PYDANTIC).dialog()

    return wrapper
