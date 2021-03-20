from app.modules import rubber_duck
from app.modules.models import sql
from tests.mocks.mock import Mock


class MockedDataAccessObject(rubber_duck.DataAccessObject, Mock):
    @staticmethod
    def get(user_id: int) -> sql.RubberDuck:
        return MockedRubberDuck.returns('get', user_id=user_id)

    @staticmethod
    def insert_follow(user_id: int) -> None:
        MockedRubberDuck.returns('insert_follow', user_id=user_id)

    def delete_follow(self, user_id: int) -> None:
        MockedRubberDuck.returns('delete_follow', user_id=user_id)


class MockedRubberDuck(rubber_duck.RubberDuck, Mock):
    @staticmethod
    def get_coin_coin_string() -> str:
        return MockedRubberDuck.returns('get_coin_coin_string')

    def follow_user(self, user_id: int) -> None:
        MockedRubberDuck.returns('follow_user', user_id=user_id)

    def unfollow_user(self, user_id: int) -> None:
        MockedRubberDuck.returns('unfollow_user', user_id=user_id)

    def is_following_user(self, user_id: int) -> bool:
        return MockedRubberDuck.returns('is_following_user', user_id=user_id)
