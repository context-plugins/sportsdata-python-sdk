from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Headshot(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique ID of the golfer"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The name of the golfer"""

    preferred_hosted_headshot_url: OptionalNullable[str] = Field(default=UNSET, alias="PreferredHostedHeadshotUrl")
    """The player's preferred hosted headshot URL. This returns the headshot with transparent background; if
    available"""

    preferred_hosted_headshot_updated: OptionalNullable[str] = Field(
        default=UNSET, alias="PreferredHostedHeadshotUpdated"
    )
    """The last updated date of the player's preferred hosted headshot"""

    hosted_headshot_with_background_url: OptionalNullable[str] = Field(
        default=UNSET, alias="HostedHeadshotWithBackgroundUrl"
    )
    """The player's hosted headshot URL"""

    hosted_headshot_with_background_updated: OptionalNullable[str] = Field(
        default=UNSET, alias="HostedHeadshotWithBackgroundUpdated"
    )
    """The timestamp of when the player's hosted headshot was last updated"""

    hosted_headshot_no_background_url: OptionalNullable[str] = Field(
        default=UNSET, alias="HostedHeadshotNoBackgroundUrl"
    )
    """The player's transparent background hosted headshot URL"""

    hosted_headshot_no_background_updated: OptionalNullable[str] = Field(
        default=UNSET, alias="HostedHeadshotNoBackgroundUpdated"
    )
    """The timestamp of when the player's transparent background hosted headshot was last updated"""


class HeadshotDict(TypedDict):
    player_id: NotRequired[int]
    name: NotRequired[str | None]
    preferred_hosted_headshot_url: NotRequired[str | None]
    preferred_hosted_headshot_updated: NotRequired[str | None]
    hosted_headshot_with_background_url: NotRequired[str | None]
    hosted_headshot_with_background_updated: NotRequired[str | None]
    hosted_headshot_no_background_url: NotRequired[str | None]
    hosted_headshot_no_background_updated: NotRequired[str | None]
