from pytest import fixture
from tests.mocks.discord import MockMessage, MockClient, MockUser
from tests.mocks.modules import hello
from app.discord.messages import on_message
import asyncio

message = MockMessage()
user = MockUser("test")
cli = MockClient(user)


helloUsecase = hello.MockUsecase()


@fixture(scope="module")
def loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@fixture
def cleanup():
    yield

    message.assert_full_filled()
    message.reset()

    helloUsecase.assert_full_filled()
    helloUsecase.reset()


class TestSayHello:
    def test_should_respond_to_hello(self, loop):
        message.set_content("hello world!")

        r = helloUsecase.on("respond", message, cli.user.name)
        r.returns(asyncio.sleep(0.1))

        loop.run_until_complete(on_message(message, helloUsecase, cli))

    def test_should_not_respond_to_non_hello(self, loop):
        message.set_content("hell world!")

        loop.run_until_complete(on_message(message, helloUsecase, cli))
