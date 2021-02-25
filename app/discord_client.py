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

ROLE_TEST1_ID = 814203001245925396
ROLE_TEST2_ID = 814251712630095904
EMOJI_CUSTOM1_ID = 814207249341087785
EMOJI_HEART_EYES_ID = None
BOT_ADMIN_USER_ID = 274655986633932800
COMMAND_PREFIX = '!'

intents_default_with_members = discord.Intents.default()
intents_default_with_members.members = True


class EnumReactionType(Enum):
    ADD = 'ADD'
    REMOVE = 'REMOVE'


class DiscordClient:
    def __init__(self, bot_secret_key):
        self._client = discord.Client(intents=intents_default_with_members,)
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
            ('😍', EMOJI_HEART_EYES_ID): ROLE_TEST1_ID,
            ('custom_emoji1', EMOJI_CUSTOM1_ID): ROLE_TEST2_ID,
        }

    def run(self):
        self._client.run(self._bot_secret_key)

    async def on_message(self, message: discord.Message):
        """ Handles messages. """
        # Avoid self answering
        print(message)
        if message.author == self._client.user:
            return

        if message.author.id != BOT_ADMIN_USER_ID:
            return

        if message.content == f'{COMMAND_PREFIX} set_role_picker':
            self._message_picker = await message.channel.send('pick a role with reactions')
            valid_emojies = [
                discord.PartialEmoji(name=name, id=id)
                for name, id in self._emoji_to_role
            ]
            await self.setup_reactions(
                self._message_picker,
                valid_emojies,
            )

    async def setup_reactions(
        self,
        message: discord.Message,
        emojies: List[discord.PartialEmoji]
    ) -> None:
        """Adds emojies to a message."""
        for emoji in emojies:
            await message.add_reaction(emoji)

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

    async def _on_raw_reaction(
        self,
        payload: discord.RawReactionActionEvent,
        reaction_type: str,
    ) -> discord.Role:
        """Handles a role based on a reaction emoji and a type of reaction."""
        if self._client.user.id == payload.user_id:
            print("reaction added by the bot itself")
            return
        
        if reaction_type not in EnumReactionType:
            print(f"Reaction type: {reaction_type} is not valid")
            return

        if not self._message_picker:
            print("No message to react to")
            return

        if payload.message_id != self._message_picker.id:
            print("The reaction is added on a different message")
            return

        role_id = self.get_role_id_from_emoji(payload.emoji)
        if not role_id:
            print(f' {payload.emoji} not associated to a role')

        try:
            role = self.get_role(payload.guild_id, role_id)
            member = self.get_member(payload.guild_id, payload.user_id)
        except GuildDoesNotExists as e:
            print(e)
            return
        except RoleDoesNotExists as e:
            print(e)
            return
        except MemberDoesNotExists as e:
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
        emoji: discord.PartialEmoji
    ) -> Optional[int]:
        """
            Returns the `role_id` associated to a give `emoji`.
        """
        emoji_key = (emoji.name, emoji.id)
        if emoji_key not in self._emoji_to_role:
            return None
        return self._emoji_to_role[emoji_key]
