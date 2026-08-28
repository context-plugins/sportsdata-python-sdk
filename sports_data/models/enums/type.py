from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type(str, Enum):
    CURRENT = "current"
    UPCOMING = "upcoming"
    COMPLETED = "completed"
    RECENT = "recent"
    ALL = "all"

    __str__ = str.__str__


TypeOrStr: TypeAlias = Annotated[Type | str, open_enum_validator(Type)]
