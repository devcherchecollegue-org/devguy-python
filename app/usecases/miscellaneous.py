from sqlite3 import IntegrityError

from app.modules.miscellaneous import Miscellaneous as MiscellaneousMod


class Miscellaneous:
    """
    Miscellaneous provides funny usecases to work on the bot simply :)
    """

    def __init__(self, miscellaneous_module: MiscellaneousMod):
        self.__miscellaneous = miscellaneous_module

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
            self.__miscellaneous.follow_user(user_id)
        except IntegrityError as e:
            print(e)
        except NotImplementedError:
            print("Method follow does not exist for coin coin command")
            return False

        return True

    def stop_coin_coin(self, user_id: int):
        """
        Stop coin coin stop following user to respond with coin coin messages.

        :return: Coin coin started correctly
        """

        self.__miscellaneous.unfollow_user(user_id)

    def coin_coin_message(self, user_id: int) -> Optional[str]:
        if not self.__miscellaneous.is_following_user(user_id):
            print("User is not followed")
            return None

        return self.__miscellaneous.get_coin_coin_string()
