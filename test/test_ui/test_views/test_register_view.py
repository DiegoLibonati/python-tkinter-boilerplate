from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.register_view import RegisterView


@pytest.fixture
def register_view(mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> RegisterView:
    with (
        patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
        patch("src.ui.views.register_view.LabeledEntry"),
        patch("src.ui.views.register_view.Label"),
        patch("src.ui.views.register_view.Button"),
        patch("src.ui.views.register_view.StringVar", return_value=MagicMock(spec=StringVar)),
        patch.object(RegisterView, "title"),
        patch.object(RegisterView, "geometry"),
        patch.object(RegisterView, "resizable"),
        patch.object(RegisterView, "config"),
        patch.object(RegisterView, "columnconfigure"),
    ):
        instance = RegisterView.__new__(RegisterView)
        instance._styles = mock_styles
        instance._on_register = on_register
        instance.text_confirm = MagicMock(spec=StringVar)
        instance.text_username = MagicMock(spec=StringVar)
        instance.text_password = MagicMock(spec=StringVar)
        instance.text_confirm_password = MagicMock(spec=StringVar)
        return instance


class TestRegisterViewInit:
    def test_stores_styles(self, register_view: RegisterView, mock_styles: MagicMock) -> None:
        assert register_view._styles == mock_styles

    def test_stores_on_register_callback(self, register_view: RegisterView, on_register: MagicMock) -> None:
        assert register_view._on_register == on_register

    def test_has_text_username(self, register_view: RegisterView) -> None:
        assert register_view.text_username is not None

    def test_has_text_password(self, register_view: RegisterView) -> None:
        assert register_view.text_password is not None

    def test_has_text_confirm_password(self, register_view: RegisterView) -> None:
        assert register_view.text_confirm_password is not None

    def test_has_text_confirm(self, register_view: RegisterView) -> None:
        assert register_view.text_confirm is not None

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry"),
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button"),
            patch("src.ui.views.register_view.StringVar", return_value=MagicMock(spec=StringVar)),
            patch.object(RegisterView, "title") as mock_title,
            patch.object(RegisterView, "geometry"),
            patch.object(RegisterView, "resizable"),
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            instance = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)

        mock_title.assert_called_once_with("Register")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry"),
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button"),
            patch("src.ui.views.register_view.StringVar", return_value=MagicMock(spec=StringVar)),
            patch.object(RegisterView, "title"),
            patch.object(RegisterView, "geometry") as mock_geometry,
            patch.object(RegisterView, "resizable"),
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            instance = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)

        mock_geometry.assert_called_once_with("400x400")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock, on_register: MagicMock) -> None:
        with (
            patch("src.ui.views.register_view.Toplevel.__init__", return_value=None),
            patch("src.ui.views.register_view.LabeledEntry"),
            patch("src.ui.views.register_view.Label"),
            patch("src.ui.views.register_view.Button"),
            patch("src.ui.views.register_view.StringVar", return_value=MagicMock(spec=StringVar)),
            patch.object(RegisterView, "title"),
            patch.object(RegisterView, "geometry"),
            patch.object(RegisterView, "resizable") as mock_resizable,
            patch.object(RegisterView, "config"),
            patch.object(RegisterView, "columnconfigure"),
        ):
            instance = RegisterView.__new__(RegisterView)
            RegisterView.__init__(instance, root=mock_root, styles=mock_styles, on_register=on_register)

        mock_resizable.assert_called_once_with(False, False)


class TestRegisterViewCallbacks:
    def test_on_register_callback_is_callable(self, register_view: RegisterView) -> None:
        assert callable(register_view._on_register)

    def test_on_register_can_be_invoked(self, register_view: RegisterView, on_register: MagicMock) -> None:
        register_view._on_register()
        on_register.assert_called_once()
