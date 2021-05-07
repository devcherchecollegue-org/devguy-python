from discord import Message
from discord import Client
from app.discord import client
from app.modules import hello


@client.event
async def on_message(
    message: Message,
    usecase: hello.Usecase = hello.Usecase(),
    cli: Client = client,
):
    if message.content.startswith("hello"):
        await usecase.respond(message, cli.user.name)
