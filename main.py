from os import environ, path
from dotenv import load_dotenv
from app.discord_client import DiscordClient
from app.app_client import AppClient

if environ.get("BOT_ENV") == "development":
    basedir = path.dirname(__file__)
    load_dotenv(path.join(basedir, '.env.development'))

discord_client = DiscordClient(environ.get("DISCORD_BOT_SECRET_KEY"))
app = AppClient(discord_client)
app.start()
