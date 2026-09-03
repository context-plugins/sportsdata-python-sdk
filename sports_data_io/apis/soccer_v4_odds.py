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
    json_decoder,
    param,
)
from ..errors.soccer_v4_odds_betting_events_by_date_error import (
    SoccerV4OddsBettingEventsByDateErrorBody,
    soccer_v4_odds_betting_events_by_date_error_mapper,
)
from ..errors.soccer_v4_odds_betting_events_by_season_error import (
    SoccerV4OddsBettingEventsBySeasonErrorBody,
    soccer_v4_odds_betting_events_by_season_error_mapper,
)
from ..errors.soccer_v4_odds_betting_futures_by_season_error import (
    SoccerV4OddsBettingFuturesBySeasonErrorBody,
    soccer_v4_odds_betting_futures_by_season_error_mapper,
)
from ..errors.soccer_v4_odds_betting_futures_by_season_sportsbook_group_error import (
    SoccerV4OddsBettingFuturesBySeasonSportsbookGroupErrorBody,
    soccer_v4_odds_betting_futures_by_season_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_betting_market_error import (
    SoccerV4OddsBettingMarketErrorBody,
    soccer_v4_odds_betting_market_error_mapper,
)
from ..errors.soccer_v4_odds_betting_market_sportsbook_group_error import (
    SoccerV4OddsBettingMarketSportsbookGroupErrorBody,
    soccer_v4_odds_betting_market_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_betting_markets_by_event_error import (
    SoccerV4OddsBettingMarketsByEventErrorBody,
    soccer_v4_odds_betting_markets_by_event_error_mapper,
)
from ..errors.soccer_v4_odds_betting_markets_by_event_sportsbook_group_error import (
    SoccerV4OddsBettingMarketsByEventSportsbookGroupErrorBody,
    soccer_v4_odds_betting_markets_by_event_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_betting_markets_by_game_error import (
    SoccerV4OddsBettingMarketsByGameErrorBody,
    soccer_v4_odds_betting_markets_by_game_error_mapper,
)
from ..errors.soccer_v4_odds_betting_markets_by_game_sportsbook_group_error import (
    SoccerV4OddsBettingMarketsByGameSportsbookGroupErrorBody,
    soccer_v4_odds_betting_markets_by_game_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_betting_markets_by_market_type_error import (
    SoccerV4OddsBettingMarketsByMarketTypeErrorBody,
    soccer_v4_odds_betting_markets_by_market_type_error_mapper,
)
from ..errors.soccer_v4_odds_betting_markets_by_market_type_sportsbook_group_error import (
    SoccerV4OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody,
    soccer_v4_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_betting_metadata_error import (
    SoccerV4OddsBettingMetadataErrorBody,
    soccer_v4_odds_betting_metadata_error_mapper,
)
from ..errors.soccer_v4_odds_betting_player_props_by_game_error import (
    SoccerV4OddsBettingPlayerPropsByGameErrorBody,
    soccer_v4_odds_betting_player_props_by_game_error_mapper,
)
from ..errors.soccer_v4_odds_betting_player_props_by_game_sportsbook_group_error import (
    SoccerV4OddsBettingPlayerPropsByGameSportsbookGroupErrorBody,
    soccer_v4_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_in_game_odds_by_date_error import (
    SoccerV4OddsInGameOddsByDateErrorBody,
    soccer_v4_odds_in_game_odds_by_date_error_mapper,
)
from ..errors.soccer_v4_odds_in_game_odds_by_date_sportsbook_group_error import (
    SoccerV4OddsInGameOddsByDateSportsbookGroupErrorBody,
    soccer_v4_odds_in_game_odds_by_date_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_in_game_odds_line_movement_error import (
    SoccerV4OddsInGameOddsLineMovementErrorBody,
    soccer_v4_odds_in_game_odds_line_movement_error_mapper,
)
from ..errors.soccer_v4_odds_in_game_odds_line_movement_sportsbook_group_error import (
    SoccerV4OddsInGameOddsLineMovementSportsbookGroupErrorBody,
    soccer_v4_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error import (
    SoccerV4OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody,
    soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_period_game_odds_by_date_error import (
    SoccerV4OddsPeriodGameOddsByDateErrorBody,
    soccer_v4_odds_period_game_odds_by_date_error_mapper,
)
from ..errors.soccer_v4_odds_period_game_odds_line_movement_error import (
    SoccerV4OddsPeriodGameOddsLineMovementErrorBody,
    soccer_v4_odds_period_game_odds_line_movement_error_mapper,
)
from ..errors.soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error import (
    SoccerV4OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody,
    soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error import (
    SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody,
    soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error import (
    SoccerV4OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody,
    soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
)
from ..errors.soccer_v4_odds_pre_game_odds_by_date_error import (
    SoccerV4OddsPreGameOddsByDateErrorBody,
    soccer_v4_odds_pre_game_odds_by_date_error_mapper,
)
from ..errors.soccer_v4_odds_pre_game_odds_line_movement_error import (
    SoccerV4OddsPreGameOddsLineMovementErrorBody,
    soccer_v4_odds_pre_game_odds_line_movement_error_mapper,
)
from ..errors.soccer_v4_odds_sportsbooks_by_active_error import (
    SoccerV4OddsSportsbooksByActiveErrorBody,
    soccer_v4_odds_sportsbooks_by_active_error_mapper,
)
from ..models.betting_entity_metadata_collection1 import BettingEntityMetadataCollection1
from ..models.betting_event3 import BettingEvent3
from ..models.betting_market1 import BettingMarket1
from ..models.enums.format import FormatOrStr
from ..models.game_info7 import GameInfo7
from ..models.game_info_result6 import GameInfoResult6
from ..models.sportsbook import Sportsbook
from ..server.server import Server


class SoccerV4Odds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoccerV4OddsWithRawResponse(client, server, auth)

    def soccer_v4_odds_betting_events_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent3]:
        """The list of current BettingEvents for the given date and competition, from which Betting Market data can be
        gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props,
        Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-11-20</code>, <code>2018-11-23</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_events_by_date(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_events_by_season(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent3]:
        """The list of current BettingEvents for the given season within a given competition, from which Betting Market
        data can be gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g.
        Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_events_by_season(
            format, competition, season, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_futures_by_season(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent3]:
        """Returns available Futures markets for the given season and a given competition. Does not include line
        movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_futures_by_season(
            format, competition, season, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_futures_by_season_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        season: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingEvent3]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_futures_by_season_sportsbook_group(
            format, competition, season, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_market(
        self,
        format: FormatOrStr,
        competition: str,
        market_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket1:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_market(
            format, competition, market_id, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        market_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket1:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_market_sportsbook_group(
            format, competition, market_id, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID within a given competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_markets_by_event(
            format, competition, event_id, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_markets_by_event_sportsbook_group(
            format, competition, event_id, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_markets_by_game(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID within a given competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_markets_by_game(
            format, competition, gameid, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_markets_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID in a competition. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_markets_by_game_sportsbook_group(
            format, competition, gameid, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        market_type_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns Markets and available outcomes for a given event (within a competition) and market type requested. A
        lighter call than by BettingEventID as it only includes markets tagged with the specific MarketType, a full list
        of which is available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_markets_by_market_type(
            format, competition, event_id, market_type_id, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_markets_by_market_type_sportsbook_group(
            format, competition, event_id, market_type_id, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> BettingEntityMetadataCollection1:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names. Also includes a list of the MarketType, BetType & PeriodType combinations which we will have
        resulting for.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_metadata(format, request_options=request_options).unwrap()

    def soccer_v4_odds_betting_player_props_by_game(
        self,
        format: FormatOrStr,
        competition: str,
        game_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            game_id: The unique GameID of the game in question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_player_props_by_game(
            format, competition, game_id, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_betting_player_props_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_betting_player_props_by_game_sportsbook_group(
            format, competition, game_id, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_in_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date in a given competition. Only
        returns the most recently seen odds, not inclusive of line movement. As this is in-game, it will only return
        results while the game is in progress.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_in_game_odds_by_date(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_in_game_odds_by_date_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        date: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo7]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date and competition. Only returns
        the most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results
        while the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_in_game_odds_by_date_sportsbook_group(
            format, competition, date, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_in_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns in-play game odds (spread, moneyline, total) for a given game in a given competition. Returns the
        full line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_in_game_odds_line_movement(
            format, competition, gameid, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo7]:
        """Returns in-play game odds (spread, moneyline, total) for a given game and competition. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_in_game_odds_line_movement_sportsbook_group(
            format, competition, gameid, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult6]:
        """Returns in-play game odds (spread, moneyline, total) for a given game in a competition. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
            format, competition, gameid, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_period_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date in a given competition.
        Non-full-game means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_period_game_odds_by_date(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_period_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given game
        within a competition. This endpoint has a longer cache as it is meant for historical data/line movement rather
        than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>41323</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_period_game_odds_line_movement(
            format, competition, gameid, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        date: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo7]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games on a given date for a given
        competition. Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must
        be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
            format, competition, date, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo7]:
        """Returns the game odds for a given game in a given competition. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
            format, competition, gameid, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult6]:
        """Returns the game odds for a given game and competition. In this endpoint both full-game and partial-game odds
        are included. This also includes Resulting: for markets with a ResultType, each line will be graded and it will
        be determined whether the bet would have won or lost. Returns the full line movement for the given game. This
        endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the
        second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
            format, competition, gameid, sportsbookgroup, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_pre_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns full game odds (spread, moneyline, total) for games from a given competition on a given date. Only
        returns the most recently seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_pre_game_odds_by_date(
            format, competition, date, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_pre_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given game
        within a competition. This endpoint has a longer cache as it is meant for historical data/line movement rather
        than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.soccer_v4_odds_pre_game_odds_line_movement(
            format, competition, gameid, request_options=request_options
        ).unwrap()

    def soccer_v4_odds_sportsbooks_by_active(
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
        return self._with_raw_response.soccer_v4_odds_sportsbooks_by_active(
            format, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SoccerV4OddsWithRawResponse:
        return self._with_raw_response


class AsyncSoccerV4Odds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoccerV4OddsWithRawResponse(client, server, auth)

    async def soccer_v4_odds_betting_events_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent3]:
        """The list of current BettingEvents for the given date and competition, from which Betting Market data can be
        gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props,
        Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-11-20</code>, <code>2018-11-23</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_events_by_date(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_events_by_season(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent3]:
        """The list of current BettingEvents for the given season within a given competition, from which Betting Market
        data can be gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g.
        Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_events_by_season(
                format, competition, season, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_futures_by_season(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent3]:
        """Returns available Futures markets for the given season and a given competition. Does not include line
        movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_futures_by_season(
                format, competition, season, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_futures_by_season_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        season: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingEvent3]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_futures_by_season_sportsbook_group(
                format, competition, season, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_market(
        self,
        format: FormatOrStr,
        competition: str,
        market_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket1:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_market(
                format, competition, market_id, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        market_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket1:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_market_sportsbook_group(
                format, competition, market_id, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID within a given competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_markets_by_event(
                format, competition, event_id, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_markets_by_event_sportsbook_group(
                format, competition, event_id, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_markets_by_game(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID within a given competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_markets_by_game(
                format, competition, gameid, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_markets_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID in a competition. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_markets_by_game_sportsbook_group(
                format, competition, gameid, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        market_type_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns Markets and available outcomes for a given event (within a competition) and market type requested. A
        lighter call than by BettingEventID as it only includes markets tagged with the specific MarketType, a full list
        of which is available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_markets_by_market_type(
                format, competition, event_id, market_type_id, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_markets_by_market_type_sportsbook_group(
                format, competition, event_id, market_type_id, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> BettingEntityMetadataCollection1:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names. Also includes a list of the MarketType, BetType & PeriodType combinations which we will have
        resulting for.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_metadata(format, request_options=request_options)
        ).unwrap()

    async def soccer_v4_odds_betting_player_props_by_game(
        self,
        format: FormatOrStr,
        competition: str,
        game_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            game_id: The unique GameID of the game in question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_player_props_by_game(
                format, competition, game_id, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_betting_player_props_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_betting_player_props_by_game_sportsbook_group(
                format, competition, game_id, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_in_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date in a given competition. Only
        returns the most recently seen odds, not inclusive of line movement. As this is in-game, it will only return
        results while the game is in progress.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_in_game_odds_by_date(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_in_game_odds_by_date_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        date: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo7]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date and competition. Only returns
        the most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results
        while the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_in_game_odds_by_date_sportsbook_group(
                format, competition, date, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_in_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns in-play game odds (spread, moneyline, total) for a given game in a given competition. Returns the
        full line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_in_game_odds_line_movement(
                format, competition, gameid, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo7]:
        """Returns in-play game odds (spread, moneyline, total) for a given game and competition. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_in_game_odds_line_movement_sportsbook_group(
                format, competition, gameid, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult6]:
        """Returns in-play game odds (spread, moneyline, total) for a given game in a competition. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
                format, competition, gameid, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_period_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date in a given competition.
        Non-full-game means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_period_game_odds_by_date(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_period_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given game
        within a competition. This endpoint has a longer cache as it is meant for historical data/line movement rather
        than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>41323</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_period_game_odds_line_movement(
                format, competition, gameid, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        date: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo7]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games on a given date for a given
        competition. Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must
        be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
                format, competition, date, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo7]:
        """Returns the game odds for a given game in a given competition. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
                format, competition, gameid, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult6]:
        """Returns the game odds for a given game and competition. In this endpoint both full-game and partial-game odds
        are included. This also includes Resulting: for markets with a ResultType, each line will be graded and it will
        be determined whether the bet would have won or lost. Returns the full line movement for the given game. This
        endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the
        second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
                format, competition, gameid, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_pre_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns full game odds (spread, moneyline, total) for games from a given competition on a given date. Only
        returns the most recently seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_pre_game_odds_by_date(
                format, competition, date, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_pre_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo7]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given game
        within a competition. This endpoint has a longer cache as it is meant for historical data/line movement rather
        than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.soccer_v4_odds_pre_game_odds_line_movement(
                format, competition, gameid, request_options=request_options
            )
        ).unwrap()

    async def soccer_v4_odds_sportsbooks_by_active(
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
            await self._with_raw_response.soccer_v4_odds_sportsbooks_by_active(format, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoccerV4OddsWithRawResponse:
        return self._with_raw_response


class SoccerV4OddsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def soccer_v4_odds_betting_events_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent3], SoccerV4OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date and competition, from which Betting Market data can be
        gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props,
        Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-11-20</code>, <code>2018-11-23</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingEventsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=soccer_v4_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_events_by_season(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent3], SoccerV4OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season within a given competition, from which Betting Market
        data can be gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g.
        Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingEventsBySeason/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=soccer_v4_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_futures_by_season(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent3], SoccerV4OddsBettingFuturesBySeasonErrorBody]:
        """Returns available Futures markets for the given season and a given competition. Does not include line
        movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingFuturesBySeason/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=soccer_v4_odds_betting_futures_by_season_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_futures_by_season_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        season: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingEvent3], SoccerV4OddsBettingFuturesBySeasonSportsbookGroupErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingFuturesBySeason/{competition}/{season}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=soccer_v4_odds_betting_futures_by_season_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_market(
        self,
        format: FormatOrStr,
        competition: str,
        market_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket1, SoccerV4OddsBettingMarketErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingMarket/{competition}/{marketId}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("marketId", market_id),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket1],
            error_mapper=soccer_v4_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        market_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket1, SoccerV4OddsBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingMarket/{competition}/{marketId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket1],
            error_mapper=soccer_v4_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByEventErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID within a given competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingMarkets/{competition}/{eventId}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("eventId", event_id),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByEventSportsbookGroupErrorBody]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingMarketsByEvent/{competition}/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_markets_by_game(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByGameErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID within a given competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingMarketsByGameID/{competition}/{gameid}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_game_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_markets_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByGameSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID in a competition. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingMarketsByGameID/{competition}/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        market_type_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event (within a competition) and market type requested. A
        lighter call than by BettingEventID as it only includes markets tagged with the specific MarketType, a full list
        of which is available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingMarketsByMarketType/{competition}/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingMarketsByMarketType/{competition}/{eventId}/{marketTypeID}/{sportsbookgroup}",
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection1, SoccerV4OddsBettingMetadataErrorBody]:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names. Also includes a list of the MarketType, BetType & PeriodType combinations which we will have
        resulting for.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection1],
            error_mapper=soccer_v4_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_player_props_by_game(
        self,
        format: FormatOrStr,
        competition: str,
        game_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingPlayerPropsByGameErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            game_id: The unique GameID of the game in question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingPlayerPropsByGameID/{competition}/{gameId}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameId", game_id),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_player_props_by_game_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_betting_player_props_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingPlayerPropsByGameID/{competition}/{gameId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameId", game_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_in_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsByDateErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date in a given competition. Only
        returns the most recently seen odds, not inclusive of line movement. As this is in-game, it will only return
        results while the game is in progress.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/LiveGameOddsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_in_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_in_game_odds_by_date_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        date: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsByDateSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date and competition. Only returns
        the most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results
        while the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/InGameOddsByDate/{competition}/{date}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("date", date),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_in_game_odds_by_date_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_in_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsLineMovementErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for a given game in a given competition. Returns the
        full line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/LiveGameOddsLineMovement/{competition}/{gameid}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_in_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for a given game and competition. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/InGameOddsLineMovement/{competition}/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfoResult6], SoccerV4OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for a given game in a competition. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/InGameOddsLineMovementWithResulting/{competition}/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfoResult6]],
            error_mapper=soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_period_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPeriodGameOddsByDateErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date in a given competition.
        Non-full-game means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/AlternateMarketGameOddsByDate/{competition}/{date}"
            ),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_period_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_period_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPeriodGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given game
        within a competition. This endpoint has a longer cache as it is meant for historical data/line movement rather
        than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>41323</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/AlternateMarketGameOddsLineMovement/{competition}/{gameid}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_period_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        date: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games on a given date for a given
        competition. Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must
        be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/PreGameOddsByDate/{competition}/{date}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("date", date),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns the game odds for a given game in a given competition. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/PreGameOddsLineMovement/{competition}/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[GameInfoResult6], SoccerV4OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody
    ]:
        """Returns the game odds for a given game and competition. In this endpoint both full-game and partial-game odds
        are included. This also includes Resulting: for markets with a ResultType, each line will be graded and it will
        be determined whether the bet would have won or lost. Returns the full line movement for the given game. This
        endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the
        second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/PreGameOddsLineMovementWithResulting/{competition}/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfoResult6]],
            error_mapper=soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_pre_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPreGameOddsByDateErrorBody]:
        """Returns full game odds (spread, moneyline, total) for games from a given competition on a given date. Only
        returns the most recently seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/GameOddsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_pre_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_pre_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPreGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given game
        within a competition. This endpoint has a longer cache as it is meant for historical data/line movement rather
        than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/GameOddsLineMovement/{competition}/{gameid}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_pre_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def soccer_v4_odds_sportsbooks_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], SoccerV4OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=soccer_v4_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )


class AsyncSoccerV4OddsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def soccer_v4_odds_betting_events_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent3], SoccerV4OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date and competition, from which Betting Market data can be
        gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props,
        Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-11-20</code>, <code>2018-11-23</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingEventsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=soccer_v4_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_events_by_season(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent3], SoccerV4OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season within a given competition, from which Betting Market
        data can be gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g.
        Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingEventsBySeason/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=soccer_v4_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_futures_by_season(
        self, format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent3], SoccerV4OddsBettingFuturesBySeasonErrorBody]:
        """Returns available Futures markets for the given season and a given competition. Does not include line
        movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingFuturesBySeason/{competition}/{season}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=soccer_v4_odds_betting_futures_by_season_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_futures_by_season_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        season: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingEvent3], SoccerV4OddsBettingFuturesBySeasonSportsbookGroupErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingFuturesBySeason/{competition}/{season}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("season", season),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=soccer_v4_odds_betting_futures_by_season_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_market(
        self,
        format: FormatOrStr,
        competition: str,
        market_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket1, SoccerV4OddsBettingMarketErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingMarket/{competition}/{marketId}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("marketId", market_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket1],
            error_mapper=soccer_v4_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        market_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket1, SoccerV4OddsBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingMarket/{competition}/{marketId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket1],
            error_mapper=soccer_v4_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByEventErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID within a given competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingMarkets/{competition}/{eventId}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("eventId", event_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByEventSportsbookGroupErrorBody]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingMarketsByEvent/{competition}/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_markets_by_game(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByGameErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID within a given competition.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingMarketsByGameID/{competition}/{gameid}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_game_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_markets_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByGameSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID in a competition. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingMarketsByGameID/{competition}/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        market_type_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event (within a competition) and market type requested. A
        lighter call than by BettingEventID as it only includes markets tagged with the specific MarketType, a full list
        of which is available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingMarketsByMarketType/{competition}/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingMarketsByMarketType/{competition}/{eventId}/{marketTypeID}/{sportsbookgroup}",
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection1, SoccerV4OddsBettingMetadataErrorBody]:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names. Also includes a list of the MarketType, BetType & PeriodType combinations which we will have
        resulting for.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection1],
            error_mapper=soccer_v4_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_player_props_by_game(
        self,
        format: FormatOrStr,
        competition: str,
        game_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingPlayerPropsByGameErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            game_id: The unique GameID of the game in question.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingPlayerPropsByGameID/{competition}/{gameId}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameId", game_id),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_player_props_by_game_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_betting_player_props_by_game_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        game_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], SoccerV4OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/BettingPlayerPropsByGameID/{competition}/{gameId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameId", game_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=soccer_v4_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_in_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsByDateErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date in a given competition. Only
        returns the most recently seen odds, not inclusive of line movement. As this is in-game, it will only return
        results while the game is in progress.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/LiveGameOddsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_in_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_in_game_odds_by_date_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        date: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsByDateSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date and competition. Only returns
        the most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results
        while the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/InGameOddsByDate/{competition}/{date}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("date", date),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_in_game_odds_by_date_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_in_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsLineMovementErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for a given game in a given competition. Returns the
        full line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/LiveGameOddsLineMovement/{competition}/{gameid}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_in_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for a given game and competition. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/InGameOddsLineMovement/{competition}/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfoResult6], SoccerV4OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for a given game in a competition. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/InGameOddsLineMovementWithResulting/{competition}/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfoResult6]],
            error_mapper=soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_period_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPeriodGameOddsByDateErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date in a given competition.
        Non-full-game means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/AlternateMarketGameOddsByDate/{competition}/{date}"
            ),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_period_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_period_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPeriodGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given game
        within a competition. This endpoint has a longer cache as it is meant for historical data/line movement rather
        than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>41323</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/AlternateMarketGameOddsLineMovement/{competition}/{gameid}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_period_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        date: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games on a given date for a given
        competition. Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must
        be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/PreGameOddsByDate/{competition}/{date}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("date", date),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns the game odds for a given game in a given competition. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/PreGameOddsLineMovement/{competition}/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        format: FormatOrStr,
        competition: str,
        gameid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[GameInfoResult6], SoccerV4OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody
    ]:
        """Returns the game odds for a given game and competition. In this endpoint both full-game and partial-game odds
        are included. This also includes Resulting: for markets with a ResultType, each line will be graded and it will
        be determined whether the bet would have won or lost. Returns the full line movement for the given game. This
        endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the
        second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v4/soccer/odds/{format}/PreGameOddsLineMovementWithResulting/{competition}/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfoResult6]],
            error_mapper=soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_pre_game_odds_by_date(
        self, format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPreGameOddsByDateErrorBody]:
        """Returns full game odds (spread, moneyline, total) for games from a given competition on a given date. Only
        returns the most recently seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            date: The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/GameOddsByDate/{competition}/{date}"),
            path_params=[
                param[FormatOrStr]("format", format), param[str]("competition", competition), param[str]("date", date)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_pre_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_pre_game_odds_line_movement(
        self, format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo7], SoccerV4OddsPreGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given game
        within a competition. This endpoint has a longer cache as it is meant for historical data/line movement rather
        than the most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            competition: An indication of a soccer competition/league. This value can be the CompetitionId or the
                Competition Key. Possible values include: <code>EPL</code>, <code>1</code>, <code>MLS</code>,
                <code>8</code>, etc.
            gameid: The GameID of a Soccer game. GameIDs can be found in the Games API. Valid entries are
                <code>14060</code>, <code>14061</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/GameOddsLineMovement/{competition}/{gameid}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("competition", competition),
                param[str]("gameid", gameid),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo7]],
            error_mapper=soccer_v4_odds_pre_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def soccer_v4_odds_sportsbooks_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], SoccerV4OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v4/soccer/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=soccer_v4_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )
