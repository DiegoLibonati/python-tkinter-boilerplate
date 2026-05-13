import tkinter as tk
from tkinter import StringVar

from src.ui.components.labeled_entry import LabeledEntry
from src.ui.styles import Styles


class TestLabeledEntry:
    def test_is_frame_subclass(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: StringVar = StringVar(root)

        entry: LabeledEntry = LabeledEntry(
            parent=root, label_text="Test", styles=styles, variable=variable
        )

        assert isinstance(entry, tk.Frame)

    def test_background_uses_styles_primary_color(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: StringVar = StringVar(root)

        entry: LabeledEntry = LabeledEntry(
            parent=root, label_text="Test", styles=styles, variable=variable
        )

        assert entry.cget("bg") == styles.PRIMARY_COLOR

    def test_variable_initial_value_is_preserved(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: StringVar = StringVar(root, value="hello")

        LabeledEntry(parent=root, label_text="Test", styles=styles, variable=variable)

        assert variable.get() == "hello"

    def test_variable_can_be_updated_after_creation(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        variable: StringVar = StringVar(root)

        LabeledEntry(parent=root, label_text="Test", styles=styles, variable=variable)
        variable.set("new value")

        assert variable.get() == "new value"
