from app.modules import hello
from pytest import fixture
from tests.mocks.discord import MockMessage, MockAuthor, MockChannel

author = MockAuthor("test")
channel = MockChannel()
message = MockMessage(channel=channel, author=author)


@fixture
def cleanup():
    yield

    channel.assert_full_filled()
    author.assert_full_filled()
    message.assert_full_filled()

    channel.reset()
    author.reset()
    message.reset()


class TestSayHello:
    def test_should_respond_hello(self):
        channel.on("send", "Hello!").returns(False)
        assert hello.respond(message, "ok") is False

        channel.reset()
        channel.on("send", "Hello!").returns("Test")
        assert hello.respond(message, "ok") == "Test"

    def test_should_not_respond_to_bot(self):
        assert hello.respond(message, "test") is None
