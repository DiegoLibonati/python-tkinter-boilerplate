from tkinter import CENTER

from src.ui.styles import Styles


class TestStyles:
    def test_primary_color_is_non_empty_string(self) -> None:
        assert isinstance(Styles.PRIMARY_COLOR, str)
        assert len(Styles.PRIMARY_COLOR) > 0

    def test_secondary_color_is_non_empty_string(self) -> None:
        assert isinstance(Styles.SECONDARY_COLOR, str)
        assert len(Styles.SECONDARY_COLOR) > 0

    def test_white_color_is_non_empty_string(self) -> None:
        assert isinstance(Styles.WHITE_COLOR, str)
        assert len(Styles.WHITE_COLOR) > 0

    def test_font_roboto_12_contains_size(self) -> None:
        assert "12" in Styles.FONT_ROBOTO_12

    def test_font_roboto_13_contains_size(self) -> None:
        assert "13" in Styles.FONT_ROBOTO_13

    def test_font_roboto_15_contains_size(self) -> None:
        assert "15" in Styles.FONT_ROBOTO_15

    def test_anchor_center_equals_tkinter_center(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER

    def test_all_colors_are_distinct(self) -> None:
        colors: list[str] = [Styles.PRIMARY_COLOR, Styles.SECONDARY_COLOR, Styles.WHITE_COLOR]

        assert len(colors) == len(set(colors))
