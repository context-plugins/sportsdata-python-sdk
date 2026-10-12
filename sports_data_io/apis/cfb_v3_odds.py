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
from ..errors.cfb_v3_odds_betting_events_by_date_error import (
    CfbV3OddsBettingEventsByDateErrorBody,
    cfb_v3_odds_betting_events_by_date_error_mapper,
)
from ..errors.cfb_v3_odds_betting_events_by_season_error import (
    CfbV3OddsBettingEventsBySeasonErrorBody,
    cfb_v3_odds_betting_events_by_season_error_mapper,
)
from ..errors.cfb_v3_odds_betting_futures_by_season_error import (
    CfbV3OddsBettingFuturesBySeasonErrorBody,
    cfb_v3_odds_betting_futures_by_season_error_mapper,
)
from ..errors.cfb_v3_odds_betting_futures_by_season_sportsbook_group_error import (
    CfbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody,
    cfb_v3_odds_betting_futures_by_season_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_betting_market_error import (
    CfbV3OddsBettingMarketErrorBody,
    cfb_v3_odds_betting_market_error_mapper,
)
from ..errors.cfb_v3_odds_betting_market_sportsbook_group_error import (
    CfbV3OddsBettingMarketSportsbookGroupErrorBody,
    cfb_v3_odds_betting_market_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_betting_markets_by_event_error import (
    CfbV3OddsBettingMarketsByEventErrorBody,
    cfb_v3_odds_betting_markets_by_event_error_mapper,
)
from ..errors.cfb_v3_odds_betting_markets_by_event_sportsbook_group_error import (
    CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody,
    cfb_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_betting_markets_by_game_error import (
    CfbV3OddsBettingMarketsByGameErrorBody,
    cfb_v3_odds_betting_markets_by_game_error_mapper,
)
from ..errors.cfb_v3_odds_betting_markets_by_game_sportsbook_group_error import (
    CfbV3OddsBettingMarketsByGameSportsbookGroupErrorBody,
    cfb_v3_odds_betting_markets_by_game_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_betting_markets_by_market_type_error import (
    CfbV3OddsBettingMarketsByMarketTypeErrorBody,
    cfb_v3_odds_betting_markets_by_market_type_error_mapper,
)
from ..errors.cfb_v3_odds_betting_markets_by_market_type_sportsbook_group_error import (
    CfbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody,
    cfb_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_betting_metadata_error import (
    CfbV3OddsBettingMetadataErrorBody,
    cfb_v3_odds_betting_metadata_error_mapper,
)
from ..errors.cfb_v3_odds_betting_player_props_by_game_error import (
    CfbV3OddsBettingPlayerPropsByGameErrorBody,
    cfb_v3_odds_betting_player_props_by_game_error_mapper,
)
from ..errors.cfb_v3_odds_betting_player_props_by_game_sportsbook_group_error import (
    CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody,
    cfb_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_betting_results_by_market_error import (
    CfbV3OddsBettingResultsByMarketErrorBody,
    cfb_v3_odds_betting_results_by_market_error_mapper,
)
from ..errors.cfb_v3_odds_betting_results_by_market_sportsbook_group_error import (
    CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody,
    cfb_v3_odds_betting_results_by_market_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_betting_splits_by_betting_market_error import (
    CfbV3OddsBettingSplitsByBettingMarketErrorBody,
    cfb_v3_odds_betting_splits_by_betting_market_error_mapper,
)
from ..errors.cfb_v3_odds_betting_splits_by_game_error import (
    CfbV3OddsBettingSplitsByGameErrorBody,
    cfb_v3_odds_betting_splits_by_game_error_mapper,
)
from ..errors.cfb_v3_odds_betting_trends_by_matchup_error import (
    CfbV3OddsBettingTrendsByMatchupErrorBody,
    cfb_v3_odds_betting_trends_by_matchup_error_mapper,
)
from ..errors.cfb_v3_odds_betting_trends_by_team_error import (
    CfbV3OddsBettingTrendsByTeamErrorBody,
    cfb_v3_odds_betting_trends_by_team_error_mapper,
)
from ..errors.cfb_v3_odds_in_game_odds_by_week_error import (
    CfbV3OddsInGameOddsByWeekErrorBody,
    cfb_v3_odds_in_game_odds_by_week_error_mapper,
)
from ..errors.cfb_v3_odds_in_game_odds_by_week_sportsbook_group_error import (
    CfbV3OddsInGameOddsByWeekSportsbookGroupErrorBody,
    cfb_v3_odds_in_game_odds_by_week_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_in_game_odds_line_movement_error import (
    CfbV3OddsInGameOddsLineMovementErrorBody,
    cfb_v3_odds_in_game_odds_line_movement_error_mapper,
)
from ..errors.cfb_v3_odds_in_game_odds_line_movement_sportsbook_group_error import (
    CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody,
    cfb_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error import (
    CfbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody,
    cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_period_game_odds_by_week_error import (
    CfbV3OddsPeriodGameOddsByWeekErrorBody,
    cfb_v3_odds_period_game_odds_by_week_error_mapper,
)
from ..errors.cfb_v3_odds_period_game_odds_line_movement_error import (
    CfbV3OddsPeriodGameOddsLineMovementErrorBody,
    cfb_v3_odds_period_game_odds_line_movement_error_mapper,
)
from ..errors.cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error import (
    CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody,
    cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error import (
    CfbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody,
    cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error import (
    CfbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody,
    cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
)
from ..errors.cfb_v3_odds_pre_game_odds_by_week_error import (
    CfbV3OddsPreGameOddsByWeekErrorBody,
    cfb_v3_odds_pre_game_odds_by_week_error_mapper,
)
from ..errors.cfb_v3_odds_pre_game_odds_line_movement_error import (
    CfbV3OddsPreGameOddsLineMovementErrorBody,
    cfb_v3_odds_pre_game_odds_line_movement_error_mapper,
)
from ..errors.cfb_v3_odds_sportsbooks_by_active_error import (
    CfbV3OddsSportsbooksByActiveErrorBody,
    cfb_v3_odds_sportsbooks_by_active_error_mapper,
)
from ..models.betting_entity_metadata_collection import BettingEntityMetadataCollection
from ..models.betting_event2 import BettingEvent2
from ..models.betting_market import BettingMarket
from ..models.betting_market_result import BettingMarketResult
from ..models.betting_market_split import BettingMarketSplit
from ..models.enums.format import Format, FormatOrStr
from ..models.enums.include import Include, IncludeOrStr
from ..models.game_betting_split2 import GameBettingSplit2
from ..models.game_info4 import GameInfo4
from ..models.game_info_result4 import GameInfoResult4
from ..models.matchup_trends4 import MatchupTrends4
from ..models.sportsbook import Sportsbook
from ..models.team_trends2 import TeamTrends2
from ..server.server import Server


class CfbV3Odds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CfbV3OddsWithRawResponse(client, server, auth)

    def cfb_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent2]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-10-17</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_events_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent2]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season<br>Examples: <code>2021</code>, <code>2022</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_events_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent2]:
        """Returns available Futures markets for the given season. Does not include line movement.

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
            self._with_raw_response.cfb_v3_odds_betting_futures_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingEvent2]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_futures_by_season_sportsbook_group(
                season, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_market(
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
            self._with_raw_response.cfb_v3_odds_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

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
            self._with_raw_response.cfb_v3_odds_betting_market_sportsbook_group(
                market_id, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_markets_by_event(
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
            self._with_raw_response.cfb_v3_odds_betting_markets_by_event(
                event_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_markets_by_event_sportsbook_group(
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
            self._with_raw_response.cfb_v3_odds_betting_markets_by_event_sportsbook_group(
                event_id, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_markets_by_game(
        self,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
            self._with_raw_response.cfb_v3_odds_betting_markets_by_game(
                gameid, format_=format_, include=include, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_markets_by_game_sportsbook_group(
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
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
            self._with_raw_response.cfb_v3_odds_betting_markets_by_game_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_markets_by_market_type(
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
            self._with_raw_response.cfb_v3_odds_betting_markets_by_market_type(
                event_id, market_type_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_markets_by_market_type_sportsbook_group(
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
            self._with_raw_response.cfb_v3_odds_betting_markets_by_market_type_sportsbook_group(
                event_id,
                market_type_id,
                sportsbookgroup,
                format_=format_,
                include=include,
                request_options=request_options,
            ),
        )

    def cfb_v3_odds_betting_metadata(
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
            self._with_raw_response.cfb_v3_odds_betting_metadata(format_=format_, request_options=request_options)
        )

    def cfb_v3_odds_betting_player_props_by_game(
        self,
        game_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            game_id: The unique GameID of the game in question.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br>
                <b>Important Note:</b> the default parameter of available is much faster and provides the best
                performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be
                several minutes old. For best performance, the default parameter is highly recommended. <br><br>
                Possible values include: <br><br> <code>available</code> - excludes any betting outcomes that have been
                removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster
                than using unlisted. <br><br> <code>unlisted</code> - includes the most recently available betting
                outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise
                unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much
                longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_player_props_by_game(
                game_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        game_id: str,
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
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br>
                <b>Important Note:</b> the default parameter of available is much faster and provides the best
                performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be
                several minutes old. For best performance, the default parameter is highly recommended. <br><br>
                Possible values include: <br><br> <code>available</code> - excludes any betting outcomes that have been
                removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster
                than using unlisted. <br><br> <code>unlisted</code> - includes the most recently available betting
                outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise
                unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much
                longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_player_props_by_game_sportsbook_group(
                game_id, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketResult:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost.

        Args:
            market_id: BettingMarketID of the market for which you would like to see resulted outcomes. Valid example ID
                <code>17819</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_results_by_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_results_by_market_sportsbook_group(
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
            market_id: BettingMarketID of the market for which you would like to see resulted outcomes. Valid example ID
                <code>17819</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_results_by_market_sportsbook_group(
                market_id, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketSplit:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The MarketId of the desired market for which to pull splits.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_splits_by_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_splits_by_game(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> GameBettingSplit2:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            gameid: The ID of the game for which you want to receive splits for. Example <code>11778</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_splits_by_game(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MatchupTrends4:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            opponent: The abbreviation of the requested opponent. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_trends_by_matchup(
                team, opponent, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> TeamTrends2:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_betting_trends_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_in_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_in_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_in_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_in_game_odds_by_week_sportsbook_group(
                season, week, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_in_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo4]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_in_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_in_game_odds_line_movement_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult4]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_period_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_period_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_period_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo4]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_period_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games in a given week and season.
        Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
                season, week, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult4]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. This also includes Resulting: for markets with a ResultType, each line will be
        graded and it will be determined whether the bet would have won or lost. Returns the full line movement for the
        given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_pre_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns full game odds (spread, moneyline, total) for games in a given week and season. Only returns the most
        recently seen odds, not inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_pre_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_pre_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo4]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_pre_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def cfb_v3_odds_sportsbooks_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Sportsbook]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.cfb_v3_odds_sportsbooks_by_active(format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> CfbV3OddsWithRawResponse:
        return self._with_raw_response


class AsyncCfbV3Odds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCfbV3OddsWithRawResponse(client, server, auth)

    async def cfb_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent2]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-10-17</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_events_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent2]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season<br>Examples: <code>2021</code>, <code>2022</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_events_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent2]:
        """Returns available Futures markets for the given season. Does not include line movement.

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
            await self._with_raw_response.cfb_v3_odds_betting_futures_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingEvent2]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_futures_by_season_sportsbook_group(
                season, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_market(
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
            await self._with_raw_response.cfb_v3_odds_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

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
            await self._with_raw_response.cfb_v3_odds_betting_market_sportsbook_group(
                market_id, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_markets_by_event(
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
            await self._with_raw_response.cfb_v3_odds_betting_markets_by_event(
                event_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_markets_by_event_sportsbook_group(
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
            await self._with_raw_response.cfb_v3_odds_betting_markets_by_event_sportsbook_group(
                event_id, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_markets_by_game(
        self,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
            await self._with_raw_response.cfb_v3_odds_betting_markets_by_game(
                gameid, format_=format_, include=include, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_markets_by_game_sportsbook_group(
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
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
            await self._with_raw_response.cfb_v3_odds_betting_markets_by_game_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_markets_by_market_type(
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
            await self._with_raw_response.cfb_v3_odds_betting_markets_by_market_type(
                event_id, market_type_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_markets_by_market_type_sportsbook_group(
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
            await self._with_raw_response.cfb_v3_odds_betting_markets_by_market_type_sportsbook_group(
                event_id,
                market_type_id,
                sportsbookgroup,
                format_=format_,
                include=include,
                request_options=request_options,
            ),
        )

    async def cfb_v3_odds_betting_metadata(
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
            await self._with_raw_response.cfb_v3_odds_betting_metadata(format_=format_, request_options=request_options)
        )

    async def cfb_v3_odds_betting_player_props_by_game(
        self,
        game_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            game_id: The unique GameID of the game in question.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br>
                <b>Important Note:</b> the default parameter of available is much faster and provides the best
                performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be
                several minutes old. For best performance, the default parameter is highly recommended. <br><br>
                Possible values include: <br><br> <code>available</code> - excludes any betting outcomes that have been
                removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster
                than using unlisted. <br><br> <code>unlisted</code> - includes the most recently available betting
                outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise
                unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much
                longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_player_props_by_game(
                game_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        game_id: str,
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
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br>
                <b>Important Note:</b> the default parameter of available is much faster and provides the best
                performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be
                several minutes old. For best performance, the default parameter is highly recommended. <br><br>
                Possible values include: <br><br> <code>available</code> - excludes any betting outcomes that have been
                removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster
                than using unlisted. <br><br> <code>unlisted</code> - includes the most recently available betting
                outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise
                unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much
                longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_player_props_by_game_sportsbook_group(
                game_id, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketResult:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost.

        Args:
            market_id: BettingMarketID of the market for which you would like to see resulted outcomes. Valid example ID
                <code>17819</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_results_by_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_results_by_market_sportsbook_group(
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
            market_id: BettingMarketID of the market for which you would like to see resulted outcomes. Valid example ID
                <code>17819</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_results_by_market_sportsbook_group(
                market_id, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketSplit:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The MarketId of the desired market for which to pull splits.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_splits_by_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_splits_by_game(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> GameBettingSplit2:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            gameid: The ID of the game for which you want to receive splits for. Example <code>11778</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_splits_by_game(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MatchupTrends4:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            opponent: The abbreviation of the requested opponent. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_trends_by_matchup(
                team, opponent, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> TeamTrends2:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_betting_trends_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_in_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_in_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_in_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_in_game_odds_by_week_sportsbook_group(
                season, week, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_in_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo4]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_in_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_in_game_odds_line_movement_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult4]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_period_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_period_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_period_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo4]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_period_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games in a given week and season.
        Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
                season, week, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult4]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. This also includes Resulting: for markets with a ResultType, each line will be
        graded and it will be determined whether the bet would have won or lost. Returns the full line movement for the
        given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
                gameid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_pre_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo4]:
        """Returns full game odds (spread, moneyline, total) for games in a given week and season. Only returns the most
        recently seen odds, not inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_pre_game_odds_by_week(
                season, week, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_pre_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo4]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_pre_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def cfb_v3_odds_sportsbooks_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[Sportsbook]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.cfb_v3_odds_sportsbooks_by_active(
                format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncCfbV3OddsWithRawResponse:
        return self._with_raw_response


class CfbV3OddsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cfb_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent2], CfbV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-10-17</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent2]],
            error_mapper=cfb_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent2], CfbV3OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season<br>Examples: <code>2021</code>, <code>2022</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent2]],
            error_mapper=cfb_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent2], CfbV3OddsBettingFuturesBySeasonErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement.

        Args:
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingFuturesBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent2]],
            error_mapper=cfb_v3_odds_betting_futures_by_season_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingEvent2], CfbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent2]],
            error_mapper=cfb_v3_odds_betting_futures_by_season_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket, CfbV3OddsBettingMarketErrorBody]:
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
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket],
            error_mapper=cfb_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket, CfbV3OddsBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

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
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket],
            error_mapper=cfb_v3_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByEventErrorBody]:
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
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody]:
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
                "/v3/cfb/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_markets_by_game(
        self,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByGameErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMarketsByGameID/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_markets_by_game_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_markets_by_game_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByGameSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
                "/v3/cfb/odds/{format}/BettingMarketsByGameID/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_markets_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByMarketTypeErrorBody]:
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
                "/v3/cfb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
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
                "/v3/cfb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}"
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
            error_mapper=cfb_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection, CfbV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection],
            error_mapper=cfb_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_player_props_by_game(
        self,
        game_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingPlayerPropsByGameErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            game_id: The unique GameID of the game in question.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br>
                <b>Important Note:</b> the default parameter of available is much faster and provides the best
                performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be
                several minutes old. For best performance, the default parameter is highly recommended. <br><br>
                Possible values include: <br><br> <code>available</code> - excludes any betting outcomes that have been
                removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster
                than using unlisted. <br><br> <code>unlisted</code> - includes the most recently available betting
                outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise
                unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much
                longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingPlayerPropsByGameID/{gameId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameId", game_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_player_props_by_game_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        game_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br>
                <b>Important Note:</b> the default parameter of available is much faster and provides the best
                performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be
                several minutes old. For best performance, the default parameter is highly recommended. <br><br>
                Possible values include: <br><br> <code>available</code> - excludes any betting outcomes that have been
                removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster
                than using unlisted. <br><br> <code>unlisted</code> - includes the most recently available betting
                outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise
                unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much
                longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameId", game_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketResult, CfbV3OddsBettingResultsByMarketErrorBody]:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost.

        Args:
            market_id: BettingMarketID of the market for which you would like to see resulted outcomes. Valid example ID
                <code>17819</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMarketResults/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarketResult],
            error_mapper=cfb_v3_odds_betting_results_by_market_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_results_by_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarketResult, CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody]:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost. A Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: BettingMarketID of the market for which you would like to see resulted outcomes. Valid example ID
                <code>17819</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarketResult],
            error_mapper=cfb_v3_odds_betting_results_by_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketSplit, CfbV3OddsBettingSplitsByBettingMarketErrorBody]:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The MarketId of the desired market for which to pull splits.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingSplitsByMarketId/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarketSplit],
            error_mapper=cfb_v3_odds_betting_splits_by_betting_market_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_splits_by_game(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GameBettingSplit2, CfbV3OddsBettingSplitsByGameErrorBody]:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            gameid: The ID of the game for which you want to receive splits for. Example <code>11778</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingSplitsByGameId/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[GameBettingSplit2],
            error_mapper=cfb_v3_odds_betting_splits_by_game_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MatchupTrends4, CfbV3OddsBettingTrendsByMatchupErrorBody]:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            opponent: The abbreviation of the requested opponent. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/MatchupTrends/{team}/{opponent}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("team", team), param[str]("opponent", opponent)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[MatchupTrends4],
            error_mapper=cfb_v3_odds_betting_trends_by_matchup_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamTrends2, CfbV3OddsBettingTrendsByTeamErrorBody]:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/TeamTrends/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TeamTrends2],
            error_mapper=cfb_v3_odds_betting_trends_by_team_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_in_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsInGameOddsByWeekErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/LiveGameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_in_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_in_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsInGameOddsByWeekSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/InGameOddsByWeek/{season}/{week}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_in_game_odds_by_week_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_in_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo4], CfbV3OddsInGameOddsLineMovementErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/LiveGameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_in_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/InGameLineMovement/{gameid}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfoResult4], CfbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/InGameLineMovementWithResulting/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfoResult4]],
            error_mapper=cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_period_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPeriodGameOddsByWeekErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/AlternateMarketGameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_period_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_period_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPeriodGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/AlternateMarketGameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_period_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games in a given week and season.
        Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/PreGameOddsByWeek/{season}/{week}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/PreGameOddsLineMovement/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[GameInfoResult4], CfbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody
    ]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. This also includes Resulting: for markets with a ResultType, each line will be
        graded and it will be determined whether the bet would have won or lost. Returns the full line movement for the
        given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/PreGameOddsLineMovementWithResulting/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfoResult4]],
            error_mapper=cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_pre_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPreGameOddsByWeekErrorBody]:
        """Returns full game odds (spread, moneyline, total) for games in a given week and season. Only returns the most
        recently seen odds, not inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/GameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_pre_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_pre_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPreGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/GameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_pre_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def cfb_v3_odds_sportsbooks_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], CfbV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=cfb_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )


class AsyncCfbV3OddsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cfb_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent2], CfbV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-10-17</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent2]],
            error_mapper=cfb_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent2], CfbV3OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season<br>Examples: <code>2021</code>, <code>2022</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent2]],
            error_mapper=cfb_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent2], CfbV3OddsBettingFuturesBySeasonErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement.

        Args:
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingFuturesBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent2]],
            error_mapper=cfb_v3_odds_betting_futures_by_season_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingEvent2], CfbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent2]],
            error_mapper=cfb_v3_odds_betting_futures_by_season_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket, CfbV3OddsBettingMarketErrorBody]:
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
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarket],
            error_mapper=cfb_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket, CfbV3OddsBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

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
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarket],
            error_mapper=cfb_v3_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByEventErrorBody]:
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
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody]:
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
                "/v3/cfb/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_markets_by_game(
        self,
        gameid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByGameErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMarketsByGameID/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_markets_by_game_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_markets_by_game_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByGameSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
                "/v3/cfb/odds/{format}/BettingMarketsByGameID/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_markets_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByMarketTypeErrorBody]:
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
                "/v3/cfb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
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
                "/v3/cfb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}"
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
            error_mapper=cfb_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection, CfbV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingEntityMetadataCollection],
            error_mapper=cfb_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_player_props_by_game(
        self,
        game_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingPlayerPropsByGameErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            game_id: The unique GameID of the game in question.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br>
                <b>Important Note:</b> the default parameter of available is much faster and provides the best
                performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be
                several minutes old. For best performance, the default parameter is highly recommended. <br><br>
                Possible values include: <br><br> <code>available</code> - excludes any betting outcomes that have been
                removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster
                than using unlisted. <br><br> <code>unlisted</code> - includes the most recently available betting
                outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise
                unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much
                longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingPlayerPropsByGameID/{gameId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameId", game_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_player_props_by_game_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        game_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            game_id: The unique GameID of the game in question.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            include: This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By
                default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br>
                <b>Important Note:</b> the default parameter of available is much faster and provides the best
                performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be
                several minutes old. For best performance, the default parameter is highly recommended. <br><br>
                Possible values include: <br><br> <code>available</code> - excludes any betting outcomes that have been
                removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster
                than using unlisted. <br><br> <code>unlisted</code> - includes the most recently available betting
                outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise
                unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much
                longer than available. <br><br>
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameId", game_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=cfb_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketResult, CfbV3OddsBettingResultsByMarketErrorBody]:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost.

        Args:
            market_id: BettingMarketID of the market for which you would like to see resulted outcomes. Valid example ID
                <code>17819</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingMarketResults/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarketResult],
            error_mapper=cfb_v3_odds_betting_results_by_market_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_results_by_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarketResult, CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody]:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost. A Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: BettingMarketID of the market for which you would like to see resulted outcomes. Valid example ID
                <code>17819</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarketResult],
            error_mapper=cfb_v3_odds_betting_results_by_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketSplit, CfbV3OddsBettingSplitsByBettingMarketErrorBody]:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The MarketId of the desired market for which to pull splits.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingSplitsByMarketId/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarketSplit],
            error_mapper=cfb_v3_odds_betting_splits_by_betting_market_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_splits_by_game(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GameBettingSplit2, CfbV3OddsBettingSplitsByGameErrorBody]:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            gameid: The ID of the game for which you want to receive splits for. Example <code>11778</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/BettingSplitsByGameId/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[GameBettingSplit2],
            error_mapper=cfb_v3_odds_betting_splits_by_game_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MatchupTrends4, CfbV3OddsBettingTrendsByMatchupErrorBody]:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            opponent: The abbreviation of the requested opponent. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/MatchupTrends/{team}/{opponent}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("team", team), param[str]("opponent", opponent)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[MatchupTrends4],
            error_mapper=cfb_v3_odds_betting_trends_by_matchup_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamTrends2, CfbV3OddsBettingTrendsByTeamErrorBody]:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>MIA</code>, <code>ND</code>,
                <code>PITT</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/TeamTrends/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TeamTrends2],
            error_mapper=cfb_v3_odds_betting_trends_by_team_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_in_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsInGameOddsByWeekErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/LiveGameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_in_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_in_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsInGameOddsByWeekSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Only returns the
        most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while
        the game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/InGameOddsByWeek/{season}/{week}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_in_game_odds_by_week_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_in_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo4], CfbV3OddsInGameOddsLineMovementErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/LiveGameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_in_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/InGameLineMovement/{gameid}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfoResult4], CfbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/InGameLineMovementWithResulting/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfoResult4]],
            error_mapper=cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_period_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPeriodGameOddsByWeekErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Only returns the most recently seen odds, not
        inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/AlternateMarketGameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_period_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_period_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPeriodGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/AlternateMarketGameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_period_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(
        self,
        season: str,
        week: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games in a given week and season.
        Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/PreGameOddsByWeek/{season}/{week}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("week", week),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/PreGameOddsLineMovement/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[GameInfoResult4], CfbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody
    ]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. This also includes Resulting: for markets with a ResultType, each line will be
        graded and it will be determined whether the bet would have won or lost. Returns the full line movement for the
        given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/cfb/odds/{format}/PreGameOddsLineMovementWithResulting/{gameid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfoResult4]],
            error_mapper=cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_pre_game_odds_by_week(
        self,
        season: str,
        week: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPreGameOddsByWeekErrorBody]:
        """Returns full game odds (spread, moneyline, total) for games in a given week and season. Only returns the most
        recently seen odds, not inclusive of line movement.

        Args:
            season: Year of the season, with optional season type. <br>Examples: <code>2018</code>,
                <code>2018POST</code>, etc.
            week: The week of the game(s). <br>Examples: <code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/GameOddsByWeek/{season}/{week}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season), param[str]("week", week)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_pre_game_odds_by_week_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_pre_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo4], CfbV3OddsPreGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an CFB game. GameIDs can be found in the Games API. Valid entries are
                <code>8487</code> or <code>8657</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/GameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo4]],
            error_mapper=cfb_v3_odds_pre_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def cfb_v3_odds_sportsbooks_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], CfbV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/cfb/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Sportsbook]],
            error_mapper=cfb_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )
