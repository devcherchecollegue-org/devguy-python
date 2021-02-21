import discord


class DiscordClient(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        # example when bot is ready
        print("Le bot est vivant!")

    async def on_message(self, message):
        # example
        # if a discord user send 'Hello', bot will answer 'bonjour'
        if message.content == "hello":
            await message.channel.send("bonjour")
