from random import randint, seed

from .dao import DAO

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


class Miscellaneous:
    def __init__(self, dao: DAO):
        seed()
        self.dao = dao

    @staticmethod
    def get_coin_coin_string() -> str:
        return coin_coins[randint(0, len(coin_coins))]

    def follow_user(self, user_id: int):
        self.dao.insert_follow(user_id)

    def unfollow_user(self, user_id: int):
        self.dao.delete_follow(user_id)
