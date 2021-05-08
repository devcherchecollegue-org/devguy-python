from .api import Kind, Messages, Validator, Channels
from discord.member import Member
from app.core import roles
from typing import Tuple


class Messenger:
    class InvalidMessage(Exception):
        def __init__(self, kind: Kind):
            super().__init__(f"candidate is not a valid {kind.name} message.")

    class ForbidenAction(Exception):
        pass

    class NoChannelDefined(Exception):
        def __init__(self, kind: Kind):
            super().__init__(f"no channel define to announce {kind.name}.")

    def __init__(self, messages: Messages, channels: Channels, validator: Validator):
        self.__messages = messages
        self.__validator = validator
        self.__channels = channels

    def set_welcome_channel(self, channel_id: int, user: Member) -> None:
        roles.requires_role(roles.ADMIN, user.roles, self.ForbidenAction)

        if not self.__channels.save(Kind.WELCOME, channel_id):
            raise Exception("could not save welcome channel")

    def set_welcome_message(self, message: str, user: Member) -> None:
        roles.requires_role(roles.ADMIN, user.roles, self.ForbidenAction)

        if not self.__validator.is_welcome(message):
            raise self.InvalidMessage(Kind.WELCOME)

        if not self.__messages.save(Kind.WELCOME, message):
            raise Exception("could not save welcome message")

    def welcome(self, new_member_name: str) -> Tuple[str, int]:
        """Welcome a new user"""
        channel_id = self.__channels.welcome()
        if not channel_id:
            raise self.NoChannelDefined(Kind.WELCOME)

        msg = self.__messages.welcome()
        if not msg:
            msg = (
                f"Hello {{{self.__validator.WELCOME_ARGS[0]}}} et bienvenue dans "
                "la communauté! Présente toi ma gueule ;) !"
            )

        format_args = {self.__validator.WELCOME_ARGS[0]: new_member_name}

        return (msg.format(**format_args), channel_id)
