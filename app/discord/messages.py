from app.discord import client
from app.modules.messaging import Messenger
from discord import Message


class Messages:
    def __init__(self, messenger: Messenger, prefix: str = "!devguy"):
        self.__messenger = messenger
        self.__prefix = prefix

    def __is_cmd(self, message: str):
        if message.startswith(self.__prefix):
            splitted = message.split(" ")
            return True, splitted[0], splitted[1:]

        return False, None

    @client.event
    async def on_message(self, message: Message):
        is_cmd, cmd, args = self.__is_cmd(message.content)
        if not is_cmd:
            return

        if cmd == "set_as_welcome_channel":
            self.__messenger.set_welcome_channel(message.channel.id, message.author)
            return

        if cmd == "set_welcome_message":
            self.__messenger.set_welcome_message(" ".join(args), message.author)
            return
