from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Playerstoinclude(str, Enum):
    ALL = "all"
    FANTASY = "fantasy"
    IDP = "idp"

    __str__ = str.__str__


PlayerstoincludeOrStr: TypeAlias = Annotated[Playerstoinclude | str, open_enum_validator(Playerstoinclude)]
