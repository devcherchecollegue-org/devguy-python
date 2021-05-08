from .api import Kind, Validator, Messages
from string import Formatter


class _Validator(Validator):
    def is_welcome(self, message: str) -> bool:
        args = [tup[1] for tup in Formatter().parse(message) if tup[1] is not None]
        return args == self.WELCOME_ARGS


class _MessageEntity(BaseModel):


class _Messages(Messages):
    def save(self, kind: Kind, msg: str):
        
