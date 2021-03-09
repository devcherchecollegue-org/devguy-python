from app.modules.miscellaneous import Miscellaneous as MiscellaneousMod

class Miscellaneous:
    """
    Miscellaneous provides funny usecases to work on the bot simply :)
    """

    def __init__(self, miscellaneous_module: MiscellaneousMod):
        self.miscellaneous = miscellaneous_module

    def coin_coin(self, user_id: str) -> bool:
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
            self.miscellaneous.follow_user(user_id)
            return True
        except NotImplemented:
            print("Method follow does not exist for coin coin command")
            return False

    def stop_coin_coin(self, user_id: str):
        """
        Stop coin coin stop following user to respond with coin coin messages.

        :return: Coin coin started correctly
        """

        self.miscellaneous.unfollow_user(user_id)
