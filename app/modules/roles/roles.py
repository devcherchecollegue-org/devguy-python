from enum import Enum
from typing import List

from discord import Guild, HTTPException, Message, PartialEmoji, Role

from app.domains import InvalidOption, MemberDoesNotExists, RoleDoesNotExists


class SetupError:
    def __init__(self, message, emoji):
        self.message = message
        self.emoji_name = emoji.name
        self.emoji_id = emoji.id

    def print(self):
        print(self.message)
        print(f"emoji '{self.emoji_name}' with id '{self.emoji_id}' was not added.")


class SetRoleOption(Enum):
    ADD = 'ADD'
    REMOVE = 'REMOVE'


class Roles:
    """
    Roles module manages the real process between role management
    """

    __role_picker_msg_id = None

    def __init__(self, emoji_to_roles: dict):
        """Initialize role classes"""
        self.__emoji_to_role = {
            (emoji_name, element['emoji_id']): element['role_id']
            for emoji_name, element in emoji_to_roles.items()
        }

        self.__valid_emojies = [
            PartialEmoji(name=name, id=emoji_id)
            for name, emoji_id in self.__emoji_to_role
        ]

    async def setup_role_message_picker(self, message: Message) -> List[SetupError]:
        """
        Remember role picker message id in memory

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
                errors.append(e.text)

        return errors

    def is_role_picker_message(self, message_id):
        return message_id == self.__role_picker_msg_id

    def emoji_to_role(self, guild: Guild, emoji_id) -> Role:
        role_id = self.__emoji_to_role[emoji_id]
        role = guild.get_role(role_id)
        if not role:
            raise RoleDoesNotExists
        return role

    @staticmethod
    async def set_role(guild: Guild, role: Role, user_id, option: SetRoleOption) -> None:
        member = guild.get_member(user_id)
        if not member:
            raise MemberDoesNotExists
        if option == SetRoleOption.ADD:
            await member.add_roles(role)
        elif option == SetRoleOption.REMOVE:
            await member.remove_roles(role)
        else:
            raise InvalidOption
