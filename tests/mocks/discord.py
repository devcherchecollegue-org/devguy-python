from elmock import Mock


class MockAuthor(Mock):
    def __init__(self, nickname: str):
        self.nick = nickname


class MockChannel(Mock):
    def send(self, message: str):
        return self.execute("send", message)


class MockMessage(Mock):
    def __init__(self, channel, author):
        self.channel = channel
        self.author = author
