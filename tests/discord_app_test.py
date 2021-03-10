from app.app_client import AppClient
from stubs.discord_client_stub import DiscordClientStub
from app.shared.event.event_bus import EventBus
from app.domain.event.message_received_event import MessageReceivedEvent
from stubs.in_memory_event_logger import InMemoryEventLogger


import pytest


def test_app_run_bot_client_on_start():
    event_bus = EventBus()
    discord_client_stub = DiscordClientStub(event_bus)
    app = AppClient(discord_client_stub, event_bus)
    app.start()
    assert discord_client_stub.is_start == True


@pytest.mark.asyncio
async def test_app_receive_event_from_bot_client():
    event_bus = EventBus()
    discord_client_stub = DiscordClientStub(event_bus)
    event_logger = InMemoryEventLogger()
    event_bus.subscribe(event_logger)
    app = AppClient(discord_client_stub, event_bus)
    app.start()

    await discord_client_stub.trigger_event(MessageReceivedEvent())
    assert len(event_logger.events), 1
