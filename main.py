from os import environ, path

from dotenv import load_dotenv

from app.discord_client import DiscordClient

if environ.get("BOT_ENV") == "development":
    basedir = path.dirname(__file__)
    load_dotenv(path.join(basedir, '.env.development'))

client = DiscordClient()
client.run(environ.get("DISCORD_BOT_SECRET_KEY"))
