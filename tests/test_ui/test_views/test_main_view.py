import tkinter as tk

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class TestMainView:
    def test_is_toplevel_subclass(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), username="alice")

        assert isinstance(view, tk.Toplevel)

        view.destroy()

    def test_title_contains_app_name(self, root: tk.Tk) -> None:
        view: MainView = MainView(root=root, styles=Styles(), username="alice")

        assert "Python Tkinter Boilerplate" in view.title()

        view.destroy()

    def test_background_uses_primary_color(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(root=root, styles=styles, username="alice")

        assert view.cget("bg") == styles.PRIMARY_COLOR

        view.destroy()
