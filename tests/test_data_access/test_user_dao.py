from src.data_access.user_dao import UserDAO
from src.models.user_model import UserModel
from src.services.hash_service import HashService


class TestUserDAO:
    def test_initializes_with_predefined_users(self) -> None:
        dao: UserDAO = UserDAO()

        assert dao.exists("pepe")
        assert dao.exists("ash")
        assert dao.exists("tom")

    def test_get_by_username_returns_user_model_instance(self) -> None:
        dao: UserDAO = UserDAO()

        user: UserModel | None = dao.get_by_username("pepe")

        assert user is not None
        assert isinstance(user, UserModel)

    def test_get_by_username_returns_correct_username(self) -> None:
        dao: UserDAO = UserDAO()

        user: UserModel | None = dao.get_by_username("ash")

        assert user is not None
        assert user.username == "ash"

    def test_get_by_username_returns_none_for_unknown_user(self) -> None:
        dao: UserDAO = UserDAO()

        user: UserModel | None = dao.get_by_username("nonexistent")

        assert user is None

    def test_exists_returns_true_for_known_user(self) -> None:
        dao: UserDAO = UserDAO()

        assert dao.exists("tom") is True

    def test_exists_returns_false_for_unknown_user(self) -> None:
        dao: UserDAO = UserDAO()

        assert dao.exists("unknown") is False

    def test_save_stores_new_user(self) -> None:
        dao: UserDAO = UserDAO()
        new_user: UserModel = UserModel(username="newuser", password=HashService.hash("pass"))

        dao.save(new_user)

        assert dao.exists("newuser") is True

    def test_save_allows_retrieving_stored_user(self) -> None:
        dao: UserDAO = UserDAO()
        new_user: UserModel = UserModel(username="savetest", password=HashService.hash("pass"))

        dao.save(new_user)
        retrieved: UserModel | None = dao.get_by_username("savetest")

        assert retrieved is not None
        assert retrieved.username == "savetest"

    def test_save_overwrites_existing_user(self) -> None:
        dao: UserDAO = UserDAO()
        updated_user: UserModel = UserModel(username="pepe", password=HashService.hash("newpass"))

        dao.save(updated_user)
        retrieved: UserModel | None = dao.get_by_username("pepe")

        assert retrieved is not None
        assert retrieved.password == updated_user.password
