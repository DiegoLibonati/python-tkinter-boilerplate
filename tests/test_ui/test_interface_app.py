import tkinter as tk
from unittest.mock import patch

from src.configs.default_config import DefaultConfig
from src.models.user_model import UserModel
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


class TestInterfaceApp:
    def test_username_returns_na_when_no_user_is_set(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=DefaultConfig(), styles=Styles())

        assert app.username == "N/A"

    def test_username_returns_user_username_when_user_is_set(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=DefaultConfig(), styles=Styles())
        app.user = UserModel(username="alice", password="hashed")

        assert app.username == "alice"

    def test_login_sets_user_on_valid_credentials(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=DefaultConfig(), styles=Styles())
        app._login_view.text_username.set("pepe")
        app._login_view.text_password.set("12345")

        with patch("src.services.auth_service.SuccessDialogInformation"):
            with patch("src.ui.interface_app.MainView"):
                app._login()

        assert app.user is not None
        assert app.user.username == "pepe"

    def test_open_register_creates_register_view(self, root: tk.Tk) -> None:
        app: InterfaceApp = InterfaceApp(root=root, config=DefaultConfig(), styles=Styles())

        app._open_register()

        assert app._register_view is not None

        if app._register_view:
            app._register_view.destroy()
            app._register_view = None
