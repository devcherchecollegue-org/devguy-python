from app.discord import client

# flake8: noqa
from app.discord import messages  # load messages

# This file cannot be tested through unit testing cause it requires to start a true discord application.
# It could be done through dependencie injection using a mocked discord instance then starting though but
# it does not have much sense testing it as it only logs some information for bot startup.


def start(token: str):  # pragma: no-cover
    client.run(token)


@client.event
async def on_ready():  # pragma: no-cover
    print(f"We have logged in as {client.user}")


@client.event
async def on_connect():  # pragma: no-cover
    print("connected")
