#!/usr/bin/env python3
from configparser import ConfigParser
from json import load
from os import environ, path

from environs import Env

from app.modules.roles.roles import Roles as RolesMod
from app.transport import Discord
from app.usecases import Roles

config = ConfigParser()
env = Env()

# Load environment and config from BOT_ENV variable name
app_env = environ.get("BOT_ENV", 'local')
basedir = path.dirname(__file__)

# Read variables from .env && constant configs
env.read_env()
config.read(path.join(basedir, app_env + '.ini'))

DISCORD_BOT_SECRET_KEY = env.str('DISCORD_BOT_SECRET_KEY')
DISCORD_BOT_ADMIN_ID = env.int('DISCORD_BOT_ADMIN_ID')

with open('emoji_to_roles.json') as f:
    emoji_to_role = load(f)

# Prepare dependencies
roles_module = RolesMod(emoji_to_role)  # find a way to cleanly inject deps in python
roles = Roles(roles_module)

client = Discord(
    bot_secret_key=DISCORD_BOT_SECRET_KEY,
    admin_id=DISCORD_BOT_ADMIN_ID,
    roles=roles
)

client.run()
