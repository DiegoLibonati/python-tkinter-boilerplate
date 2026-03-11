from src.configs.logger_config import setup_logger
from src.constants.messages import (
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_NOT_VALID_MATCH_PASSWORD,
    MESSAGE_NOT_VALID_PASSWORD,
    MESSAGE_SUCCESS_LOGIN,
    MESSAGE_SUCCESS_REGISTER,
    MESSAGE_USER_NOT_EXISTS,
    MESSAGE_USERNAME_ALREADY_EXISTS,
)
from src.data_access.user_dao import UserDAO
from src.models.user_model import UserModel
from src.services.hash_service import HashService
from src.utils.dialogs import ConflictDialogError, NotFoundDialogError, SuccessDialogInformation, ValidationDialogError

logger = setup_logger("tkinter-app - auth_service.py")


class AuthService:
    @staticmethod
    def login(username: str, password: str) -> UserModel | None:
        if not username or not password or username.isspace() or password.isspace():
            ValidationDialogError(message=MESSAGE_NOT_VALID_FIELDS).dialog()
            return None

        user = UserDAO().get_by_username(username)

        if not user:
            NotFoundDialogError(message=MESSAGE_USER_NOT_EXISTS).dialog()
            return None

        if not HashService.verify(password, user.password):
            ValidationDialogError(message=MESSAGE_NOT_VALID_PASSWORD).dialog()
            return None

        SuccessDialogInformation(message=MESSAGE_SUCCESS_LOGIN).dialog()
        return user

    @staticmethod
    def register(username: str, password: str, confirm_password: str) -> bool:
        if not username or not password or not confirm_password or username.isspace() or password.isspace():
            ValidationDialogError(message=MESSAGE_NOT_VALID_FIELDS).dialog()
            return False

        if password != confirm_password:
            ValidationDialogError(message=MESSAGE_NOT_VALID_MATCH_PASSWORD).dialog()
            return False

        if UserDAO().exists(username):
            ConflictDialogError(message=MESSAGE_USERNAME_ALREADY_EXISTS).dialog()
            return False

        user = UserModel(username=username, password=HashService.hash(password))

        UserDAO().save(user)
        logger.info(user)

        SuccessDialogInformation(message=MESSAGE_SUCCESS_REGISTER).dialog()
        return True
