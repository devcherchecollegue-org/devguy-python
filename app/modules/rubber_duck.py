from random import randint, seed
from sqlite3 import connect, Error

from dependency_injector.providers import Configuration


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
    def __init__(self, config: Configuration):
        try:
            self.conn = connect(config.get('database', {}).get('name'))
        except Error as e:
            print(e)
            raise EnvironmentError("Could not connect to database!") from e

    def __cursor(self):
        return self.conn.cursor()

    def __commit(self):
        return self.conn.commit()

    def get(self, user_id: int):
        """
        Add user to followed list.

        :param user_id:
        :raises: sqlite3 errors
        """
        query = """
        SELECT * FROM coin_coin WHERE user_id = :uid
        """
        return self.__cursor().execute(query, {'uid': user_id}).fetchone()

    def insert_follow(self, user_id: int):
        """
        Add user to followed list.

        :param user_id:
        :raises: sqlite3 errors
        """
        query = """
        INSERT INTO coin_coin (user_id)
        VALUES (:uid)
        """
        self.__cursor().execute(query, {'uid': user_id})
        self.__commit()

    def delete_follow(self, user_id: int):
        """
        Forgot followed user.

        :param user_id:
        :raises: sqlite3 errors
        """
        query = """
        DELETE FROM coin_coin
        WHERE user_id = ?
        """

        self.__cursor().execute(query, [user_id])
        self.__commit()


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

    def follow_user(self, user_id: int) -> None:
        """
        Start following user
        """
        self.dao.insert_follow(user_id)

    def unfollow_user(self, user_id: int) -> None:
        """
        Stop following user
        """
        self.dao.delete_follow(user_id)

    def is_following_user(self, user_id: int) -> bool:
        """
        Check if user is ducked
        """
        return self.dao.get(user_id) is not None
