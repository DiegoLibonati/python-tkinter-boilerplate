import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger("test-returns-instance")

        assert isinstance(logger, logging.Logger)

    def test_uses_provided_name(self) -> None:
        logger: logging.Logger = setup_logger("test-custom-name")

        assert logger.name == "test-custom-name"

    def test_uses_default_name_when_none_provided(self) -> None:
        logger: logging.Logger = setup_logger()

        assert logger.name == "tkinter-app"

    def test_logger_has_at_least_one_handler(self) -> None:
        logger: logging.Logger = setup_logger("test-has-handlers")

        assert len(logger.handlers) > 0

    def test_calling_twice_does_not_duplicate_handlers(self) -> None:
        logger: logging.Logger = setup_logger("test-idempotent-handlers")
        count_after_first_call: int = len(logger.handlers)

        setup_logger("test-idempotent-handlers")

        assert len(logger.handlers) == count_after_first_call
