from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Lineup4(SdkBaseModel):
    lineup_id: Optional[int] = Field(default=UNSET, alias="LineupId")
    """The unique ID of this lineup"""

    game_id: Optional[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of the game tied to this lineup"""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="Type")
    """The player's status in the lineup. Possible values: Substitute In; Starter; Bench."""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamId")
    """The unique ID of the team associated with this lineup"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerId")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID stays with the player their entire
    career."""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The player's full name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The position of the player. Possible values include: A (Attacker); M (Midfielder); D (Defender); GK
    (Goalkeeper)."""

    replaced_player_id: OptionalNullable[int] = Field(default=UNSET, alias="ReplacedPlayerId")
    """The unique ID of the replaced player"""

    replaced_player_name: OptionalNullable[str] = Field(default=UNSET, alias="ReplacedPlayerName")
    """The name of the replaced player"""

    game_minute: OptionalNullable[int] = Field(default=UNSET, alias="GameMinute")
    """The minute of the game"""

    game_minute_extra: OptionalNullable[int] = Field(default=UNSET, alias="GameMinuteExtra")
    """The extra minute of the game"""

    pitch_position_horizontal: OptionalNullable[int] = Field(default=UNSET, alias="PitchPositionHorizontal")
    """The pitch position of where this player lined up on the field. Note: This is used for rendering an image of a
    soccer/football field with the players marked as such. This will be a number between 0 and 50."""

    pitch_position_vertical: OptionalNullable[int] = Field(default=UNSET, alias="PitchPositionVertical")
    """The pitch position of where this player lined up on the field. Note: This is used for rendering an image of a
    soccer/football field with the players marked as such. This will be a number between 0 and 50."""


class Lineup4Dict(TypedDict):
    lineup_id: NotRequired[int]
    game_id: NotRequired[int]
    type_: NotRequired[str | None]
    team_id: NotRequired[int]
    player_id: NotRequired[int]
    name: NotRequired[str | None]
    position: NotRequired[str | None]
    replaced_player_id: NotRequired[int | None]
    replaced_player_name: NotRequired[str | None]
    game_minute: NotRequired[int | None]
    game_minute_extra: NotRequired[int | None]
    pitch_position_horizontal: NotRequired[int | None]
    pitch_position_vertical: NotRequired[int | None]
