from elmock import Mock
from app.modules.messaging.api import Messages, Kind, Validator, Channels


class MockValidator(Mock, Validator):
    def is_welcome(self, message: str) -> bool:
        return self.execute("is_welcome", message)


class MockMessages(Mock, Messages):
    def save(self, kind: Kind, msg: str) -> bool:
        return self.execute("save", kind, msg)

    def welcome(self) -> str:
        return self.execute("welcome")


class MockChannels(Mock, Channels):
    def save(self, kind: Kind, channel_id: int) -> bool:
        return self.execute("save", kind, channel_id)

    def welcome(self) -> int:
        return self.execute("welcome")
