from discord import User

from app.discord import client
from app.modules.messaging import Messenger


class Events:
    def __init__(self, messenger: Messenger):
        self.__messenger = messenger

    @client.event
    async def on_member_join(self, member: User):
        msg, channel_id = self.__messenger.welcome(member.name)
        chan = client.get_channel(channel_id)
        await chan.send(msg)
