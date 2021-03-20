from abc import ABC, abstractmethod
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


# Abstract definitions
class DataAccessObject(ABC):
    """
    Abstraction couch for Data anticorruption layers.
    """

    @staticmethod
    @abstractmethod
    def get(user_id: int) -> sql.RubberDuck:
        """
        Add user to followed list.

        :param user_id:
        :raises: databases errors
        """

    @staticmethod
    @abstractmethod
    def insert_follow(user_id: int) -> None:
        """
        Add user to followed list.

        :param user_id:
        :raises: databases errors
        """

    @abstractmethod
    def delete_follow(self, user_id: int) -> None:
        """
        Forgot followed user.

        :param user_id:
        :raises: sqlite3 errors
        """


class RubberDuck(ABC):
    """
    Abstraction couch for rubber duck features.
    """

    @staticmethod
    @abstractmethod
    def get_coin_coin_string() -> str:
        """Return a random string for rubber duck to speak"""

    @abstractmethod
    def follow_user(self, user_id: int) -> None:
        """Start following user to react with rubber duck messages"""

    @abstractmethod
    def unfollow_user(self, user_id: int) -> None:
        """Stop following user"""

    @abstractmethod
    def is_following_user(self, user_id: int) -> bool:
        """Check if user is followed by Rubber Duck"""


# Implémentation of interfaces
class SqliteDataAccessObject(DataAccessObject):
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


class VanillaRubberDuck(RubberDuck):
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
