from sqlite3 import Error, IntegrityError
from typing import Optional

from app.modules import rubber_duck


class RubberDuck:
    """
    RubberDuck provides funny usecases to work on the bot simply :)
    """

    def __init__(self, rubber_duck_module: rubber_duck.RubberDuck):
        self.__duck = rubber_duck_module

    def coin_coin(self, user_id: int) -> bool:
        """
        Coin coin usecase will start following messages from specified user
        and will respond with a random coin coin string every X messages
        until stop is called.

        :param user_id: ID of user to follow
        :type user_id: str
        :return: Coin coin started correctly
        :rtype: bool
        """
        try:
            self.__duck.follow_user(user_id)
        except IntegrityError as e:
            print(e)
        except NotImplementedError:
            print("Method follow does not exist for coin coin command")
            return False
        except Error:
            print('Error while running db command')
            return False

        return True

    def stop_coin_coin(self, user_id: int):
        """
        Stop coin coin stop following user to respond with coin coin messages.

        :return: Coin coin started correctly
        """

        self.__duck.unfollow_user(user_id)

    def coin_coin_message(self, user_id: int) -> Optional[str]:
        if not self.__duck.is_following_user(user_id):
            print("User is not followed")
            return None

        return self.__duck.get_coin_coin_string()
