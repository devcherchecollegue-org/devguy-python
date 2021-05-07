from discord import Message


class Usecase:
    @staticmethod
    def respond(message: Message, owner: str):
        if message.author.nick == owner:
            print("Bot speaking here")
            return

        return message.channel.send("Hello!")
