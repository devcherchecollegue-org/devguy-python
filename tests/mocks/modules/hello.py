from discord.message import Message
from elmock import Mock


class MockUsecase(Mock):
    def respond(self, message: Message, owner: str):
        return self.execute("respond", message, owner)
