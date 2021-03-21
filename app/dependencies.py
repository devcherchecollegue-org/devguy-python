from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory, Singleton
from dependency_injector.wiring import Provide

from app import pony_db
from app.modules import roles_management, rubber_duck
# noinspection PyUnresolvedReferences
# from app.modules.models import sql  # import sql to make generate_mapping work
from app.transport import Discord
from app.usecases import Roles, RubberDuck


def _setup_pony(
        provider: str,
        filename: str,
        create_db: bool = True,
        create_tables: bool = True,
) -> None:
    pony_db.bind(provider=provider, filename=filename, create_db=create_db)
    pony_db.generate_mapping(create_tables=create_tables)


class Dependencies(DeclarativeContainer):
    """
    Contain and manages dependencies for the bot
    """
    config = Configuration()

    # Setup db
    db = Singleton(
        _setup_pony,
        provider=config.database.type,
        filename=config.database.name,
    )

    # Inject roles
    role_module = Singleton(roles_management.Picker, emoji_to_role=config.emoji_to_role)
    role = Factory(Roles, roles=role_module)

    # Inject mis
    rubber_duck_dao = Singleton(rubber_duck.DataAccessObject)
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


def init_null_deps(_db=Provide(Dependencies.db)):
    pass
