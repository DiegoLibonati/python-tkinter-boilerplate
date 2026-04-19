import pytest

from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_debug_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.DEBUG is False

    def test_testing_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.TESTING is False

    def test_tz_default_value(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("TZ", raising=False)
        config: DefaultConfig = DefaultConfig()
        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_tz_reads_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("TZ", "UTC")
        config: DefaultConfig = DefaultConfig()
        assert config.TZ == "UTC"

    def test_env_name_default_value(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("ENV_NAME", raising=False)
        config: DefaultConfig = DefaultConfig()
        assert config.ENV_NAME == "python tkinter boilerplate"

    def test_env_name_reads_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("ENV_NAME", "my_app")
        config: DefaultConfig = DefaultConfig()
        assert config.ENV_NAME == "my_app"
