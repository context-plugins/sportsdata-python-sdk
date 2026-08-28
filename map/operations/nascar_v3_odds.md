<!-- Generated file — do not edit; regenerated with the SDK. -->

# NascarV3Odds — operations

Accessor: `client.nascar_v3_odds` · Source: `sports_data/apis/nascar_v3_odds.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nascar_v3_odds.nascar_v3_odds_betting_events_by_date

- **Route**: `GET /v3/nascar/odds/{format}/BettingEventsByDate/{date}`
- **Signature**: `def nascar_v3_odds_betting_events_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BettingEvent4]`
- **Returns (raw)**: `ApiResult[list[BettingEvent4], NascarV3OddsBettingEventsByDateErrorBody]`
- **Error**: `NascarV3OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent4` | `sports_data/models/betting_event4.py` |
| `NascarV3OddsBettingEventsByDateErrorBody` | `sports_data/errors/nascar_v3_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nascar_v3_odds.nascar_v3_odds_betting_events_by_season

- **Route**: `GET /v3/nascar/odds/{format}/BettingEvents/{season}`
- **Signature**: `def nascar_v3_odds_betting_events_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent4]`
- **Returns (raw)**: `ApiResult[list[BettingEvent4], NascarV3OddsBettingEventsBySeasonErrorBody]`
- **Error**: `NascarV3OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent4` | `sports_data/models/betting_event4.py` |
| `NascarV3OddsBettingEventsBySeasonErrorBody` | `sports_data/errors/nascar_v3_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nascar_v3_odds.nascar_v3_odds_betting_market

- **Route**: `GET /v3/nascar/odds/{format}/BettingMarket/{marketId}`
- **Signature**: `def nascar_v3_odds_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket3`
- **Returns (raw)**: `ApiResult[BettingMarket3, NascarV3OddsBettingMarketErrorBody]`
- **Error**: `NascarV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket3` | `sports_data/models/betting_market3.py` |
| `NascarV3OddsBettingMarketErrorBody` | `sports_data/errors/nascar_v3_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nascar_v3_odds.nascar_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/nascar/odds/{format}/BettingMarkets/{eventId}`
- **Signature**: `def nascar_v3_odds_betting_markets_by_event(format: FormatOrStr, event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket3]`
- **Returns (raw)**: `ApiResult[list[BettingMarket3], NascarV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `NascarV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket3` | `sports_data/models/betting_market3.py` |
| `NascarV3OddsBettingMarketsByEventErrorBody` | `sports_data/errors/nascar_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nascar_v3_odds.nascar_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/nascar/odds/{format}/BettingMarketsByMarketType/{eventID}/{marketTypeID}`
- **Signature**: `def nascar_v3_odds_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`
- **Params**: `format` — path · `event_id` — path `eventID` · `market_type_id` — path `marketTypeID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket3]`
- **Returns (raw)**: `ApiResult[list[BettingMarket3], NascarV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `NascarV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket3` | `sports_data/models/betting_market3.py` |
| `NascarV3OddsBettingMarketsByMarketTypeErrorBody` | `sports_data/errors/nascar_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nascar_v3_odds.nascar_v3_odds_betting_markets_by_race

- **Route**: `GET /v3/nascar/odds/{format}/BettingMarketsByRaceID/{raceID}`
- **Signature**: `def nascar_v3_odds_betting_markets_by_race(format: FormatOrStr, race_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `race_id`
- **Params**: `format` — path · `race_id` — path `raceID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket3]`
- **Returns (raw)**: `ApiResult[list[BettingMarket3], NascarV3OddsBettingMarketsByRaceErrorBody]`
- **Error**: `NascarV3OddsBettingMarketsByRaceErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket3` | `sports_data/models/betting_market3.py` |
| `NascarV3OddsBettingMarketsByRaceErrorBody` | `sports_data/errors/nascar_v3_odds_betting_markets_by_race_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nascar_v3_odds.nascar_v3_odds_betting_metadata

- **Route**: `GET /v3/nascar/odds/{format}/BettingMetaData`
- **Signature**: `def nascar_v3_odds_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `BettingEntityMetadataCollection1`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection1, NascarV3OddsBettingMetadataErrorBody]`
- **Error**: `NascarV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEntityMetadataCollection1` | `sports_data/models/betting_entity_metadata_collection1.py` |
| `NascarV3OddsBettingMetadataErrorBody` | `sports_data/errors/nascar_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nascar_v3_odds.nascar_v3_odds_race_odds

- **Route**: `GET /v3/nascar/odds/{format}/RaceOdds/{Raceid}`
- **Signature**: `def nascar_v3_odds_race_odds(format: FormatOrStr, raceid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `raceid`
- **Params**: `format` — path · `raceid` — path `Raceid`
- **Returns (parsed)**: `RaceOdds`
- **Returns (raw)**: `ApiResult[RaceOdds, NascarV3OddsRaceOddsErrorBody]`
- **Error**: `NascarV3OddsRaceOddsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `RaceOdds` | `sports_data/models/race_odds.py` |
| `NascarV3OddsRaceOddsErrorBody` | `sports_data/errors/nascar_v3_odds_race_odds_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nascar_v3_odds.nascar_v3_odds_race_odds_line_movement

- **Route**: `GET /v3/nascar/odds/{format}/RaceOddsLineMovement/{Raceid}`
- **Signature**: `def nascar_v3_odds_race_odds_line_movement(format: FormatOrStr, raceid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `raceid`
- **Params**: `format` — path · `raceid` — path `Raceid`
- **Returns (parsed)**: `RaceOdds`
- **Returns (raw)**: `ApiResult[RaceOdds, NascarV3OddsRaceOddsLineMovementErrorBody]`
- **Error**: `NascarV3OddsRaceOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `RaceOdds` | `sports_data/models/race_odds.py` |
| `NascarV3OddsRaceOddsLineMovementErrorBody` | `sports_data/errors/nascar_v3_odds_race_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nascar_v3_odds.nascar_v3_odds_sportsbooks_by_active

- **Route**: `GET /v3/nascar/odds/{format}/ActiveSportsbooks`
- **Signature**: `def nascar_v3_odds_sportsbooks_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], NascarV3OddsSportsbooksByActiveErrorBody]`
- **Error**: `NascarV3OddsSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Sportsbook` | `sports_data/models/sportsbook.py` |
| `NascarV3OddsSportsbooksByActiveErrorBody` | `sports_data/errors/nascar_v3_odds_sportsbooks_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

