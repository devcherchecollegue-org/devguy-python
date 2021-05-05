from elmock import Mock


class MockAuthor(Mock):
    def __init__(self, nickname: str):
        self.nick = nickname
        super().__init__()

    def reset(self):
        self.nick = ""
        super().reset()


class MockChannel(Mock):
    def send(self, message: str):
        return self.execute("send", message)


class MockMessage(Mock):
    def __init__(self, content: str = "", channel=None, author=None):
        self.content = content
        self.channel = channel
        self.author = author

        super().__init__()

    def set_content(self, content: str):
        self.content = content
        return self

    def reset(self):
        self.content = ""
        super().reset()


class MockUser(Mock):
    def __init__(self, name: str):
        self.name = name


class MockClient(Mock):
    def __init__(self, user):
        self.user = user


class MockRole:
    def __init__(self):
        self.name = ""

    def set_name(self, name):
        self.name = name
        return self

    def reset(self):
        self.name = ""


class MockMembers(Mock):
    def __init__(self):
        self.roles = []
        super().__init__()

    def set_roles(self, roles):
        self.roles = roles
        return self

    def reset(self):
        self.roles = []
        super().reset()
