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
from ..errors.golf_v3_odds_betting_events_by_date_error import (
    GolfV3OddsBettingEventsByDateErrorBody,
    golf_v3_odds_betting_events_by_date_error_mapper,
)
from ..errors.golf_v3_odds_betting_events_by_season_error import (
    GolfV3OddsBettingEventsBySeasonErrorBody,
    golf_v3_odds_betting_events_by_season_error_mapper,
)
from ..errors.golf_v3_odds_betting_market_error import (
    GolfV3OddsBettingMarketErrorBody,
    golf_v3_odds_betting_market_error_mapper,
)
from ..errors.golf_v3_odds_betting_market_sportsbook_group_error import (
    GolfV3OddsBettingMarketSportsbookGroupErrorBody,
    golf_v3_odds_betting_market_sportsbook_group_error_mapper,
)
from ..errors.golf_v3_odds_betting_markets_by_event_error import (
    GolfV3OddsBettingMarketsByEventErrorBody,
    golf_v3_odds_betting_markets_by_event_error_mapper,
)
from ..errors.golf_v3_odds_betting_markets_by_event_sportsbook_group_error import (
    GolfV3OddsBettingMarketsByEventSportsbookGroupErrorBody,
    golf_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
)
from ..errors.golf_v3_odds_betting_markets_by_market_type_error import (
    GolfV3OddsBettingMarketsByMarketTypeErrorBody,
    golf_v3_odds_betting_markets_by_market_type_error_mapper,
)
from ..errors.golf_v3_odds_betting_markets_by_market_type_sportsbook_group_error import (
    GolfV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody,
    golf_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
)
from ..errors.golf_v3_odds_betting_markets_by_tournament_error import (
    GolfV3OddsBettingMarketsByTournamentErrorBody,
    golf_v3_odds_betting_markets_by_tournament_error_mapper,
)
from ..errors.golf_v3_odds_betting_markets_by_tournament_sportsbook_group_error import (
    GolfV3OddsBettingMarketsByTournamentSportsbookGroupErrorBody,
    golf_v3_odds_betting_markets_by_tournament_sportsbook_group_error_mapper,
)
from ..errors.golf_v3_odds_betting_metadata_error import (
    GolfV3OddsBettingMetadataErrorBody,
    golf_v3_odds_betting_metadata_error_mapper,
)
from ..errors.golf_v3_odds_betting_player_props_by_tournament_sportsbook_group_error import (
    GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody,
    golf_v3_odds_betting_player_props_by_tournament_sportsbook_group_error_mapper,
)
from ..errors.golf_v3_odds_in_play_tournament_odds_error import (
    GolfV3OddsInPlayTournamentOddsErrorBody,
    golf_v3_odds_in_play_tournament_odds_error_mapper,
)
from ..errors.golf_v3_odds_in_play_tournament_odds_line_movement_error import (
    GolfV3OddsInPlayTournamentOddsLineMovementErrorBody,
    golf_v3_odds_in_play_tournament_odds_line_movement_error_mapper,
)
from ..errors.golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group_error import (
    GolfV3OddsInPlayTournamentOddsLineMovementSportsbookGroupErrorBody,
    golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group_error_mapper,
)
from ..errors.golf_v3_odds_in_play_tournament_odds_sportsbook_group_error import (
    GolfV3OddsInPlayTournamentOddsSportsbookGroupErrorBody,
    golf_v3_odds_in_play_tournament_odds_sportsbook_group_error_mapper,
)
from ..errors.golf_v3_odds_sportsbooks_by_active_error import (
    GolfV3OddsSportsbooksByActiveErrorBody,
    golf_v3_odds_sportsbooks_by_active_error_mapper,
)
from ..errors.golf_v3_odds_tournament_odds_error import (
    GolfV3OddsTournamentOddsErrorBody,
    golf_v3_odds_tournament_odds_error_mapper,
)
from ..errors.golf_v3_odds_tournament_odds_line_movement_error import (
    GolfV3OddsTournamentOddsLineMovementErrorBody,
    golf_v3_odds_tournament_odds_line_movement_error_mapper,
)
from ..errors.golf_v3_odds_tournament_odds_line_movement_sportsbook_group_error import (
    GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody,
    golf_v3_odds_tournament_odds_line_movement_sportsbook_group_error_mapper,
)
from ..errors.golf_v3_odds_tournament_odds_sportsbook_group_error import (
    GolfV3OddsTournamentOddsSportsbookGroupErrorBody,
    golf_v3_odds_tournament_odds_sportsbook_group_error_mapper,
)
from ..models.betting_entity_metadata_collection2 import BettingEntityMetadataCollection2
from ..models.betting_event4 import BettingEvent4
from ..models.betting_market2 import BettingMarket2
from ..models.enums.format import Format, FormatOrStr
from ..models.enums.include import Include, IncludeOrStr
from ..models.sportsbook import Sportsbook
from ..models.tournament_odds import TournamentOdds
from ..server.server import Server


class GolfV3Odds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GolfV3OddsWithRawResponse(client, server, auth)

    def golf_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent4]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the tournament(s). Can be any of the dates for the span of a tournament (i.e. Thursday
                through Sunday). <br>Examples: <code>2020-10-17</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.golf_v3_odds_betting_events_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent4]:
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
            self._with_raw_response.golf_v3_odds_betting_events_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket2:
        """Betting MarketReturns full line movement for a given BettingMarket. Due to the sheer size of the output and
        the level of detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

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
            self._with_raw_response.golf_v3_odds_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket2:
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
            self._with_raw_response.golf_v3_odds_betting_market_sportsbook_group(
                market_id, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
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
            self._with_raw_response.golf_v3_odds_betting_markets_by_event(
                event_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def golf_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
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
            self._with_raw_response.golf_v3_odds_betting_markets_by_event_sportsbook_group(
                event_id, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    def golf_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
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
            self._with_raw_response.golf_v3_odds_betting_markets_by_market_type(
                event_id, market_type_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
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
            self._with_raw_response.golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
                event_id,
                market_type_id,
                sportsbookgroup,
                format_=format_,
                include=include,
                request_options=request_options,
            ),
        )

    def golf_v3_odds_betting_markets_by_tournament(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
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
            self._with_raw_response.golf_v3_odds_betting_markets_by_tournament(
                tournamentid, format_=format_, include=include, request_options=request_options
            ),
        )

    def golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
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
            self._with_raw_response.golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    def golf_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingEntityMetadataCollection2:
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
            self._with_raw_response.golf_v3_odds_betting_metadata(format_=format_, request_options=request_options)
        )

    def golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want other types of props
        it is recommended to use the by Market Type endpoint.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
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
            self._with_raw_response.golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    def golf_v3_odds_in_play_tournament_odds(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """In-tournament odds, updating constantly throughout the tournament, without line movement.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.golf_v3_odds_in_play_tournament_odds(
                tournamentid, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_in_play_tournament_odds_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.golf_v3_odds_in_play_tournament_odds_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_in_play_tournament_odds_line_movement(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """In-tournament odds, updating constantly throughout the tournament, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal In-Play Tournament Odds endpoint.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.golf_v3_odds_in_play_tournament_odds_line_movement(
                tournamentid, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_sportsbooks_by_active(
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
            self._with_raw_response.golf_v3_odds_sportsbooks_by_active(format_=format_, request_options=request_options)
        )

    def golf_v3_odds_tournament_odds(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, without line movement.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.golf_v3_odds_tournament_odds(
                tournamentid, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_tournament_odds_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.golf_v3_odds_tournament_odds_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_tournament_odds_line_movement(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.golf_v3_odds_tournament_odds_line_movement(
                tournamentid, format_=format_, request_options=request_options
            ),
        )

    def golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> GolfV3OddsWithRawResponse:
        return self._with_raw_response


class AsyncGolfV3Odds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGolfV3OddsWithRawResponse(client, server, auth)

    async def golf_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent4]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the tournament(s). Can be any of the dates for the span of a tournament (i.e. Thursday
                through Sunday). <br>Examples: <code>2020-10-17</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.golf_v3_odds_betting_events_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent4]:
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
            await self._with_raw_response.golf_v3_odds_betting_events_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket2:
        """Betting MarketReturns full line movement for a given BettingMarket. Due to the sheer size of the output and
        the level of detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

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
            await self._with_raw_response.golf_v3_odds_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BettingMarket2:
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
            await self._with_raw_response.golf_v3_odds_betting_market_sportsbook_group(
                market_id, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
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
            await self._with_raw_response.golf_v3_odds_betting_markets_by_event(
                event_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def golf_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
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
            await self._with_raw_response.golf_v3_odds_betting_markets_by_event_sportsbook_group(
                event_id, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    async def golf_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
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
            await self._with_raw_response.golf_v3_odds_betting_markets_by_market_type(
                event_id, market_type_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
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
            await self._with_raw_response.golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
                event_id,
                market_type_id,
                sportsbookgroup,
                format_=format_,
                include=include,
                request_options=request_options,
            ),
        )

    async def golf_v3_odds_betting_markets_by_tournament(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
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
            await self._with_raw_response.golf_v3_odds_betting_markets_by_tournament(
                tournamentid, format_=format_, include=include, request_options=request_options
            ),
        )

    async def golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
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
            await self._with_raw_response.golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    async def golf_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingEntityMetadataCollection2:
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
            await self._with_raw_response.golf_v3_odds_betting_metadata(
                format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want other types of props
        it is recommended to use the by Market Type endpoint.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
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
            await self._with_raw_response.golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, include=include, request_options=request_options
            ),
        )

    async def golf_v3_odds_in_play_tournament_odds(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """In-tournament odds, updating constantly throughout the tournament, without line movement.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.golf_v3_odds_in_play_tournament_odds(
                tournamentid, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_in_play_tournament_odds_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.golf_v3_odds_in_play_tournament_odds_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_in_play_tournament_odds_line_movement(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """In-tournament odds, updating constantly throughout the tournament, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal In-Play Tournament Odds endpoint.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.golf_v3_odds_in_play_tournament_odds_line_movement(
                tournamentid, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_sportsbooks_by_active(
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
            await self._with_raw_response.golf_v3_odds_sportsbooks_by_active(
                format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_tournament_odds(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, without line movement.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.golf_v3_odds_tournament_odds(
                tournamentid, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_tournament_odds_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.golf_v3_odds_tournament_odds_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_tournament_odds_line_movement(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.golf_v3_odds_tournament_odds_line_movement(
                tournamentid, format_=format_, request_options=request_options
            ),
        )

    async def golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
                tournamentid, sportsbookgroup, format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncGolfV3OddsWithRawResponse:
        return self._with_raw_response


class GolfV3OddsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def golf_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent4], GolfV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the tournament(s). Can be any of the dates for the span of a tournament (i.e. Thursday
                through Sunday). <br>Examples: <code>2020-10-17</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent4]],
            error_mapper=golf_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent4], GolfV3OddsBettingEventsBySeasonErrorBody]:
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent4]],
            error_mapper=golf_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket2, GolfV3OddsBettingMarketErrorBody]:
        """Betting MarketReturns full line movement for a given BettingMarket. Due to the sheer size of the output and
        the level of detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket2],
            error_mapper=golf_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket2, GolfV3OddsBettingMarketSportsbookGroupErrorBody]:
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket2],
            error_mapper=golf_v3_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByEventErrorBody]:
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByEventSportsbookGroupErrorBody]:
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
                "/v3/golf/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
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
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
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
                "/v3/golf/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_tournament(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByTournamentErrorBody]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarketsByTournamentID/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("tournamentid", tournamentid)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_tournament_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByTournamentSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
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
                "/v3/golf/odds/{format}/BettingMarketsByTournamentID/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_tournament_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection2, GolfV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection2],
            error_mapper=golf_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want other types of props
        it is recommended to use the by Market Type endpoint.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
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
                "/v3/golf/odds/{format}/BettingPlayerPropsByTournamentID/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_player_props_by_tournament_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_in_play_tournament_odds(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsErrorBody]:
        """In-tournament odds, updating constantly throughout the tournament, without line movement.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/InPlayTournamentOdds/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_in_play_tournament_odds_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/InPlayTournamentOdds/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_in_play_tournament_odds_line_movement(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsLineMovementErrorBody]:
        """In-tournament odds, updating constantly throughout the tournament, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal In-Play Tournament Odds endpoint.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/InPlayTournamentOddsLineMovement/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsLineMovementSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/InPlayTournamentOddsLineMovement/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_sportsbooks_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], GolfV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=golf_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_tournament_odds(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, without line movement.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOdds/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_tournament_odds_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOdds/{tournamentid}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_tournament_odds_line_movement(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsLineMovementErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOddsLineMovement/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/TournamentOddsLineMovement/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )


class AsyncGolfV3OddsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def golf_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent4], GolfV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the tournament(s). Can be any of the dates for the span of a tournament (i.e. Thursday
                through Sunday). <br>Examples: <code>2020-10-17</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent4]],
            error_mapper=golf_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent4], GolfV3OddsBettingEventsBySeasonErrorBody]:
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent4]],
            error_mapper=golf_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket2, GolfV3OddsBettingMarketErrorBody]:
        """Betting MarketReturns full line movement for a given BettingMarket. Due to the sheer size of the output and
        the level of detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarket2],
            error_mapper=golf_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_market_sportsbook_group(
        self,
        market_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket2, GolfV3OddsBettingMarketSportsbookGroupErrorBody]:
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarket2],
            error_mapper=golf_v3_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByEventErrorBody]:
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        event_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByEventSportsbookGroupErrorBody]:
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
                "/v3/golf/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
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
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
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
                "/v3/golf/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_tournament(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByTournamentErrorBody]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarketsByTournamentID/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("tournamentid", tournamentid)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_tournament_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingMarketsByTournamentSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
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
                "/v3/golf/odds/{format}/BettingMarketsByTournamentID/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_markets_by_tournament_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection2, GolfV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingEntityMetadataCollection2],
            error_mapper=golf_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want other types of props
        it is recommended to use the by Market Type endpoint.

        Args:
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
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
                "/v3/golf/odds/{format}/BettingPlayerPropsByTournamentID/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket2]],
            error_mapper=golf_v3_odds_betting_player_props_by_tournament_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_in_play_tournament_odds(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsErrorBody]:
        """In-tournament odds, updating constantly throughout the tournament, without line movement.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/InPlayTournamentOdds/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_in_play_tournament_odds_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/InPlayTournamentOdds/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_in_play_tournament_odds_line_movement(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsLineMovementErrorBody]:
        """In-tournament odds, updating constantly throughout the tournament, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal In-Play Tournament Odds endpoint.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/InPlayTournamentOddsLineMovement/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsLineMovementSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/InPlayTournamentOddsLineMovement/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_sportsbooks_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], GolfV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Sportsbook]],
            error_mapper=golf_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_tournament_odds(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, without line movement.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOdds/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_tournament_odds_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOdds/{tournamentid}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_tournament_odds_line_movement(
        self,
        tournamentid: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsLineMovementErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOddsLineMovement/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
        self,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        format_: FormatOrStr = Format.JSON,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/TournamentOddsLineMovement/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )
