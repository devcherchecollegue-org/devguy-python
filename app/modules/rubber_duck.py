from random import randint, seed

from pony.orm import db_session

from app.modules.models import sql


coin_coins = [
    'Coin coin',
    """
>o)
(_>
    """,
    """
   (@_
\\\\\\_\\
<____)
    """
]


class DataAccessObject:
    """Anti corruption layer for persistence."""

    @staticmethod
    def get(user_id: int) -> sql.RubberDuck:
        """
        Add user to followed list.

        :param user_id:
        :raises: sqlite3 errors
        """
        return sql.RubberDuck.get(user_id=user_id)

    @staticmethod
    def insert_follow(user_id: int):
        """
        Add user to followed list.

        :param user_id:
        :raises: sqlite3 errors
        """
        sql.RubberDuck(user_id=user_id)

    def delete_follow(self, user_id: int):
        """
        Forgot followed user.

        :param user_id:
        :raises: sqlite3 errors
        """
        rubber_duck = self.get(user_id)
        if rubber_duck:
            rubber_duck.delete()


class RubberDuck:
    def __init__(self, dao: DataAccessObject):
        seed()
        self.dao = dao

    @staticmethod
    def get_coin_coin_string() -> str:
        """
        Provide random coin-coin string
        """
        return coin_coins[randint(0, len(coin_coins) - 1)]

    @db_session
    def follow_user(self, user_id: int) -> None:
        """
        Start following user
        """
        self.dao.insert_follow(user_id)

    @db_session
    def unfollow_user(self, user_id: int) -> None:
        """
        Stop following user
        """
        self.dao.delete_follow(user_id)

    @db_session
    def is_following_user(self, user_id: int) -> bool:
        """
        Check if user is ducked
        """
        return self.dao.get(user_id) is not None
