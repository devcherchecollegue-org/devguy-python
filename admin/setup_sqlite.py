#!/usr/bin/env python3

import sqlite3
import sys
from configparser import ConfigParser
from os import environ, pardir, path

config = ConfigParser()

# Load environment and config from BOT_ENV variable name
env = environ.get('BOT_ENV', 'local')
basedir = path.abspath(path.join(path.dirname(__file__), pardir))

config.read(path.join(basedir, env + '.ini'))

INIT_DATABASE_REQUEST = """
CREATE TABLE IF NOT EXISTS coin_coin (
    id integer primary key,
    user_id text not null   
);

"""

try:
    CONN = sqlite3.connect(config.get('database', 'database'))
except sqlite3.Error as error:
    print(error)
    sys.exit(2)

try:
    cursor = CONN.cursor()
    cursor.execute(INIT_DATABASE_REQUEST)
    CONN.close()
except sqlite3.Error as error:
    print(error)
    CONN.close()
    sys.exit(3)
