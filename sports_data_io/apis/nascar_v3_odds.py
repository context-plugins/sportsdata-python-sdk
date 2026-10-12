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
from ..errors.nascar_v3_odds_betting_events_by_date_error import (
    NascarV3OddsBettingEventsByDateErrorBody,
    nascar_v3_odds_betting_events_by_date_error_mapper,
)
from ..errors.nascar_v3_odds_betting_events_by_season_error import (
    NascarV3OddsBettingEventsBySeasonErrorBody,
    nascar_v3_odds_betting_events_by_season_error_mapper,
)
from ..errors.nascar_v3_odds_betting_market_error import (
    NascarV3OddsBettingMarketErrorBody,
    nascar_v3_odds_betting_market_error_mapper,
)
from ..errors.nascar_v3_odds_betting_markets_by_event_error import (
    NascarV3OddsBettingMarketsByEventErrorBody,
    nascar_v3_odds_betting_markets_by_event_error_mapper,
)
from ..errors.nascar_v3_odds_betting_markets_by_market_type_error import (
    NascarV3OddsBettingMarketsByMarketTypeErrorBody,
    nascar_v3_odds_betting_markets_by_market_type_error_mapper,
)
from ..errors.nascar_v3_odds_betting_markets_by_race_error import (
    NascarV3OddsBettingMarketsByRaceErrorBody,
    nascar_v3_odds_betting_markets_by_race_error_mapper,
)
from ..errors.nascar_v3_odds_betting_metadata_error import (
    NascarV3OddsBettingMetadataErrorBody,
    nascar_v3_odds_betting_metadata_error_mapper,
)
from ..errors.nascar_v3_odds_race_odds_error import NascarV3OddsRaceOddsErrorBody, nascar_v3_odds_race_odds_error_mapper
from ..errors.nascar_v3_odds_race_odds_line_movement_error import (
    NascarV3OddsRaceOddsLineMovementErrorBody,
    nascar_v3_odds_race_odds_line_movement_error_mapper,
)
from ..errors.nascar_v3_odds_sportsbooks_by_active_error import (
    NascarV3OddsSportsbooksByActiveErrorBody,
    nascar_v3_odds_sportsbooks_by_active_error_mapper,
)
from ..models.betting_entity_metadata_collection3 import BettingEntityMetadataCollection3
from ..models.betting_event5 import BettingEvent5
from ..models.betting_market3 import BettingMarket3
from ..models.enums.format import Format, FormatOrStr
from ..models.enums.include import Include, IncludeOrStr
from ..models.race_odds import RaceOdds
from ..models.sportsbook import Sportsbook
from ..server.server import Server


class NascarV3Odds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NascarV3OddsWithRawResponse(client, server, auth)

    def nascar_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent5]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the race(s). Examples: 2023-02-19.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v3_odds_betting_events_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    def nascar_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent5]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: The season to get BettingEvents. Valid entries are formatted as years such as <code>2023</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v3_odds_betting_events_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    def nascar_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket3:
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
            self._with_raw_response.nascar_v3_odds_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    def nascar_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket3]:
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
            self._with_raw_response.nascar_v3_odds_betting_markets_by_event(
                event_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def nascar_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket3]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include: 1 for Race
                Lines, 2 for Driver Props, 3 for Head to Head Props, 4 for Group Props, 6 for Race Props
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
            self._with_raw_response.nascar_v3_odds_betting_markets_by_market_type(
                event_id, market_type_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def nascar_v3_odds_betting_markets_by_race(
        self,
        race_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket3]:
        """Returns the markets and available outcomes for a given RaceID. Works the same as by BettingEventID but
        requires less ID mapping.

        Args:
            race_id: The RaceID of the desired race for which to pull all betting markets (includes outcomes/bets).
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
            self._with_raw_response.nascar_v3_odds_betting_markets_by_race(
                race_id, format_=format_, include=include, request_options=request_options
            ),
        )

    def nascar_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingEntityMetadataCollection3:
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
            self._with_raw_response.nascar_v3_odds_betting_metadata(format_=format_, request_options=request_options)
        )

    def nascar_v3_odds_race_odds(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceOdds:
        """Returns pre-race for a given race. Only returns the most recently seen odds, not inclusive of line movement.

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v3_odds_race_odds(raceid, format_=format_, request_options=request_options)
        )

    def nascar_v3_odds_race_odds_line_movement(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceOdds:
        """Returns pre-race for a given race. Only returns the most recently seen odds. This is inclusive of line
        movement; as it is best suited for viewing historical odds, its cache time is slower than the Race Odds
        endpoint.

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            self._with_raw_response.nascar_v3_odds_race_odds_line_movement(
                raceid, format_=format_, request_options=request_options
            ),
        )

    def nascar_v3_odds_sportsbooks_by_active(
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
            self._with_raw_response.nascar_v3_odds_sportsbooks_by_active(
                format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> NascarV3OddsWithRawResponse:
        return self._with_raw_response


class AsyncNascarV3Odds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNascarV3OddsWithRawResponse(client, server, auth)

    async def nascar_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent5]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the race(s). Examples: 2023-02-19.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v3_odds_betting_events_by_date(
                date, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent5]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: The season to get BettingEvents. Valid entries are formatted as years such as <code>2023</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v3_odds_betting_events_by_season(
                season, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket3:
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
            await self._with_raw_response.nascar_v3_odds_betting_market(
                market_id, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket3]:
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
            await self._with_raw_response.nascar_v3_odds_betting_markets_by_event(
                event_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def nascar_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket3]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include: 1 for Race
                Lines, 2 for Driver Props, 3 for Head to Head Props, 4 for Group Props, 6 for Race Props
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
            await self._with_raw_response.nascar_v3_odds_betting_markets_by_market_type(
                event_id, market_type_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def nascar_v3_odds_betting_markets_by_race(
        self,
        race_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket3]:
        """Returns the markets and available outcomes for a given RaceID. Works the same as by BettingEventID but
        requires less ID mapping.

        Args:
            race_id: The RaceID of the desired race for which to pull all betting markets (includes outcomes/bets).
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
            await self._with_raw_response.nascar_v3_odds_betting_markets_by_race(
                race_id, format_=format_, include=include, request_options=request_options
            ),
        )

    async def nascar_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> BettingEntityMetadataCollection3:
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
            await self._with_raw_response.nascar_v3_odds_betting_metadata(
                format_=format_, request_options=request_options
            ),
        )

    async def nascar_v3_odds_race_odds(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceOdds:
        """Returns pre-race for a given race. Only returns the most recently seen odds, not inclusive of line movement.

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v3_odds_race_odds(
                raceid, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v3_odds_race_odds_line_movement(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> RaceOdds:
        """Returns pre-race for a given race. Only returns the most recently seen odds. This is inclusive of line
        movement; as it is best suited for viewing historical odds, its cache time is slower than the Race Odds
        endpoint.

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return unwrap(
            await self._with_raw_response.nascar_v3_odds_race_odds_line_movement(
                raceid, format_=format_, request_options=request_options
            ),
        )

    async def nascar_v3_odds_sportsbooks_by_active(
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
            await self._with_raw_response.nascar_v3_odds_sportsbooks_by_active(
                format_=format_, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNascarV3OddsWithRawResponse:
        return self._with_raw_response


class NascarV3OddsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def nascar_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent5], NascarV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the race(s). Examples: 2023-02-19.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent5]],
            error_mapper=nascar_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    def nascar_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent5], NascarV3OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: The season to get BettingEvents. Valid entries are formatted as years such as <code>2023</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent5]],
            error_mapper=nascar_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    def nascar_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket3, NascarV3OddsBettingMarketErrorBody]:
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
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket3],
            error_mapper=nascar_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    def nascar_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket3], NascarV3OddsBettingMarketsByEventErrorBody]:
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
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket3]],
            error_mapper=nascar_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    def nascar_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket3], NascarV3OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include: 1 for Race
                Lines, 2 for Driver Props, 3 for Head to Head Props, 4 for Group Props, 6 for Race Props
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
                "/v3/nascar/odds/{format}/BettingMarketsByMarketType/{eventID}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventID", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket3]],
            error_mapper=nascar_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    def nascar_v3_odds_betting_markets_by_race(
        self,
        race_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket3], NascarV3OddsBettingMarketsByRaceErrorBody]:
        """Returns the markets and available outcomes for a given RaceID. Works the same as by BettingEventID but
        requires less ID mapping.

        Args:
            race_id: The RaceID of the desired race for which to pull all betting markets (includes outcomes/bets).
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
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingMarketsByRaceID/{raceID}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceID", race_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket3]],
            error_mapper=nascar_v3_odds_betting_markets_by_race_error_mapper,
            request_options=request_options,
        )

    def nascar_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection3, NascarV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingMetaData"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection3],
            error_mapper=nascar_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    def nascar_v3_odds_race_odds(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceOdds, NascarV3OddsRaceOddsErrorBody]:
        """Returns pre-race for a given race. Only returns the most recently seen odds, not inclusive of line movement.

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nascar/odds/{format}/RaceOdds/{Raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("Raceid", raceid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[RaceOdds],
            error_mapper=nascar_v3_odds_race_odds_error_mapper,
            request_options=request_options,
        )

    def nascar_v3_odds_race_odds_line_movement(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceOdds, NascarV3OddsRaceOddsLineMovementErrorBody]:
        """Returns pre-race for a given race. Only returns the most recently seen odds. This is inclusive of line
        movement; as it is best suited for viewing historical odds, its cache time is slower than the Race Odds
        endpoint.

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nascar/odds/{format}/RaceOddsLineMovement/{Raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("Raceid", raceid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[RaceOdds],
            error_mapper=nascar_v3_odds_race_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def nascar_v3_odds_sportsbooks_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], NascarV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nascar/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=nascar_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )


class AsyncNascarV3OddsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def nascar_v3_odds_betting_events_by_date(
        self, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent5], NascarV3OddsBettingEventsByDateErrorBody]:
        """The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the
        Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            date: The date of the race(s). Examples: 2023-02-19.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingEventsByDate/{date}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("date", date)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent5]],
            error_mapper=nascar_v3_odds_betting_events_by_date_error_mapper,
            request_options=request_options,
        )

    async def nascar_v3_odds_betting_events_by_season(
        self, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent5], NascarV3OddsBettingEventsBySeasonErrorBody]:
        """The list of current BettingEvents for the given season, from which Betting Market data can be gathered via
        the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

        Args:
            season: The season to get BettingEvents. Valid entries are formatted as years such as <code>2023</code>
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingEvents/{season}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("season", season)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingEvent5]],
            error_mapper=nascar_v3_odds_betting_events_by_season_error_mapper,
            request_options=request_options,
        )

    async def nascar_v3_odds_betting_market(
        self, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket3, NascarV3OddsBettingMarketErrorBody]:
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
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingMarket3],
            error_mapper=nascar_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    async def nascar_v3_odds_betting_markets_by_event(
        self,
        event_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket3], NascarV3OddsBettingMarketsByEventErrorBody]:
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
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingMarkets/{eventId}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket3]],
            error_mapper=nascar_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    async def nascar_v3_odds_betting_markets_by_market_type(
        self,
        event_id: str,
        market_type_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket3], NascarV3OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            event_id: The EventId of the desired event/game for which to pull all betting markets (includes
                outcomes/bets).
            market_type_id: The Market Type ID of the desired MarketTypes to pull. Some common types include: 1 for Race
                Lines, 2 for Driver Props, 3 for Head to Head Props, 4 for Group Props, 6 for Race Props
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
                "/v3/nascar/odds/{format}/BettingMarketsByMarketType/{eventID}/{marketTypeID}"
            ),
            path_params=[
                param[FormatOrStr]("format", format_),
                param[str]("eventID", event_id),
                param[str]("marketTypeID", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket3]],
            error_mapper=nascar_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    async def nascar_v3_odds_betting_markets_by_race(
        self,
        race_id: str,
        *,
        format_: FormatOrStr = Format.JSON,
        include: IncludeOrStr | None = Include.AVAILABLE,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket3], NascarV3OddsBettingMarketsByRaceErrorBody]:
        """Returns the markets and available outcomes for a given RaceID. Works the same as by BettingEventID but
        requires less ID mapping.

        Args:
            race_id: The RaceID of the desired race for which to pull all betting markets (includes outcomes/bets).
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
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingMarketsByRaceID/{raceID}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("raceID", race_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[BettingMarket3]],
            error_mapper=nascar_v3_odds_betting_markets_by_race_error_mapper,
            request_options=request_options,
        )

    async def nascar_v3_odds_betting_metadata(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection3, NascarV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/nascar/odds/{format}/BettingMetaData"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[BettingEntityMetadataCollection3],
            error_mapper=nascar_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    async def nascar_v3_odds_race_odds(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceOdds, NascarV3OddsRaceOddsErrorBody]:
        """Returns pre-race for a given race. Only returns the most recently seen odds, not inclusive of line movement.

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nascar/odds/{format}/RaceOdds/{Raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("Raceid", raceid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[RaceOdds],
            error_mapper=nascar_v3_odds_race_odds_error_mapper,
            request_options=request_options,
        )

    async def nascar_v3_odds_race_odds_line_movement(
        self, raceid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RaceOdds, NascarV3OddsRaceOddsLineMovementErrorBody]:
        """Returns pre-race for a given race. Only returns the most recently seen odds. This is inclusive of line
        movement; as it is best suited for viewing historical odds, its cache time is slower than the Race Odds
        endpoint.

        Args:
            raceid: Unique FantasyData Race ID. Example:<code>1</code>, <code>2</code>, etc.
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nascar/odds/{format}/RaceOddsLineMovement/{Raceid}"),
            path_params=[param[FormatOrStr]("format", format_), param[str]("Raceid", raceid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[RaceOdds],
            error_mapper=nascar_v3_odds_race_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def nascar_v3_odds_sportsbooks_by_active(
        self, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], NascarV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format_: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/nascar/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format_)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=async_json_decoder[list[Sportsbook]],
            error_mapper=nascar_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )
