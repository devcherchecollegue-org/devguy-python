from enum import Enum

from discord import Client, Intents, Message, RawReactionActionEvent
from discord.ext import commands

from app.domains.exceptions import InvalidReactionType
from app.usecases import Miscellaneous, Roles

COMMAND_PREFIX = '!'

intents_default_with_members = Intents.default()
# pylint: disable=E0237
# -> assigning members not defined in class slots
intents_default_with_members.members = True


class EnumReactionType(Enum):
    ADD = 'ADD'
    REMOVE = 'REMOVE'


class MessageCommand:
    pass


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
            roles: Roles,
            misc: Miscellaneous,
    ) -> None:
        self._client = Client(intents=intents_default_with_members)
        self.admin_id = admin_id
        self.bot = commands.Bot(
            command_prefix=COMMAND_PREFIX,
            intents=intents_default_with_members,
        )
        self._bot_secret_key = bot_secret_key
        self._client.on_raw_reaction_add = self.on_raw_reaction_add
        self._client.on_raw_reaction_remove = self.on_raw_reaction_remove
        self._client.on_message = self.on_message
        self.__roles = roles
        self.__misc = misc

        self.__cmd = {
            f'{COMMAND_PREFIX}set_role_picker': self.__cmd_set_role_picker,
            f'{COMMAND_PREFIX}coin_coin':       self.__cmd_coin_coin_follow,
            f'{COMMAND_PREFIX}coin_coin_stop':  self.__cmd_coin_coin_unfollow,
        }

    def run(self):
        """Run the bot in listening mode. """
        self._client.run(self._bot_secret_key)

    async def __cmd_set_role_picker(self, message: Message):
        _role_message_picker = await message.channel.send('pick a role with reactions')
        await self.__roles.setup_role_picker(_role_message_picker)

    async def __cmd_coin_coin_follow(self, message: Message):
        self.__misc.coin_coin(message.author.id)

    async def __cmd_coin_coin_unfollow(self, message: Message):
        self.__misc.stop_coin_coin(message.author.id)

    async def on_message(self, message: Message):
        """ Handles messages. """
        # Avoid self answering
        if message.author.id == self._client.user.id:
            return

        if message.author.id != self.admin_id:
            return

        if message.content in self.__cmd:
            await self.__cmd[message.content](message)
            return

        coin_coin = self.__misc.coin_coin_message(message.author.id)
        if coin_coin:
            await message.channel.send(coin_coin)

    async def on_raw_reaction_add(
            self,
            payload: RawReactionActionEvent
    ) -> None:
        """Gives a role based on a reaction emoji."""
        await self._on_raw_reaction(payload, EnumReactionType.ADD)

    async def on_raw_reaction_remove(
            self,
            payload: RawReactionActionEvent
    ) -> None:
        """Removes a role based on a reaction emoji."""
        await self._on_raw_reaction(payload, EnumReactionType.REMOVE)

    def __is_self(self, user_id: int) -> bool:
        return self._client.user.id == user_id

    async def _on_raw_reaction(
            self,
            payload: RawReactionActionEvent,
            reaction_type: EnumReactionType,
    ) -> None:
        """Handles a role based on a reaction emoji and a type of reaction."""
        if self.__is_self(payload.user_id):
            print("reaction added by the bot itself")
            return

        guild = self._client.get_guild(payload.guild_id)

        if reaction_type == EnumReactionType.ADD:
            await self.__roles.add_role(
                guild, payload.message_id,
                payload.emoji, payload.user_id,

            )
        elif reaction_type == EnumReactionType.REMOVE:
            await self.__roles.remove_role(
                guild, payload.message_id,
                payload.emoji, payload.user_id,
            )
        else:
            raise InvalidReactionType
