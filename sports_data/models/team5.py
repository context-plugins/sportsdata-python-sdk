from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .stadium41 import Stadium41, Stadium41Dict


class Team5(SdkBaseModel):
    key: OptionalNullable[str] = Field(default=UNSET, alias="Key")
    """Abbreviation [Key] of the team (e.g. PHI; NE; IND; etc.)"""

    team_id: Optional[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The auto-generated unique ID of the Team; that avoids collisions with PlayerIDs. This is useful when combining
    players and fantasy defenses to create fantasy teams"""

    city: OptionalNullable[str] = Field(default=UNSET, alias="City")
    """The city/location of the team (e.g. Minnesota; Philadelphia; New England; Indianapolis; etc.)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """The mascot of the team (e.g. Eagles; Patriots; Colts; etc.)"""

    conference: OptionalNullable[str] = Field(default=UNSET, alias="Conference")
    """The conference of the team (e.g. AFC or NFC)"""

    division: OptionalNullable[str] = Field(default=UNSET, alias="Division")
    """The division of the team (e.g. East, North, South, West)"""

    full_name: OptionalNullable[str] = Field(default=UNSET, alias="FullName")
    """The full name of the team (e.g. New England Patriots)"""

    stadium_id: OptionalNullable[int] = Field(default=UNSET, alias="StadiumID")
    """The unique ID of the team's current home stadium"""

    bye_week: OptionalNullable[int] = Field(default=UNSET, alias="ByeWeek")
    """The bye week of the team in the upcoming or current regular season"""

    average_draft_position: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPosition")
    """The average draft position of the team's fantasy defense (DST) in re-draft leagues"""

    average_draft_position_ppr: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPositionPPR")
    """The average draft position of the team (DST) in Points Per Reception (PPR) leagues"""

    head_coach: OptionalNullable[str] = Field(default=UNSET, alias="HeadCoach")
    """The current head coach of the team"""

    offensive_coordinator: OptionalNullable[str] = Field(default=UNSET, alias="OffensiveCoordinator")
    """The current offensive coordinator of the team. Note: field will be NULL if team doesn't have an OFF
    coordinator"""

    defensive_coordinator: OptionalNullable[str] = Field(default=UNSET, alias="DefensiveCoordinator")
    """The current offensive coordinator of the team. Note: field will be NULL if team doesn't have an DEF
    coordinator"""

    special_teams_coach: OptionalNullable[str] = Field(default=UNSET, alias="SpecialTeamsCoach")
    """The current special teams coordinator of the team. Note: field will be NULL if team doesn't have an ST
    coordinator"""

    offensive_scheme: OptionalNullable[str] = Field(default=UNSET, alias="OffensiveScheme")
    """The offensive scheme this team runs (PRO, 2TE, 3WR). This is decided at our discretion."""

    defensive_scheme: OptionalNullable[str] = Field(default=UNSET, alias="DefensiveScheme")
    """The current defensive scheme this team runs (3-4, 4-3)"""

    upcoming_salary: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingSalary")
    """The team's DEF/ST salary for the upcoming week in accordance with a $50,000 salary cap. This is used for daily
    fantasy sports salary cap contests. Salaries represent those published by DraftKings. When DraftKings doesn't
    publish a salary for a given game; the most recent DraftKings salary is used"""

    upcoming_opponent: OptionalNullable[str] = Field(default=UNSET, alias="UpcomingOpponent")
    """The opponent team the team is playing against in the upcoming week"""

    upcoming_opponent_rank: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingOpponentRank")
    """The team's upcoming opponent's rank in DEF/ST fantasy points allowed."""

    upcoming_opponent_position_rank: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingOpponentPositionRank")
    """The team's upcoming opponent's rank in DEF/ST fantasy points allowed."""

    upcoming_fan_duel_salary: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingFanDuelSalary")
    """The team's DEF/ST DraftKings salary for the upcoming week. Note: We recommend using our new DFS endpoints
    instead."""

    upcoming_draft_kings_salary: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingDraftKingsSalary")
    """The team's DEF/ST DraftKings salary for the upcoming week. Note: We recommend using our new DFS endpoints
    instead"""

    upcoming_yahoo_salary: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingYahooSalary")
    """The team's DEF/ST Yahoo salary for the upcoming week"""

    primary_color: OptionalNullable[str] = Field(default=UNSET, alias="PrimaryColor")
    """The team's primary color. (This is not licensed for public or commercial use)"""

    secondary_color: OptionalNullable[str] = Field(default=UNSET, alias="SecondaryColor")
    """The team's secondary color. (This is not licensed for public or commercial use)"""

    tertiary_color: OptionalNullable[str] = Field(default=UNSET, alias="TertiaryColor")
    """The team's tertiary color. (This is not licensed for public or commercial use)"""

    quaternary_color: OptionalNullable[str] = Field(default=UNSET, alias="QuaternaryColor")
    """The team's quaternary color. (This is not licensed for public or commercial use)"""

    wikipedia_logo_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaLogoUrl")
    """The link to the team's logo hosted on Wikipedia (This is not licensed for public or commercial use)"""

    wikipedia_word_mark_url: OptionalNullable[str] = Field(default=UNSET, alias="WikipediaWordMarkUrl")
    """The link to the team's wordmark logo hosted on Wikipedia (This is not licensed for public or commercial use)"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    draft_kings_name: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsName")
    """Team's D/ST name on DraftKings daily fantasy contests"""

    draft_kings_player_id: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsPlayerID")
    """Team's D/ST player ID on DraftKings daily fantasy contests"""

    fan_duel_name: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelName")
    """Team's D/ST name on FanDuel daily fantasy contests"""

    fan_duel_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FanDuelPlayerID")
    """Team's DST player ID on FanDuel daily fantasy contests"""

    fantasy_draft_name: OptionalNullable[str] = Field(default=UNSET, alias="FantasyDraftName")
    """Team's D/ST name on daily FantasyDraft daily fantasy contests"""

    fantasy_draft_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDraftPlayerID")
    """Team's D/ST player ID on daily FantasyDraft daily fantasy contests"""

    yahoo_name: OptionalNullable[str] = Field(default=UNSET, alias="YahooName")
    """Team's D/ST name on Yahoo daily fantasy contests"""

    yahoo_player_id: OptionalNullable[int] = Field(default=UNSET, alias="YahooPlayerID")
    """Team's D/ST player ID on Yahoo daily fantasy contests"""

    stadium_details: Optional[Stadium41] = Field(default=UNSET, alias="StadiumDetails")
    """The details of this team's home stadium"""

    average_draft_position2_qb: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPosition2QB")
    """The average draft position of the team (DST) in 2 Quarterback leagues"""

    average_draft_position_dynasty: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPositionDynasty")
    """The average draft position of this team (DST) in dynasty leagues"""


class Team5Dict(TypedDict):
    key: NotRequired[str | None]
    team_id: NotRequired[int]
    player_id: NotRequired[int]
    city: NotRequired[str | None]
    name: NotRequired[str | None]
    conference: NotRequired[str | None]
    division: NotRequired[str | None]
    full_name: NotRequired[str | None]
    stadium_id: NotRequired[int | None]
    bye_week: NotRequired[int | None]
    average_draft_position: NotRequired[float | None]
    average_draft_position_ppr: NotRequired[float | None]
    head_coach: NotRequired[str | None]
    offensive_coordinator: NotRequired[str | None]
    defensive_coordinator: NotRequired[str | None]
    special_teams_coach: NotRequired[str | None]
    offensive_scheme: NotRequired[str | None]
    defensive_scheme: NotRequired[str | None]
    upcoming_salary: NotRequired[int | None]
    upcoming_opponent: NotRequired[str | None]
    upcoming_opponent_rank: NotRequired[int | None]
    upcoming_opponent_position_rank: NotRequired[int | None]
    upcoming_fan_duel_salary: NotRequired[int | None]
    upcoming_draft_kings_salary: NotRequired[int | None]
    upcoming_yahoo_salary: NotRequired[int | None]
    primary_color: NotRequired[str | None]
    secondary_color: NotRequired[str | None]
    tertiary_color: NotRequired[str | None]
    quaternary_color: NotRequired[str | None]
    wikipedia_logo_url: NotRequired[str | None]
    wikipedia_word_mark_url: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
    draft_kings_name: NotRequired[str | None]
    draft_kings_player_id: NotRequired[int | None]
    fan_duel_name: NotRequired[str | None]
    fan_duel_player_id: NotRequired[int | None]
    fantasy_draft_name: NotRequired[str | None]
    fantasy_draft_player_id: NotRequired[int | None]
    yahoo_name: NotRequired[str | None]
    yahoo_player_id: NotRequired[int | None]
    stadium_details: NotRequired[Stadium41 | Stadium41Dict]
    average_draft_position2_qb: NotRequired[float | None]
    average_draft_position_dynasty: NotRequired[float | None]
