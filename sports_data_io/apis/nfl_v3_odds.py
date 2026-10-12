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
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.nfl_v3_odds_betting_events_by_date_error import (
    NflV3OddsBettingEventsByDateErrorBody,
    nfl_v3_odds_betting_events_by_date_error_mapper,
)
from ..errors.nfl_v3_odds_betting_events_by_season_error import (
    NflV3OddsBettingEventsBySeasonErrorBody,
    nfl_v3_odds_betting_events_by_season_error_mapper,
)
from ..errors.nfl_v3_odds_betting_futures_by_season_error import (
    NflV3OddsBettingFuturesBySeasonErrorBody,
    nfl_v3_odds_betting_futures_by_season_error_mapper,
)
from ..errors.nfl_v3_odds_betting_futures_by_season_sportsbook_group_error import (
    NflV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody,
    nfl_v3_odds_betting_futures_by_season_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_betting_market_error import (
    NflV3OddsBettingMarketErrorBody,
    nfl_v3_odds_betting_market_error_mapper,
)
from ..errors.nfl_v3_odds_betting_market_sportsbook_group_error import (
    NflV3OddsBettingMarketSportsbookGroupErrorBody,
    nfl_v3_odds_betting_market_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_betting_markets_by_event_error import (
    NflV3OddsBettingMarketsByEventErrorBody,
    nfl_v3_odds_betting_markets_by_event_error_mapper,
)
from ..errors.nfl_v3_odds_betting_markets_by_event_sportsbook_group_error import (
    NflV3OddsBettingMarketsByEventSportsbookGroupErrorBody,
    nfl_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_betting_markets_by_game_error import (
    NflV3OddsBettingMarketsByGameErrorBody,
    nfl_v3_odds_betting_markets_by_game_error_mapper,
)
from ..errors.nfl_v3_odds_betting_markets_by_game_sportsbook_group_error import (
    NflV3OddsBettingMarketsByGameSportsbookGroupErrorBody,
    nfl_v3_odds_betting_markets_by_game_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_betting_markets_by_market_type_error import (
    NflV3OddsBettingMarketsByMarketTypeErrorBody,
    nfl_v3_odds_betting_markets_by_market_type_error_mapper,
)
from ..errors.nfl_v3_odds_betting_markets_by_market_type_sportsbook_group_error import (
    NflV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody,
    nfl_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_betting_metadata_error import (
    NflV3OddsBettingMetadataErrorBody,
    nfl_v3_odds_betting_metadata_error_mapper,
)
from ..errors.nfl_v3_odds_betting_player_props_by_game_error import (
    NflV3OddsBettingPlayerPropsByGameErrorBody,
    nfl_v3_odds_betting_player_props_by_game_error_mapper,
)
from ..errors.nfl_v3_odds_betting_player_props_by_game_sportsbook_group_error import (
    NflV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody,
    nfl_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_betting_results_by_market_error import (
    NflV3OddsBettingResultsByMarketErrorBody,
    nfl_v3_odds_betting_results_by_market_error_mapper,
)
from ..errors.nfl_v3_odds_betting_results_by_market_sportsbook_group_error import (
    NflV3OddsBettingResultsByMarketSportsbookGroupErrorBody,
    nfl_v3_odds_betting_results_by_market_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_betting_splits_by_betting_market_error import (
    NflV3OddsBettingSplitsByBettingMarketErrorBody,
    nfl_v3_odds_betting_splits_by_betting_market_error_mapper,
)
from ..errors.nfl_v3_odds_betting_splits_by_game_error import (
    NflV3OddsBettingSplitsByGameErrorBody,
    nfl_v3_odds_betting_splits_by_game_error_mapper,
)
from ..errors.nfl_v3_odds_betting_trends_by_matchup_error import (
    NflV3OddsBettingTrendsByMatchupErrorBody,
    nfl_v3_odds_betting_trends_by_matchup_error_mapper,
)
from ..errors.nfl_v3_odds_betting_trends_by_team_error import (
    NflV3OddsBettingTrendsByTeamErrorBody,
    nfl_v3_odds_betting_trends_by_team_error_mapper,
)
from ..errors.nfl_v3_odds_in_game_odds_by_week_error import (
    NflV3OddsInGameOddsByWeekErrorBody,
    nfl_v3_odds_in_game_odds_by_week_error_mapper,
)
from ..errors.nfl_v3_odds_in_game_odds_by_week_sportsbook_group_error import (
    NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody,
    nfl_v3_odds_in_game_odds_by_week_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_in_game_odds_line_movement_error import (
    NflV3OddsInGameOddsLineMovementErrorBody,
    nfl_v3_odds_in_game_odds_line_movement_error_mapper,
)
from ..errors.nfl_v3_odds_in_game_odds_line_movement_sportsbook_group_error import (
    NflV3OddsInGameOddsLineMovementSportsbookGroupErrorBody,
    nfl_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error import (
    NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody,
    nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_period_game_odds_by_week_error import (
    NflV3OddsPeriodGameOddsByWeekErrorBody,
    nfl_v3_odds_period_game_odds_by_week_error_mapper,
)
from ..errors.nfl_v3_odds_period_game_odds_line_movement_error import (
    NflV3OddsPeriodGameOddsLineMovementErrorBody,
    nfl_v3_odds_period_game_odds_line_movement_error_mapper,
)
from ..errors.nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error import (
    NflV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody,
    nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error import (
    NflV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody,
    nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error import (
    NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody,
    nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
)
from ..errors.nfl_v3_odds_pre_game_odds_by_week_error import (
    NflV3OddsPreGameOddsByWeekErrorBody,
    nfl_v3_odds_pre_game_odds_by_week_error_mapper,
)
from ..errors.nfl_v3_odds_pre_game_odds_line_movement_error import (
    NflV3OddsPreGameOddsLineMovementErrorBody,
    nfl_v3_odds_pre_game_odds_line_movement_error_mapper,
)
from ..errors.nfl_v3_odds_sportsbooks_active_error import (
    NflV3OddsSportsbooksActiveErrorBody,
    nfl_v3_odds_sportsbooks_active_error_mapper,
)
from ..models.betting_entity_metadata_collection import BettingEntityMetadataCollection
from ..models.betting_event import BettingEvent
from ..models.betting_market import BettingMarket
from ..models.betting_market_result import BettingMarketResult
from ..models.betting_market_split import BettingMarketSplit
from ..models.enums.format import Format, FormatOrStr
from ..models.enums.include import Include, IncludeOrStr
from ..models.game_betting_split import GameBettingSplit
from ..models.game_info import GameInfo
from ..models.game_info_result import GameInfoResult
from ..models.matchup_trends import MatchupTrends
from ..models.sportsbook import Sportsbook
from ..models.team_trends import TeamTrends
from ..server.server import Server


class NflV3Odds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NflV3OddsWithRawResponse(client, server, auth)

    def nfl_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-09-10</code>, <code>2020-09-13</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_events_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_events_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent]:
        """Returns available Futures markets for the given season. Does not include line movement.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020REG</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_futures_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingEvent]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020REG</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_futures_by_season_sportsbook_group(
                season, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.<br><br>A
        Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_market_sportsbook_group(
                market_id, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_markets_by_event(
                event_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_markets_by_event_sportsbook_group(
                event_id, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_markets_by_game(
        self,
        scoreid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            scoreid: The ScoreID of the desired game/score for which to pull all betting markets (includes
                outcomes/bets).
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_markets_by_game(
                scoreid, format_=format_, include=include, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_markets_by_game_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of the desired game/score for which to pull all betting markets (includes outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_markets_by_game_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_markets_by_market_type(
                event_id, market_type_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_markets_by_market_type_sportsbook_group(
                event_id,
                market_type_id,
                sportsbookgroup,
                format_=format_,
                include=include,
                request_options=request_options,
            ),
        )

    def nfl_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingEntityMetadataCollection:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names. Also includes a list of the MarketType, BetType & PeriodType combinations which we will have
        resulting for.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_metadata(format_=format_, request_options=request_options)
        )

    def nfl_v3_odds_betting_player_props_by_game(
        self,
        scoreid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            scoreid: The unique ScoreID of the game in question.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_player_props_by_game(
                scoreid, format_=format_, include=include, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The unique ScoreID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_player_props_by_game_sportsbook_group(
                scoreid, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketResult:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_results_by_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_results_by_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarketResult:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost. A Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_results_by_market_sportsbook_group(
                market_id, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketSplit:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The BettingMarketID of the market you would like to get splits for. Note that markets we do not
                have split information on will return an empty response.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_splits_by_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_splits_by_game(
        self, score_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> GameBettingSplit:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            score_id: The ScoreID of the desired game to get Betting Market Splits for
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_splits_by_game(
                score_id, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MatchupTrends:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: Abbreviation of a team. Example: <code>PHI</code>.
            opponent: Abbreviation of an opponent. Example: <code>NE</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_trends_by_matchup(
                team, opponent, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> TeamTrends:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: Abbreviation of a team. Example: <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_betting_trends_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_in_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_in_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_in_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_in_game_odds_by_week_sportsbook_group(
                season, week, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_in_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_in_game_odds_line_movement(
                scoreid, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_in_game_odds_line_movement_sportsbook_group(
                scoreid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult]:
        """Provides in-play odds line movement data for a given game. This means odds for games which are in-progress.
        Serves full line movement and is intended for showing the trend over a game rather than the most up-to-the
        second lines.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
                scoreid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_period_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_period_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_period_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_period_game_odds_line_movement(
                scoreid, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games in a given week and season.
        Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
                season, week, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns the game odds (for games in a given week and season. In this endpoint both full-game and partial-game
        odds are included. Returns the full line movement for the given game. This endpoint has a longer cache as it is
        meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group must be
        specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
                scoreid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included.<br><br>This also includes Resulting: for markets with a ResultType, each line
        will be graded and it will be determined whether the bet would have won or lost.<br><br>Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.<br><br>A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
                scoreid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_pre_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns the full-game core odds for games in a given week & season. This means moneyline, spread, and total.
        Only returns the most recently seen odds, not-including line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_pre_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_pre_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo]:
        """Returns the full-game core odds for a given ScoreID. This means moneyline, spread, and total. Only returns
        the most recently seen odds, not-including line movement. This endpoint has a longer cache as it is meant for
        historical data/line movement rather than the most up to the second line.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_pre_game_odds_line_movement(
                scoreid, format_=format_, request_options=request_options
            ),
        )

    def nfl_v3_odds_sportsbooks_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Sportsbook]:
        """Returns a list for mapping SportsbookID to the Sportsbook name.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nfl_v3_odds_sportsbooks_active(format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> NflV3OddsWithRawResponse:
        return self._with_raw_response


class AsyncNflV3Odds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNflV3OddsWithRawResponse(client, server, auth)

    async def nfl_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-09-10</code>, <code>2020-09-13</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_events_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_events_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent]:
        """Returns available Futures markets for the given season. Does not include line movement.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020REG</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_futures_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingEvent]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020REG</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_futures_by_season_sportsbook_group(
                season, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.<br><br>A
        Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_market_sportsbook_group(
                market_id, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_markets_by_event(
                event_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_markets_by_event_sportsbook_group(
                event_id, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_markets_by_game(
        self,
        scoreid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            scoreid: The ScoreID of the desired game/score for which to pull all betting markets (includes
                outcomes/bets).
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_markets_by_game(
                scoreid, format_=format_, include=include, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_markets_by_game_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of the desired game/score for which to pull all betting markets (includes outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_markets_by_game_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_markets_by_market_type(
                event_id, market_type_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_markets_by_market_type_sportsbook_group(
                event_id,
                market_type_id,
                sportsbookgroup,
                format_=format_,
                include=include,
                request_options=request_options,
            ),
        )

    async def nfl_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingEntityMetadataCollection:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names. Also includes a list of the MarketType, BetType & PeriodType combinations which we will have
        resulting for.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_metadata(format_=format_, request_options=request_options)
        )

    async def nfl_v3_odds_betting_player_props_by_game(
        self,
        scoreid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            scoreid: The unique ScoreID of the game in question.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_player_props_by_game(
                scoreid, format_=format_, include=include, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The unique ScoreID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_player_props_by_game_sportsbook_group(
                scoreid, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketResult:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_results_by_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_results_by_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarketResult:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost. A Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_results_by_market_sportsbook_group(
                market_id, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketSplit:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The BettingMarketID of the market you would like to get splits for. Note that markets we do not
                have split information on will return an empty response.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_splits_by_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_splits_by_game(
        self, score_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> GameBettingSplit:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            score_id: The ScoreID of the desired game to get Betting Market Splits for
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_splits_by_game(
                score_id, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MatchupTrends:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: Abbreviation of a team. Example: <code>PHI</code>.
            opponent: Abbreviation of an opponent. Example: <code>NE</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_trends_by_matchup(
                team, opponent, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> TeamTrends:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: Abbreviation of a team. Example: <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_betting_trends_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_in_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_in_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_in_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_in_game_odds_by_week_sportsbook_group(
                season, week, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_in_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_in_game_odds_line_movement(
                scoreid, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_in_game_odds_line_movement_sportsbook_group(
                scoreid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult]:
        """Provides in-play odds line movement data for a given game. This means odds for games which are in-progress.
        Serves full line movement and is intended for showing the trend over a game rather than the most up-to-the
        second lines.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
                scoreid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_period_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_period_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_period_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_period_game_odds_line_movement(
                scoreid, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games in a given week and season.
        Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
                season, week, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns the game odds (for games in a given week and season. In this endpoint both full-game and partial-game
        odds are included. Returns the full line movement for the given game. This endpoint has a longer cache as it is
        meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group must be
        specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
                scoreid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included.<br><br>This also includes Resulting: for markets with a ResultType, each line
        will be graded and it will be determined whether the bet would have won or lost.<br><br>Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.<br><br>A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
                scoreid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_pre_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo]:
        """Returns the full-game core odds for games in a given week & season. This means moneyline, spread, and total.
        Only returns the most recently seen odds, not-including line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_pre_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_pre_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo]:
        """Returns the full-game core odds for a given ScoreID. This means moneyline, spread, and total. Only returns
        the most recently seen odds, not-including line movement. This endpoint has a longer cache as it is meant for
        historical data/line movement rather than the most up to the second line.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_pre_game_odds_line_movement(
                scoreid, format_=format_, request_options=request_options
            ),
        )

    async def nfl_v3_odds_sportsbooks_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Sportsbook]:
        """Returns a list for mapping SportsbookID to the Sportsbook name.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nfl_v3_odds_sportsbooks_active(
                format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNflV3OddsWithRawResponse:
        return self._with_raw_response


class NflV3OddsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nfl_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent], NflV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-09-10</code>, <code>2020-09-13</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent]],
            error_mapper=nfl_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent], NflV3OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent]],
            error_mapper=nfl_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent], NflV3OddsBettingFuturesBySeasonErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020REG</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingFuturesBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent]],
            error_mapper=nfl_v3_odds_betting_futures_by_season_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingEvent], NflV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020REG</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent]],
            error_mapper=nfl_v3_odds_betting_futures_by_season_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket, NflV3OddsBettingMarketErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket],
            error_mapper=nfl_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket, NflV3OddsBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.<br><br>A
        Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket],
            error_mapper=nfl_v3_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByEventErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByEventSportsbookGroupErrorBody]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_markets_by_game(
        self,
        scoreid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByGameErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            scoreid: The ScoreID of the desired game/score for which to pull all betting markets (includes
                outcomes/bets).
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMarketsByScoreID/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_game_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_markets_by_game_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByGameSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of the desired game/score for which to pull all betting markets (includes outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingMarketsByGameID/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection, NflV3OddsBettingMetadataErrorBody]:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names. Also includes a list of the MarketType, BetType & PeriodType combinations which we will have
        resulting for.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection],
            error_mapper=nfl_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_player_props_by_game(
        self,
        scoreid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingPlayerPropsByGameErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            scoreid: The unique ScoreID of the game in question.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingPlayerPropsByScoreID/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_player_props_by_game_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The unique ScoreID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingPlayerPropsByScoreID/{scoreid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("scoreid", scoreid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketResult, NflV3OddsBettingResultsByMarketErrorBody]:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMarketResults/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarketResult],
            error_mapper=nfl_v3_odds_betting_results_by_market_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_results_by_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarketResult, NflV3OddsBettingResultsByMarketSportsbookGroupErrorBody]:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost. A Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarketResult],
            error_mapper=nfl_v3_odds_betting_results_by_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketSplit, NflV3OddsBettingSplitsByBettingMarketErrorBody]:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The BettingMarketID of the market you would like to get splits for. Note that markets we do not
                have split information on will return an empty response.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingSplitsByMarketId/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarketSplit],
            error_mapper=nfl_v3_odds_betting_splits_by_betting_market_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_splits_by_game(
        self, score_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GameBettingSplit, NflV3OddsBettingSplitsByGameErrorBody]:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            score_id: The ScoreID of the desired game to get Betting Market Splits for
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingSplitsByScoreId/{scoreId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreId", score_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[GameBettingSplit],
            error_mapper=nfl_v3_odds_betting_splits_by_game_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MatchupTrends, NflV3OddsBettingTrendsByMatchupErrorBody]:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: Abbreviation of a team. Example: <code>PHI</code>.
            opponent: Abbreviation of an opponent. Example: <code>NE</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/MatchupTrends/{team}/{opponent}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("team", team), param[str]("opponent", opponent)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[MatchupTrends],
            error_mapper=nfl_v3_odds_betting_trends_by_matchup_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamTrends, NflV3OddsBettingTrendsByTeamErrorBody]:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: Abbreviation of a team. Example: <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/TeamTrends/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TeamTrends],
            error_mapper=nfl_v3_odds_betting_trends_by_team_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_in_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsInGameOddsByWeekErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/LiveGameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_in_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_in_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/InGameOddsByWeek/{season}/{week}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_in_game_odds_by_week_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_in_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo], NflV3OddsInGameOddsLineMovementErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/LiveGameOddsLineMovement/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_in_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/InGameLineMovement/{scoreid}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("scoreid", scoreid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfoResult], NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]:
        """Provides in-play odds line movement data for a given game. This means odds for games which are in-progress.
        Serves full line movement and is intended for showing the trend over a game rather than the most up-to-the
        second lines.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/InGameLineMovementWithResulting/{scoreid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("scoreid", scoreid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfoResult]],
            error_mapper=nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_period_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsPeriodGameOddsByWeekErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/AlternateMarketGameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_period_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_period_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo], NflV3OddsPeriodGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/AlternateMarketGameOddsLineMovement/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_period_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games in a given week and season.
        Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/PreGameOddsByWeek/{season}/{week}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns the game odds (for games in a given week and season. In this endpoint both full-game and partial-game
        odds are included. Returns the full line movement for the given game. This endpoint has a longer cache as it is
        meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group must be
        specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/PreGameOddsLineMovement/{scoreid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("scoreid", scoreid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[GameInfoResult], NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody
    ]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included.<br><br>This also includes Resulting: for markets with a ResultType, each line
        will be graded and it will be determined whether the bet would have won or lost.<br><br>Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.<br><br>A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/PreGameOddsLineMovementWithResulting/{scoreid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("scoreid", scoreid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfoResult]],
            error_mapper=nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_pre_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsPreGameOddsByWeekErrorBody]:
        """Returns the full-game core odds for games in a given week & season. This means moneyline, spread, and total.
        Only returns the most recently seen odds, not-including line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/GameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_pre_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_pre_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo], NflV3OddsPreGameOddsLineMovementErrorBody]:
        """Returns the full-game core odds for a given ScoreID. This means moneyline, spread, and total. Only returns
        the most recently seen odds, not-including line movement. This endpoint has a longer cache as it is meant for
        historical data/line movement rather than the most up to the second line.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/GameOddsLineMovement/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_pre_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def nfl_v3_odds_sportsbooks_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], NflV3OddsSportsbooksActiveErrorBody]:
        """Returns a list for mapping SportsbookID to the Sportsbook name.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=nfl_v3_odds_sportsbooks_active_error_mapper,
            request_options=request_options,
        )


class AsyncNflV3OddsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nfl_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent], NflV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-09-10</code>, <code>2020-09-13</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent]],
            error_mapper=nfl_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent], NflV3OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent]],
            error_mapper=nfl_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent], NflV3OddsBettingFuturesBySeasonErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020REG</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingFuturesBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent]],
            error_mapper=nfl_v3_odds_betting_futures_by_season_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingEvent], NflV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020REG</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent]],
            error_mapper=nfl_v3_odds_betting_futures_by_season_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket, NflV3OddsBettingMarketErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarket],
            error_mapper=nfl_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket, NflV3OddsBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.<br><br>A
        Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarket],
            error_mapper=nfl_v3_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByEventErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByEventSportsbookGroupErrorBody]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_markets_by_game(
        self,
        scoreid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByGameErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            scoreid: The ScoreID of the desired game/score for which to pull all betting markets (includes
                outcomes/bets).
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMarketsByScoreID/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_game_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_markets_by_game_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByGameSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of the desired game/score for which to pull all betting markets (includes outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingMarketsByGameID/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include:
                <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props,
                <code>6</code> for Game Props
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection, NflV3OddsBettingMetadataErrorBody]:
        """Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to
        descriptive names. Also includes a list of the MarketType, BetType & PeriodType combinations which we will have
        resulting for.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingEntityMetadataCollection],
            error_mapper=nfl_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_player_props_by_game(
        self,
        scoreid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingPlayerPropsByGameErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            scoreid: The unique ScoreID of the game in question.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingPlayerPropsByScoreID/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_player_props_by_game_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], NflV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The unique ScoreID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets.
                <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and
                provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much
                longer and may be several minutes old. For best performance, the default parameter is highly
                recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting
                outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and
                delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most
                recently available betting outcome per sportsbook, for each listed market, even those outcomes are
                expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload,
                and it's cached for much longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingPlayerPropsByScoreID/{scoreid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("scoreid", scoreid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=nfl_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketResult, NflV3OddsBettingResultsByMarketErrorBody]:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingMarketResults/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarketResult],
            error_mapper=nfl_v3_odds_betting_results_by_market_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_results_by_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarketResult, NflV3OddsBettingResultsByMarketSportsbookGroupErrorBody]:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost. A Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarketResult],
            error_mapper=nfl_v3_odds_betting_results_by_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketSplit, NflV3OddsBettingSplitsByBettingMarketErrorBody]:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The BettingMarketID of the market you would like to get splits for. Note that markets we do not
                have split information on will return an empty response.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingSplitsByMarketId/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarketSplit],
            error_mapper=nfl_v3_odds_betting_splits_by_betting_market_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_splits_by_game(
        self, score_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GameBettingSplit, NflV3OddsBettingSplitsByGameErrorBody]:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            score_id: The ScoreID of the desired game to get Betting Market Splits for
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/BettingSplitsByScoreId/{scoreId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreId", score_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[GameBettingSplit],
            error_mapper=nfl_v3_odds_betting_splits_by_game_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MatchupTrends, NflV3OddsBettingTrendsByMatchupErrorBody]:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: Abbreviation of a team. Example: <code>PHI</code>.
            opponent: Abbreviation of an opponent. Example: <code>NE</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/MatchupTrends/{team}/{opponent}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("team", team), param[str]("opponent", opponent)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[MatchupTrends],
            error_mapper=nfl_v3_odds_betting_trends_by_matchup_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamTrends, NflV3OddsBettingTrendsByTeamErrorBody]:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: Abbreviation of a team. Example: <code>PHI</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/TeamTrends/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TeamTrends],
            error_mapper=nfl_v3_odds_betting_trends_by_team_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_in_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsInGameOddsByWeekErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/LiveGameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_in_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_in_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/InGameOddsByWeek/{season}/{week}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_in_game_odds_by_week_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_in_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo], NflV3OddsInGameOddsLineMovementErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/LiveGameOddsLineMovement/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_in_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/InGameLineMovement/{scoreid}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("scoreid", scoreid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfoResult], NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]:
        """Provides in-play odds line movement data for a given game. This means odds for games which are in-progress.
        Serves full line movement and is intended for showing the trend over a game rather than the most up-to-the
        second lines.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/InGameLineMovementWithResulting/{scoreid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("scoreid", scoreid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfoResult]],
            error_mapper=nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_period_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsPeriodGameOddsByWeekErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/AlternateMarketGameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_period_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_period_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo], NflV3OddsPeriodGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/AlternateMarketGameOddsLineMovement/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_period_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games in a given week and season.
        Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/PreGameOddsByWeek/{season}/{week}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns the game odds (for games in a given week and season. In this endpoint both full-game and partial-game
        odds are included. Returns the full line movement for the given game. This endpoint has a longer cache as it is
        meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group must be
        specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/PreGameOddsLineMovement/{scoreid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("scoreid", scoreid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        scoreid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[GameInfoResult], NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody
    ]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included.<br><br>This also includes Resulting: for markets with a ResultType, each line
        will be graded and it will be determined whether the bet would have won or lost.<br><br>Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.<br><br>A Sportsbook Group must be specified as a URL parameter.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/nfl/odds/{format}/PreGameOddsLineMovementWithResulting/{scoreid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("scoreid", scoreid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfoResult]],
            error_mapper=nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_pre_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo], NflV3OddsPreGameOddsByWeekErrorBody]:
        """Returns the full-game core odds for games in a given week & season. This means moneyline, spread, and total.
        Only returns the most recently seen odds, not-including line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the scores (games). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/GameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_pre_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_pre_game_odds_line_movement(
        self, scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo], NflV3OddsPreGameOddsLineMovementErrorBody]:
        """Returns the full-game core odds for a given ScoreID. This means moneyline, spread, and total. Only returns
        the most recently seen odds, not-including line movement. This endpoint has a longer cache as it is meant for
        historical data/line movement rather than the most up to the second line.

        Args:
            scoreid: The ScoreID of an NFL score (game). ScoreIDs can be found in the Scores API. Valid entries are
                <code>16654</code> or <code>16667</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/GameOddsLineMovement/{scoreid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("scoreid", scoreid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo]],
            error_mapper=nfl_v3_odds_pre_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def nfl_v3_odds_sportsbooks_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], NflV3OddsSportsbooksActiveErrorBody]:
        """Returns a list for mapping SportsbookID to the Sportsbook name.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nfl/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Sportsbook]],
            error_mapper=nfl_v3_odds_sportsbooks_active_error_mapper,
            request_options=request_options,
        )
