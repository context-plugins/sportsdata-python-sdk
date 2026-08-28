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
from ..models.betting_entity_metadata_collection1 import BettingEntityMetadataCollection1
from ..models.betting_event1 import BettingEvent1
from ..models.betting_market1 import BettingMarket1
from ..models.enums.format import FormatOrStr
from ..models.enums.include import IncludeOrStr
from ..models.sportsbook import Sportsbook
from ..models.tournament_odds import TournamentOdds
from ..server.server import Server


class GolfV3Odds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GolfV3OddsWithRawResponse(client, server, auth)

    def golf_v3_odds_betting_events_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the tournament(s). Can be any of the dates for the span of a tournament (i.e. Thursday
                through Sunday). <br>Examples: <code>2020-10-17</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_events_by_date(
            format, date, request_options=request_options
        ).unwrap()

    def golf_v3_odds_betting_events_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_events_by_season(
            format, season, request_options=request_options
        ).unwrap()

    def golf_v3_odds_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket1:
        """Betting MarketReturns full line movement for a given BettingMarket. Due to the sheer size of the output and
        the level of detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_market(
            format, market_id, request_options=request_options
        ).unwrap()

    def golf_v3_odds_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
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
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_market_sportsbook_group(
            format, market_id, sportsbookgroup, request_options=request_options
        ).unwrap()

    def golf_v3_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_markets_by_event(
            format, event_id, include=include, request_options=request_options
        ).unwrap()

    def golf_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_markets_by_event_sportsbook_group(
            format, event_id, sportsbookgroup, include=include, request_options=request_options
        ).unwrap()

    def golf_v3_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_markets_by_market_type(
            format, event_id, market_type_id, include=include, request_options=request_options
        ).unwrap()

    def golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
            format, event_id, market_type_id, sportsbookgroup, include=include, request_options=request_options
        ).unwrap()

    def golf_v3_odds_betting_markets_by_tournament(
        self,
        format: FormatOrStr,
        tournamentid: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_markets_by_tournament(
            format, tournamentid, include=include, request_options=request_options
        ).unwrap()

    def golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
            format, tournamentid, sportsbookgroup, include=include, request_options=request_options
        ).unwrap()

    def golf_v3_odds_betting_metadata(
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
        return self._with_raw_response.golf_v3_odds_betting_metadata(format, request_options=request_options).unwrap()

    def golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want other types of props
        it is recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
            format, tournamentid, sportsbookgroup, include=include, request_options=request_options
        ).unwrap()

    def golf_v3_odds_in_play_tournament_odds(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TournamentOdds:
        """In-tournament odds, updating constantly throughout the tournament, without line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_in_play_tournament_odds(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v3_odds_in_play_tournament_odds_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_in_play_tournament_odds_sportsbook_group(
            format, tournamentid, sportsbookgroup, request_options=request_options
        ).unwrap()

    def golf_v3_odds_in_play_tournament_odds_line_movement(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TournamentOdds:
        """In-tournament odds, updating constantly throughout the tournament, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal In-Play Tournament Odds endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_in_play_tournament_odds_line_movement(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
            format, tournamentid, sportsbookgroup, request_options=request_options
        ).unwrap()

    def golf_v3_odds_sportsbooks_by_active(
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
        return self._with_raw_response.golf_v3_odds_sportsbooks_by_active(
            format, request_options=request_options
        ).unwrap()

    def golf_v3_odds_tournament_odds(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, without line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_tournament_odds(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v3_odds_tournament_odds_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_tournament_odds_sportsbook_group(
            format, tournamentid, sportsbookgroup, request_options=request_options
        ).unwrap()

    def golf_v3_odds_tournament_odds_line_movement(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_tournament_odds_line_movement(
            format, tournamentid, request_options=request_options
        ).unwrap()

    def golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
            format, tournamentid, sportsbookgroup, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> GolfV3OddsWithRawResponse:
        return self._with_raw_response


class AsyncGolfV3Odds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGolfV3OddsWithRawResponse(client, server, auth)

    async def golf_v3_odds_betting_events_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the tournament(s). Can be any of the dates for the span of a tournament (i.e. Thursday
                through Sunday). <br>Examples: <code>2020-10-17</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_events_by_date(
                format, date, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_betting_events_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent1]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_events_by_season(
                format, season, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket1:
        """Betting MarketReturns full line movement for a given BettingMarket. Due to the sheer size of the output and
        the level of detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_market(
                format, market_id, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
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
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_market_sportsbook_group(
                format, market_id, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_markets_by_event(
                format, event_id, include=include, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_markets_by_event_sportsbook_group(
                format, event_id, sportsbookgroup, include=include, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_markets_by_market_type(
                format, event_id, market_type_id, include=include, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
                format, event_id, market_type_id, sportsbookgroup, include=include, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_betting_markets_by_tournament(
        self,
        format: FormatOrStr,
        tournamentid: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_markets_by_tournament(
                format, tournamentid, include=include, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
                format, tournamentid, sportsbookgroup, include=include, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_betting_metadata(
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
            await self._with_raw_response.golf_v3_odds_betting_metadata(format, request_options=request_options)
        ).unwrap()

    async def golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket1]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want other types of props
        it is recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
                format, tournamentid, sportsbookgroup, include=include, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_in_play_tournament_odds(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TournamentOdds:
        """In-tournament odds, updating constantly throughout the tournament, without line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_in_play_tournament_odds(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_in_play_tournament_odds_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_in_play_tournament_odds_sportsbook_group(
                format, tournamentid, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_in_play_tournament_odds_line_movement(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TournamentOdds:
        """In-tournament odds, updating constantly throughout the tournament, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal In-Play Tournament Odds endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_in_play_tournament_odds_line_movement(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
                format, tournamentid, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_sportsbooks_by_active(
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
            await self._with_raw_response.golf_v3_odds_sportsbooks_by_active(format, request_options=request_options)
        ).unwrap()

    async def golf_v3_odds_tournament_odds(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, without line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_tournament_odds(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_tournament_odds_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_tournament_odds_sportsbook_group(
                format, tournamentid, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_tournament_odds_line_movement(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_tournament_odds_line_movement(
                format, tournamentid, request_options=request_options
            )
        ).unwrap()

    async def golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TournamentOdds:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
                format, tournamentid, sportsbookgroup, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncGolfV3OddsWithRawResponse:
        return self._with_raw_response


class GolfV3OddsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def golf_v3_odds_betting_events_by_date(
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], GolfV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the tournament(s). Can be any of the dates for the span of a tournament (i.e. Thursday
                through Sunday). <br>Examples: <code>2020-10-17</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=golf_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_events_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], GolfV3OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=golf_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket1, GolfV3OddsBettingMarketErrorBody]:
        """Betting MarketReturns full line movement for a given BettingMarket. Due to the sheer size of the output and
        the level of detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket1],
            error_mapper=golf_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
        market_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket1, GolfV3OddsBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket1],
            error_mapper=golf_v3_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByEventErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByEventSportsbookGroupErrorBody]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_tournament(
        self,
        format: FormatOrStr,
        tournamentid: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByTournamentErrorBody]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarketsByTournamentID/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_tournament_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByTournamentSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingMarketsByTournamentID/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_tournament_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection1, GolfV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection1],
            error_mapper=golf_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want other types of props
        it is recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingPlayerPropsByTournamentID/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_player_props_by_tournament_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_in_play_tournament_odds(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsErrorBody]:
        """In-tournament odds, updating constantly throughout the tournament, without line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/InPlayTournamentOdds/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_in_play_tournament_odds_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/InPlayTournamentOdds/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_in_play_tournament_odds_line_movement(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsLineMovementErrorBody]:
        """In-tournament odds, updating constantly throughout the tournament, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal In-Play Tournament Odds endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/InPlayTournamentOddsLineMovement/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsLineMovementSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/InPlayTournamentOddsLineMovement/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_sportsbooks_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], GolfV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=golf_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_tournament_odds(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, without line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOdds/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_tournament_odds_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOdds/{tournamentid}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_tournament_odds_line_movement(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsLineMovementErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOddsLineMovement/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/TournamentOddsLineMovement/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
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
        self, format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], GolfV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            date: The date of the tournament(s). Can be any of the dates for the span of a tournament (i.e. Thursday
                through Sunday). <br>Examples: <code>2020-10-17</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=golf_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_events_by_season(
        self, format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent1], GolfV3OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            season: Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent1]],
            error_mapper=golf_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket1, GolfV3OddsBettingMarketErrorBody]:
        """Betting MarketReturns full line movement for a given BettingMarket. Due to the sheer size of the output and
        the level of detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket1],
            error_mapper=golf_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_market_sportsbook_group(
        self,
        format: FormatOrStr,
        market_id: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BettingMarket1, GolfV3OddsBettingMarketSportsbookGroupErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook
        Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The MarketId of the desired market for which to pull all outcomes/bets.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("marketId", market_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket1],
            error_mapper=golf_v3_odds_betting_market_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByEventErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given
        BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_event_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByEventSportsbookGroupErrorBody]:
        """Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified
        as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_event_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_market_type_sportsbook_group(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL
        parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("marketTypeID", market_type_id),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_market_type_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_tournament(
        self,
        format: FormatOrStr,
        tournamentid: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByTournamentErrorBody]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMarketsByTournamentID/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_tournament_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_markets_by_tournament_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByTournamentSportsbookGroupErrorBody]:
        """Returns the markets of all available types (e.g. Player Props) and available outcomes for a given
        TournamentID. A Sportsbook Group must be specified as a URL parameter.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingMarketsByTournamentID/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_markets_by_tournament_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection1, GolfV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/golf/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection1],
            error_mapper=golf_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket1], GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type
        only. Ideal if your application will only ever require Player Props, but if you also want other types of props
        it is recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of the desired tournament for which to pull all betting markets (includes
                outcomes/bets).
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/BettingPlayerPropsByTournamentID/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket1]],
            error_mapper=golf_v3_odds_betting_player_props_by_tournament_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_in_play_tournament_odds(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsErrorBody]:
        """In-tournament odds, updating constantly throughout the tournament, without line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/InPlayTournamentOdds/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_in_play_tournament_odds_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/InPlayTournamentOdds/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_in_play_tournament_odds_line_movement(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsLineMovementErrorBody]:
        """In-tournament odds, updating constantly throughout the tournament, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal In-Play Tournament Odds endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/InPlayTournamentOddsLineMovement/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsLineMovementSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/InPlayTournamentOddsLineMovement/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_sportsbooks_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], GolfV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=golf_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_tournament_odds(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, without line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOdds/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_tournament_odds_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOdds/{tournamentid}/{sportsbookgroup}"),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_sportsbook_group_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_tournament_odds_line_movement(
        self, format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsLineMovementErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/golf/odds/{format}/TournamentOddsLineMovement/{tournamentid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("tournamentid", tournamentid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def golf_v3_odds_tournament_odds_line_movement_sportsbook_group(
        self,
        format: FormatOrStr,
        tournamentid: str,
        sportsbookgroup: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TournamentOdds, GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody]:
        """Pre-tournament odds, updating constantly until the tournament begins, with line movement. As this is for
        historical line movement, the cache time is set slower than the normal Tournament Odds endpoint. Called by
        Sportsbook Group.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            tournamentid: The TournamentID of a tournament. TournamentIDs can be found in the Tournaments API. Valid
                entries are <code>58</code>, <code>61</code>, etc.
            sportsbookgroup: The name of the Sportsbook grouping. <br>Examples: <code>G1100</code>
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v3/golf/odds/{format}/TournamentOddsLineMovement/{tournamentid}/{sportsbookgroup}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("tournamentid", tournamentid),
                param[str]("sportsbookgroup", sportsbookgroup),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[TournamentOdds],
            error_mapper=golf_v3_odds_tournament_odds_line_movement_sportsbook_group_error_mapper,
            request_options=request_options,
        )
