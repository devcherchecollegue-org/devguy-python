from typing import Optional

from discord import Guild, HTTPException, Message, PartialEmoji, Role

from app.domains import (
    GuildDoesNotExists, MemberDoesNotExists,
    RoleDoesNotExists,
)
from app.modules.roles_management import Picker


class Roles:
    """
    Roles describes how to setup and use
    role management in the bot.

    The Role usecases is heavily linked to discord
    so the usecases are based on discord global objects.

    This specific usecase has no sense outside of a discord
    bot as the notion of roles will differ between messaging
    system!

    We could abstract it but it would be a heavy premature
    abstraction as we do not intend to make the bot run on
    another platform for now!
    """

    def __init__(self, roles: Picker):
        self.__roles = roles

    # This is a not a perfectly clean implem as emojies are return directly as
    # discord entities so there is a link between transport and usecase...
    # I will avoid it as much as possible but such depencies CAN be accepted
    # for specific cases and I liked to introduce it here though
    # it could be done another way.
    async def setup_role_picker(self, message: Message) -> None:
        """
        Set message to pick role on!
        """
        errors = await self.__roles.create_message(message)

        for err in errors:
            err.print()

    async def add_role(
            self, guild: Optional[Guild],
            message_id: int, emoji: PartialEmoji, user_id: int,
    ) -> None:
        await self.__set_role(guild, message_id, emoji, user_id, Picker.Options.ADD)

    async def remove_role(
            self, guild: Optional[Guild],
            message_id: int, emoji: PartialEmoji, user_id: int,
    ) -> None:
        await self.__set_role(guild, message_id, emoji, user_id, Picker.Options.REMOVE)

    # This is not a good practice while dealing with usecases but I really hate this kind of
    # duplication ... Perhaps I should just keep this usecase 
    async def __set_role(
            self, guild: Optional[Guild],
            message_id: int, emoji: PartialEmoji, user_id: int,
            opt: Picker.Options,
    ) -> Optional[Role]:
        if not self.__roles.is_active_message(message_id):
            print("reaction is not on role picker message")
            return

        if not guild:
            print(GuildDoesNotExists)

        try:
            role = self.__roles.emoji_to_role(guild, emoji)
            await self.__roles.assign(guild, role, user_id, opt)

        except (RoleDoesNotExists, MemberDoesNotExists, HTTPException) as e:
            print(e)
        else:
            print(f"Successful {opt} role {role} on user {user_id}")
