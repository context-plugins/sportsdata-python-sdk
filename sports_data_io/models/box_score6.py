from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .booking import Booking, BookingDict
from .coach1 import Coach1, Coach1Dict
from .coach3 import Coach3, Coach3Dict
from .game25 import Game25, Game25Dict
from .goal import Goal, GoalDict
from .lineup4 import Lineup4, Lineup4Dict
from .penalty_shootout import PenaltyShootout, PenaltyShootoutDict
from .player_game7 import PlayerGame7, PlayerGame7Dict
from .referee3 import Referee3, Referee3Dict
from .referee4 import Referee4, Referee4Dict
from .referee5 import Referee5, Referee5Dict
from .referee6 import Referee6, Referee6Dict
from .referee8 import Referee8, Referee8Dict
from .referee11 import Referee11, Referee11Dict
from .referee21 import Referee21, Referee21Dict
from .team_game7 import TeamGame7, TeamGame7Dict


class BoxScore6(SdkBaseModel):
    game: Optional[Game25] = Field(default=UNSET, alias="Game")
    """The game details associated with this box score"""

    away_team_coach: Optional[Coach3] = Field(default=UNSET, alias="AwayTeamCoach")
    """The coach of the away team"""

    home_team_coach: Optional[Coach1] = Field(default=UNSET, alias="HomeTeamCoach")
    """The coach of the home team"""

    main_referee: Optional[Referee8] = Field(default=UNSET, alias="MainReferee")
    """The main referee"""

    assistant_referee1: Optional[Referee11] = Field(default=UNSET, alias="AssistantReferee1")
    """The first assistant referee"""

    assistant_referee2: Optional[Referee21] = Field(default=UNSET, alias="AssistantReferee2")
    """The second assistant referee"""

    fourth_referee: Optional[Referee3] = Field(default=UNSET, alias="FourthReferee")
    """The information about the fourth referee working the match"""

    additional_assistant_referee1: Optional[Referee4] = Field(default=UNSET, alias="AdditionalAssistantReferee1")
    """The first additional assistant referee"""

    additional_assistant_referee2: Optional[Referee5] = Field(default=UNSET, alias="AdditionalAssistantReferee2")
    """The second additional assistant referee"""

    lineups: Optional[list[Lineup4]] = Field(default=UNSET, alias="Lineups")
    """The details of the lineups for each team"""

    goals: Optional[list[Goal]] = Field(default=UNSET, alias="Goals")
    """The details of the goals scored during this game"""

    bookings: Optional[list[Booking]] = Field(default=UNSET, alias="Bookings")
    """The details of the bookings (yellow/red cards) recorded during this game"""

    penalty_shootouts: Optional[list[PenaltyShootout]] = Field(default=UNSET, alias="PenaltyShootouts")
    """The details of the penalty shootouts recorded during this game"""

    team_games: Optional[list[TeamGame7]] = Field(default=UNSET, alias="TeamGames")
    """The stats by the team in the game"""

    player_games: Optional[list[PlayerGame7]] = Field(default=UNSET, alias="PlayerGames")
    """The player stats for this game"""

    video_assistant_referee: Optional[Referee6] = Field(default=UNSET, alias="VideoAssistantReferee")
    """The name of the referee in charge of the video reviews (VAR)"""


class BoxScore6Dict(TypedDict):
    game: NotRequired[Game25 | Game25Dict]
    away_team_coach: NotRequired[Coach3 | Coach3Dict]
    home_team_coach: NotRequired[Coach1 | Coach1Dict]
    main_referee: NotRequired[Referee8 | Referee8Dict]
    assistant_referee1: NotRequired[Referee11 | Referee11Dict]
    assistant_referee2: NotRequired[Referee21 | Referee21Dict]
    fourth_referee: NotRequired[Referee3 | Referee3Dict]
    additional_assistant_referee1: NotRequired[Referee4 | Referee4Dict]
    additional_assistant_referee2: NotRequired[Referee5 | Referee5Dict]
    lineups: NotRequired[list[Lineup4 | Lineup4Dict]]
    goals: NotRequired[list[Goal | GoalDict]]
    bookings: NotRequired[list[Booking | BookingDict]]
    penalty_shootouts: NotRequired[list[PenaltyShootout | PenaltyShootoutDict]]
    team_games: NotRequired[list[TeamGame7 | TeamGame7Dict]]
    player_games: NotRequired[list[PlayerGame7 | PlayerGame7Dict]]
    video_assistant_referee: NotRequired[Referee6 | Referee6Dict]
