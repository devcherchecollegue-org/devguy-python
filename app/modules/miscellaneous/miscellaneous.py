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
        return coin_coins[randint(0, len(coin_coins) - 1)]

    def follow_user(self, user_id: int) -> None:
        self.dao.insert_follow(user_id)

    def unfollow_user(self, user_id: int) -> None:
        self.dao.delete_follow(user_id)

    def is_following_user(self, user_id: int) -> bool:
        return self.dao.get(user_id) is not None
