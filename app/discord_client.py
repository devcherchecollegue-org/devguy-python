import discord
from domain.event.message_received_event import MessageReceivedEvent


class DiscordClient():
    def __init__(self, bot_secret_key, event_bus):
        self._client = discord.Client()
        self._bot_secret_key = bot_secret_key
        self.event_bus = event_bus

        self._client.on_message = self.on_message

    def run(self):
        self._client.run(self._bot_secret_key)

    async def on_message(self, _message):
        await self.event_bus.publish(MessageReceivedEvent())
