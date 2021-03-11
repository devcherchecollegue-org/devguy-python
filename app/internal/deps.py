from configparser import ConfigParser

from dependency_injector import containers, providers

from app.modules import miscellaneous as miscellaneous_mod
from app.modules.roles.roles import Roles as RolesMod
from app.transport import Discord
from app.usecases import Miscellaneous, Roles


class Inject(containers.DeclarativeContainer):
    config = providers.Configuration()
    __config = ConfigParser()
    __config.read(str(config.conf_path))

    # Inject roles
    role_module = providers.Singleton(RolesMod, config.emoji_to_role)

    role = providers.Factory(Roles, role_module)

    # Inject mis
    misc_dao = providers.Singleton(miscellaneous_mod.DAO, __config)
    misc_mod = providers.Factory(miscellaneous_mod.Miscellaneous, misc_dao)
    misc = providers.Factory(Miscellaneous, misc_mod)

    # Inject transport
    discord = providers.Factory(
        Discord,
        bot_secret_key=config.bot_secret,
        admin_id=config.admin_id,
        roles=role,
        misc=misc,
    )
