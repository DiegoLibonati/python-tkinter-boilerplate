from src.configs.logger_config import setup_logger
from src.constants.messages import (
    MESSAGE_ALREADY_EXISTS_USERNAME,
    MESSAGE_NOT_EXISTS_USER,
    MESSAGE_NOT_VALID_FIELDS,
    MESSAGE_NOT_VALID_MATCH_PASSWORD,
    MESSAGE_NOT_VALID_PASSWORD,
    MESSAGE_SUCCESS_LOGIN,
    MESSAGE_SUCCESS_REGISTER,
)
from src.data_access.user_dao import UserDAO
from src.models.user_model import UserModel
from src.services.hash_service import HashService
from src.utils.dialogs import ConflictDialogError, NotFoundDialogError, SuccessDialogInformation, ValidationDialogError

logger = setup_logger("tkinter-app - auth_service.py")


class AuthService:
    # The DAO is injected here because UserDAO uses an in-memory dictionary as the data store.
    # If using a real database, the DAO would be imported and used directly inside each method
    # without needing to initialize it in the constructor.
    def __init__(self, dao: UserDAO) -> None:
        self._dao = dao

    def login(self, username: str, password: str) -> UserModel:
        if not username or not password or username.isspace() or password.isspace():
            raise ValidationDialogError(message=MESSAGE_NOT_VALID_FIELDS)

        user = self._dao.get_by_username(username)

        if not user:
            raise NotFoundDialogError(message=MESSAGE_NOT_EXISTS_USER)

        if not HashService.verify(password, user.password):
            raise ValidationDialogError(message=MESSAGE_NOT_VALID_PASSWORD)

        SuccessDialogInformation(message=MESSAGE_SUCCESS_LOGIN).open()
        return user

    def register(self, username: str, password: str, confirm_password: str) -> bool:
        if not username or not password or not confirm_password or username.isspace() or password.isspace():
            raise ValidationDialogError(message=MESSAGE_NOT_VALID_FIELDS)

        if password != confirm_password:
            raise ValidationDialogError(message=MESSAGE_NOT_VALID_MATCH_PASSWORD)

        if self._dao.exists(username):
            raise ConflictDialogError(message=MESSAGE_ALREADY_EXISTS_USERNAME)

        user = UserModel(username=username, password=HashService.hash(password))

        self._dao.save(user)

        SuccessDialogInformation(message=MESSAGE_SUCCESS_REGISTER).open()
        return True
