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
from ..errors.mma_v3_odds_betting_events_by_event_error import (
    MmaV3OddsBettingEventsByEventErrorBody,
    mma_v3_odds_betting_events_by_event_error_mapper,
)
from ..errors.mma_v3_odds_betting_events_upcoming_error import (
    MmaV3OddsBettingEventsUpcomingErrorBody,
    mma_v3_odds_betting_events_upcoming_error_mapper,
)
from ..errors.mma_v3_odds_betting_fighter_props_by_event_error import (
    MmaV3OddsBettingFighterPropsByEventErrorBody,
    mma_v3_odds_betting_fighter_props_by_event_error_mapper,
)
from ..errors.mma_v3_odds_betting_market_error import (
    MmaV3OddsBettingMarketErrorBody,
    mma_v3_odds_betting_market_error_mapper,
)
from ..errors.mma_v3_odds_betting_markets_by_event_error import (
    MmaV3OddsBettingMarketsByEventErrorBody,
    mma_v3_odds_betting_markets_by_event_error_mapper,
)
from ..errors.mma_v3_odds_betting_markets_by_market_type_error import (
    MmaV3OddsBettingMarketsByMarketTypeErrorBody,
    mma_v3_odds_betting_markets_by_market_type_error_mapper,
)
from ..errors.mma_v3_odds_betting_metadata_error import (
    MmaV3OddsBettingMetadataErrorBody,
    mma_v3_odds_betting_metadata_error_mapper,
)
from ..errors.mma_v3_odds_event_fight_odds_error import (
    MmaV3OddsEventFightOddsErrorBody,
    mma_v3_odds_event_fight_odds_error_mapper,
)
from ..errors.mma_v3_odds_event_fight_odds_line_movement_error import (
    MmaV3OddsEventFightOddsLineMovementErrorBody,
    mma_v3_odds_event_fight_odds_line_movement_error_mapper,
)
from ..errors.mma_v3_odds_sportsbooks_by_active_error import (
    MmaV3OddsSportsbooksByActiveErrorBody,
    mma_v3_odds_sportsbooks_by_active_error_mapper,
)
from ..models.betting_entity_metadata_collection1 import BettingEntityMetadataCollection1
from ..models.betting_event3 import BettingEvent3
from ..models.betting_market2 import BettingMarket2
from ..models.enums.format import FormatOrStr
from ..models.enums.include import IncludeOrStr
from ..models.event_odds import EventOdds
from ..models.sportsbook import Sportsbook
from ..server.server import Server


class MmaV3Odds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MmaV3OddsWithRawResponse(client, server, auth)

    def mma_v3_odds_betting_events_by_event(
        self, format: FormatOrStr, event_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent3]:
        """The list of current BettingEvents for the given fight event (i.e. card of fights), from which Betting Market
        data can be gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g.
        Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.mma_v3_odds_betting_events_by_event(
            format, event_id, request_options=request_options
        ).unwrap()

    def mma_v3_odds_betting_events_upcoming(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent3]:
        """A list of all BettingEvents that are currently scheduled and that have associated FightIds.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.mma_v3_odds_betting_events_upcoming(
            format, request_options=request_options
        ).unwrap()

    def mma_v3_odds_betting_fighter_props_by_event(
        self,
        format: FormatOrStr,
        event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player (Fighter) Props
        type only. Ideal if your application will only ever require Player Props, but if you also want Fight Props etc.
        it is recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
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
        return self._with_raw_response.mma_v3_odds_betting_fighter_props_by_event(
            format, event_id, include=include, request_options=request_options
        ).unwrap()

    def mma_v3_odds_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket2:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The BettingMarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.mma_v3_odds_betting_market(
            format, market_id, request_options=request_options
        ).unwrap()

    def mma_v3_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        betting_event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns the markets of all available types (e.g. Player Props, Fight Props) and available outcomes for a
        given BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            betting_event_id: The BettingEventId for which to pull all betting markets (includes outcomes/bets).
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
        return self._with_raw_response.mma_v3_odds_betting_markets_by_event(
            format, betting_event_id, include=include, request_options=request_options
        ).unwrap()

    def mma_v3_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
            market_type_id: The BettingMarketTypeId of the desired market types to pull. See BettingMetaData endpoint
                for all of the types.
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
        return self._with_raw_response.mma_v3_odds_betting_markets_by_market_type(
            format, event_id, market_type_id, include=include, request_options=request_options
        ).unwrap()

    def mma_v3_odds_betting_metadata(
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
        return self._with_raw_response.mma_v3_odds_betting_metadata(format, request_options=request_options).unwrap()

    def mma_v3_odds_event_fight_odds(
        self, format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventOdds:
        """Returns basic fight odds (e.g. moneyline) for all fights in a given event. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.mma_v3_odds_event_fight_odds(
            format, eventid, request_options=request_options
        ).unwrap()

    def mma_v3_odds_event_fight_odds_line_movement(
        self, format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventOdds:
        """Returns basic fight odds (e.g. moneyline) for all fights in a given event. Returns the full line movement for
        the fights. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return self._with_raw_response.mma_v3_odds_event_fight_odds_line_movement(
            format, eventid, request_options=request_options
        ).unwrap()

    def mma_v3_odds_sportsbooks_by_active(
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
        return self._with_raw_response.mma_v3_odds_sportsbooks_by_active(
            format, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MmaV3OddsWithRawResponse:
        return self._with_raw_response


class AsyncMmaV3Odds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMmaV3OddsWithRawResponse(client, server, auth)

    async def mma_v3_odds_betting_events_by_event(
        self, format: FormatOrStr, event_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent3]:
        """The list of current BettingEvents for the given fight event (i.e. card of fights), from which Betting Market
        data can be gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g.
        Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.mma_v3_odds_betting_events_by_event(
                format, event_id, request_options=request_options
            )
        ).unwrap()

    async def mma_v3_odds_betting_events_upcoming(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[BettingEvent3]:
        """A list of all BettingEvents that are currently scheduled and that have associated FightIds.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.mma_v3_odds_betting_events_upcoming(format, request_options=request_options)
        ).unwrap()

    async def mma_v3_odds_betting_fighter_props_by_event(
        self,
        format: FormatOrStr,
        event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player (Fighter) Props
        type only. Ideal if your application will only ever require Player Props, but if you also want Fight Props etc.
        it is recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
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
            await self._with_raw_response.mma_v3_odds_betting_fighter_props_by_event(
                format, event_id, include=include, request_options=request_options
            )
        ).unwrap()

    async def mma_v3_odds_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BettingMarket2:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The BettingMarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.mma_v3_odds_betting_market(format, market_id, request_options=request_options)
        ).unwrap()

    async def mma_v3_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        betting_event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns the markets of all available types (e.g. Player Props, Fight Props) and available outcomes for a
        given BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            betting_event_id: The BettingEventId for which to pull all betting markets (includes outcomes/bets).
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
            await self._with_raw_response.mma_v3_odds_betting_markets_by_event(
                format, betting_event_id, include=include, request_options=request_options
            )
        ).unwrap()

    async def mma_v3_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[BettingMarket2]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
            market_type_id: The BettingMarketTypeId of the desired market types to pull. See BettingMetaData endpoint
                for all of the types.
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
            await self._with_raw_response.mma_v3_odds_betting_markets_by_market_type(
                format, event_id, market_type_id, include=include, request_options=request_options
            )
        ).unwrap()

    async def mma_v3_odds_betting_metadata(
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
            await self._with_raw_response.mma_v3_odds_betting_metadata(format, request_options=request_options)
        ).unwrap()

    async def mma_v3_odds_event_fight_odds(
        self, format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventOdds:
        """Returns basic fight odds (e.g. moneyline) for all fights in a given event. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.mma_v3_odds_event_fight_odds(format, eventid, request_options=request_options)
        ).unwrap()

    async def mma_v3_odds_event_fight_odds_line_movement(
        self, format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EventOdds:
        """Returns basic fight odds (e.g. moneyline) for all fights in a given event. Returns the full line movement for
        the fights. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: Unauthorized ``error`` is ``Unauthorized | RawError``."""
        return (
            await self._with_raw_response.mma_v3_odds_event_fight_odds_line_movement(
                format, eventid, request_options=request_options
            )
        ).unwrap()

    async def mma_v3_odds_sportsbooks_by_active(
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
            await self._with_raw_response.mma_v3_odds_sportsbooks_by_active(format, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMmaV3OddsWithRawResponse:
        return self._with_raw_response


class MmaV3OddsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def mma_v3_odds_betting_events_by_event(
        self, format: FormatOrStr, event_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent3], MmaV3OddsBettingEventsByEventErrorBody]:
        """The list of current BettingEvents for the given fight event (i.e. card of fights), from which Betting Market
        data can be gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g.
        Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/BettingEventsByEvent/{eventId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventId", event_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=mma_v3_odds_betting_events_by_event_error_mapper,
            request_options=request_options,
        )

    def mma_v3_odds_betting_events_upcoming(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent3], MmaV3OddsBettingEventsUpcomingErrorBody]:
        """A list of all BettingEvents that are currently scheduled and that have associated FightIds.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/UpcomingBettingEvents"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=mma_v3_odds_betting_events_upcoming_error_mapper,
            request_options=request_options,
        )

    def mma_v3_odds_betting_fighter_props_by_event(
        self,
        format: FormatOrStr,
        event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], MmaV3OddsBettingFighterPropsByEventErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player (Fighter) Props
        type only. Ideal if your application will only ever require Player Props, but if you also want Fight Props etc.
        it is recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
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
            url_template=self._server.default("/v3/mma/odds/{format}/BettingFighterPropsByEvent/{eventId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=mma_v3_odds_betting_fighter_props_by_event_error_mapper,
            request_options=request_options,
        )

    def mma_v3_odds_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket2, MmaV3OddsBettingMarketErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The BettingMarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("marketId", market_id)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket2],
            error_mapper=mma_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    def mma_v3_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        betting_event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], MmaV3OddsBettingMarketsByEventErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Fight Props) and available outcomes for a
        given BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            betting_event_id: The BettingEventId for which to pull all betting markets (includes outcomes/bets).
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
            url_template=self._server.default("/v3/mma/odds/{format}/BettingMarketsByBettingEvent/{bettingEventId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("bettingEventId", betting_event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=mma_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    def mma_v3_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], MmaV3OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
            market_type_id: The BettingMarketTypeId of the desired market types to pull. See BettingMetaData endpoint
                for all of the types.
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
                "/v3/mma/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeId}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("marketTypeId", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=mma_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    def mma_v3_odds_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection1, MmaV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/mma/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection1],
            error_mapper=mma_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    def mma_v3_odds_event_fight_odds(
        self, format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventOdds, MmaV3OddsEventFightOddsErrorBody]:
        """Returns basic fight odds (e.g. moneyline) for all fights in a given event. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/EventOdds/{eventid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventid", eventid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[EventOdds],
            error_mapper=mma_v3_odds_event_fight_odds_error_mapper,
            request_options=request_options,
        )

    def mma_v3_odds_event_fight_odds_line_movement(
        self, format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventOdds, MmaV3OddsEventFightOddsLineMovementErrorBody]:
        """Returns basic fight odds (e.g. moneyline) for all fights in a given event. Returns the full line movement for
        the fights. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/EventOddsLineMovement/{eventid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventid", eventid)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[EventOdds],
            error_mapper=mma_v3_odds_event_fight_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    def mma_v3_odds_sportsbooks_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], MmaV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=mma_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )


class AsyncMmaV3OddsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def mma_v3_odds_betting_events_by_event(
        self, format: FormatOrStr, event_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent3], MmaV3OddsBettingEventsByEventErrorBody]:
        """The list of current BettingEvents for the given fight event (i.e. card of fights), from which Betting Market
        data can be gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g.
        Player Props, Team Props.)

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/BettingEventsByEvent/{eventId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventId", event_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=mma_v3_odds_betting_events_by_event_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_odds_betting_events_upcoming(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[BettingEvent3], MmaV3OddsBettingEventsUpcomingErrorBody]:
        """A list of all BettingEvents that are currently scheduled and that have associated FightIds.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/UpcomingBettingEvents"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingEvent3]],
            error_mapper=mma_v3_odds_betting_events_upcoming_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_odds_betting_fighter_props_by_event(
        self,
        format: FormatOrStr,
        event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], MmaV3OddsBettingFighterPropsByEventErrorBody]:
        """This works in the same way as Betting Markets by Market Type but is prefiltered to the Player (Fighter) Props
        type only. Ideal if your application will only ever require Player Props, but if you also want Fight Props etc.
        it is recommended to use the by Market Type endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
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
            url_template=self._server.default("/v3/mma/odds/{format}/BettingFighterPropsByEvent/{eventId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventId", event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=mma_v3_odds_betting_fighter_props_by_event_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_odds_betting_market(
        self, format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingMarket2, MmaV3OddsBettingMarketErrorBody]:
        """Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of
        detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            market_id: The BettingMarketId of the desired market for which to pull all outcomes/bets.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/BettingMarket/{marketId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("marketId", market_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingMarket2],
            error_mapper=mma_v3_odds_betting_market_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_odds_betting_markets_by_event(
        self,
        format: FormatOrStr,
        betting_event_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], MmaV3OddsBettingMarketsByEventErrorBody]:
        """Returns the markets of all available types (e.g. Player Props, Fight Props) and available outcomes for a
        given BettingEventID.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            betting_event_id: The BettingEventId for which to pull all betting markets (includes outcomes/bets).
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
            url_template=self._server.default("/v3/mma/odds/{format}/BettingMarketsByBettingEvent/{bettingEventId}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("bettingEventId", betting_event_id)],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=mma_v3_odds_betting_markets_by_event_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_odds_betting_markets_by_market_type(
        self,
        format: FormatOrStr,
        event_id: str,
        market_type_id: str,
        *,
        include: IncludeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[BettingMarket2], MmaV3OddsBettingMarketsByMarketTypeErrorBody]:
        """Returns Markets and available outcomes for a given event and market type requested. A lighter call than by
        BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is
        available for each sport in its Betting Metadata endpoint.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            event_id: The top level EventId for the event (i.e. UFC 250). Distinct from the BettingEventId.
            market_type_id: The BettingMarketTypeId of the desired market types to pull. See BettingMetaData endpoint
                for all of the types.
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
                "/v3/mma/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeId}"
            ),
            path_params=[
                param[FormatOrStr]("format", format),
                param[str]("eventId", event_id),
                param[str]("marketTypeId", market_type_id),
            ],
            query_params=[param[IncludeOrStr | None]("include", include)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[BettingMarket2]],
            error_mapper=mma_v3_odds_betting_markets_by_market_type_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_odds_betting_metadata(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BettingEntityMetadataCollection1, MmaV3OddsBettingMetadataErrorBody]:
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
            url_template=self._server.default("/v3/mma/odds/{format}/BettingMetadata"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[BettingEntityMetadataCollection1],
            error_mapper=mma_v3_odds_betting_metadata_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_odds_event_fight_odds(
        self, format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventOdds, MmaV3OddsEventFightOddsErrorBody]:
        """Returns basic fight odds (e.g. moneyline) for all fights in a given event. Only returns the most recently
        seen odds, not inclusive of line movement.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/EventOdds/{eventid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventid", eventid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[EventOdds],
            error_mapper=mma_v3_odds_event_fight_odds_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_odds_event_fight_odds_line_movement(
        self, format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EventOdds, MmaV3OddsEventFightOddsLineMovementErrorBody]:
        """Returns basic fight odds (e.g. moneyline) for all fights in a given event. Returns the full line movement for
        the fights. This endpoint has a longer cache as it is meant for historical data/line movement rather than the
        most up to the second line.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            eventid: The unique ID of this event. <br> Examples: <code>51</code>, <code>52</code>, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/EventOddsLineMovement/{eventid}"),
            path_params=[param[FormatOrStr]("format", format), param[str]("eventid", eventid)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[EventOdds],
            error_mapper=mma_v3_odds_event_fight_odds_line_movement_error_mapper,
            request_options=request_options,
        )

    async def mma_v3_odds_sportsbooks_by_active(
        self, format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[Sportsbook], MmaV3OddsSportsbooksByActiveErrorBody]:
        """A list of all available sportsbooks with their associated unique IDs.

        Args:
            format: Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v3/mma/odds/{format}/ActiveSportsbooks"),
            path_params=[param[FormatOrStr]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key_header, self._auth.api_key_query),
            decoder=json_decoder[list[Sportsbook]],
            error_mapper=mma_v3_odds_sportsbooks_by_active_error_mapper,
            request_options=request_options,
        )
