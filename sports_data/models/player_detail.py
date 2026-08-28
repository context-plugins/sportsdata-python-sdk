from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .news1 import News1, News1Dict
from .player_season21 import PlayerSeason21, PlayerSeason21Dict


class PlayerDetail(SdkBaseModel):
    player_season: Optional[PlayerSeason21] = Field(default=UNSET, alias="PlayerSeason")
    """This field is expected to be NULL"""

    latest_news: Optional[list[News1]] = Field(default=UNSET, alias="LatestNews")
    """The latest news associated with this player"""

    player_id: Optional[int] = Field(default=UNSET, alias="PlayerID")
    """The unique PlayerID of the player as assigned by SportsDataIO. Note: this ID will stay with the player throughout
    their entire career."""

    team: OptionalNullable[str] = Field(default=UNSET, alias="Team")
    """The abbreviation [Key] of the team that the player is on. Note: If this player is a free agent; this field is
    NULL."""

    number: OptionalNullable[int] = Field(default=UNSET, alias="Number")
    """Player's jersey number"""

    first_name: OptionalNullable[str] = Field(default=UNSET, alias="FirstName")
    """Player's first name"""

    last_name: OptionalNullable[str] = Field(default=UNSET, alias="LastName")
    """Player's last name"""

    position: OptionalNullable[str] = Field(default=UNSET, alias="Position")
    """The primary position of the player. Possible Values: C; CB; DB; DE; DL; DT; FB; FS; G; ILB; K; KR; LB; LS; NT;
    OL; OLB; OT; P; QB; RB; S; SS; T; TE; WR."""

    status: OptionalNullable[str] = Field(default=UNSET, alias="Status")
    """The player's current status. Possible values include Active, Inactive, Injured Reserve, Physically Unable to
    Perform, Practice Squad, Suspended, Non Football Injury, Non-Football Illness, Commissioner Exempt List, Exempt/Left
    Team, Paternity, Bereavement, Reserve/COVID-19, and Voluntary Opt Out. Inactive indicates that this player is a free
    agent. Active indicates that this player is on his team's active roster."""

    height: OptionalNullable[str] = Field(default=UNSET, alias="Height")
    """Height in feet, inches"""

    weight: OptionalNullable[int] = Field(default=UNSET, alias="Weight")
    """Player's weight in pounds"""

    birth_date: OptionalNullable[str] = Field(default=UNSET, alias="BirthDate")
    """Player's date of birth"""

    college: OptionalNullable[str] = Field(default=UNSET, alias="College")
    """College team the player played for prior to turning professional"""

    experience: OptionalNullable[int] = Field(default=UNSET, alias="Experience")
    """Number of years experience. Note: This number is incremented every year; in the Spring; when we load the rookies
    following the NFL Draft. Rookies will have Experience = 0; while second year players will have Experience = 2."""

    fantasy_position: OptionalNullable[str] = Field(default=UNSET, alias="FantasyPosition")
    """The player's fantasy football position. Possible values: QB; RB; WR; TE; DL; LB; DB; K; P; OL."""

    active: OptionalNullable[bool] = Field(default=UNSET, alias="Active")
    """Whether or not the player is on the active roster of the NFL team (True/False)"""

    position_category: OptionalNullable[str] = Field(default=UNSET, alias="PositionCategory")
    """The category of the player's position (OFF; DEF; ST)"""

    name: OptionalNullable[str] = Field(default=UNSET, alias="Name")
    """Player's full name"""

    age: OptionalNullable[int] = Field(default=UNSET, alias="Age")
    """The player's current age"""

    experience_string: OptionalNullable[str] = Field(default=UNSET, alias="ExperienceString")
    """The player's experience converted to a string"""

    birth_date_string: OptionalNullable[str] = Field(default=UNSET, alias="BirthDateString")
    """The player's date of birth converted to a string"""

    photo_url: OptionalNullable[str] = Field(default=UNSET, alias="PhotoUrl")
    """This field is deprecated. Note: Headshots are now delivered through IMAGN. Please see our Headshots products for
    further information."""

    bye_week: OptionalNullable[int] = Field(default=UNSET, alias="ByeWeek")
    """The week the player is on bye for the upcoming or current season"""

    upcoming_game_opponent: OptionalNullable[str] = Field(default=UNSET, alias="UpcomingGameOpponent")
    """The opposing team the player is playing against in the upcoming week"""

    upcoming_game_week: Optional[int] = Field(default=UNSET, alias="UpcomingGameWeek")
    """The week of the player's upcoming game (this will be the upcoming week unless the player is on Bye that week,
    which would bump it to the next week)"""

    short_name: OptionalNullable[str] = Field(default=UNSET, alias="ShortName")
    """The first initial and last name of the player (J. Doe)"""

    average_draft_position: OptionalNullable[float] = Field(default=UNSET, alias="AverageDraftPosition")
    """The average draft position of the player in re-draft leagues"""

    depth_position_category: OptionalNullable[str] = Field(default=UNSET, alias="DepthPositionCategory")
    """The category (Offense, Defense or Special Teams) of the players DepthPositionCategory (OFF, DEF, ST)"""

    depth_position: OptionalNullable[str] = Field(default=UNSET, alias="DepthPosition")
    """The position this player is listed at on his team's depth chart (e.g. QB; LWR; RDE; LILB, K)"""

    depth_order: OptionalNullable[int] = Field(default=UNSET, alias="DepthOrder")
    """The order this player is at his position (1 = Starter; 2 = Backup; 3 = 3rd String; 4 = 4th String; 5 = 5th
    String)"""

    depth_display_order: OptionalNullable[int] = Field(default=UNSET, alias="DepthDisplayOrder")
    """The display order of the positions (for display purposes)"""

    current_team: OptionalNullable[str] = Field(default=UNSET, alias="CurrentTeam")
    """The team who currently employs this player. This value is null when this player is unemployed (for example a free
    agent or retired player)."""

    college_draft_team: OptionalNullable[str] = Field(default=UNSET, alias="CollegeDraftTeam")
    """The team who drafted this player. Note: If this player was an Undrafted Free Agent; then it's the team who first
    signed him as a rookie."""

    college_draft_year: OptionalNullable[int] = Field(default=UNSET, alias="CollegeDraftYear")
    """The year this player entered the NFL as a rookie"""

    college_draft_round: OptionalNullable[int] = Field(default=UNSET, alias="CollegeDraftRound")
    """The round this player was drafted in"""

    college_draft_pick: OptionalNullable[int] = Field(default=UNSET, alias="CollegeDraftPick")
    """The overall pick in the draft this player was selected"""

    is_undrafted_free_agent: Optional[bool] = Field(default=UNSET, alias="IsUndraftedFreeAgent")
    """Whether this player was an undrafted free agent. This value is True if the player was not drafted."""

    height_feet: OptionalNullable[int] = Field(default=UNSET, alias="HeightFeet")
    """The feet component of a player's height (if player is 6'3", then this value would be 6)"""

    height_inches: OptionalNullable[int] = Field(default=UNSET, alias="HeightInches")
    """The inches component of a player's height (if player is 6'3", then this value would be 3)"""

    upcoming_opponent_rank: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingOpponentRank")
    """The player's upcoming opponent's rank in fantasy points allowed"""

    upcoming_opponent_position_rank: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingOpponentPositionRank")
    """The player's upcoming opponent's rank in fantasy points allowed to his fantasy position"""

    current_status: OptionalNullable[str] = Field(default=UNSET, alias="CurrentStatus")
    """The player's current status. Possible values include Active, Inactive, Injured Reserve, Physically Unable to
    Perform, Practice Squad, Suspended, Non Football Injury, Non-Football Illness, Commissioner Exempt List, Exempt/Left
    Team, Paternity, Bereavement, Reserve/COVID-19, and Voluntary Opt Out. Inactive indicates that this player is a free
    agent. Active indicates that this player is on his team's active roster. Can also include injury status."""

    upcoming_salary: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingSalary")
    """The player's salary for the upcoming week in accordance with a $50,000 salary cap. This is used for daily fantasy
    sports salary cap contests. Salaries represent those published by DraftKings. When DraftKings doesn't publish a
    salary for a given game; the most recent DraftKings salary is used. We recommend using our new DFS endpoints
    instead."""

    fantasy_alarm_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyAlarmPlayerID")
    """The player's cross reference PlayerID to the FantasyAlarm news feed"""

    sport_radar_player_id: OptionalNullable[str] = Field(default=UNSET, alias="SportRadarPlayerID")
    """The player's cross reference PlayerID to the SportRadar API"""

    rotoworld_player_id: OptionalNullable[int] = Field(default=UNSET, alias="RotoworldPlayerID")
    """The player's cross reference PlayerID to the Rotoworld news feed"""

    roto_wire_player_id: OptionalNullable[int] = Field(default=UNSET, alias="RotoWirePlayerID")
    """The player's cross reference PlayerID to the RotoWire news feed"""

    stats_player_id: OptionalNullable[int] = Field(default=UNSET, alias="StatsPlayerID")
    """The player's cross reference PlayerID to the STATS data feeds"""

    sports_direct_player_id: OptionalNullable[int] = Field(default=UNSET, alias="SportsDirectPlayerID")
    """The player's cross reference PlayerID to the SportsDirect data feeds, now part of Nielsen GraceNote"""

    xml_team_player_id: OptionalNullable[int] = Field(default=UNSET, alias="XmlTeamPlayerID")
    """The player's unique PlayerID for cross reference use with XML Team data feeds"""

    fan_duel_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FanDuelPlayerID")
    """The player's cross reference PlayerID to FanDuel"""

    draft_kings_player_id: OptionalNullable[int] = Field(default=UNSET, alias="DraftKingsPlayerID")
    """The player's cross reference PlayerID to DraftKings"""

    yahoo_player_id: OptionalNullable[int] = Field(default=UNSET, alias="YahooPlayerID")
    """The player's unique PlayerID for cross reference use with Yahoo"""

    injury_status: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStatus")
    """The player's current injury status, in the form of likelihood that player plays (Probable, Questionable,
    Doubtful, Out)"""

    injury_body_part: OptionalNullable[str] = Field(default=UNSET, alias="InjuryBodyPart")
    """The body part that is injured for the player (Knee; Groin; Calf; Hamstring; etc.)"""

    injury_start_date: OptionalNullable[str] = Field(default=UNSET, alias="InjuryStartDate")
    """The day that the player's injury started or was first discovered"""

    injury_notes: OptionalNullable[str] = Field(default=UNSET, alias="InjuryNotes")
    """A brief description of the player's injury and expected availability"""

    fan_duel_name: OptionalNullable[str] = Field(default=UNSET, alias="FanDuelName")
    """The player's full name in FanDuel's daily fantasy sports platform"""

    draft_kings_name: OptionalNullable[str] = Field(default=UNSET, alias="DraftKingsName")
    """The player's full name in DraftKings' daily fantasy sports platform"""

    yahoo_name: OptionalNullable[str] = Field(default=UNSET, alias="YahooName")
    """The player's name in Yahoo's daily fantasy sports platform"""

    fantasy_position_depth_order: OptionalNullable[int] = Field(default=UNSET, alias="FantasyPositionDepthOrder")
    """The order this player is at his team's FantasyPosition"""

    injury_practice: OptionalNullable[str] = Field(default=UNSET, alias="InjuryPractice")
    """This field is deprecated"""

    injury_practice_description: OptionalNullable[str] = Field(default=UNSET, alias="InjuryPracticeDescription")
    """This field is deprecated"""

    declared_inactive: Optional[bool] = Field(default=UNSET, alias="DeclaredInactive")
    """Whether the player has been declared inactive. This value is updated in the hours leading up to game start time;
    as teams announce their inactive players. Note: This is only updated for offensive skill position players (QB; RB;
    WR; TE)."""

    upcoming_fan_duel_salary: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingFanDuelSalary")
    """The player's FanDuel salary for the upcoming week. Note: We recommend using our new DFS endpoints instead."""

    upcoming_draft_kings_salary: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingDraftKingsSalary")
    """The player's DraftKings salary for the upcoming week. Note: We recommend using our new DFS endpoints instead."""

    upcoming_yahoo_salary: OptionalNullable[int] = Field(default=UNSET, alias="UpcomingYahooSalary")
    """The player's Yahoo salary for the upcoming week. We recommend using our new DFS endpoints instead."""

    team_id: OptionalNullable[int] = Field(default=UNSET, alias="TeamID")
    """The unique ID of the team that the player is on. Note: If the player is a free agent; this field is NULL"""

    global_team_id: OptionalNullable[int] = Field(default=UNSET, alias="GlobalTeamID")
    """A globally unique ID for this team. This value is guaranteed to be unique across all sports/leagues."""

    fantasy_draft_player_id: OptionalNullable[int] = Field(default=UNSET, alias="FantasyDraftPlayerID")
    """The player's cross reference PlayerID to FantasyDraft"""

    fantasy_draft_name: OptionalNullable[str] = Field(default=UNSET, alias="FantasyDraftName")
    """The player's full name in FantasyDraft's daily fantasy sports platform"""

    usa_today_player_id: OptionalNullable[int] = Field(default=UNSET, alias="UsaTodayPlayerID")
    """The player's cross reference PlayerID to USA Today headshot data feeds"""

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


class PlayerDetailDict(TypedDict):
    player_season: NotRequired[PlayerSeason21 | PlayerSeason21Dict]
    latest_news: NotRequired[list[News1 | News1Dict]]
    player_id: NotRequired[int]
    team: NotRequired[str | None]
    number: NotRequired[int | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    position: NotRequired[str | None]
    status: NotRequired[str | None]
    height: NotRequired[str | None]
    weight: NotRequired[int | None]
    birth_date: NotRequired[str | None]
    college: NotRequired[str | None]
    experience: NotRequired[int | None]
    fantasy_position: NotRequired[str | None]
    active: NotRequired[bool | None]
    position_category: NotRequired[str | None]
    name: NotRequired[str | None]
    age: NotRequired[int | None]
    experience_string: NotRequired[str | None]
    birth_date_string: NotRequired[str | None]
    photo_url: NotRequired[str | None]
    bye_week: NotRequired[int | None]
    upcoming_game_opponent: NotRequired[str | None]
    upcoming_game_week: NotRequired[int]
    short_name: NotRequired[str | None]
    average_draft_position: NotRequired[float | None]
    depth_position_category: NotRequired[str | None]
    depth_position: NotRequired[str | None]
    depth_order: NotRequired[int | None]
    depth_display_order: NotRequired[int | None]
    current_team: NotRequired[str | None]
    college_draft_team: NotRequired[str | None]
    college_draft_year: NotRequired[int | None]
    college_draft_round: NotRequired[int | None]
    college_draft_pick: NotRequired[int | None]
    is_undrafted_free_agent: NotRequired[bool]
    height_feet: NotRequired[int | None]
    height_inches: NotRequired[int | None]
    upcoming_opponent_rank: NotRequired[int | None]
    upcoming_opponent_position_rank: NotRequired[int | None]
    current_status: NotRequired[str | None]
    upcoming_salary: NotRequired[int | None]
    fantasy_alarm_player_id: NotRequired[int | None]
    sport_radar_player_id: NotRequired[str | None]
    rotoworld_player_id: NotRequired[int | None]
    roto_wire_player_id: NotRequired[int | None]
    stats_player_id: NotRequired[int | None]
    sports_direct_player_id: NotRequired[int | None]
    xml_team_player_id: NotRequired[int | None]
    fan_duel_player_id: NotRequired[int | None]
    draft_kings_player_id: NotRequired[int | None]
    yahoo_player_id: NotRequired[int | None]
    injury_status: NotRequired[str | None]
    injury_body_part: NotRequired[str | None]
    injury_start_date: NotRequired[str | None]
    injury_notes: NotRequired[str | None]
    fan_duel_name: NotRequired[str | None]
    draft_kings_name: NotRequired[str | None]
    yahoo_name: NotRequired[str | None]
    fantasy_position_depth_order: NotRequired[int | None]
    injury_practice: NotRequired[str | None]
    injury_practice_description: NotRequired[str | None]
    declared_inactive: NotRequired[bool]
    upcoming_fan_duel_salary: NotRequired[int | None]
    upcoming_draft_kings_salary: NotRequired[int | None]
    upcoming_yahoo_salary: NotRequired[int | None]
    team_id: NotRequired[int | None]
    global_team_id: NotRequired[int | None]
    fantasy_draft_player_id: NotRequired[int | None]
    fantasy_draft_name: NotRequired[str | None]
    usa_today_player_id: NotRequired[int | None]
    usa_today_headshot_url: NotRequired[str | None]
    usa_today_headshot_no_background_url: NotRequired[str | None]
    usa_today_headshot_updated: NotRequired[str | None]
    usa_today_headshot_no_background_updated: NotRequired[str | None]
