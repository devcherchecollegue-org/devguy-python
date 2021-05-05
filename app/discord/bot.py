from app.discord import client

from app.discord import messages, events

# This file cannot be tested through unit testing cause it requires to start a true discord application.
# It could be done through dependencie injection using a mocked discord instance then starting though but
# it does not have much sense testing it as it only logs some information for bot startup.


def start(token: str):  # pragma: no-cover
    events.Events(None)  # TODO: inject messenger
    messages.Message(None)
    client.run(token)


@client.event  # pragma: no-cover
async def on_ready():  # pragma: no-cover
    print(f"We have logged in as {client.user}")
