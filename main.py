from os import environ, path
from dotenv import load_dotenv
from app.discord_client import DiscordClient
from app.app_client import AppClient
from app.shared.event.event_bus import EventBus
from app.shared.event.event_logger import EventLogger

if environ.get("BOT_ENV") == "development":
    basedir = path.dirname(__file__)
    load_dotenv(path.join(basedir, '.env.development'))

event_bus = EventBus()
event_logger = EventLogger()
event_bus.subscribe(event_logger)

discord_client = DiscordClient(
    environ.get("DISCORD_BOT_SECRET_KEY"), event_bus)
app = AppClient(discord_client, event_bus)
app.start()
