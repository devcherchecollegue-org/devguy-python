from enum import Enum
from typing import List

from discord import Guild, HTTPException, Message, PartialEmoji, Role

from app.domains import InvalidOption, MemberDoesNotExists, RoleDoesNotExists, UnexpectedError


class Picker:
    """
    Roles module manages the real process between role management.
    """

    class InvalidPickerMessage(Exception):
        pass

    class CreateMessageError:
        """
        Manages error for picker create message.
        """

        def __init__(self, message: str, emoji: PartialEmoji):
            self.message = message
            self.emoji_name = emoji.name
            self.emoji_id = emoji.id

        def print(self):
            """
            Print error as multiline string message.
            """
            print(self.message)
            print(f"emoji '{self.emoji_name}' with id '{self.emoji_id}' was not added.")

    class Options(Enum):
        """
        Options represent an option in role management actions.
        """
        ADD = 'ADD'
        REMOVE = 'REMOVE'

    __role_picker_msg_id = None

    def __init__(self, emoji_to_role: dict):
        """Initialize role classes."""
        self.__emoji_to_role = {
            (emoji_name, element['emoji_id']): element['role_id']
            for emoji_name, element in emoji_to_role.items()
        }

        self.__valid_emojies = [
            PartialEmoji(name=name, id=emoji_id)
            for name, emoji_id in self.__emoji_to_role
        ]

    async def create_message(self, message: Message) -> List[CreateMessageError]:
        """
        Remember role picker message id in memory.

        :param message: discord message
        """
        # should impact all classes
        # cause not defined in  __init__
        self.__role_picker_msg_id = message.id

        errors = []
        for emoji in self.__valid_emojies:
            try:
                await message.add_reaction(emoji)
            except HTTPException as e:
                errors.append(Picker.CreateMessageError(e.text, emoji))

        return errors

    def is_active_message(self, message_id: int):
        """
        Check if candidate message is the one sat to pick
        roles.
        """
        return message_id == self.__role_picker_msg_id

    def emoji_to_role(self, guild: Guild, emoji: PartialEmoji) -> Role:
        """
        Convert emoji to guild role.
        """
        role_id = self.__emoji_to_role.get((emoji.name, emoji.id))
        if not role_id:
            print(role_id, self.__emoji_to_role)
            raise UnexpectedError

        role = guild.get_role(role_id)
        if not role:
            raise RoleDoesNotExists

        return role

    @staticmethod
    async def assign(guild: Guild, role: Role, user_id: int, option: Options) -> None:
        """
        Assign or remove role from user in a guild.
        """
        member = guild.get_member(user_id)
        if not member:
            raise MemberDoesNotExists
        if option == Picker.Options.ADD:
            await member.add_roles(role)
        elif option == Picker.Options.REMOVE:
            await member.remove_roles(role)
        else:
            raise InvalidOption
