from app.modules.messaging._api import _Validator


class TestValidator:
    validator = _Validator()

    def test_validate_correct_welcome_message(self):
        assert self.validator.is_welcome("Test for {new_member_name}") is True

    def test_invalidate_incorrect_welcome_message(self):
        assert self.validator.is_welcome("Test for {}") is False
        assert self.validator.is_welcome("Test message") is False
        assert self.validator.is_welcome("Test for {not_ok}") is False
