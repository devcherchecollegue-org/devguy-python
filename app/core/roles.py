from pydantic import BaseModel
from discord import Guild, colour
from typing import Optional, List


class Role(BaseModel):
    color: Optional[str] = None
    name: str

    async def create(self, guild: Guild):
        if self.color:
            return guild.create_role(
                name=self.name,
                colour=colour.Colour(f"0x{self.color}"),
            )

        return guild.create_role(name=self.name)


def requires_role(
    role: Role, in_roles: List[Role], err: Exception = Exception("forbiden")
):
    if all(role.name != candidate.name for candidate in in_roles):
        raise err


ADMIN = Role(name="devguy_admin")
