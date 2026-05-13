from src.services.hash_service import HashService


class TestHashService:
    def test_hash_returns_string(self) -> None:
        result: str = HashService.hash("password")

        assert isinstance(result, str)

    def test_hash_contains_dollar_separator(self) -> None:
        result: str = HashService.hash("password")

        assert "$" in result

    def test_hash_is_non_empty(self) -> None:
        result: str = HashService.hash("password")

        assert len(result) > 0

    def test_two_hashes_of_same_text_differ_due_to_salt(self) -> None:
        hash1: str = HashService.hash("password")
        hash2: str = HashService.hash("password")

        assert hash1 != hash2

    def test_verify_returns_true_for_correct_password(self) -> None:
        hashed: str = HashService.hash("mypassword")

        assert HashService.verify("mypassword", hashed) is True

    def test_verify_returns_false_for_wrong_password(self) -> None:
        hashed: str = HashService.hash("mypassword")

        assert HashService.verify("wrongpassword", hashed) is False

    def test_verify_returns_false_for_malformed_hash(self) -> None:
        assert HashService.verify("password", "notahash") is False

    def test_verify_returns_false_for_empty_hash(self) -> None:
        assert HashService.verify("password", "") is False
