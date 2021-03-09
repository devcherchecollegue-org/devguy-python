from configparser import ConfigParser
from json import load
from os import environ, path

from environs import Env

from app.discord_client import DiscordClient

config = ConfigParser()
env = Env()

# Load environment and config from BOT_ENV variable name
env = environ.get("BOT_ENV", 'local')
basedir = path.dirname(__file__)

env.read_env()
config.read(path.join(basedir, env + '.ini'))

DISCORD_BOT_SECRET_KEY = env.str('DISCORD_BOT_SECRET_KEY')
DISCORD_BOT_ADMIN_ID = env.int('DISCORD_BOT_ADMIN_ID')

with open('emoji_to_roles.json') as f:
    emoji_to_role = load(f)

client = DiscordClient(
    bot_secret_key=DISCORD_BOT_SECRET_KEY,
    admin_id=DISCORD_BOT_ADMIN_ID,
    emoji_to_role=emoji_to_role
)
client.run()
