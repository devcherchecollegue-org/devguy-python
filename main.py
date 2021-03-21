#!/usr/bin/env python3
from json import load
from os import path

from environs import Env

from app import bot, dependencies
from app.dependencies import Dependencies


env = Env()
basedir = path.dirname(__file__)

with open('emoji_to_roles.json') as f:
    emoji_to_role = load(f)

# Read variables from .env && constant configs
env.read_env()

# Load environment and config from BOT_ENV variable name
app_env = env.str('BOT_ENV', 'local')

# Prepare dependencies
inject = Dependencies()
inject.config.from_ini(path.join(basedir, app_env + '.ini'), required=True)
inject.config.from_dict({
    'bot_secret_key': env.str('DISCORD_BOT_SECRET_KEY'),
    'admin_id':       env.int('DISCORD_BOT_ADMIN_ID'),
    'emoji_to_role':  emoji_to_role,
})

inject.wire(modules=[bot, dependencies])
dependencies.init_null_deps()  # setup database with orm ~~

# Start features :)
bot.run()
