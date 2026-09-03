from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_decoder,
    param,
)
from ..errors.wnba_v3_scores_are_games_in_progress_error import (
    WnbaV3ScoresAreGamesInProgressErrorBody,
    wnba_v3_scores_are_games_in_progress_error_mapper,
)
from ..errors.wnba_v3_scores_betting_events_by_date_error import (
    WnbaV3ScoresBettingEventsByDateErrorBody,
    wnba_v3_scores_betting_events_by_date_error_mapper,
)
from ..errors.wnba_v3_scores_betting_events_by_season_error import (
    WnbaV3ScoresBettingEventsBySeasonErrorBody,
    wnba_v3_scores_betting_events_by_season_error_mapper,
)
from ..errors.wnba_v3_scores_betting_futures_by_season_error import (
    WnbaV3ScoresBettingFuturesBySeasonErrorBody,
    wnba_v3_scores_betting_futures_by_season_error_mapper,
)
from ..errors.wnba_v3_scores_betting_futures_by_season_sportsbook_group_error import (
    WnbaV3ScoresBettingFuturesBySeasonSportsbookGroupErrorBody,
    wnba_v3_scores_betting_futures_by_season_sportsbook_group_error_mapper,
)
from ..errors.wnba_v3_scores_betting_market_error import (
    WnbaV3ScoresBettingMarketErrorBody,
    wnba_v3_scores_betting_market_error_mapper,
)
from ..errors.wnba_v3_scores_betting_market_sportsbook_group_error import (
    WnbaV3ScoresBettingMarketSportsbookGroupErrorBody,
    wnba_v3_scores_betting_market_sportsbook_group_error_mapper,
)
from ..errors.wnba_v3_scores_betting_markets_by_event_error import (
    WnbaV3ScoresBettingMarketsByEventErrorBody,
    wnba_v3_scores_betting_markets_by_event_error_mapper,
)
from ..errors.wnba_v3_scores_betting_markets_by_event_sportsbook_group_error import (
    WnbaV3ScoresBettingMarketsByEventSportsbookGroupErrorBody,
    wnba_v3_scores_betting_markets_by_event_sportsbook_group_error_mapper,
)
from ..errors.wnba_v3_scores_betting_markets_by_game_error import (
    WnbaV3ScoresBettingMarketsByGameErrorBody,
    wnba_v3_scores_betting_markets_by_game_error_mapper,
)
from ..errors.wnba_v3_scores_betting_markets_by_game_sportsbook_group_error import (
    WnbaV3ScoresBettingMarketsByGameSportsbookGroupErrorBody,
    wnba_v3_scores_betting_markets_by_game_sportsbook_group_error_mapper,
)
from ..errors.wnba_v3_scores_betting_markets_by_market_type_error import (
    WnbaV3ScoresBettingMarketsByMarketTypeErrorBody,
    wnba_v3_scores_betting_markets_by_market_type_error_mapper,
)
from ..errors.wnba_v3_scores_betting_markets_by_market_type_sportsbook_group_error import (
    WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupErrorBody,
    wnba_v3_scores_betting_markets_by_market_type_sportsbook_group_error_mapper,
)
from ..errors.wnba_v3_scores_betting_metadata_error import (
    WnbaV3ScoresBettingMetadataErrorBody,
    wnba_v3_scores_betting_metadata_error_mapper,
)
from ..errors.wnba_v3_scores_betting_player_props_by_game_error import (
    WnbaV3ScoresBettingPlayerPropsByGameErrorBody,
    wnba_v3_scores_betting_player_props_by_game_error_mapper,
)
from ..errors.wnba_v3_scores_betting_player_props_by_game_sportsbook_group_error import (
    WnbaV3ScoresBettingPlayerPropsByGameSportsbookGroupErrorBody,
    wnba_v3_scores_betting_player_props_by_game_sportsbook_group_error_mapper,
)
from ..errors.wnba_v3_scores_box_score_final_error import (
    WnbaV3ScoresBoxScoreFinalErrorBody,
    wnba_v3_scores_box_score_final_error_mapper,
)
from ..errors.wnba_v3_scores_box_score_live_final_error import (
    WnbaV3ScoresBoxScoreLiveFinalErrorBody,
    wnba_v3_scores_box_score_live_final_error_mapper,
)
from ..errors.wnba_v3_scores_box_scores_by_date_final_error import (
    WnbaV3ScoresBoxScoresByDateFinalErrorBody,
    wnba_v3_scores_box_scores_by_date_final_error_mapper,
)
from ..errors.wnba_v3_scores_box_scores_by_date_live_final_error import (
    WnbaV3ScoresBoxScoresByDateLiveFinalErrorBody,
    wnba_v3_scores_box_scores_by_date_live_final_error_mapper,
)
from ..errors.wnba_v3_scores_games_basic_by_date_final_error import (
    WnbaV3ScoresGamesBasicByDateFinalErrorBody,
    wnba_v3_scores_games_basic_by_date_final_error_mapper,
)
from ..errors.wnba_v3_scores_games_basic_by_date_live_final_error import (
    WnbaV3ScoresGamesBasicByDateLiveFinalErrorBody,
    wnba_v3_scores_games_basic_by_date_live_final_error_mapper,
)
from ..errors.wnba_v3_scores_games_by_date_final_error import (
    WnbaV3ScoresGamesByDateFinalErrorBody,
    wnba_v3_scores_games_by_date_final_error_mapper,
)
from ..errors.wnba_v3_scores_games_by_date_live_final_error import (
    WnbaV3ScoresGamesByDateLiveFinalErrorBody,
    wnba_v3_scores_games_by_date_live_final_error_mapper,
)
from ..errors.wnba_v3_scores_player_details_by_active_error import (
    WnbaV3ScoresPlayerDetailsByActiveErrorBody,
    wnba_v3_scores_player_details_by_active_error_mapper,
)
from ..errors.wnba_v3_scores_player_details_by_team_error import (
    WnbaV3ScoresPlayerDetailsByTeamErrorBody,
    wnba_v3_scores_player_details_by_team_error_mapper,
)
from ..errors.wnba_v3_scores_player_season_stats_by_team_error import (
    WnbaV3ScoresPlayerSeasonStatsByTeamErrorBody,
    wnba_v3_scores_player_season_stats_by_team_error_mapper,
)
from ..errors.wnba_v3_scores_player_season_stats_error import (
    WnbaV3ScoresPlayerSeasonStatsErrorBody,
    wnba_v3_scores_player_season_stats_error_mapper,
)
from ..errors.wnba_v3_scores_pre_game_odds_by_date_error import (
    WnbaV3ScoresPreGameOddsByDateErrorBody,
    wnba_v3_scores_pre_game_odds_by_date_error_mapper,
)
from ..errors.wnba_v3_scores_pre_game_odds_line_movement_error import (
    WnbaV3ScoresPreGameOddsLineMovementErrorBody,
    wnba_v3_scores_pre_game_odds_line_movement_error_mapper,
)
from ..errors.wnba_v3_scores_schedules_basic_error import (
    WnbaV3ScoresSchedulesBasicErrorBody,
    wnba_v3_scores_schedules_basic_error_mapper,
)
from ..errors.wnba_v3_scores_schedules_error import (
    WnbaV3ScoresSchedulesErrorBody,
    wnba_v3_scores_schedules_error_mapper,
)
from ..errors.wnba_v3_scores_season_current_error import (
    WnbaV3ScoresSeasonCurrentErrorBody,
    wnba_v3_scores_season_current_error_mapper,
)
from ..errors.wnba_v3_scores_sportsbooks_by_active_error import (
    WnbaV3ScoresSportsbooksByActiveErrorBody,
    wnba_v3_scores_sportsbooks_by_active_error_mapper,
)
from ..errors.wnba_v3_scores_stadiums_error import WnbaV3ScoresStadiumsErrorBody, wnba_v3_scores_stadiums_error_mapper
from ..errors.wnba_v3_scores_standings_error import (
    WnbaV3ScoresStandingsErrorBody,
    wnba_v3_scores_standings_error_mapper,
)
from ..errors.wnba_v3_scores_team_game_stats_by_date_final_error import (
    WnbaV3ScoresTeamGameStatsByDateFinalErrorBody,
    wnba_v3_scores_team_game_stats_by_date_final_error_mapper,
)
from ..errors.wnba_v3_scores_team_game_stats_by_date_live_final_error import (
    WnbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody,
    wnba_v3_scores_team_game_stats_by_date_live_final_error_mapper,
)
from ..errors.wnba_v3_scores_team_profiles_all_error import (
    WnbaV3ScoresTeamProfilesAllErrorBody,
    wnba_v3_scores_team_profiles_all_error_mapper,
)
from ..errors.wnba_v3_scores_team_season_stats_error import (
    WnbaV3ScoresTeamSeasonStatsErrorBody,
    wnba_v3_scores_team_season_stats_error_mapper,
)
from ..models.betting_entity_metadata_collection import BettingEntityMetadataCollection
from ..models.betting_event1 import BettingEvent1
from ..models.betting_market import BettingMarket
from ..models.box_score5 import BoxScore5
from ..models.enums.format import FormatOrStr
from ..models.game10 import Game10
from ..models.game_info6 import GameInfo6
from ..models.player6 import Player6
from ..models.player_season7 import PlayerSeason7
from ..models.schedules_basic import SchedulesBasic
from ..models.score_basic6 import ScoreBasic6
from ..models.season4 import Season4
from ..models.sportsbook import Sportsbook
from ..models.stadium6 import Stadium6
from ..models.team6 import Team6
from ..models.team_game6 import TeamGame6
from ..models.team_season6 import TeamSeason6
from ..server.server import Server


class WnbaV3Scores:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WnbaV3ScoresWithRawResponse(client, server, auth)

    def wnba_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> bool:
        """Are Games In Progress

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_are_games_in_progress(
            format, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_events_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """The list of current BettingEvents for the given date. Events in this include market information but no
        outcomes will be included here. Intended to allow both visibility to Events in order to match up Events -> Games
        via the included GameID (where applicable) as well as provide a list of MarketIDs which are included in the
        given event.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2025-05-30</code>, <code>2025-MAY-28</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_events_by_date(
            format, date, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_events_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """Returns the full list of BetttingEvents for the given season. Intended for those who need to tie
        BettingEventIDs to GameIDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_events_by_season(
            format, season, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_futures_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """Returns available Futures outcomes for the given season. Does not include line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_futures_by_season(
            format, season, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_futures_by_season_sportsbook_group(
        self,
        format: FormatOrStr,
        season: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingEvent1]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_futures_by_season_sportsbook_group(
            format, season, sportsbookgroup, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid entries include:
                <code>36</code>, <code>342</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_market(
            format, market_id, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
        market_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid entries include:
                <code>36</code>, <code>342</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>, <code>G1001</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_market_sportsbook_group(
            format, market_id, sportsbookgroup, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_markets_by_event(
        self, format: FormatOrStr, event_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_markets_by_event(
            format, event_id, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets and available outcomes for a given BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_markets_by_event_sportsbook_group(
            format, event_id, sportsbookgroup, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_markets_by_game(
        self, format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
                Valid entries include: <code>1934</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_markets_by_game(
            format, game_id, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_markets_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
                Valid entries include: <code>1934</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_markets_by_game_sportsbook_group(
            format, game_id, sportsbookgroup, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for ``Game Lines`` <code>2</code> for ``Player Props`` <code>3</code> for ``Team Props``
                <code>6</code> for ``Game Props``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_markets_by_market_type(
            format, event_id, market_type_id, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for ``Game Lines`` <code>2</code> for ``Player Props`` <code>3</code> for ``Team Props``
                <code>6</code> for ``Game Props``
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_markets_by_market_type_sportsbook_group(
            format, event_id, market_type_id, sportsbookgroup, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> BettingEntityMetadataCollection:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_metadata(format, request_options=request_options).unwrap()

    def wnba_v3_scores_betting_player_props_by_game(
        self, format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingMarket]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The unique GameID of the game in question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_player_props_by_game(
            format, game_id, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_betting_player_props_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_betting_player_props_by_game_sportsbook_group(
            format, game_id, sportsbookgroup, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_box_score_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore5:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an WNBA game. GameIDs can be found in the Games API. Valid entries are
                <code>1686</code>, <code>1899</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_box_score_final(
            format, gameid, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_box_score_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore5:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an WNBA game. GameIDs can be found in the Games API. Valid entries are
                <code>1686</code>, <code>1899</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_box_score_live_final(
            format, gameid, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_box_scores_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore5]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2024-MAY-16</code>, <code>2023-OCT-20</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_box_scores_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_box_scores_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore5]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2024-MAY-16</code>, <code>2024-OCT-20</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_box_scores_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game10]:
        """Full scores and gameday info, as well as all of the quarter scores and full-time score, delivered as the game
        ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_games_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game10]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_games_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic6]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_games_basic_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic6]:
        """A slimmed-down score endpoint, giving just the quarter scores and full gane score, for simple applications,
        updated live.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_games_basic_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player6]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_player_details_by_active(
            format, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player6]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>LA</code>, <code>IND</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_player_details_by_team(
            format, team, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason7]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_player_season_stats(
            format, season, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_player_season_stats_by_team(
        self, format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason7]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season on a given team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            team: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_player_season_stats_by_team(
            format, season, team, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_pre_game_odds_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo6]:
        """Returns full game odds (spread, moneyline, total) for games on a given date. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_pre_game_odds_by_date(
            format, date, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_pre_game_odds_line_movement(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo6]:
        """Returns the full-game odds (spread, moneyline, total) for games on a given date. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The unique GameID of the game for which to pull data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_pre_game_odds_line_movement(
            format, gameid, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game10]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2019</code>,
                <code>2019PRE</code>, <code>2019POST</code>, <code>2019REG</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_schedules(
            format, season, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SchedulesBasic]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2019</code>,
                <code>2019PRE</code>, <code>2019POST</code>, <code>2019REG</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_schedules_basic(
            format, season, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> Season4:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_season_current(format, request_options=request_options).unwrap()

    def wnba_v3_scores_sportsbooks_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Sportsbook]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_sportsbooks_by_active(
            format, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium6]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_stadiums(format, request_options=request_options).unwrap()

    def wnba_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_standings(
            format, season, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_team_game_stats_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame6]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games on a given date,
        delivered as each game concludes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_team_game_stats_by_date_final(
            format, date, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame6]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_team_game_stats_by_date_live_final(
            format, date, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team6]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_team_profiles_all(
            format, request_options=request_options
        ).unwrap()

    def wnba_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason6]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.wnba_v3_scores_team_season_stats(
            format, season, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> WnbaV3ScoresWithRawResponse:
        return self._with_raw_response


class AsyncWnbaV3Scores:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWnbaV3ScoresWithRawResponse(client, server, auth)

    async def wnba_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> bool:
        """Are Games In Progress

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_are_games_in_progress(format, request_options=request_options)
        ).unwrap()

    async def wnba_v3_scores_betting_events_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """The list of current BettingEvents for the given date. Events in this include market information but no
        outcomes will be included here. Intended to allow both visibility to Events in order to match up Events -> Games
        via the included GameID (where applicable) as well as provide a list of MarketIDs which are included in the
        given event.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2025-05-30</code>, <code>2025-MAY-28</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_events_by_date(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_events_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """Returns the full list of BetttingEvents for the given season. Intended for those who need to tie
        BettingEventIDs to GameIDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_events_by_season(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_futures_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """Returns available Futures outcomes for the given season. Does not include line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_futures_by_season(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_futures_by_season_sportsbook_group(
        self,
        format: FormatOrStr,
        season: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingEvent1]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_futures_by_season_sportsbook_group(
                format, season, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid entries include:
                <code>36</code>, <code>342</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_market(
                format, market_id, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
        market_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid entries include:
                <code>36</code>, <code>342</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>, <code>G1001</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_market_sportsbook_group(
                format, market_id, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_markets_by_event(
        self, format: FormatOrStr, event_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_markets_by_event(
                format, event_id, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets and available outcomes for a given BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_markets_by_event_sportsbook_group(
                format, event_id, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_markets_by_game(
        self, format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
                Valid entries include: <code>1934</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_markets_by_game(
                format, game_id, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_markets_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
                Valid entries include: <code>1934</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_markets_by_game_sportsbook_group(
                format, game_id, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for ``Game Lines`` <code>2</code> for ``Player Props`` <code>3</code> for ``Team Props``
                <code>6</code> for ``Game Props``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_markets_by_market_type(
                format, event_id, market_type_id, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for ``Game Lines`` <code>2</code> for ``Player Props`` <code>3</code> for ``Team Props``
                <code>6</code> for ``Game Props``
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_markets_by_market_type_sportsbook_group(
                format, event_id, market_type_id, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> BettingEntityMetadataCollection:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_metadata(format, request_options=request_options)
        ).unwrap()

    async def wnba_v3_scores_betting_player_props_by_game(
        self, format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingMarket]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The unique GameID of the game in question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_player_props_by_game(
                format, game_id, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_betting_player_props_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_betting_player_props_by_game_sportsbook_group(
                format, game_id, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_box_score_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore5:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an WNBA game. GameIDs can be found in the Games API. Valid entries are
                <code>1686</code>, <code>1899</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_box_score_final(
                format, gameid, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_box_score_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BoxScore5:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an WNBA game. GameIDs can be found in the Games API. Valid entries are
                <code>1686</code>, <code>1899</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_box_score_live_final(
                format, gameid, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_box_scores_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore5]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2024-MAY-16</code>, <code>2023-OCT-20</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_box_scores_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_box_scores_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BoxScore5]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2024-MAY-16</code>, <code>2024-OCT-20</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_box_scores_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game10]:
        """Full scores and gameday info, as well as all of the quarter scores and full-time score, delivered as the game
        ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_games_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game10]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_games_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic6]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_games_basic_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ScoreBasic6]:
        """A slimmed-down score endpoint, giving just the quarter scores and full gane score, for simple applications,
        updated live.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_games_basic_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player6]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_player_details_by_active(
                format, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Player6]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>LA</code>, <code>IND</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_player_details_by_team(
                format, team, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason7]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_player_season_stats(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_player_season_stats_by_team(
        self, format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[PlayerSeason7]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season on a given team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            team: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_player_season_stats_by_team(
                format, season, team, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_pre_game_odds_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo6]:
        """Returns full game odds (spread, moneyline, total) for games on a given date. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_pre_game_odds_by_date(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_pre_game_odds_line_movement(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo6]:
        """Returns the full-game odds (spread, moneyline, total) for games on a given date. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The unique GameID of the game for which to pull data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_pre_game_odds_line_movement(
                format, gameid, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Game10]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2019</code>,
                <code>2019PRE</code>, <code>2019POST</code>, <code>2019REG</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_schedules(format, season, request_options=request_options)
        ).unwrap()

    async def wnba_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[SchedulesBasic]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2019</code>,
                <code>2019PRE</code>, <code>2019POST</code>, <code>2019REG</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_schedules_basic(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> Season4:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_season_current(format, request_options=request_options)
        ).unwrap()

    async def wnba_v3_scores_sportsbooks_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Sportsbook]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_sportsbooks_by_active(format, request_options=request_options)
        ).unwrap()

    async def wnba_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Stadium6]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (await self._with_raw_response.wnba_v3_scores_stadiums(format, request_options=request_options)).unwrap()

    async def wnba_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_standings(format, season, request_options=request_options)
        ).unwrap()

    async def wnba_v3_scores_team_game_stats_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame6]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games on a given date,
        delivered as each game concludes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_team_game_stats_by_date_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamGame6]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_team_game_stats_by_date_live_final(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def wnba_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[Team6]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_team_profiles_all(format, request_options=request_options)
        ).unwrap()

    async def wnba_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[TeamSeason6]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.wnba_v3_scores_team_season_stats(
                format, season, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncWnbaV3ScoresWithRawResponse:
        return self._with_raw_response


class WnbaV3ScoresWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def wnba_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, WnbaV3ScoresAreGamesInProgressErrorBody]:
        """Are Games In Progress

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=wnba_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_events_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], WnbaV3ScoresBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date. Events in this include market information but no
        outcomes will be included here. Intended to allow both visibility to Events in order to match up Events -> Games
        via the included GameID (where applicable) as well as provide a list of MarketIDs which are included in the
        given event.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2025-05-30</code>, <code>2025-MAY-28</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=wnba_v3_scores_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_events_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], WnbaV3ScoresBettingEventsBySeasonErrorBody]:
        """Returns the full list of BetttingEvents for the given season. Intended for those who need to tie
        BettingEventIDs to GameIDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=wnba_v3_scores_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_futures_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], WnbaV3ScoresBettingFuturesBySeasonErrorBody]:
        """Returns available Futures outcomes for the given season. Does not include line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingFuturesBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=wnba_v3_scores_betting_futures_by_season_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_futures_by_season_sportsbook_group(
        self,
        format: FormatOrStr,
        season: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingEvent1], WnbaV3ScoresBettingFuturesBySeasonSportsbookGroupErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=wnba_v3_scores_betting_futures_by_season_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket, WnbaV3ScoresBettingMarketErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid entries include:
                <code>36</code>, <code>342</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket],
            error_mapper=wnba_v3_scores_betting_market_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
        market_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket, WnbaV3ScoresBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid entries include:
                <code>36</code>, <code>342</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>, <code>G1001</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingMarket/{marketId}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket],
            error_mapper=wnba_v3_scores_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_markets_by_event(
        self, format: FormatOrStr, event_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByEventErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventId", event_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByEventSportsbookGroupErrorBody]:
        """Returns the markets and available outcomes for a given BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_markets_by_game(
        self, format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByGameErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
                Valid entries include: <code>1934</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingMarketsByGameID/{gameID}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameID", game_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_game_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_markets_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByGameSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
                Valid entries include: <code>1934</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingMarketsByGameID/{gameID}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("gameID", game_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for ``Game Lines`` <code>2</code> for ``Player Props`` <code>3</code> for ``Team Props``
                <code>6</code> for ``Game Props``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for ``Game Lines`` <code>2</code> for ``Player Props`` <code>3</code> for ``Team Props``
                <code>6</code> for ``Game Props``
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection, WnbaV3ScoresBettingMetadataErrorBody]:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection],
            error_mapper=wnba_v3_scores_betting_metadata_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_player_props_by_game(
        self, format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingPlayerPropsByGameErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The unique GameID of the game in question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingPlayerPropsByGameID/{gameId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameId", game_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_player_props_by_game_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_betting_player_props_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingPlayerPropsByGameSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("gameId", game_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_player_props_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_box_score_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore5, WnbaV3ScoresBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an WNBA game. GameIDs can be found in the Games API. Valid entries are
                <code>1686</code>, <code>1899</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore5],
            error_mapper=wnba_v3_scores_box_score_final_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_box_score_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore5, WnbaV3ScoresBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an WNBA game. GameIDs can be found in the Games API. Valid entries are
                <code>1686</code>, <code>1899</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore5],
            error_mapper=wnba_v3_scores_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_box_scores_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore5], WnbaV3ScoresBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2024-MAY-16</code>, <code>2023-OCT-20</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore5]],
            error_mapper=wnba_v3_scores_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_box_scores_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore5], WnbaV3ScoresBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2024-MAY-16</code>, <code>2024-OCT-20</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BoxScores/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore5]],
            error_mapper=wnba_v3_scores_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game10], WnbaV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, as well as all of the quarter scores and full-time score, delivered as the game
        ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game10]],
            error_mapper=wnba_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game10], WnbaV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game10]],
            error_mapper=wnba_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic6], WnbaV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic6]],
            error_mapper=wnba_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic6], WnbaV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and full gane score, for simple applications,
        updated live.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic6]],
            error_mapper=wnba_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player6], WnbaV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player6]],
            error_mapper=wnba_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player6], WnbaV3ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>LA</code>, <code>IND</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player6]],
            error_mapper=wnba_v3_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason7], WnbaV3ScoresPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason7]],
            error_mapper=wnba_v3_scores_player_season_stats_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_player_season_stats_by_team(
        self, format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason7], WnbaV3ScoresPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season on a given team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            team: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason7]],
            error_mapper=wnba_v3_scores_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_pre_game_odds_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo6], WnbaV3ScoresPreGameOddsByDateErrorBody]:
        """Returns full game odds (spread, moneyline, total) for games on a given date. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/GameOddsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo6]],
            error_mapper=wnba_v3_scores_pre_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_pre_game_odds_line_movement(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo6], WnbaV3ScoresPreGameOddsLineMovementErrorBody]:
        """Returns the full-game odds (spread, moneyline, total) for games on a given date. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The unique GameID of the game for which to pull data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/GameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo6]],
            error_mapper=wnba_v3_scores_pre_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game10], WnbaV3ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2019</code>,
                <code>2019PRE</code>, <code>2019POST</code>, <code>2019REG</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Games/{Season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("Season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game10]],
            error_mapper=wnba_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SchedulesBasic], WnbaV3ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2019</code>,
                <code>2019PRE</code>, <code>2019POST</code>, <code>2019REG</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/SchedulesBasic/{Season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("Season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[SchedulesBasic]],
            error_mapper=wnba_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season4, WnbaV3ScoresSeasonCurrentErrorBody]:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season4],
            error_mapper=wnba_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_sportsbooks_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], WnbaV3ScoresSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=wnba_v3_scores_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium6], WnbaV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium6]],
            error_mapper=wnba_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, WnbaV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=empty_response,
            error_mapper=wnba_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_team_game_stats_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame6], WnbaV3ScoresTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games on a given date,
        delivered as each game concludes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/TeamGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame6]],
            error_mapper=wnba_v3_scores_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame6], WnbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/TeamGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame6]],
            error_mapper=wnba_v3_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team6], WnbaV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Teams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team6]],
            error_mapper=wnba_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    def wnba_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason6], WnbaV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason6]],
            error_mapper=wnba_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )


class AsyncWnbaV3ScoresWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def wnba_v3_scores_are_games_in_progress(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[bool, WnbaV3ScoresAreGamesInProgressErrorBody]:
        """Are Games In Progress

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/AreAnyGamesInProgress"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[bool],
            error_mapper=wnba_v3_scores_are_games_in_progress_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_events_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], WnbaV3ScoresBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date. Events in this include market information but no
        outcomes will be included here. Intended to allow both visibility to Events in order to match up Events -> Games
        via the included GameID (where applicable) as well as provide a list of MarketIDs which are included in the
        given event.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s). <br>Examples: <code>2025-05-30</code>, <code>2025-MAY-28</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=wnba_v3_scores_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_events_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], WnbaV3ScoresBettingEventsBySeasonErrorBody]:
        """Returns the full list of BetttingEvents for the given season. Intended for those who need to tie
        BettingEventIDs to GameIDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=wnba_v3_scores_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_futures_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], WnbaV3ScoresBettingFuturesBySeasonErrorBody]:
        """Returns available Futures outcomes for the given season. Does not include line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingFuturesBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=wnba_v3_scores_betting_futures_by_season_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_futures_by_season_sportsbook_group(
        self,
        format: FormatOrStr,
        season: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingEvent1], WnbaV3ScoresBettingFuturesBySeasonSportsbookGroupErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season. Just the api year, no season codes. <br>Examples: <code>2025</code>, etc
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("season", season),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=wnba_v3_scores_betting_futures_by_season_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket, WnbaV3ScoresBettingMarketErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid entries include:
                <code>36</code>, <code>342</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket],
            error_mapper=wnba_v3_scores_betting_market_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
        market_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket, WnbaV3ScoresBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid entries include:
                <code>36</code>, <code>342</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>, <code>G1001</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingMarket/{marketId}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket],
            error_mapper=wnba_v3_scores_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_markets_by_event(
        self, format: FormatOrStr, event_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByEventErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventId", event_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByEventSportsbookGroupErrorBody]:
        """Returns the markets and available outcomes for a given BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_markets_by_game(
        self, format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByGameErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
                Valid entries include: <code>1934</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingMarketsByGameID/{gameID}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameID", game_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_game_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_markets_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByGameSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
                Valid entries include: <code>1934</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingMarketsByGameID/{gameID}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("gameID", game_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for ``Game Lines`` <code>2</code> for ``Player Props`` <code>3</code> for ``Team Props``
                <code>6</code> for ``Game Props``
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets). Valid entries include: <code>12</code>, <code>8</code>, etc.
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for ``Game Lines`` <code>2</code> for ``Player Props`` <code>3</code> for ``Team Props``
                <code>6</code> for ``Game Props``
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection, WnbaV3ScoresBettingMetadataErrorBody]:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection],
            error_mapper=wnba_v3_scores_betting_metadata_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_player_props_by_game(
        self, format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingPlayerPropsByGameErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The unique GameID of the game in question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BettingPlayerPropsByGameID/{gameId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameId", game_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_player_props_by_game_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_betting_player_props_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], WnbaV3ScoresBettingPlayerPropsByGameSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/wnba/scores/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("gameId", game_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=wnba_v3_scores_betting_player_props_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_box_score_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore5, WnbaV3ScoresBoxScoreFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered after
        the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an WNBA game. GameIDs can be found in the Games API. Valid entries are
                <code>1686</code>, <code>1899</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BoxScoreFinal/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore5],
            error_mapper=wnba_v3_scores_box_score_final_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_box_score_live_final(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BoxScore5, WnbaV3ScoresBoxScoreLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the game, called per individual game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The GameID of an WNBA game. GameIDs can be found in the Games API. Valid entries are
                <code>1686</code>, <code>1899</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BoxScore/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BoxScore5],
            error_mapper=wnba_v3_scores_box_score_live_final_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_box_scores_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore5], WnbaV3ScoresBoxScoresByDateFinalErrorBody]:
        """Full statistical information for a specified date for each game that took place, down to the team and player
        stat level, delivered after the game is complete.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2024-MAY-16</code>, <code>2023-OCT-20</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BoxScoresFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore5]],
            error_mapper=wnba_v3_scores_box_scores_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_box_scores_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BoxScore5], WnbaV3ScoresBoxScoresByDateLiveFinalErrorBody]:
        """Full statistical information for a specified game, down to the team and player stat level, delivered live
        during the games, called for all games on a given date.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2024-MAY-16</code>, <code>2024-OCT-20</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/BoxScores/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BoxScore5]],
            error_mapper=wnba_v3_scores_box_scores_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_games_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game10], WnbaV3ScoresGamesByDateFinalErrorBody]:
        """Full scores and gameday info, as well as all of the quarter scores and full-time score, delivered as the game
        ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/GamesByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game10]],
            error_mapper=wnba_v3_scores_games_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_games_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game10], WnbaV3ScoresGamesByDateLiveFinalErrorBody]:
        """Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday
        info includes TV channel etc

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/GamesByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game10]],
            error_mapper=wnba_v3_scores_games_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_games_basic_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic6], WnbaV3ScoresGamesBasicByDateFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/ScoresBasicFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic6]],
            error_mapper=wnba_v3_scores_games_basic_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_games_basic_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ScoreBasic6], WnbaV3ScoresGamesBasicByDateLiveFinalErrorBody]:
        """A slimmed-down score endpoint, giving just the quarter scores and full gane score, for simple applications,
        updated live.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/ScoresBasic/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[ScoreBasic6]],
            error_mapper=wnba_v3_scores_games_basic_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_player_details_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player6], WnbaV3ScoresPlayerDetailsByActiveErrorBody]:
        """Full player bio and details, including injury notes, for all active players.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Players"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player6]],
            error_mapper=wnba_v3_scores_player_details_by_active_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_player_details_by_team(
        self, format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Player6], WnbaV3ScoresPlayerDetailsByTeamErrorBody]:
        """Full player bio and details, including injury notes, for all available players by team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            team: The abbreviation of the requested team. <br>Examples: <code>LA</code>, <code>IND</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Players/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Player6]],
            error_mapper=wnba_v3_scores_player_details_by_team_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_player_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason7], WnbaV3ScoresPlayerSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/PlayerSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason7]],
            error_mapper=wnba_v3_scores_player_season_stats_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_player_season_stats_by_team(
        self, format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[PlayerSeason7], WnbaV3ScoresPlayerSeasonStatsByTeamErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a
        given season on a given team.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            team: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/PlayerSeasonStatsByTeam/{season}/{team}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[PlayerSeason7]],
            error_mapper=wnba_v3_scores_player_season_stats_by_team_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_pre_game_odds_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo6], WnbaV3ScoresPreGameOddsByDateErrorBody]:
        """Returns full game odds (spread, moneyline, total) for games on a given date. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the game(s).<br>Examples: <code>2019-MAY-16</code>, <code>2019-MAY-25</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/GameOddsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo6]],
            error_mapper=wnba_v3_scores_pre_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_pre_game_odds_line_movement(
        self, format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo6], WnbaV3ScoresPreGameOddsLineMovementErrorBody]:
        """Returns the full-game odds (spread, moneyline, total) for games on a given date. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            gameid: The unique GameID of the game for which to pull data.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/GameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo6]],
            error_mapper=wnba_v3_scores_pre_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_schedules(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Game10], WnbaV3ScoresSchedulesErrorBody]:
        """Home and away teams, date and time, season type and week etc. are included. Also includes gameday
        information. This includes full stadium information (capacity, lat/long, surface etc.), top-line betting
        information (spread, moneyline, total), and broadcast information.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2019</code>,
                <code>2019PRE</code>, <code>2019POST</code>, <code>2019REG</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Games/{Season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("Season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Game10]],
            error_mapper=wnba_v3_scores_schedules_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_schedules_basic(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SchedulesBasic], WnbaV3ScoresSchedulesBasicErrorBody]:
        """A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the
        game, and season type, week etc. are included. Ideal for the most basic information required to build a
        schedule.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season (with optional season type).<br>Examples: <code>2019</code>,
                <code>2019PRE</code>, <code>2019POST</code>, <code>2019REG</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/SchedulesBasic/{Season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("Season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[SchedulesBasic]],
            error_mapper=wnba_v3_scores_schedules_basic_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_season_current(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Season4, WnbaV3ScoresSeasonCurrentErrorBody]:
        """Year of the current season. This value changes at the start of the new league year. For leagues that run over
        two years, this is the year the season starts, not ends.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/CurrentSeason"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[Season4],
            error_mapper=wnba_v3_scores_season_current_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_sportsbooks_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], WnbaV3ScoresSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=wnba_v3_scores_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_stadiums(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Stadium6], WnbaV3ScoresStadiumsErrorBody]:
        """Returns all stadiums in the league with capacity, surface, latitude/longitude, city and state (and where
        applicable country.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Stadiums"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Stadium6]],
            error_mapper=wnba_v3_scores_stadiums_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_standings(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, WnbaV3ScoresStandingsErrorBody]:
        """Includes regular season standings in division and conference, from which postseason seeding can be derived.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Standings/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=empty_response,
            error_mapper=wnba_v3_scores_standings_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_team_game_stats_by_date_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame6], WnbaV3ScoresTeamGameStatsByDateFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for a games on a given date,
        delivered as each game concludes.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/TeamGameStatsByDateFinal/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame6]],
            error_mapper=wnba_v3_scores_team_game_stats_by_date_final_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_team_game_stats_by_date_live_final(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamGame6], WnbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody]:
        """Returns the box score statistical record team-wide (aggregated from all players) for all games on a given
        date, both live and post-game.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/TeamGameStatsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamGame6]],
            error_mapper=wnba_v3_scores_team_game_stats_by_date_live_final_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_team_profiles_all(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Team6], WnbaV3ScoresTeamProfilesAllErrorBody]:
        """Full team information: team name and city, conference and division, and colors. Also contains basic fantasy
        info such as IDs as well as full stadium data. This endpoint returns all teams regardless of current active
        status.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/Teams"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Team6]],
            error_mapper=wnba_v3_scores_team_profiles_all_error_mapper,
            request_options=request_options,
        )

    async def wnba_v3_scores_team_season_stats(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[TeamSeason6], WnbaV3ScoresTeamSeasonStatsErrorBody]:
        """Returns all season-long stats (i.e. the season total, not each individual game record) for all teams
        (aggregated from all players) for a given season.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/wnba/scores/{format}/TeamSeasonStats/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[TeamSeason6]],
            error_mapper=wnba_v3_scores_team_season_stats_error_mapper,
            request_options=request_options,
        )
