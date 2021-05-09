from app.modules.messaging.api import Kind
from app.modules.messaging import Messenger
from pytest import fixture, fail, raises
from tests.mocks.modules.messaging.api_mock import (
    MockMessages,
    MockValidator,
    MockChannels,
)
from tests.mocks.discord import MockRole, MockMembers
from app.core import roles

validator = MockValidator()
messages = MockMessages()
channels = MockChannels()


@fixture
def admin_member():
    member_roles = [
        MockRole().set_name("Luna"),
        MockRole().set_name("Test"),
        MockRole().set_name(roles.ADMIN.name),
    ]
    member = MockMembers().set_roles(member_roles)
    yield member
    member.reset()


@fixture
def non_admin_member():
    member_roles = [
        MockRole().set_name("Neville"),
        MockRole().set_name("Hell"),
    ]
    member = MockMembers().set_roles(member_roles)
    yield member
    member.reset()


@fixture(autouse=True)
def cleanup():
    yield

    validator.assert_full_filled()
    messages.assert_full_filled()
    channels.assert_full_filled()

    validator.reset()
    messages.reset()
    channels.reset()


class TestMessenger:
    messenger = Messenger(messages=messages, validator=validator, channels=channels)

    class TestSetWelcomeMessage:
        def test_valid_message(self, admin_member):
            msg = "This is a test message for {}"

            validator.on("is_welcome", msg).returns(True)
            messages.on("save", Kind.WELCOME, msg).returns(True)

            try:
                TestMessenger.messenger.set_welcome_message(msg, admin_member)

            except (Messenger.ForbidenAction, Messenger.InvalidMessage):
                fail("should not raise Forbiden nor Invalid")
            except Exception as e:
                if str(e) == "could not save welcome message":
                    fail("should not raise Save error")

                raise e

        def test_raises_forbidden_error_on_non_admin(self, non_admin_member):
            msg = "This is a test message for {}"

            with raises(Messenger.ForbidenAction):
                TestMessenger.messenger.set_welcome_message(
                    msg,
                    non_admin_member,
                )

        def test_raises_on_invalid_message(self, admin_member):
            msg = "This is a wront test message for"

            validator.on("is_welcome", msg).returns(False)

            with raises(Messenger.InvalidMessage):
                TestMessenger.messenger.set_welcome_message(msg, admin_member)

        def test_raises_on_save_failure(self, admin_member):
            msg = "This is a wront test message for"

            validator.on("is_welcome", msg).returns(True)
            messages.on("save", Kind.WELCOME, msg).returns(False)

            with raises(Exception):
                TestMessenger.messenger.set_welcome_message(msg, admin_member)

    class TestSetWelcomeChannel:
        def test_insert(self, admin_member):
            channels.on("save", Kind.WELCOME, 10).returns(True)

            try:
                TestMessenger.messenger.set_welcome_channel(10, admin_member)

            except (Messenger.ForbidenAction):
                fail("should not raise Forbiden nor Invalid")
            except Exception as e:
                if str(e) == "could not save welcome message":
                    fail("should not raise Save error")

                raise e

        def test_raises_forbidden_error_on_non_admin(self, non_admin_member):

            with raises(Messenger.ForbidenAction):
                TestMessenger.messenger.set_welcome_channel(10, non_admin_member)

        def test_raises_on_save_failure(self, admin_member):
            channels.on("save", Kind.WELCOME, 10).returns(False)

            with raises(Exception):
                TestMessenger.messenger.set_welcome_channel(10, admin_member)

    class TestGetWelcomeString:
        def test_default(self):
            usr = "test user"

            messages.on("welcome").returns(None)
            channels.on("welcome").returns(10)

            msg, channel = TestMessenger.messenger.welcome(usr)

            assert f"Hello {usr}" in msg
            assert channel == 10

            messages.reset()
            messages.on("welcome").returns("")

            msg, channel = TestMessenger.messenger.welcome(usr)

            assert f"Hello {usr}" in msg
            assert channel == 10

        def test_from_saved_message(self):
            msg = "Hello {new_member_name} from test"
            usr = "test user"
            expected = msg.format(new_member_name=usr)

            messages.on("welcome").returns(msg)
            channels.on("welcome").returns(10)

            msg, channel = TestMessenger.messenger.welcome(usr)

            assert expected == msg
            assert channel == 10

        def test_raise_when_no_channel_defined(self):
            msg = "Hello {new_member_name} from test"
            usr = "test user"

            messages.on("welcome").returns(msg)
            channels.on("welcome").returns(None)

            with raises(Messenger.NoChannelDefined):
                TestMessenger.messenger.welcome(usr)
