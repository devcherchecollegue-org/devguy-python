from dependency_injector.wiring import Provide

from app.internal.deps import Inject
from app.transport import Discord


def run(discord: Discord = Provide(Inject.discord)):
    discord.run()
