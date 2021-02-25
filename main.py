from environs import Env

from app.discord_client import DiscordClient

env = Env()
env.read_env()

DISCORD_BOT_SECRET_KEY = env.str('DISCORD_BOT_SECRET_KEY')
client = DiscordClient(DISCORD_BOT_SECRET_KEY)
client.run()
