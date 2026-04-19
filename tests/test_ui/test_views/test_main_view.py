import tkinter as tk

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class TestMainView:
    def test_instantiation(self, root: tk.Tk, styles: Styles) -> None:
        view: MainView = MainView(root=root, styles=styles, username="alice")
        assert view is not None
        view.destroy()

    def test_title_is_set_correctly(self, root: tk.Tk, styles: Styles) -> None:
        view: MainView = MainView(root=root, styles=styles, username="alice")
        assert view.title() == "PythonTkinterBoilerplate Main"
        view.destroy()

    def test_is_not_resizable(self, root: tk.Tk, styles: Styles) -> None:
        view: MainView = MainView(root=root, styles=styles, username="bob")
        assert view.resizable() == (False, False)
        view.destroy()

    def test_instantiation_with_different_username(self, root: tk.Tk, styles: Styles) -> None:
        view: MainView = MainView(root=root, styles=styles, username="charlie")
        assert view is not None
        view.destroy()
