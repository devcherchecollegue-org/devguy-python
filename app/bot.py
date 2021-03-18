from dependency_injector.wiring import Provide

from app.dependencies import Dependencies
from app.transport import Discord


def run(discord: Discord = Provide(Dependencies.discord)):
    """
    Start running discord bot instance
    """
    discord.run()
