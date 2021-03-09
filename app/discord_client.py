from enum import Enum
from typing import Optional, List

import discord
from discord.ext import commands

from app.exceptions import (
    GuildDoesNotExists,
    RoleDoesNotExists,
    MemberDoesNotExists,
    InvalidReactionType,
)

COMMAND_PREFIX = '!'

intents_default_with_members = discord.Intents.default()
intents_default_with_members.members = True


class EnumReactionType(Enum):
    ADD = 'ADD'
    REMOVE = 'REMOVE'


class DiscordClient:
    """
        That class handles events recorded from discord by a bot.
        bot_secret_key is the secret key of the bot given by discord.
        admin_id is the id of the user able to create message which can be reacted to.
        role_id_1 and role_id_2 are the id of the roles you want to assign to emojies.
    """
    def __init__(
        self,
        bot_secret_key: str,
        admin_id: int,
        emoji_to_role: dict
    ) -> None:
        self._client = discord.Client(intents=intents_default_with_members)
        self.admin_id = admin_id
        self._message_picker = None
        self.bot = commands.Bot(
            command_prefix=COMMAND_PREFIX,
            intents=intents_default_with_members,
        )
        self._bot_secret_key = bot_secret_key
        self._client.on_raw_reaction_add = self.on_raw_reaction_add
        self._client.on_raw_reaction_remove = self.on_raw_reaction_remove
        self._client.on_message = self.on_message
        self._emoji_to_role = {
            (emoji_name, element['emoji_id']): element['role_id']
            for emoji_name, element in emoji_to_role.items()
        }

    def run(self):
        """Run the bot in listening mode. """
        self._client.run(self._bot_secret_key)

    async def on_message(self, message: discord.Message):
        """ Handles messages. """
        # Avoid self answering
        if message.author.id == self._client.user.id:
            return

        if message.author.id != self.admin_id:
            return

        if message.content == f'{COMMAND_PREFIX} set_role_picker':
            self._message_picker = await message.channel.send('pick a role with reactions')
            valid_emojies = [
                discord.PartialEmoji(name=name, id=id)
                for name, id in self._emoji_to_role
            ]
            await self.setup_emojies(
                self._message_picker,
                valid_emojies
            )

    async def on_raw_reaction_add(
        self,
        payload: discord.RawReactionActionEvent
    ) -> None:
        """Gives a role based on a reaction emoji."""
        await self._on_raw_reaction(payload, EnumReactionType.ADD)

    async def on_raw_reaction_remove(
        self,
        payload: discord.RawReactionActionEvent
    ) -> None:
        """Removes a role based on a reaction emoji."""
        await self._on_raw_reaction(payload, EnumReactionType.REMOVE)

    async def setup_emojies(
        self,
        message: discord.Message,
        emojies: List[discord.PartialEmoji]
    ) -> None:
        """Adds emojies to a message."""
        for emoji in emojies:
            try:
                await message.add_reaction(emoji)
            except discord.HTTPException as e:
                print(e.text)
                print(
                    f"emoji '{emoji.name}' with id '{emoji.id}' was not added."
                )

    def get_guild(self, guild_id: int) -> discord.Guild:
        """
            Retrieve the `discord.Guild` object
            associated to the give `guild_id`.
        """
        guild = self._client.get_guild(guild_id)
        if not guild:
            raise GuildDoesNotExists
        return guild

    def get_role(self, guild_id: int, role_id: int) -> discord.Role:
        """
            Retrieve the `discord.Role` object
            associated to a given `discord.Guild` and `role_id`.
        """
        guild = self.get_guild(guild_id)
        role = guild.get_role(role_id)
        if not role:
            raise RoleDoesNotExists
        return role

    def get_member(self, guild_id: int, user_id: int) -> discord.Member:
        """
            Retrieve the `discord.Member` object
            associated to a given `discord.Guild` and `user_id`.
        """
        guild = self.get_guild(guild_id)
        member = guild.get_member(user_id)
        if not member:
            raise MemberDoesNotExists
        return member

    def get_role_id_from_emoji(
        self,
        emoji: str
    ) -> Optional[int]:
        """
            Returns the `role_id` associated to a give `emoji`.
        """
        if emoji not in self._emoji_to_role:
            return None
        return self._emoji_to_role[emoji]

    def _is_bot_itself(self, user_id: int) -> bool:
        return self._client.user.id == user_id

    def _is_message_picker(self, message_id: int) -> bool:
        if not self._message_picker:
            print("No message to react to")
            return False
        return message_id == self._message_picker.id

    async def _on_raw_reaction(
        self,
        payload: discord.RawReactionActionEvent,
        reaction_type: str,
    ) -> discord.Role:
        """Handles a role based on a reaction emoji and a type of reaction."""
        if self._is_bot_itself(payload.user_id):
            print("reaction added by the bot itself")
            return

        if not self._is_message_picker(payload.message_id):
            print("This message is not monitored for reactions")
            return

        role_id = self.get_role_id_from_emoji(payload.emoji.name)
        if not role_id:
            print(f'{payload.emoji.name} with id {payload.emoji.id} is not associated to a role')
            return

        try:
            role = self.get_role(payload.guild_id, role_id)
            member = self.get_member(payload.guild_id, payload.user_id)
        except (GuildDoesNotExists, RoleDoesNotExists, MemberDoesNotExists) as e:
            print(e)
            return

        try:
            if reaction_type == EnumReactionType.ADD:
                await member.add_roles(role)
            elif reaction_type == EnumReactionType.REMOVE:
                await member.remove_roles(role)
            else:
                raise InvalidReactionType
        except discord.HTTPException as e:
            print(e)
            return
        else:
            print(f"Successful update of type {reaction_type.value} on {role}")
