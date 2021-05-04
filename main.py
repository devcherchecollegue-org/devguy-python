#!/usr/bin/env python3
from app.discord import bot
from configparser import ConfigParser
from os import environ, path

config = ConfigParser(environ)
config.read(f"{path.dirname(__file__)}/config.ini")

bot.start(config.get("bot", "token"))
