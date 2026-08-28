from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class Player3(SdkBaseModel):
    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The player's unique PlayerID as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their MLB career"""

    sports_data_id: OptionalNullable[str] = Field(default=UNSET, alias="SportsDataID")
    """Deprecated. Use SportRadarPlayerID instead."""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """Indicates the player's status of being on an Major League Active Roster. Possible values include: Active, 40 Man
    Active, Non-Roster Invitee, Minors, Inactive, 7 Day Injury List, 10 Day Injury List, 15 Day Injury List, 60 Day
    Injury List, Restricted List, Paternity List, Bereavement List, Military List"""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The team's unique TeamID as assigned by SportsDataIO"""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that the player belongs to"""

    jersey: OptionalNullable[int] = Field(default=UNSET, alias="Jersey")
    """The player's jersey number."""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The player's position category. Possible values: DH, IF, OF, P, PH, PR"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The player's position associated with the given game or season. Possible values: 1B; 2B; 3B; C; CF; DH; IF; LF;
    OF; P; PH; PR; RF; RP; SP; SS"""

    mlbamid: OptionalNullable[int] = Field(default=UNSET, alias="MLBAMID")
    """The player's unique PlayerID for cross reference use with MLB AM"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """The player's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """The player's last name"""

    bat_hand: OptionalNullable[str] = Field(default=UNSET, alias="BatHand")
    """The player's batting hand. Possible values: R, L, S"""

    throw_hand: OptionalNullable[str] = Field(default=UNSET, alias="ThrowHand")
    """The player's throwing hand. Possible values: R, L, S"""

    height: OptionalNullable[int] = Field(default=UNSET, alias="Height")
    """The player's height in inches"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """The weight of the player in pounds (lbs)."""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """The player's date of birth"""

    birth_city: OptionalNullable[str] = Field(default=UNSET, alias="BirthCity")
    """The city in which the player was born"""

    birth_state: OptionalNullable[str] = Field(default=UNSET, alias="BirthState")
    """The state in which the player was born. Note: State will be NULL for all countries outside of North America and
    Australia"""

    birth_country: OptionalNullable[str] = Field(default=UNSET, alias="BirthCountry")
    """The country in which the player was born"""

    high_school: OptionalNullable[str] = Field(default=UNSET, alias="HighSchool")
    """The high school that the player attended. Note: If the player attended a college, this field will be NULL"""

    college: OptionalNullable[str] = Field(default=UNSET, alias="College")
    """The college that the player attended. Note: If player did not attend college this field will contain "None" and a
    high school will be added if applicable"""

    pro_debut: OptionalNullable[str] = Field(default=UNSET, alias="ProDebut")
    """The date that this player made his MLB debut."""

    salary: OptionalNullable[int] = Field(default=UNSET, alias="Salary")
    """Field is expected to be NULL"""

    photo_url: OptionalNullable[str] = Field(default=UNSET, alias="PhotoUrl")
    """Field is expected to be NULL"""

    sport_radar_player_id: OptionalNullable[str] = Field(default=UNSET, alias="SportRadarPlayerID")
    """The player's unique PlayerID for cross reference use with Stats Player"""

    rotoworld_player_id: OptionalNullable[int] = Field(default=UNSET, alias="RotoworldPlayerID")
    """The player's unique PlayerID for cross reference use with Rotoworld."""

    roto_wire_player_id: OptionalNullable[int] = Field(default=UNSET, alias="RotoWirePlayerID")
    """The player's unique PlayerID for cross reference use with RotoWire."""

    fantasy_alarm_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyAlarmPlayerID")
    """The player's unique PlayerID for cross reference use with FantasyAlarm"""

    stats_player_id: OptionalNullable[int] = Field(default=UNSET, alias="StatsPlayerID")
    """The player's unique PlayerID for cross reference use with Stats Player."""

    sports_direct_player_id: OptionalNullable[int] = Field(default=UNSET, alias="SportsDirectPlayerID")
    """The player's cross reference PlayerID to the SportsDirect data feeds, now part of Nielsen GraceNote."""

    xml_team_player_id: OptionalNullable[int] = Field(default=UNSET, alias="XmlTeamPlayerID")
    """The player's unique PlayerID for cross reference use with Xml Team"""

    injury_status: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStatus")
    """The player's current injury status; in the form of likelihood that player plays. Possible values: Probable;
    Questionable; Doubtful; Out"""

    injury_body_part: OptionalNullable[str] = Field(default=UNSET, alias="InjuryBodyPart")
    """Indicates the player's injured body part. (e.g. ankle; knee; elbow; etc.)"""

    injury_start_date: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStartDate")
    """The day that the injury started or first discovered."""

    injury_notes: OptionalNullable[str] = Field(default=UNSET, alias="InjuryNotes")
    """Brief description of the player's injury and expected availability"""

    fan_duel_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FanDuelPlayerID")
    """The player's unique PlayerID for cross reference use with FanDuel"""

    draft_kings_player_id: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsPlayerID")
    """The player's unique PlayerID for cross reference use with DraftKings."""

    yahoo_player_id: OptionalNullable[int] = Field(default=UNSET, alias="YahooPlayerID")
    """The player's unique PlayerID for cross reference use with Yahoo"""

    upcoming_game_id: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingGameID")
    """The unique ID of a player's next upcoming game"""

    fan_duel_name: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelName")
    """The player's name on FanDuel"""

    draft_kings_name: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsName")
    """The player's name on DraftKings"""

    yahoo_name: OptionalNullable[str] = Field(default=UNSET, alias="YahooName")
    """The player's name as displayed on/by Yahoo"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues"""

    fantasy_draft_name: OptionalNullable[str] = Field(default=UNSET, alias="FantasyDraftName")
    """The player's name on Fantasy Draft"""

    fantasy_draft_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDraftPlayerID")
    """The player's unique PlayerID for cross reference use with Fantasy Draft"""

    experience: OptionalNullable[str] = Field(default=UNSET, alias="Experience")
    """The player's years of experience"""

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
    sports_data_id: NotRequired[str | None]
    status: NotRequired[str | None]
    team_id: NotRequired[int | None]
    team: NotRequired[str | None]
    jersey: NotRequired[int | None]
    position_category: NotRequired[str | None]
    position: NotRequired[str | None]
    mlbamid: NotRequired[int | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    bat_hand: NotRequired[str | None]
    throw_hand: NotRequired[str | None]
    height: NotRequired[int | None]
    weight: NotRequired[int | None]
    birth_date: NotRequired[str | None]
    birth_city: NotRequired[str | None]
    birth_state: NotRequired[str | None]
    birth_country: NotRequired[str | None]
    high_school: NotRequired[str | None]
    college: NotRequired[str | None]
    pro_debut: NotRequired[str | None]
    salary: NotRequired[int | None]
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
    upcoming_game_id: NotRequired[int | None]
    fan_duel_name: NotRequired[str | None]
    draft_kings_name: NotRequired[str | None]
    yahoo_name: NotRequired[str | None]
    global_team_id: NotRequired[int | None]
    fantasy_draft_name: NotRequired[str | None]
    fantasy_draft_player_id: NotRequired[int | None]
    experience: NotRequired[str | None]
    usa_today_player_id: NotRequired[int | None]
    usa_today_headshot_url: NotRequired[str | None]
    usa_today_headshot_no_background_url: NotRequired[str | None]
    usa_today_headshot_updated: NotRequired[str | None]
    usa_today_headshot_no_background_updated: NotRequired[str | None]
