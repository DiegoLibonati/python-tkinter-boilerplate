from src.constants.messages import (
    MESSAGE_ALREADY_EXISTS_USERNAME,
    MESSAGE_ERROR_APP,
    MESSAGE_ERROR_PYDANTIC,
    MESSAGE_NOT_EXISTS_USER,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_NOT_VALID_MATCH_PASSWORD,
    MESSAGE_NOT_VALID_PASSWORD,
    MESSAGE_SUCCESS_LOGIN,
    MESSAGE_SUCCESS_REGISTER,
)


class TestMessages:
    def test_message_success_login_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_SUCCESS_LOGIN, str)
        assert len(MESSAGE_SUCCESS_LOGIN) > 0

    def test_message_success_register_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_SUCCESS_REGISTER, str)
        assert len(MESSAGE_SUCCESS_REGISTER) > 0

    def test_message_error_app_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)
        assert len(MESSAGE_ERROR_APP) > 0

    def test_message_error_pydantic_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_PYDANTIC, str)
        assert len(MESSAGE_ERROR_PYDANTIC) > 0

    def test_message_not_valid_password_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_PASSWORD, str)
        assert len(MESSAGE_NOT_VALID_PASSWORD) > 0

    def test_message_not_valid_match_password_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_MATCH_PASSWORD, str)
        assert len(MESSAGE_NOT_VALID_MATCH_PASSWORD) > 0

    def test_message_not_valid_fields_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_FIELDS, str)
        assert len(MESSAGE_NOT_VALID_FIELDS) > 0

    def test_message_not_exists_user_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_NOT_EXISTS_USER, str)
        assert len(MESSAGE_NOT_EXISTS_USER) > 0

    def test_message_already_exists_username_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_ALREADY_EXISTS_USERNAME, str)
        assert len(MESSAGE_ALREADY_EXISTS_USERNAME) > 0

    def test_message_not_found_dialog_type_is_non_empty_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)
        assert len(MESSAGE_NOT_FOUND_DIALOG_TYPE) > 0

    def test_all_messages_are_distinct(self) -> None:
        messages: list[str] = [
            MESSAGE_SUCCESS_LOGIN,
            MESSAGE_SUCCESS_REGISTER,
            MESSAGE_ERROR_APP,
            MESSAGE_ERROR_PYDANTIC,
            MESSAGE_NOT_VALID_PASSWORD,
            MESSAGE_NOT_VALID_MATCH_PASSWORD,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_EXISTS_USER,
            MESSAGE_ALREADY_EXISTS_USERNAME,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]
        assert len(messages) == len(set(messages))
