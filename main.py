from environs import Env
from json import load

from app.discord_client import DiscordClient

env = Env()
env.read_env()

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
