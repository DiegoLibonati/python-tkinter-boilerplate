from unittest.mock import MagicMock, patch

import pytest

from src.models.user_model import UserModel
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
        mock_login_view: MagicMock = MagicMock()
        mock_login_view.pack = MagicMock()
        mock_login_view_class.return_value = mock_login_view
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._root = mock_root
        instance._config = MagicMock()
        instance.user = None
        instance._login_view = mock_login_view
        return instance


class TestInterfaceAppInit:
    def test_user_initial_value_is_none(self, interface_app: InterfaceApp) -> None:
        assert interface_app.user is None

    def test_stores_styles(self, interface_app: InterfaceApp, mock_styles: MagicMock) -> None:
        assert interface_app._styles == mock_styles

    def test_stores_root(self, interface_app: InterfaceApp, mock_root: MagicMock) -> None:
        assert interface_app._root == mock_root

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view_class.return_value.pack = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.title.assert_called_once_with("Template Tkinter")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view_class.return_value.pack = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.geometry.assert_called_once_with("400x400")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view_class.return_value.pack = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.resizable.assert_called_once_with(False, False)

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock) -> None:
        with patch("src.ui.interface_app.LoginView") as mock_login_view_class:
            mock_login_view_class.return_value.pack = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock())

        assert isinstance(app._styles, Styles)


class TestInterfaceAppUsernameProperty:
    def test_returns_username_when_user_is_set(self, interface_app: InterfaceApp, sample_user: UserModel) -> None:
        interface_app.user = sample_user
        assert interface_app.username == sample_user.username

    def test_returns_na_when_user_is_none(self, interface_app: InterfaceApp) -> None:
        interface_app.user = None
        assert interface_app.username == "N/A"


class TestInterfaceAppLogin:
    def test_user_is_set_on_successful_login(self, interface_app: InterfaceApp, sample_user: UserModel) -> None:
        interface_app._login_view.text_username.get.return_value = sample_user.username
        interface_app._login_view.text_password.get.return_value = "testpass"

        with (
            patch("src.ui.interface_app.AuthService.login", return_value=sample_user),
            patch("src.ui.interface_app.MainView"),
        ):
            interface_app._login()

        assert interface_app.user == sample_user

    def test_user_remains_none_when_login_returns_none(self, interface_app: InterfaceApp, invalid_credentials: dict[str, str]) -> None:
        interface_app._login_view.text_username.get.return_value = invalid_credentials["username"]
        interface_app._login_view.text_password.get.return_value = invalid_credentials["password"]

        with patch("src.ui.interface_app.AuthService.login", return_value=None):
            interface_app._login()

        assert interface_app.user is None

    def test_main_view_created_on_successful_login(self, interface_app: InterfaceApp, sample_user: UserModel) -> None:
        interface_app._login_view.text_username.get.return_value = sample_user.username
        interface_app._login_view.text_password.get.return_value = "testpass"

        with (
            patch("src.ui.interface_app.AuthService.login", return_value=sample_user),
            patch("src.ui.interface_app.MainView") as mock_main_view,
        ):
            interface_app._login()

        mock_main_view.assert_called_once()

    def test_main_view_not_created_when_login_returns_none(self, interface_app: InterfaceApp, invalid_credentials: dict[str, str]) -> None:
        interface_app._login_view.text_username.get.return_value = invalid_credentials["username"]
        interface_app._login_view.text_password.get.return_value = invalid_credentials["password"]

        with (
            patch("src.ui.interface_app.AuthService.login", return_value=None),
            patch("src.ui.interface_app.MainView") as mock_main_view,
        ):
            interface_app._login()

        mock_main_view.assert_not_called()

    def test_auth_service_called_with_credentials(self, interface_app: InterfaceApp, valid_credentials: dict[str, str]) -> None:
        interface_app._login_view.text_username.get.return_value = valid_credentials["username"]
        interface_app._login_view.text_password.get.return_value = valid_credentials["password"]

        with patch("src.ui.interface_app.AuthService.login", return_value=None) as mock_login:
            interface_app._login()

        mock_login.assert_called_once_with(
            username=valid_credentials["username"],
            password=valid_credentials["password"],
        )


class TestInterfaceAppOpenRegister:
    def test_register_view_is_created(self, interface_app: InterfaceApp) -> None:
        with patch("src.ui.interface_app.RegisterView") as mock_register_view:
            interface_app._open_register()

        mock_register_view.assert_called_once()

    def test_register_view_on_register_is_bound(self, interface_app: InterfaceApp) -> None:
        with patch("src.ui.interface_app.RegisterView") as mock_register_view:
            interface_app._open_register()

        _, kwargs = mock_register_view.call_args
        assert callable(kwargs.get("on_register"))


class TestInterfaceAppRegister:
    def test_register_view_destroyed_when_register_succeeds(self, interface_app: InterfaceApp, registration_data: dict[str, str]) -> None:
        mock_register_view: MagicMock = MagicMock()
        mock_register_view.text_username.get.return_value = registration_data["username"]
        mock_register_view.text_password.get.return_value = registration_data["password"]
        mock_register_view.text_confirm_password.get.return_value = registration_data["confirm_password"]
        interface_app._register_view = mock_register_view

        with patch("src.ui.interface_app.AuthService.register", return_value=True):
            interface_app._register()

        mock_register_view.destroy.assert_called_once()

    def test_register_view_not_destroyed_when_register_fails(self, interface_app: InterfaceApp) -> None:
        mock_register_view: MagicMock = MagicMock()
        mock_register_view.text_username.get.return_value = ""
        mock_register_view.text_password.get.return_value = ""
        mock_register_view.text_confirm_password.get.return_value = ""
        interface_app._register_view = mock_register_view

        with patch("src.ui.interface_app.AuthService.register", return_value=False):
            interface_app._register()

        mock_register_view.destroy.assert_not_called()

    def test_auth_service_register_called_with_credentials(self, interface_app: InterfaceApp, registration_data: dict[str, str]) -> None:
        mock_register_view: MagicMock = MagicMock()
        mock_register_view.text_username.get.return_value = registration_data["username"]
        mock_register_view.text_password.get.return_value = registration_data["password"]
        mock_register_view.text_confirm_password.get.return_value = registration_data["confirm_password"]
        interface_app._register_view = mock_register_view

        with patch("src.ui.interface_app.AuthService.register", return_value=True) as mock_register:
            interface_app._register()

        mock_register.assert_called_once_with(
            username=registration_data["username"],
            password=registration_data["password"],
            confirm_password=registration_data["confirm_password"],
        )
