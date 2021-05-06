from discord import Message

from app.discord import client
from app.modules import hello


@client.event
async def on_message(message: Message):
    if message.content.startswith("hello"):
        await hello.respond(message, client.user.name)
