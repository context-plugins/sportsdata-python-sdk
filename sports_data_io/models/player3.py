from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Player3(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """"The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career"
    """

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The first name of the player"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The player's last name"""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """The player's current status. Possible values include Active; Inactive; Injured Reserve; Minors; Suspended;
    Bereavement; Paternity"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team this player is employed by"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's primary position. Possible values: C, RW, LW, D, or G."""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number"""

    catches: OptionalNullable[str] = Field(default=UNSET, alias="Catches")
    """The hand in which the player uses to catch the puck (Right or Left). Note: This field will be null for
    non-goaltenders"""

    shoots: OptionalNullable[str] = Field(default=UNSET, alias="Shoots")
    """The hand the player shoots the puck with (right or left)"""

    height: OptionalNullable[int] = Field(default=UNSET, alias="Height")
    """The player's height in inches"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The player's weight in pounds (lbs)."""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The player's date of birth"""

    birth_city: OptionalNullable[str] = Field(default=UNSET, alias="BirthCity")
    """The city in which the player was born"""

    birth_state: OptionalNullable[str] = Field(default=UNSET, alias="BirthState")
    """The US state in which the player was born. NOTE: If a player was born outside of North America or Australia, this
    field will be null"""

    photo_url: OptionalNullable[str] = Field(default=UNSET, alias="PhotoUrl")
    """This field is deprecated. Photos are no longer available through it. Headshots are now delivered through IMAGN.
    Please see our Headshots products for further information."""

    sport_radar_player_id: OptionalNullable[str] = Field(default=UNSET, alias="SportRadarPlayerID")
    """The player's cross reference PlayerID to the SportRadar API."""

    rotoworld_player_id: OptionalNullable[int] = Field(default=UNSET, alias="RotoworldPlayerID")
    """The player's cross reference PlayerID to the Rotoworld news feed"""

    roto_wire_player_id: OptionalNullable[int] = Field(default=UNSET, alias="RotoWirePlayerID")
    """The player's cross reference PlayerID to the RotoWire news feed"""

    fantasy_alarm_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyAlarmPlayerID")
    """The player's cross reference PlayerID to the FantasyAlarm news feed"""

    stats_player_id: OptionalNullable[int] = Field(default=UNSET, alias="StatsPlayerID")
    """The player's cross reference PlayerID to the STATS data feeds"""

    sports_direct_player_id: OptionalNullable[int] = Field(default=UNSET, alias="SportsDirectPlayerID")
    """The player's cross reference PlayerID to the SportsDirect data feeds, now part of Nielsen GraceNote."""

    xml_team_player_id: OptionalNullable[int] = Field(default=UNSET, alias="XmlTeamPlayerID")
    """The player's cross reference PlayerID to the XML Team data feeds."""

    injury_status: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStatus")
    """The player's current injury status; in the form of likelihood that player plays. Possible values: Probable;
    Questionable; Doubtful; Out"""

    injury_body_part: OptionalNullable[str] = Field(default=UNSET, alias="InjuryBodyPart")
    """The body part that is injured for the player (Knee; Groin; Calf; Upper-body; etc.)"""

    injury_start_date: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStartDate")
    """The day that the injury started or was first discovered"""

    injury_notes: OptionalNullable[str] = Field(default=UNSET, alias="InjuryNotes")
    """Brief description of the player's injury and expected availability"""

    fan_duel_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FanDuelPlayerID")
    """The player's cross reference PlayerID to FanDuel"""

    draft_kings_player_id: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsPlayerID")
    """The player's cross reference PlayerID to DraftKings"""

    yahoo_player_id: OptionalNullable[int] = Field(default=UNSET, alias="YahooPlayerID")
    """The player's cross reference PlayerID to Yahoo Daily Fantasy Sports Contests."""

    fan_duel_name: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelName")
    """The player's full name in FanDuel's daily fantasy sports platform"""

    draft_kings_name: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsName")
    """The player's full name in DraftKings' daily fantasy sports platform"""

    yahoo_name: OptionalNullable[str] = Field(default=UNSET, alias="YahooName")
    """The player's full name in Yahoo's daily fantasy sports platform."""

    depth_chart_position: OptionalNullable[str] = Field(default=UNSET, alias="DepthChartPosition")
    """The position of the player in the team's depth chart"""

    depth_chart_order: OptionalNullable[int] = Field(default=UNSET, alias="DepthChartOrder")
    """The order of the player in the team's depth chart"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    fantasy_draft_name: OptionalNullable[str] = Field(default=UNSET, alias="FantasyDraftName")
    """The player's full name in FantasyDraft's daily fantasy sports platform"""

    fantasy_draft_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDraftPlayerID")
    """The player's cross reference PlayerID to FantasyDraft"""

    usa_today_player_id: OptionalNullable[int] = Field(default=UNSET, alias="UsaTodayPlayerID")
    """The player's cross reference PlayerID to USA Today headshot data feeds."""

    usa_today_headshot_url: OptionalNullable[str] = Field(default=UNSET, alias="UsaTodayHeadshotUrl")
    """The player's headshot URL as provided by USA Today. License from USA Today is required."""

    usa_today_headshot_no_background_url: OptionalNullable[str] = Field(
        default=UNSET, alias="UsaTodayHeadshotNoBackgroundUrl"
    )
    """The player's transparent background headshot URL as provided by USA Today. License from USA Today is required."""

    usa_today_headshot_updated: OptionalNullable[str] = Field(default=UNSET, alias="UsaTodayHeadshotUpdated")
    """The last updated date of the player's headshot as provided by USA Today. License from USA Today is required."""

    usa_today_headshot_no_background_updated: OptionalNullable[str] = Field(
        default=UNSET, alias="UsaTodayHeadshotNoBackgroundUpdated"
    )
    """The last updated date of the player's transparent background headshot as provided by USA Today. License from USA
    Today is required."""


class Player3Dict(TypedDict):
    player_id: NotRequired[int]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    status: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    position: NotRequired[str | None]
    jersey: NotRequired[int | None]
    catches: NotRequired[str | None]
    shoots: NotRequired[str | None]
    height: NotRequired[int | None]
    weight: NotRequired[int | None]
    birth_date: NotRequired[str | None]
    birth_city: NotRequired[str | None]
    birth_state: NotRequired[str | None]
    photo_url: NotRequired[str | None]
    sport_radar_player_id: NotRequired[str | None]
    rotoworld_player_id: NotRequired[int | None]
    roto_wire_player_id: NotRequired[int | None]
    fantasy_alarm_player_id: NotRequired[int | None]
    stats_player_id: NotRequired[int | None]
    sports_direct_player_id: NotRequired[int | None]
    xml_team_player_id: NotRequired[int | None]
    injury_status: NotRequired[str | None]
    injury_body_part: NotRequired[str | None]
    injury_start_date: NotRequired[str | None]
    injury_notes: NotRequired[str | None]
    fan_duel_player_id: NotRequired[int | None]
    draft_kings_player_id: NotRequired[int | None]
    yahoo_player_id: NotRequired[int | None]
    fan_duel_name: NotRequired[str | None]
    draft_kings_name: NotRequired[str | None]
    yahoo_name: NotRequired[str | None]
    depth_chart_position: NotRequired[str | None]
    depth_chart_order: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    fantasy_draft_name: NotRequired[str | None]
    fantasy_draft_player_id: NotRequired[int | None]
    usa_today_player_id: NotRequired[int | None]
    usa_today_headshot_url: NotRequired[str | None]
    usa_today_headshot_no_background_url: NotRequired[str | None]
    usa_today_headshot_updated: NotRequired[str | None]
    usa_today_headshot_no_background_updated: NotRequired[str | None]
