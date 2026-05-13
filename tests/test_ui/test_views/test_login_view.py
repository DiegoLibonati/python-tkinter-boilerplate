import tkinter as tk
from unittest.mock import MagicMock

from src.ui.styles import Styles
from src.ui.views.login_view import LoginView


class TestLoginView:
    def test_is_frame_subclass(self, root: tk.Tk) -> None:
        view: LoginView = LoginView(
            master=root, styles=Styles(), on_login=MagicMock(), on_register=MagicMock()
        )

        assert isinstance(view, tk.Frame)

    def test_text_confirm_has_welcome_as_default_value(self, root: tk.Tk) -> None:
        view: LoginView = LoginView(
            master=root, styles=Styles(), on_login=MagicMock(), on_register=MagicMock()
        )

        assert view.text_confirm.get() == "Welcome"

    def test_text_username_starts_empty(self, root: tk.Tk) -> None:
        view: LoginView = LoginView(
            master=root, styles=Styles(), on_login=MagicMock(), on_register=MagicMock()
        )

        assert view.text_username.get() == ""

    def test_text_password_starts_empty(self, root: tk.Tk) -> None:
        view: LoginView = LoginView(
            master=root, styles=Styles(), on_login=MagicMock(), on_register=MagicMock()
        )

        assert view.text_password.get() == ""

    def test_on_login_callback_is_invoked_when_called(self, root: tk.Tk) -> None:
        on_login: MagicMock = MagicMock()
        view: LoginView = LoginView(
            master=root, styles=Styles(), on_login=on_login, on_register=MagicMock()
        )

        view._on_login()

        on_login.assert_called_once()

    def test_on_register_callback_is_invoked_when_called(self, root: tk.Tk) -> None:
        on_register: MagicMock = MagicMock()
        view: LoginView = LoginView(
            master=root, styles=Styles(), on_login=MagicMock(), on_register=on_register
        )

        view._on_register()

        on_register.assert_called_once()
