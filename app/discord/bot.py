from app.discord import client

# flake8: noqa
from app.discord import messages  # load messages


def start(token: str):
    client.run(token)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_connect():
    print("connected")
