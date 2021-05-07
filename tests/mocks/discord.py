from elmock import Mock


class MockAuthor(Mock):
    def __init__(self, nickname: str):
        self.nick = nickname


class MockChannel(Mock):
    def send(self, message: str):
        return self.execute("send", message)


class MockMessage(Mock):
    def __init__(self, content: str = "", channel=None, author=None):
        self.content = content
        self.channel = channel
        self.author = author

    def set_content(self, content: str):
        self.content = content


class MockUser(Mock):
    def __init__(self, name: str):
        self.name = name


class MockClient(Mock):
    def __init__(self, user):
        self.user = user
