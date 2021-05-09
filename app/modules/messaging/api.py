from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional


class Kind(Enum):
    WELCOME = 0


class Validator(ABC):
    WELCOME_ARGS = ["new_member_name"]

    @abstractmethod
    def is_welcome(self, message: str) -> bool:
        """
        Ensure provided message is a correctly
        formatted welcome one.
        """


class Messages(ABC):
    @abstractmethod
    def save(self, kind: Kind, msg: str) -> bool:
        """
        Store message with correct kind.
        Variables has to be passed using the
        python format syntax.
        """

    @abstractmethod
    def welcome(self) -> str:
        """
        Retrieve stored welcome message if exits.
        """


class Channels(ABC):
    @abstractmethod
    def save(self, kind: Kind, id: int) -> bool:
        """
        Store channel id with correct kind.
        Those channel will be used for announcement.
        """

    @abstractmethod
    def welcome(self) -> Optional[int]:
        """Retrieve stored channel for welcome message"""
