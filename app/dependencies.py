from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory, Singleton

from app.modules import roles_management, rubber_duck
from app.transport import Discord
from app.usecases import Roles, RubberDuck


class Dependencies(DeclarativeContainer):
    """
    Contain and manages dependencies for the bot
    """
    config = Configuration()

    # Inject roles
    role_module = Singleton(roles_management.Picker, emoji_to_role=config.emoji_to_role)
    role = Factory(Roles, roles=role_module)

    # Inject mis
    rubber_duck_dao = Singleton(rubber_duck.DataAccessObject, config=config)
    rubber_duck_mod = Factory(rubber_duck.RubberDuck, dao=rubber_duck_dao)
    rubber_duck_uc = Factory(RubberDuck, rubber_duck_module=rubber_duck_mod)

    # Inject transport
    discord = Factory(
        Discord,
        bot_secret_key=config.bot_secret_key,
        admin_id=config.admin_id,
        command_prefix=config.bot.prefix,
        roles=role,
        rubber_duck=rubber_duck_uc,
    )
