from sqlite3 import Error, IntegrityError

import pytest

from app.usecases import RubberDuck
from tests.mocks.modules.rubber_duck import MockedRubberDuck


rubber_duck_module = MockedRubberDuck()
usecase = RubberDuck(rubber_duck_module)


@pytest.fixture(autouse=True)
def __cleanup_mocks(tmpdir):
    # Setup: fill with any logic you want

    yield  # run test

    # Teardown : fill with any logic you want
    rubber_duck_module.reset()


class TestFollow:
    def test_should_follow_unknown_user(self):
        rubber_duck_module.on('follow_user', user_id=123)
        assert usecase.coin_coin(123) is True

    def test_should_be_ok_with_known_user(self):
        rubber_duck_module.on('follow_user', raises=IntegrityError, user_id=123)
        assert usecase.coin_coin(123) is True

    def test_should_be_false_on_not_implemented_or_sqlite_error(self, capsys):
        rubber_duck_module.on('follow_user', raises=NotImplementedError, user_id=123)
        assert usecase.coin_coin(123) is False
        assert 'Method follow does not exist' in capsys.readouterr().out

        rubber_duck_module.reset()
        rubber_duck_module.on('follow_user', raises=Error, user_id=123)
        assert usecase.coin_coin(123) is False
        assert 'Error while running db command' in capsys.readouterr().out


class TestUnfollow:
    def test_return_none_when_unfollowing(self):
        rubber_duck_module.on('unfollow_user', user_id=123, )
        assert usecase.stop_coin_coin(123) is None

    def test_raises_un_captured(self):
        rubber_duck_module.on('unfollow_user', raises=Error, user_id=123)
        with pytest.raises(Error):
            usecase.stop_coin_coin(123)


class TestCoinCoin:
    def test_return_message_for_followed_user(self):
        rubber_duck_module.on('is_following_user', return_value=True, user_id=123, )
        rubber_duck_module.on('get_coin_coin_string', return_value='test coin coin')
        assert usecase.coin_coin_message(123) == 'test coin coin'

    def test_return_none_if_user_not_followed(self):
        rubber_duck_module.on('is_following_user', return_value=None, user_id=123, )
        assert usecase.coin_coin_message(123) is None

    def test_raises_un_captured(self):
        rubber_duck_module.on('is_following_user', raises=Error, user_id=123)
        with pytest.raises(Error):
            usecase.coin_coin_message(123)
