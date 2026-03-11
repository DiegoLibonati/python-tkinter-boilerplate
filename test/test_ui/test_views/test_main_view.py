from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.main_view import MainView


@pytest.fixture
def main_view(mock_root: MagicMock, mock_styles: MagicMock) -> MainView:
    with (
        patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
        patch("src.ui.views.main_view.Label"),
        patch.object(MainView, "title"),
        patch.object(MainView, "geometry"),
        patch.object(MainView, "resizable"),
        patch.object(MainView, "config"),
        patch.object(MainView, "columnconfigure"),
        patch.object(MainView, "rowconfigure"),
    ):
        instance = MainView.__new__(MainView)
        instance._styles = mock_styles
        return instance


class TestMainViewInit:
    def test_stores_styles(self, main_view: MainView, mock_styles: MagicMock) -> None:
        assert main_view._styles == mock_styles

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label"),
            patch.object(MainView, "title") as mock_title,
            patch.object(MainView, "geometry"),
            patch.object(MainView, "resizable"),
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure"),
        ):
            instance = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="pepe")

        mock_title.assert_called_once_with("Template Tkinter Program")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label"),
            patch.object(MainView, "title"),
            patch.object(MainView, "geometry") as mock_geometry,
            patch.object(MainView, "resizable"),
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure"),
        ):
            instance = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="pepe")

        mock_geometry.assert_called_once_with("200x200")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label"),
            patch.object(MainView, "title"),
            patch.object(MainView, "geometry"),
            patch.object(MainView, "resizable") as mock_resizable,
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure"),
        ):
            instance = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="pepe")

        mock_resizable.assert_called_once_with(False, False)

    def test_label_includes_username(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with (
            patch("src.ui.views.main_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.main_view.Label") as mock_label,
            patch.object(MainView, "title"),
            patch.object(MainView, "geometry"),
            patch.object(MainView, "resizable"),
            patch.object(MainView, "config"),
            patch.object(MainView, "columnconfigure"),
            patch.object(MainView, "rowconfigure"),
        ):
            mock_label.return_value.grid = MagicMock()
            instance = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(instance, root=mock_root, styles=mock_styles, username="pepe")

        _, kwargs = mock_label.call_args
        assert "pepe" in kwargs.get("text", "")
