import tkinter as tk
from unittest.mock import MagicMock

from src.ui.styles import Styles
from src.ui.views.register_view import RegisterView


class TestRegisterView:
    def test_is_toplevel_subclass(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(master=root, styles=Styles(), on_register=MagicMock())

        assert isinstance(view, tk.Toplevel)

        view.destroy()

    def test_text_username_starts_empty(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(master=root, styles=Styles(), on_register=MagicMock())

        assert view.text_username.get() == ""

        view.destroy()

    def test_text_password_starts_empty(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(master=root, styles=Styles(), on_register=MagicMock())

        assert view.text_password.get() == ""

        view.destroy()

    def test_text_confirm_password_starts_empty(self, root: tk.Tk) -> None:
        view: RegisterView = RegisterView(master=root, styles=Styles(), on_register=MagicMock())

        assert view.text_confirm_password.get() == ""

        view.destroy()

    def test_on_register_callback_is_invoked_when_called(self, root: tk.Tk) -> None:
        on_register: MagicMock = MagicMock()
        view: RegisterView = RegisterView(master=root, styles=Styles(), on_register=on_register)

        view._on_register()

        on_register.assert_called_once()
        view.destroy()
