from pony.orm import PrimaryKey, Required

from app import pony_db


class RubberDuck(pony_db.Entity):
    id = PrimaryKey(int, auto=True)
    user_id = Required(int, size=64)

    def to_domains(self) -> int:
        return self.user_id
