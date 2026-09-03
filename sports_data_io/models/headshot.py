from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Headshot(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The primary position of the player. Possible Values: C; CB; DB; DE; DL; DT; FB; FS; G; ILB; K; KR; LB; LS; NT;
    OL; OLB; OT; P; QB; RB; S; SS; T; TE; WR"""

    preferred_hosted_headshot_url: OptionalNullable[str] = Field(default=UNSET, alias="PreferredHostedHeadshotUrl")
    """The player's preferred hosted headshot URL. This returns the headshot with transparent background, if
    available."""

    preferred_hosted_headshot_updated: OptionalNullable[str] = Field(
        default=UNSET, alias="PreferredHostedHeadshotUpdated"
    )
    """The last updated date of the player's preferred hosted headshot."""

    hosted_headshot_with_background_url: OptionalNullable[str] = Field(
        default=UNSET, alias="HostedHeadshotWithBackgroundUrl"
    )
    """The player's hosted headshot URL."""

    hosted_headshot_with_background_updated: OptionalNullable[str] = Field(
        default=UNSET, alias="HostedHeadshotWithBackgroundUpdated"
    )
    """The last updated date of the player's hosted headshot."""

    hosted_headshot_no_background_url: OptionalNullable[str] = Field(
        default=UNSET, alias="HostedHeadshotNoBackgroundUrl"
    )
    """The player's transparent background hosted headshot URL."""

    hosted_headshot_no_background_updated: OptionalNullable[str] = Field(
        default=UNSET, alias="HostedHeadshotNoBackgroundUpdated"
    )
    """The last updated date of the player's transparent background hosted headshot."""


class HeadshotDict(TypedDict):
    player_id: NotRequired[int]
    name: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    position: NotRequired[str | None]
    preferred_hosted_headshot_url: NotRequired[str | None]
    preferred_hosted_headshot_updated: NotRequired[str | None]
    hosted_headshot_with_background_url: NotRequired[str | None]
    hosted_headshot_with_background_updated: NotRequired[str | None]
    hosted_headshot_no_background_url: NotRequired[str | None]
    hosted_headshot_no_background_updated: NotRequired[str | None]
