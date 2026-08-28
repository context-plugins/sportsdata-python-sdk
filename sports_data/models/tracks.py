from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Tracks(SdkBaseModel):
    track: OptionalNullable[str] = Field(default=UNSET, alias="Track")
    """The name of the track for this race"""


class TracksDict(TypedDict):
    track: NotRequired[str | None]
