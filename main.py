#!/usr/bin/env python3
import sys
from configparser import ConfigParser
from json import load
from os import environ, path

from environs import Env

from app.internal import bot
from app.internal.deps import Inject

config = ConfigParser()
env = Env()

# Load environment and config from BOT_ENV variable name
app_env = environ.get("BOT_ENV", 'local')
basedir = path.dirname(__file__)

# Read variables from .env && constant configs
env.read_env()

with open('emoji_to_roles.json') as f:
    emoji_to_role = load(f)

# Prepare dependencies
inject = Inject()
inject.config.from_ini(path.join(basedir, app_env + '.ini'), required=True)
inject.config.from_dict({
    'bot_secret':    env.str('DISCORD_BOT_SECRET_KEY'),
    'admin_id':      env.int('DISCORD_BOT_ADMIN_ID'),
    'emoji_to_role': emoji_to_role,
})
inject.wire(modules=[sys.modules['app.internal.bot']])
# Start features :)
bot.run()
