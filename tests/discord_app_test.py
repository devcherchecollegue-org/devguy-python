from app.app_client import AppClient
from stubs.discord_client_stub import DiscordClientStub


def test_app_run_bot_client_on_start():
    discord_client_stub = DiscordClientStub()
    app = AppClient(discord_client_stub)
    app.start()
    assert discord_client_stub.is_start == True
