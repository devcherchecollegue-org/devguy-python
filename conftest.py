# Prepare dependencies
from json import load
from os import path

from environs import Env

from app import bot, dependencies
from app.dependencies import Dependencies


env = Env()
basedir = path.dirname(__file__)

with open(path.join(basedir, 'emoji_to_roles.json')) as f:
    emoji_to_role = load(f)

# Read variables from .env && constant configs
env.read_env()

# Load environment and config from BOT_ENV variable name
app_env = env.str('BOT_ENV', 'test')

inject = Dependencies()
inject.config.from_ini(path.join(basedir, app_env + '.ini'), required=True)
inject.config.from_dict({
    'bot_secret_key': 'TEST_BOT_SECRET',
    'admin_id':       1587,
    'emoji_to_role':  emoji_to_role,
})

inject.wire(modules=[bot, dependencies])
dependencies.init_null_deps()  # setup database with orm ~~
