from abc import abstractmethod, ABC
from app.core.sqlalchemy import Base
from .api import Kind, Validator, Messages
from string import Formatter
from sqlalchemy.orm import Column, Integer, Varchar, Datetime
from datetime import datetime


class _Validator(Validator):
    def is_welcome(self, message: str) -> bool:
        args = [tup[1] for tup in Formatter().parse(message) if tup[1] is not None]
        return args == self.WELCOME_ARGS


class _MessageEntity(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key="true", autoincrement=True)
    kind = Column(Integer, nullable=False)
    content = Column(Varchar(500), nullable=False)

    created_at = Column(Datetime, nullable=False, default=datetime.utcnow)
    last_updated_at = Column(Datetime, nullable=False, default=datetime.utcnow)


class _MessageQueries(ABC):
    @abstractmethod
    def insert(self, message: _MessageEntity):
        """Insert message into DB"""

    @abstractmethod
    def update(self, message: _MessageEntity):
        """Update message into DB"""

    @abstractmethod
    def get(self, message_kind: Kind):
        """Get current message for provided kind"""


class _Messages(Messages):
    def __init__(self, querier: _MessageQueries):
        self.__query = querier

    def save(self, kind: Kind, content: str):
        msg = None
        try:
            msg = self.__query.get(kind)
        except Exception as e:
            print(e)
            return False

        if not msg:
            msg = _MessageEntity(kind=kind.value, content=content)
            return self.__query.insert(msg)

        msg.content = content
        return self.__query.update(msg)
