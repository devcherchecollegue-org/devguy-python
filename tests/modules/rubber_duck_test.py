import faker
import pytest
from pony.orm import db_session

from app import pony_db
from app.modules import rubber_duck, VanillaRubberDuck
from app.modules.models import sql
from app.modules.rubber_duck import SqliteDataAccessObject
from tests.mocks.modules.rubber_duck import MockedDataAccessObject


rubber_duck_dao = MockedDataAccessObject()
rubber_duck_mod = VanillaRubberDuck(rubber_duck_dao)

fake = faker.Faker('fr_FR')


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


class TestSQLiteDAO:
    _dao = SqliteDataAccessObject()

    @db_session
    def test_get_known_user(self, insert_random_user):
        user = self._dao.get(insert_random_user)
        assert user is not None
        assert self._dao.get(insert_random_user).user_id == insert_random_user


@pytest.fixture
@db_session
def insert_random_user() -> int:
    id = fake.pyint()
    pony_db.insert('RubberDuck', user_id=id)
    return id
