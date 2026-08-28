from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Split(str, Enum):
    L = "L"
    R = "R"
    S = "S"

    __str__ = str.__str__


SplitOrStr: TypeAlias = Annotated[Split | str, open_enum_validator(Split)]
