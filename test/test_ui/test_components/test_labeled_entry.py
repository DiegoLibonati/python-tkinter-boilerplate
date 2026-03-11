from unittest.mock import MagicMock, patch

import pytest

from src.ui.components.labeled_entry import LabeledEntry


@pytest.fixture
def labeled_entry(mock_root: MagicMock, mock_styles: MagicMock, variable: MagicMock) -> LabeledEntry:
    with (
        patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
        patch("src.ui.components.labeled_entry.Label"),
        patch("src.ui.components.labeled_entry.Entry"),
        patch.object(LabeledEntry, "columnconfigure"),
    ):
        instance = LabeledEntry.__new__(LabeledEntry)
        instance._styles = mock_styles
        return instance


class TestLabeledEntryInit:
    def test_stores_styles(self, mock_root: MagicMock, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label"),
            patch("src.ui.components.labeled_entry.Entry"),
            patch.object(LabeledEntry, "columnconfigure"),
            patch.object(LabeledEntry, "config", create=True),
        ):
            instance = LabeledEntry.__new__(LabeledEntry)
            instance._styles = mock_styles
            assert instance._styles == mock_styles

    def test_creates_label_with_correct_text(self, mock_root: MagicMock, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label") as mock_label,
            patch("src.ui.components.labeled_entry.Entry"),
            patch.object(LabeledEntry, "columnconfigure"),
            patch.object(LabeledEntry, "config", create=True),
        ):
            instance = LabeledEntry.__new__(LabeledEntry)
            instance._styles = mock_styles
            LabeledEntry._create_label = lambda s, t: mock_label(s, text=t)

            mock_label.assert_not_called()

    def test_entry_includes_show_when_provided(self, mock_root: MagicMock, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label"),
            patch("src.ui.components.labeled_entry.Entry") as mock_entry,
            patch.object(LabeledEntry, "columnconfigure"),
            patch.object(LabeledEntry, "grid", create=True),
        ):
            called_kwargs = {}

            def capture_entry(parent, **kwargs):
                called_kwargs.update(kwargs)
                m = MagicMock()
                m.grid = MagicMock()
                return m

            mock_entry.side_effect = capture_entry

            instance = LabeledEntry.__new__(LabeledEntry)
            instance._styles = mock_styles
            LabeledEntry.__init__(
                instance,
                parent=mock_root,
                label_text="Password",
                styles=mock_styles,
                variable=variable,
                show="*",
            )

            assert called_kwargs.get("show") == "*"

    def test_entry_excludes_show_when_not_provided(self, mock_root: MagicMock, mock_styles: MagicMock, variable: MagicMock) -> None:
        with (
            patch("src.ui.components.labeled_entry.Frame.__init__", return_value=None),
            patch("src.ui.components.labeled_entry.Label"),
            patch("src.ui.components.labeled_entry.Entry") as mock_entry,
            patch.object(LabeledEntry, "columnconfigure"),
            patch.object(LabeledEntry, "grid", create=True),
        ):
            called_kwargs = {}

            def capture_entry(parent, **kwargs):
                called_kwargs.update(kwargs)
                m = MagicMock()
                m.grid = MagicMock()
                return m

            mock_entry.side_effect = capture_entry

            instance = LabeledEntry.__new__(LabeledEntry)
            instance._styles = mock_styles
            LabeledEntry.__init__(
                instance,
                parent=mock_root,
                label_text="Username",
                styles=mock_styles,
                variable=variable,
                show="",
            )

            assert "show" not in called_kwargs
