import pytest
from pony.orm import db_session

from app.modules import rubber_duck, VanillaRubberDuck
from app.modules.models import sql
from tests.mocks.modules.rubber_duck import MockedDataAccessObject


rubber_duck_dao = MockedDataAccessObject()
rubber_duck_mod = VanillaRubberDuck(rubber_duck_dao)


@pytest.fixture(autouse=True)
def __cleanup_mocks(tmpdir):
    # Setup: fill with any logic you want

    yield  # run test

    # Teardown : fill with any logic you want
    rubber_duck_dao.reset()


class TestVanillaRubberDuck:
    def test_should_retrieve_random_coin_coin_string(self):
        assert rubber_duck_mod.get_coin_coin_string() in rubber_duck.coin_coins
        assert rubber_duck_mod.get_coin_coin_string() in rubber_duck.coin_coins
        assert rubber_duck_mod.get_coin_coin_string() in rubber_duck.coin_coins
        assert rubber_duck_mod.get_coin_coin_string() in rubber_duck.coin_coins
        assert rubber_duck_mod.get_coin_coin_string() in rubber_duck.coin_coins
        assert rubber_duck_mod.get_coin_coin_string() in rubber_duck.coin_coins

    def test_should_follow_user(self):
        rubber_duck_dao.on('insert_follow', user_id=123)
        assert rubber_duck_mod.follow_user(123) is None

    def test_should_un_follow_user(self):
        rubber_duck_dao.on('delete_follow', user_id=123)
        assert rubber_duck_mod.unfollow_user(123) is None

    @db_session
    def test_should_now_if_user_is_followed(self):
        rubber_duck_dao.on('get', user_id=123)
        assert rubber_duck_mod.is_following_user(123) is False

        rubber_duck_dao.on('get', return_value=sql.RubberDuck(user_id=198), user_id=198)
        assert rubber_duck_mod.is_following_user(198) is True
