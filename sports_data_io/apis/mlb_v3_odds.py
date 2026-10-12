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
from ..errors.mlb_v3_odds_betting_events_by_date_error import (
    MlbV3OddsBettingEventsByDateErrorBody,
    mlb_v3_odds_betting_events_by_date_error_mapper,
)
from ..errors.mlb_v3_odds_betting_events_by_season_error import (
    MlbV3OddsBettingEventsBySeasonErrorBody,
    mlb_v3_odds_betting_events_by_season_error_mapper,
)
from ..errors.mlb_v3_odds_betting_futures_by_season_error import (
    MlbV3OddsBettingFuturesBySeasonErrorBody,
    mlb_v3_odds_betting_futures_by_season_error_mapper,
)
from ..errors.mlb_v3_odds_betting_futures_by_season_sportsbook_group_error import (
    MlbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody,
    mlb_v3_odds_betting_futures_by_season_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_betting_market_error import (
    MlbV3OddsBettingMarketErrorBody,
    mlb_v3_odds_betting_market_error_mapper,
)
from ..errors.mlb_v3_odds_betting_market_sportsbook_group_error import (
    MlbV3OddsBettingMarketSportsbookGroupErrorBody,
    mlb_v3_odds_betting_market_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_betting_markets_by_event_error import (
    MlbV3OddsBettingMarketsByEventErrorBody,
    mlb_v3_odds_betting_markets_by_event_error_mapper,
)
from ..errors.mlb_v3_odds_betting_markets_by_event_sportsbook_group_error import (
    MlbV3OddsBettingMarketsByEventSportsbookGroupErrorBody,
    mlb_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_betting_markets_by_game_error import (
    MlbV3OddsBettingMarketsByGameErrorBody,
    mlb_v3_odds_betting_markets_by_game_error_mapper,
)
from ..errors.mlb_v3_odds_betting_markets_by_game_sportsbook_group_error import (
    MlbV3OddsBettingMarketsByGameSportsbookGroupErrorBody,
    mlb_v3_odds_betting_markets_by_game_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_betting_markets_by_market_type_error import (
    MlbV3OddsBettingMarketsByMarketTypeErrorBody,
    mlb_v3_odds_betting_markets_by_market_type_error_mapper,
)
from ..errors.mlb_v3_odds_betting_markets_by_market_type_sportsbook_group_error import (
    MlbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody,
    mlb_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_betting_metadata_error import (
    MlbV3OddsBettingMetadataErrorBody,
    mlb_v3_odds_betting_metadata_error_mapper,
)
from ..errors.mlb_v3_odds_betting_player_props_by_game_error import (
    MlbV3OddsBettingPlayerPropsByGameErrorBody,
    mlb_v3_odds_betting_player_props_by_game_error_mapper,
)
from ..errors.mlb_v3_odds_betting_player_props_by_game_sportsbook_group_error import (
    MlbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody,
    mlb_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_betting_results_by_market_error import (
    MlbV3OddsBettingResultsByMarketErrorBody,
    mlb_v3_odds_betting_results_by_market_error_mapper,
)
from ..errors.mlb_v3_odds_betting_results_by_market_sportsbook_group_error import (
    MlbV3OddsBettingResultsByMarketSportsbookGroupErrorBody,
    mlb_v3_odds_betting_results_by_market_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_betting_splits_by_betting_market_error import (
    MlbV3OddsBettingSplitsByBettingMarketErrorBody,
    mlb_v3_odds_betting_splits_by_betting_market_error_mapper,
)
from ..errors.mlb_v3_odds_betting_splits_by_game_error import (
    MlbV3OddsBettingSplitsByGameErrorBody,
    mlb_v3_odds_betting_splits_by_game_error_mapper,
)
from ..errors.mlb_v3_odds_betting_trends_by_matchup_error import (
    MlbV3OddsBettingTrendsByMatchupErrorBody,
    mlb_v3_odds_betting_trends_by_matchup_error_mapper,
)
from ..errors.mlb_v3_odds_betting_trends_by_team_error import (
    MlbV3OddsBettingTrendsByTeamErrorBody,
    mlb_v3_odds_betting_trends_by_team_error_mapper,
)
from ..errors.mlb_v3_odds_in_game_odds_by_date_error import (
    MlbV3OddsInGameOddsByDateErrorBody,
    mlb_v3_odds_in_game_odds_by_date_error_mapper,
)
from ..errors.mlb_v3_odds_in_game_odds_by_date_sportsbook_group_error import (
    MlbV3OddsInGameOddsByDateSportsbookGroupErrorBody,
    mlb_v3_odds_in_game_odds_by_date_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_in_game_odds_line_movement_error import (
    MlbV3OddsInGameOddsLineMovementErrorBody,
    mlb_v3_odds_in_game_odds_line_movement_error_mapper,
)
from ..errors.mlb_v3_odds_in_game_odds_line_movement_sportsbook_group_error import (
    MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody,
    mlb_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error import (
    MlbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody,
    mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_period_game_odds_by_date_error import (
    MlbV3OddsPeriodGameOddsByDateErrorBody,
    mlb_v3_odds_period_game_odds_by_date_error_mapper,
)
from ..errors.mlb_v3_odds_period_game_odds_line_movement_error import (
    MlbV3OddsPeriodGameOddsLineMovementErrorBody,
    mlb_v3_odds_period_game_odds_line_movement_error_mapper,
)
from ..errors.mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error import (
    MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody,
    mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error import (
    MlbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody,
    mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error import (
    MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody,
    mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
)
from ..errors.mlb_v3_odds_pre_game_odds_by_date_error import (
    MlbV3OddsPreGameOddsByDateErrorBody,
    mlb_v3_odds_pre_game_odds_by_date_error_mapper,
)
from ..errors.mlb_v3_odds_pre_game_odds_line_movement_error import (
    MlbV3OddsPreGameOddsLineMovementErrorBody,
    mlb_v3_odds_pre_game_odds_line_movement_error_mapper,
)
from ..errors.mlb_v3_odds_sportsbooks_by_active_error import (
    MlbV3OddsSportsbooksByActiveErrorBody,
    mlb_v3_odds_sportsbooks_by_active_error_mapper,
)
from ..models.betting_entity_metadata_collection import BettingEntityMetadataCollection
from ..models.betting_event1 import BettingEvent1
from ..models.betting_market import BettingMarket
from ..models.betting_market_result import BettingMarketResult
from ..models.betting_market_split import BettingMarketSplit
from ..models.enums.format import Format, FormatOrStr
from ..models.enums.include import Include, IncludeOrStr
from ..models.game_betting_split1 import GameBettingSplit1
from ..models.game_info2 import GameInfo2
from ..models.game_info_result2 import GameInfoResult2
from ..models.matchup_trends2 import MatchupTrends2
from ..models.sportsbook import Sportsbook
from ..models.team_trends1 import TeamTrends1
from ..server.server import Server


class MlbV3Odds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MlbV3OddsWithRawResponse(client, server, auth)

    def mlb_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-08-20</code>, <code>2020-08-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_betting_events_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_betting_events_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """Returns available Futures markets for the given season. Does not include line movement.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_betting_futures_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingEvent1]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_betting_futures_by_season_sportsbook_group(
                season, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_market(
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
            self._with_raw_response.mlb_v3_odds_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            self._with_raw_response.mlb_v3_odds_betting_market_sportsbook_group(
                market_id, sportsbook_group, format_=format_, include=include, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_markets_by_event(
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
            self._with_raw_response.mlb_v3_odds_betting_markets_by_event(
                event_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbook_group: str,
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
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            self._with_raw_response.mlb_v3_odds_betting_markets_by_event_sportsbook_group(
                event_id, sportsbook_group, format_=format_, include=include, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_markets_by_game(
        self,
        game_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
            self._with_raw_response.mlb_v3_odds_betting_markets_by_game(
                game_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_markets_by_game_sportsbook_group(
        self,
        game_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            self._with_raw_response.mlb_v3_odds_betting_markets_by_game_sportsbook_group(
                game_id, sportsbook_group, format_=format_, include=include, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_markets_by_market_type(
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
            self._with_raw_response.mlb_v3_odds_betting_markets_by_market_type(
                event_id, market_type_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbook_group: str,
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
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            self._with_raw_response.mlb_v3_odds_betting_markets_by_market_type_sportsbook_group(
                event_id,
                market_type_id,
                sportsbook_group,
                format_=format_,
                include=include,
                request_options=request_options,
            ),
        )

    def mlb_v3_odds_betting_metadata(
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
            self._with_raw_response.mlb_v3_odds_betting_metadata(format_=format_, request_options=request_options)
        )

    def mlb_v3_odds_betting_player_props_by_game(
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
            self._with_raw_response.mlb_v3_odds_betting_player_props_by_game(
                game_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        game_id: str,
        sportsbook_group: str,
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
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            self._with_raw_response.mlb_v3_odds_betting_player_props_by_game_sportsbook_group(
                game_id, sportsbook_group, format_=format_, include=include, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketResult:
        """Returns all outcomes under this market which have a result type associated. Will return empty list if
        resulting has not yet processed for the given game. Resulting processes shortly after game closing.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid IDs include
                <code>837872</code>, <code>841068</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_betting_results_by_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_results_by_market_sportsbook_group(
        self,
        market_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarketResult:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost. A Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid IDs include
                <code>837872</code>, <code>841068</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_betting_results_by_market_sportsbook_group(
                market_id, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_splits_by_game(
        self, game_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> GameBettingSplit1:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            game_id: The ID of the game for which you want to receive splits for. Example <code>63266</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_betting_splits_by_game(
                game_id, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketSplit:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The MarketId of the desired market for which to pull splits.. Valid IDs include
                <code>837872</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_betting_splits_by_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MatchupTrends2:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            opponent: The abbreviation of the requested opponent. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_betting_trends_by_matchup(
                team, opponent, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> TeamTrends1:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_betting_trends_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_in_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Only returns the most
        recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while the
        game is in progress.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_in_game_odds_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_in_game_odds_by_date_sportsbook_group(
        self,
        date: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo2]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Only returns the most
        recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while the
        game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_in_game_odds_by_date_sportsbook_group(
                date, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_in_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_in_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo2]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_in_game_odds_line_movement_sportsbook_group(
                gameid, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult2]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
                gameid, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_period_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        first five innings, for example, rather than full game. Only returns the most recently seen odds, not inclusive
        of line movement.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_period_game_odds_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_period_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        first five innings, for example, rather than full game. Returns the full line movement for the given game. This
        endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the
        second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_period_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
        self,
        date: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo2]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games on a given date. Only
        returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified as a
        URL parameter.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
                date, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo2]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
                gameid, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult2]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. This also includes Resulting: for markets with a ResultType, each line will be
        graded and it will be determined whether the bet would have won or lost. Returns the full line movement for the
        given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
                gameid, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_pre_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns full game odds (spread, moneyline, total) for games on a given date. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_pre_game_odds_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_pre_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.mlb_v3_odds_pre_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    def mlb_v3_odds_sportsbooks_by_active(
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
            self._with_raw_response.mlb_v3_odds_sportsbooks_by_active(format_=format_, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> MlbV3OddsWithRawResponse:
        return self._with_raw_response


class AsyncMlbV3Odds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMlbV3OddsWithRawResponse(client, server, auth)

    async def mlb_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-08-20</code>, <code>2020-08-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_betting_events_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_betting_events_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """Returns available Futures markets for the given season. Does not include line movement.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_betting_futures_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingEvent1]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_betting_futures_by_season_sportsbook_group(
                season, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_market(
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
            await self._with_raw_response.mlb_v3_odds_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            await self._with_raw_response.mlb_v3_odds_betting_market_sportsbook_group(
                market_id, sportsbook_group, format_=format_, include=include, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_markets_by_event(
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
            await self._with_raw_response.mlb_v3_odds_betting_markets_by_event(
                event_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbook_group: str,
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
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            await self._with_raw_response.mlb_v3_odds_betting_markets_by_event_sportsbook_group(
                event_id, sportsbook_group, format_=format_, include=include, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_markets_by_game(
        self,
        game_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
            await self._with_raw_response.mlb_v3_odds_betting_markets_by_game(
                game_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_markets_by_game_sportsbook_group(
        self,
        game_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            await self._with_raw_response.mlb_v3_odds_betting_markets_by_game_sportsbook_group(
                game_id, sportsbook_group, format_=format_, include=include, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_markets_by_market_type(
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
            await self._with_raw_response.mlb_v3_odds_betting_markets_by_market_type(
                event_id, market_type_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbook_group: str,
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
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            await self._with_raw_response.mlb_v3_odds_betting_markets_by_market_type_sportsbook_group(
                event_id,
                market_type_id,
                sportsbook_group,
                format_=format_,
                include=include,
                request_options=request_options,
            ),
        )

    async def mlb_v3_odds_betting_metadata(
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
            await self._with_raw_response.mlb_v3_odds_betting_metadata(format_=format_, request_options=request_options)
        )

    async def mlb_v3_odds_betting_player_props_by_game(
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
            await self._with_raw_response.mlb_v3_odds_betting_player_props_by_game(
                game_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        game_id: str,
        sportsbook_group: str,
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
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            await self._with_raw_response.mlb_v3_odds_betting_player_props_by_game_sportsbook_group(
                game_id, sportsbook_group, format_=format_, include=include, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketResult:
        """Returns all outcomes under this market which have a result type associated. Will return empty list if
        resulting has not yet processed for the given game. Resulting processes shortly after game closing.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid IDs include
                <code>837872</code>, <code>841068</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_betting_results_by_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_results_by_market_sportsbook_group(
        self,
        market_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarketResult:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost. A Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid IDs include
                <code>837872</code>, <code>841068</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_betting_results_by_market_sportsbook_group(
                market_id, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_splits_by_game(
        self, game_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> GameBettingSplit1:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            game_id: The ID of the game for which you want to receive splits for. Example <code>63266</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_betting_splits_by_game(
                game_id, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarketSplit:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The MarketId of the desired market for which to pull splits.. Valid IDs include
                <code>837872</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_betting_splits_by_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MatchupTrends2:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            opponent: The abbreviation of the requested opponent. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_betting_trends_by_matchup(
                team, opponent, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> TeamTrends1:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_betting_trends_by_team(
                team, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_in_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Only returns the most
        recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while the
        game is in progress.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_in_game_odds_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_in_game_odds_by_date_sportsbook_group(
        self,
        date: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo2]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Only returns the most
        recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while the
        game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_in_game_odds_by_date_sportsbook_group(
                date, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_in_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_in_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo2]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_in_game_odds_line_movement_sportsbook_group(
                gameid, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult2]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
                gameid, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_period_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        first five innings, for example, rather than full game. Only returns the most recently seen odds, not inclusive
        of line movement.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_period_game_odds_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_period_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        first five innings, for example, rather than full game. Returns the full line movement for the given game. This
        endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the
        second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_period_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
        self,
        date: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo2]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games on a given date. Only
        returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified as a
        URL parameter.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
                date, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfo2]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
                gameid, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[GameInfoResult2]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. This also includes Resulting: for markets with a ResultType, each line will be
        graded and it will be determined whether the bet would have won or lost. Returns the full line movement for the
        given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
                gameid, sportsbook_group, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_pre_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns full game odds (spread, moneyline, total) for games on a given date. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_pre_game_odds_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_pre_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[GameInfo2]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.mlb_v3_odds_pre_game_odds_line_movement(
                gameid, format_=format_, request_options=request_options
            ),
        )

    async def mlb_v3_odds_sportsbooks_by_active(
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
            await self._with_raw_response.mlb_v3_odds_sportsbooks_by_active(
                format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncMlbV3OddsWithRawResponse:
        return self._with_raw_response


class MlbV3OddsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def mlb_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], MlbV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-08-20</code>, <code>2020-08-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=mlb_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], MlbV3OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=mlb_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], MlbV3OddsBettingFuturesBySeasonErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingFuturesBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=mlb_v3_odds_betting_futures_by_season_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingEvent1], MlbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=mlb_v3_odds_betting_futures_by_season_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket, MlbV3OddsBettingMarketErrorBody]:
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket],
            error_mapper=mlb_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket, MlbV3OddsBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMarket/{marketId}/{sportsbookGroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket],
            error_mapper=mlb_v3_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByEventErrorBody]:
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByEventSportsbookGroupErrorBody]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
                "/v3/mlb/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_markets_by_game(
        self,
        game_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByGameErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMarketsByGameID/{gameID}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameID", game_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_game_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_markets_by_game_sportsbook_group(
        self,
        game_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByGameSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
                "/v3/mlb/odds/{format}/BettingMarketsByGameID/{gameID}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameID", game_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByMarketTypeErrorBody]:
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
                "/v3/mlb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
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
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
                "/v3/mlb/odds/{format}/BettingMarketsByMarketType/{eventID}/{marketTypeID}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventID", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection, MlbV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection],
            error_mapper=mlb_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_player_props_by_game(
        self,
        game_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingPlayerPropsByGameErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            game_id: The unique GameID of the game in question.
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingPlayerPropsByGameID/{gameId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameId", game_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_player_props_by_game_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        game_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            game_id: The unique GameID of the game in question.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
                "/v3/mlb/odds/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameId", game_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketResult, MlbV3OddsBettingResultsByMarketErrorBody]:
        """Returns all outcomes under this market which have a result type associated. Will return empty list if
        resulting has not yet processed for the given game. Resulting processes shortly after game closing.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid IDs include
                <code>837872</code>, <code>841068</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMarketResults/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarketResult],
            error_mapper=mlb_v3_odds_betting_results_by_market_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_results_by_market_sportsbook_group(
        self,
        market_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarketResult, MlbV3OddsBettingResultsByMarketSportsbookGroupErrorBody]:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost. A Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid IDs include
                <code>837872</code>, <code>841068</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/BettingResultsByMarket/{marketID}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketID", market_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarketResult],
            error_mapper=mlb_v3_odds_betting_results_by_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_splits_by_game(
        self, game_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GameBettingSplit1, MlbV3OddsBettingSplitsByGameErrorBody]:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            game_id: The ID of the game for which you want to receive splits for. Example <code>63266</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingSplitsByGameId/{gameId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameId", game_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[GameBettingSplit1],
            error_mapper=mlb_v3_odds_betting_splits_by_game_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketSplit, MlbV3OddsBettingSplitsByBettingMarketErrorBody]:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The MarketId of the desired market for which to pull splits.. Valid IDs include
                <code>837872</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingSplitsByMarketId/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarketSplit],
            error_mapper=mlb_v3_odds_betting_splits_by_betting_market_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MatchupTrends2, MlbV3OddsBettingTrendsByMatchupErrorBody]:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            opponent: The abbreviation of the requested opponent. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/MatchupTrends/{team}/{opponent}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("team", team), param[str]("opponent", opponent)
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[MatchupTrends2],
            error_mapper=mlb_v3_odds_betting_trends_by_matchup_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamTrends1, MlbV3OddsBettingTrendsByTeamErrorBody]:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/TeamTrends/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TeamTrends1],
            error_mapper=mlb_v3_odds_betting_trends_by_team_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_in_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsInGameOddsByDateErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Only returns the most
        recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while the
        game is in progress.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/LiveGameOddsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_in_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_in_game_odds_by_date_sportsbook_group(
        self,
        date: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo2], MlbV3OddsInGameOddsByDateSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Only returns the most
        recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while the
        game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/InGameOddsByDate/{date}/{sportsbookGroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("date", date),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_in_game_odds_by_date_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_in_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsInGameOddsLineMovementErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/LiveGameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_in_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo2], MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/InGameOddsLineMovement/{gameid}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfoResult2], MlbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/InGameOddsLineMovementWithResulting/{gameid}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfoResult2]],
            error_mapper=mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_period_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPeriodGameOddsByDateErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        first five innings, for example, rather than full game. Only returns the most recently seen odds, not inclusive
        of line movement.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/AlternateMarketGameOddsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_period_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_period_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPeriodGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        first five innings, for example, rather than full game. Returns the full line movement for the given game. This
        endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the
        second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/AlternateMarketGameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_period_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
        self,
        date: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games on a given date. Only
        returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified as a
        URL parameter.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/PreGameOddsByDate/{date}/{sportsbookGroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("date", date),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/PreGameOddsLineMovement/{gameid}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[GameInfoResult2], MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody
    ]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. This also includes Resulting: for markets with a ResultType, each line will be
        graded and it will be determined whether the bet would have won or lost. Returns the full line movement for the
        given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/PreGameOddsLineMovementWithResulting/{gameid}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfoResult2]],
            error_mapper=mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_pre_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPreGameOddsByDateErrorBody]:
        """Returns full game odds (spread, moneyline, total) for games on a given date. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/GameOddsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_pre_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_pre_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPreGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/GameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_pre_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def mlb_v3_odds_sportsbooks_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], MlbV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=mlb_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )


class AsyncMlbV3OddsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def mlb_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], MlbV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the game(s). <br>Examples: <code>2020-08-20</code>, <code>2020-08-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent1]],
            error_mapper=mlb_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], MlbV3OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent1]],
            error_mapper=mlb_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_futures_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], MlbV3OddsBettingFuturesBySeasonErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingFuturesBySeason/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent1]],
            error_mapper=mlb_v3_odds_betting_futures_by_season_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_futures_by_season_sportsbook_group(
        self,
        season: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingEvent1], MlbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]:
        """Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            season: Year of the season (with optional season type).<br>Examples: <code>2020</code>,
                <code>2020PRE</code>, <code>2020POST</code>, <code>2020STAR</code>, <code>2021</code>, etc.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("season", season),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent1]],
            error_mapper=mlb_v3_odds_betting_futures_by_season_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket, MlbV3OddsBettingMarketErrorBody]:
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarket],
            error_mapper=mlb_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket, MlbV3OddsBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMarket/{marketId}/{sportsbookGroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarket],
            error_mapper=mlb_v3_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByEventErrorBody]:
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByEventSportsbookGroupErrorBody]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
                "/v3/mlb/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_markets_by_game(
        self,
        game_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByGameErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID.

        Args:
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMarketsByGameID/{gameID}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameID", game_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_game_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_markets_by_game_sportsbook_group(
        self,
        game_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByGameSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        GameID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            game_id: The GameID of the desired game for which to pull all betting markets (includes outcomes/bets).
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
                "/v3/mlb/odds/{format}/BettingMarketsByGameID/{gameID}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameID", game_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByMarketTypeErrorBody]:
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
                "/v3/mlb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
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
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
                "/v3/mlb/odds/{format}/BettingMarketsByMarketType/{eventID}/{marketTypeID}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventID", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection, MlbV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingEntityMetadataCollection],
            error_mapper=mlb_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_player_props_by_game(
        self,
        game_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingPlayerPropsByGameErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint.

        Args:
            game_id: The unique GameID of the game in question.
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
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingPlayerPropsByGameID/{gameId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameId", game_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_player_props_by_game_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_player_props_by_game_sportsbook_group(
        self,
        game_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket], MlbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is
        recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

        Args:
            game_id: The unique GameID of the game in question.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
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
                "/v3/mlb/odds/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameId", game_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket]],
            error_mapper=mlb_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_results_by_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketResult, MlbV3OddsBettingResultsByMarketErrorBody]:
        """Returns all outcomes under this market which have a result type associated. Will return empty list if
        resulting has not yet processed for the given game. Resulting processes shortly after game closing.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid IDs include
                <code>837872</code>, <code>841068</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingMarketResults/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarketResult],
            error_mapper=mlb_v3_odds_betting_results_by_market_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_results_by_market_sportsbook_group(
        self,
        market_id: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarketResult, MlbV3OddsBettingResultsByMarketSportsbookGroupErrorBody]:
        """Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result:
        for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won
        or lost. A Sportsbook Group must be specified as a URL parameter.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets. Valid IDs include
                <code>837872</code>, <code>841068</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/BettingResultsByMarket/{marketID}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketID", market_id),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarketResult],
            error_mapper=mlb_v3_odds_betting_results_by_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_splits_by_game(
        self, game_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GameBettingSplit1, MlbV3OddsBettingSplitsByGameErrorBody]:
        """List of Money and Bet Percentage splits for each market and their respective outcome types available in this
        game. This specific endpoint will return current splits for each available market and no line movement.

        Args:
            game_id: The ID of the game for which you want to receive splits for. Example <code>63266</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingSplitsByGameId/{gameId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameId", game_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[GameBettingSplit1],
            error_mapper=mlb_v3_odds_betting_splits_by_game_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_splits_by_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarketSplit, MlbV3OddsBettingSplitsByBettingMarketErrorBody]:
        """List of Money and Bet Percentage splits for each outcome type available in this market. This specific
        endpoint will return the movement from this market as well as the most recent.

        Args:
            market_id: The MarketId of the desired market for which to pull splits.. Valid IDs include
                <code>837872</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/BettingSplitsByMarketId/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarketSplit],
            error_mapper=mlb_v3_odds_betting_splits_by_betting_market_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_trends_by_matchup(
        self,
        team: str,
        opponent: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MatchupTrends2, MlbV3OddsBettingTrendsByMatchupErrorBody]:
        """Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this
        season. Intended for use on a specific game, though it will work for other comparisons if applicable.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            opponent: The abbreviation of the requested opponent. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/MatchupTrends/{team}/{opponent}"),
            path_params=[
                param[FormatOrStr]("format", format_), param[str]("team", team), param[str]("opponent", opponent)
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[MatchupTrends2],
            error_mapper=mlb_v3_odds_betting_trends_by_matchup_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_betting_trends_by_team(
        self, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TeamTrends1, MlbV3OddsBettingTrendsByTeamErrorBody]:
        """Describes recent team trends and performance against betting data in recent sets of games.

        Args:
            team: The abbreviation of the requested team. <br> Examples: <code>PHI</code>, <code>MIN</code>,
                <code>DET</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/TeamTrends/{team}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("team", team)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TeamTrends1],
            error_mapper=mlb_v3_odds_betting_trends_by_team_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_in_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsInGameOddsByDateErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Only returns the most
        recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while the
        game is in progress.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/LiveGameOddsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_in_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_in_game_odds_by_date_sportsbook_group(
        self,
        date: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo2], MlbV3OddsInGameOddsByDateSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Only returns the most
        recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while the
        game is in progress. A Sportsbook Group must be specified as a URL parameter.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/InGameOddsByDate/{date}/{sportsbookGroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("date", date),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_in_game_odds_by_date_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_in_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsInGameOddsLineMovementErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games on a given date. Returns the full line
        movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement
        rather than the most up to the second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/LiveGameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_in_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_in_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo2], MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. Returns the full
        line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line
        movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/InGameOddsLineMovement/{gameid}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_in_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfoResult2], MlbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]:
        """Returns in-play game odds (spread, moneyline, total) for games in a given week and season. This also includes
        Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet
        would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as
        it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group
        must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/InGameOddsLineMovementWithResulting/{gameid}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfoResult2]],
            error_mapper=mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_period_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPeriodGameOddsByDateErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        first five innings, for example, rather than full game. Only returns the most recently seen odds, not inclusive
        of line movement.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/AlternateMarketGameOddsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_period_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_period_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPeriodGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games on a given date. Non-full-game means
        first five innings, for example, rather than full game. Returns the full line movement for the given game. This
        endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the
        second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/AlternateMarketGameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_period_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
        self,
        date: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]:
        """Returns the full-game and non-full-game odds (spread, moneyline, total) for games on a given date. Only
        returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified as a
        URL parameter.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/PreGameOddsByDate/{date}/{sportsbookGroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("date", date),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer
        cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/PreGameOddsLineMovement/{gameid}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
        self,
        gameid: str,
        sportsbook_group: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        list[GameInfoResult2], MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody
    ]:
        """Returns the game odds ( for games in a given week and season. In this endpoint both full-game and
        partial-game odds are included. This also includes Resulting: for markets with a ResultType, each line will be
        graded and it will be determined whether the bet would have won or lost. Returns the full line movement for the
        given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line. A Sportsbook Group must be specified as a URL parameter.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            sportsbook_group: The name of the sportsbook group that will filter outcomes.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/mlb/odds/{format}/PreGameOddsLineMovementWithResulting/{gameid}/{sportsbookGroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("gameid", gameid),
                param[str]("sportsbookGroup", sportsbook_group),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfoResult2]],
            error_mapper=mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_pre_game_odds_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPreGameOddsByDateErrorBody]:
        """Returns full game odds (spread, moneyline, total) for games on a given date. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            date: The date of the game(s). <br>Examples: <code>2018-06-20</code>, <code>2018-06-23</code>.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/GameOddsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_pre_game_odds_by_date_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_pre_game_odds_line_movement(
        self, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[GameInfo2], MlbV3OddsPreGameOddsLineMovementErrorBody]:
        """Returns the non-full-game odds (spread, moneyline, total) for games in a given week and season. Non-full-game
        means 1st-half or 1st-quarter, for example, rather than full game. Returns the full line movement for the given
        game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up
        to the second line.

        Args:
            gameid: The GameID of an MLB game. GameIDs can be found in the Games API. Valid entries are
                <code>51735</code> or <code>51745</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/GameOddsLineMovement/{gameid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("gameid", gameid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[GameInfo2]],
            error_mapper=mlb_v3_odds_pre_game_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def mlb_v3_odds_sportsbooks_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], MlbV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mlb/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Sportsbook]],
            error_mapper=mlb_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )
