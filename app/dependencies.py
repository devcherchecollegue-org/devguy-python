from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Singleton, Factory

from app.modules import roles_management, rubber_duck
from app.transport import Discord
from app.usecases import Roles, RubberDuck


class Dependencies(DeclarativeContainer):
    """
    Contain and manages dependencies for the bot
    """
    config = Configuration()

    # Inject roles
    role_module = Singleton(roles_management.Picker, emoji_to_roles=config.emoji_to_role)
    role = Factory(Roles, roles=role_module)

    # Inject mis
    misc_dao = Singleton(rubber_duck.DataAccessObject, config=config)
    misc_mod = Factory(rubber_duck.RubberDuck, dao=misc_dao)
    misc = Factory(RubberDuck, miscellaneous_module=misc_mod)

    # Inject transport
    discord = Factory(
        Discord,
        bot_secret_key=config.bot_secret,
        admin_id=config.admin_id,
        roles=role,
        misc=misc,
    )
