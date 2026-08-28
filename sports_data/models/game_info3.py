from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .game_odd3 import GameOdd3, GameOdd3Dict


class GameInfo3(SdkBaseModel):
    game_id: Optional[int] = Field(default=UNSET, alias="GameId")
    """The unique ID of the game"""

    round_id: Optional[int] = Field(default=UNSET, alias="RoundId")
    """The unique ID of the round that this game is associated with"""

    season: Optional[int] = Field(default=UNSET, alias="Season")
    """The soccer regular season for which these totals apply"""

    season_type: Optional[int] = Field(default=UNSET, alias="SeasonType")
    """The type of season that this record corresponds to (1=Regular Season, 2=Preseason, 3=Postseason, 4=Offseason,
    5=AllStar)."""

    week: OptionalNullable[int] = Field(default=UNSET, alias="Week")
    """The week during the season/round in which this game occurs"""

    day: OptionalNullable[str] = Field(default=UNSET, alias="Day")
    """The day of the game"""

    date_time: OptionalNullable[str] = Field(default=UNSET, alias="DateTime")
    """The date and time of the game (in UTC)"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the game's status. Possible values include: Scheduled, InProgress, Break, Final, Awarded, Postponed,
    Canceled, Suspended, Start Delay, Rain Delay, No Result, & NotNecessary. If a game is called off before it starts,
    the Status is set to Postponed, until a new date/time is scheduled, at which point, the DateTime is updated, and the
    Status is set back to Scheduled. If a game has already started, and temporarily interrupted, it's Status is set to
    Suspended, until it either resumes, or gets postponed and replayed at a later date. If the game is at halftime, then
    the Status will be Break. Awarded is used in cases where a game is decided on the so called "green table." That
    means that a game was decided by the Federation/League to one team for a reason. This can include situations like
    riots, where the opponent team gets 3:0 win awarded as punishment. Awarded is also used when a club withdraws during
    the season from the competition then all the remaining matches getting awarded 3:0."""

    away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamId")
    """The unique ID of the away team"""

    home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamId")
    """The unique ID of the home team"""

    away_team_name: OptionalNullable[str] = Field(default=UNSET, alias="AwayTeamName")
    """The name of the away team"""

    home_team_name: OptionalNullable[str] = Field(default=UNSET, alias="HomeTeamName")
    """The name of the home team"""

    global_game_id: Optional[int] = Field(default=UNSET, alias="GlobalGameId")
    """A globally unique ID for this game. This value is guaranteed to be unique across all sports/leagues."""

    global_away_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalAwayTeamId")
    """A globally unique ID for the away team. This value is guaranteed to be unique across all sports/leagues."""

    global_home_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalHomeTeamId")
    """A globally unique ID for the home team. This value is guaranteed to be unique across all sports/leagues."""

    pregame_odds: Optional[list[GameOdd3]] = Field(default=UNSET, alias="PregameOdds")
    """List of Pregame Odds from different sportsbooks"""

    live_odds: Optional[list[GameOdd3]] = Field(default=UNSET, alias="LiveOdds")
    """List of Live Odds from different sportsbooks"""

    home_team_score: OptionalNullable[int] = Field(default=UNSET, alias="HomeTeamScore")
    """Score of the home team (updated after game ends to allow for resolving bets)"""

    away_team_score: OptionalNullable[int] = Field(default=UNSET, alias="AwayTeamScore")
    """Score of the away team (updated after game ends to allow for resolving bets)"""

    total_score: OptionalNullable[int] = Field(default=UNSET, alias="TotalScore")
    """The total combined score of both teams in the game (updated after game ends to allow for resolving bets)"""

    alternate_market_pregame_odds: Optional[list[GameOdd3]] = Field(default=UNSET, alias="AlternateMarketPregameOdds")
    """List of Alternate Market GameOdds from different sportsbooks (such as 1st-half, 1st-qtr, etc)"""


class GameInfo3Dict(TypedDict):
    game_id: NotRequired[int]
    round_id: NotRequired[int]
    season: NotRequired[int]
    season_type: NotRequired[int]
    week: NotRequired[int | None]
    day: NotRequired[str | None]
    date_time: NotRequired[str | None]
    status: NotRequired[str | None]
    away_team_id: NotRequired[int | None]
    home_team_id: NotRequired[int | None]
    away_team_name: NotRequired[str | None]
    home_team_name: NotRequired[str | None]
    global_game_id: NotRequired[int]
    global_away_team_id: NotRequired[int | None]
    global_home_team_id: NotRequired[int | None]
    pregame_odds: NotRequired[list[GameOdd3 | GameOdd3Dict]]
    live_odds: NotRequired[list[GameOdd3 | GameOdd3Dict]]
    home_team_score: NotRequired[int | None]
    away_team_score: NotRequired[int | None]
    total_score: NotRequired[int | None]
    alternate_market_pregame_odds: NotRequired[list[GameOdd3 | GameOdd3Dict]]
