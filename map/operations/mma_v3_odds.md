<!-- Generated file — do not edit; regenerated with the SDK. -->

# MmaV3Odds — operations

Accessor: `client.mma_v3_odds` · Source: `sports_data/apis/mma_v3_odds.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mma_v3_odds.mma_v3_odds_betting_events_by_event

- **Route**: `GET /v3/mma/odds/{format}/BettingEventsByEvent/{eventId}`
- **Signature**: `def mma_v3_odds_betting_events_by_event(format: FormatOrStr, event_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId`
- **Returns (parsed)**: `list[BettingEvent3]`
- **Returns (raw)**: `ApiResult[list[BettingEvent3], MmaV3OddsBettingEventsByEventErrorBody]`
- **Error**: `MmaV3OddsBettingEventsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent3` | `sports_data/models/betting_event3.py` |
| `MmaV3OddsBettingEventsByEventErrorBody` | `sports_data/errors/mma_v3_odds_betting_events_by_event_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_odds.mma_v3_odds_betting_events_upcoming

- **Route**: `GET /v3/mma/odds/{format}/UpcomingBettingEvents`
- **Signature**: `def mma_v3_odds_betting_events_upcoming(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[BettingEvent3]`
- **Returns (raw)**: `ApiResult[list[BettingEvent3], MmaV3OddsBettingEventsUpcomingErrorBody]`
- **Error**: `MmaV3OddsBettingEventsUpcomingErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent3` | `sports_data/models/betting_event3.py` |
| `MmaV3OddsBettingEventsUpcomingErrorBody` | `sports_data/errors/mma_v3_odds_betting_events_upcoming_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_odds.mma_v3_odds_betting_fighter_props_by_event

- **Route**: `GET /v3/mma/odds/{format}/BettingFighterPropsByEvent/{eventId}`
- **Signature**: `def mma_v3_odds_betting_fighter_props_by_event(format: FormatOrStr, event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket2]`
- **Returns (raw)**: `ApiResult[list[BettingMarket2], MmaV3OddsBettingFighterPropsByEventErrorBody]`
- **Error**: `MmaV3OddsBettingFighterPropsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket2` | `sports_data/models/betting_market2.py` |
| `MmaV3OddsBettingFighterPropsByEventErrorBody` | `sports_data/errors/mma_v3_odds_betting_fighter_props_by_event_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_odds.mma_v3_odds_betting_market

- **Route**: `GET /v3/mma/odds/{format}/BettingMarket/{marketId}`
- **Signature**: `def mma_v3_odds_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket2`
- **Returns (raw)**: `ApiResult[BettingMarket2, MmaV3OddsBettingMarketErrorBody]`
- **Error**: `MmaV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket2` | `sports_data/models/betting_market2.py` |
| `MmaV3OddsBettingMarketErrorBody` | `sports_data/errors/mma_v3_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_odds.mma_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/mma/odds/{format}/BettingMarketsByBettingEvent/{bettingEventId}`
- **Signature**: `def mma_v3_odds_betting_markets_by_event(format: FormatOrStr, betting_event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `betting_event_id`
- **Params**: `format` — path · `betting_event_id` — path `bettingEventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket2]`
- **Returns (raw)**: `ApiResult[list[BettingMarket2], MmaV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `MmaV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket2` | `sports_data/models/betting_market2.py` |
| `MmaV3OddsBettingMarketsByEventErrorBody` | `sports_data/errors/mma_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_odds.mma_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/mma/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeId}`
- **Signature**: `def mma_v3_odds_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket2]`
- **Returns (raw)**: `ApiResult[list[BettingMarket2], MmaV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `MmaV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket2` | `sports_data/models/betting_market2.py` |
| `MmaV3OddsBettingMarketsByMarketTypeErrorBody` | `sports_data/errors/mma_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_odds.mma_v3_odds_betting_metadata

- **Route**: `GET /v3/mma/odds/{format}/BettingMetadata`
- **Signature**: `def mma_v3_odds_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `BettingEntityMetadataCollection1`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection1, MmaV3OddsBettingMetadataErrorBody]`
- **Error**: `MmaV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEntityMetadataCollection1` | `sports_data/models/betting_entity_metadata_collection1.py` |
| `MmaV3OddsBettingMetadataErrorBody` | `sports_data/errors/mma_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_odds.mma_v3_odds_event_fight_odds

- **Route**: `GET /v3/mma/odds/{format}/EventOdds/{eventid}`
- **Signature**: `def mma_v3_odds_event_fight_odds(format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `eventid`
- **Params**: `format` — path · `eventid` — path
- **Returns (parsed)**: `EventOdds`
- **Returns (raw)**: `ApiResult[EventOdds, MmaV3OddsEventFightOddsErrorBody]`
- **Error**: `MmaV3OddsEventFightOddsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `EventOdds` | `sports_data/models/event_odds.py` |
| `MmaV3OddsEventFightOddsErrorBody` | `sports_data/errors/mma_v3_odds_event_fight_odds_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_odds.mma_v3_odds_event_fight_odds_line_movement

- **Route**: `GET /v3/mma/odds/{format}/EventOddsLineMovement/{eventid}`
- **Signature**: `def mma_v3_odds_event_fight_odds_line_movement(format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `eventid`
- **Params**: `format` — path · `eventid` — path
- **Returns (parsed)**: `EventOdds`
- **Returns (raw)**: `ApiResult[EventOdds, MmaV3OddsEventFightOddsLineMovementErrorBody]`
- **Error**: `MmaV3OddsEventFightOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `EventOdds` | `sports_data/models/event_odds.py` |
| `MmaV3OddsEventFightOddsLineMovementErrorBody` | `sports_data/errors/mma_v3_odds_event_fight_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_odds.mma_v3_odds_sportsbooks_by_active

- **Route**: `GET /v3/mma/odds/{format}/ActiveSportsbooks`
- **Signature**: `def mma_v3_odds_sportsbooks_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], MmaV3OddsSportsbooksByActiveErrorBody]`
- **Error**: `MmaV3OddsSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Sportsbook` | `sports_data/models/sportsbook.py` |
| `MmaV3OddsSportsbooksByActiveErrorBody` | `sports_data/errors/mma_v3_odds_sportsbooks_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

