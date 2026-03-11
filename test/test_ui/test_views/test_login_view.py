from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.login_view import LoginView


@pytest.fixture
def on_login() -> MagicMock:
    return MagicMock()


@pytest.fixture
def login_view(mock_root: MagicMock, mock_styles: MagicMock, on_login: MagicMock, on_register: MagicMock) -> LoginView:
    with (
        patch("src.ui.views.login_view.Frame.__init__", return_value=None),
        patch("src.ui.views.login_view.LabeledEntry"),
        patch("src.ui.views.login_view.Label"),
        patch("src.ui.views.login_view.Button"),
        patch("src.ui.views.login_view.StringVar", return_value=MagicMock(spec=StringVar)),
        patch.object(LoginView, "columnconfigure"),
    ):
        instance = LoginView.__new__(LoginView)
        instance._styles = mock_styles
        instance._on_login = on_login
        instance._on_register = on_register
        instance.text_confirm = MagicMock(spec=StringVar)
        instance.text_username = MagicMock(spec=StringVar)
        instance.text_password = MagicMock(spec=StringVar)
        return instance


class TestLoginViewInit:
    def test_stores_styles(self, login_view: LoginView, mock_styles: MagicMock) -> None:
        assert login_view._styles == mock_styles

    def test_stores_on_login_callback(self, login_view: LoginView, on_login: MagicMock) -> None:
        assert login_view._on_login == on_login

    def test_stores_on_register_callback(self, login_view: LoginView, on_register: MagicMock) -> None:
        assert login_view._on_register == on_register

    def test_text_confirm_initial_value(self, mock_root, mock_styles, on_login, on_register) -> None:
        captured = {}

        def capture_stringvar(*args, **kwargs):
            m = MagicMock(spec=StringVar)
            if "value" not in captured:
                captured["value"] = kwargs.get("value") or (args[0] if args else None)
            return m

        with (
            patch("src.ui.views.login_view.Frame.__init__", return_value=None),
            patch("src.ui.views.login_view.LabeledEntry"),
            patch("src.ui.views.login_view.Label"),
            patch("src.ui.views.login_view.Button"),
            patch("src.ui.views.login_view.StringVar", side_effect=capture_stringvar),
            patch.object(LoginView, "columnconfigure"),
        ):
            instance = LoginView.__new__(LoginView)
            LoginView.__init__(instance, root=mock_root, styles=mock_styles, on_login=on_login, on_register=on_register)

        assert captured.get("value") == "Welcome"

    def test_has_text_username(self, login_view: LoginView) -> None:
        assert login_view.text_username is not None

    def test_has_text_password(self, login_view: LoginView) -> None:
        assert login_view.text_password is not None


class TestLoginViewCallbacks:
    def test_on_login_callback_is_callable(self, login_view: LoginView) -> None:
        assert callable(login_view._on_login)

    def test_on_register_callback_is_callable(self, login_view: LoginView) -> None:
        assert callable(login_view._on_register)

    def test_on_login_can_be_invoked(self, login_view: LoginView, on_login: MagicMock) -> None:
        login_view._on_login()
        on_login.assert_called_once()

    def test_on_register_can_be_invoked(self, login_view: LoginView, on_register: MagicMock) -> None:
        login_view._on_register()
        on_register.assert_called_once()
