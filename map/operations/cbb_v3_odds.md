<!-- Generated file — do not edit; regenerated with the SDK. -->

# CbbV3Odds — operations

Accessor: `client.cbb_v3_odds` · Source: `cbb_api/apis/cbb_v3_odds.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cbb_v3_odds.cbb_v3_odds_alternate_market_pre_game_odds_by_date

- **Route**: `GET /v3/cbb/odds/{format}/AlternateMarketGameOddsByDate/{date}`
- **Signature**: `def cbb_v3_odds_alternate_market_pre_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody]`
- **Error**: `CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfo` | `cbb_api/models/game_info.py` |
| `CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody` | `cbb_api/errors/cbb_v3_odds_alternate_market_pre_game_odds_by_date_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_alternate_market_pre_game_odds_line_movement

- **Route**: `GET /v3/cbb/odds/{format}/AlternateMarketGameOddsLineMovement/{gameid}`
- **Signature**: `def cbb_v3_odds_alternate_market_pre_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], CbbV3OddsAlternateMarketPreGameOddsLineMovementErrorBody]`
- **Error**: `CbbV3OddsAlternateMarketPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfo` | `cbb_api/models/game_info.py` |
| `CbbV3OddsAlternateMarketPreGameOddsLineMovementErrorBody` | `cbb_api/errors/cbb_v3_odds_alternate_market_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_events_by_date

- **Route**: `GET /v3/cbb/odds/{format}/BettingEventsByDate/{date}`
- **Signature**: `def cbb_v3_odds_betting_events_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], CbbV3OddsBettingEventsByDateErrorBody]`
- **Error**: `CbbV3OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `BettingEvent` | `cbb_api/models/betting_event.py` |
| `CbbV3OddsBettingEventsByDateErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_events_by_season

- **Route**: `GET /v3/cbb/odds/{format}/BettingEvents/{season}`
- **Signature**: `def cbb_v3_odds_betting_events_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], CbbV3OddsBettingEventsBySeasonErrorBody]`
- **Error**: `CbbV3OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `BettingEvent` | `cbb_api/models/betting_event.py` |
| `CbbV3OddsBettingEventsBySeasonErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_futures_by_season

- **Route**: `GET /v3/cbb/odds/{format}/BettingFuturesBySeason/{season}`
- **Signature**: `def cbb_v3_odds_betting_futures_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], CbbV3OddsBettingFuturesBySeasonErrorBody]`
- **Error**: `CbbV3OddsBettingFuturesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `BettingEvent` | `cbb_api/models/betting_event.py` |
| `CbbV3OddsBettingFuturesBySeasonErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_futures_by_season_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_futures_by_season_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_betting_futures_by_season_sportsbook_group(format: FormatOrStr, season: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `sportsbookgroup`
- **Params**: `format` — path · `season` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], CbbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `BettingEvent` | `cbb_api/models/betting_event.py` |
| `CbbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_futures_by_season_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_market

- **Route**: `GET /v3/cbb/odds/{format}/BettingMarket/{marketId}`
- **Signature**: `def cbb_v3_odds_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, CbbV3OddsBettingMarketErrorBody]`
- **Error**: `CbbV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `BettingMarket` | `cbb_api/models/betting_market.py` |
| `CbbV3OddsBettingMarketErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_market_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_market_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_betting_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, CbbV3OddsBettingMarketSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `BettingMarket` | `cbb_api/models/betting_market.py` |
| `CbbV3OddsBettingMarketSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/cbb/odds/{format}/BettingMarkets/{eventId}`
- **Signature**: `def cbb_v3_odds_betting_markets_by_event(format: FormatOrStr, event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `CbbV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `IncludeOrStr` | `cbb_api/models/enums/include.py` |
| `BettingMarket` | `cbb_api/models/betting_market.py` |
| `CbbV3OddsBettingMarketsByEventErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_betting_markets_by_event_sportsbook_group(format: FormatOrStr, event_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `IncludeOrStr` | `cbb_api/models/enums/include.py` |
| `BettingMarket` | `cbb_api/models/betting_market.py` |
| `CbbV3OddsBettingMarketsByEventSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_markets_by_game

- **Route**: `GET /v3/cbb/odds/{format}/BettingMarketsByGameID/{gameid}`
- **Signature**: `def cbb_v3_odds_betting_markets_by_game(format: FormatOrStr, gameid: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByGameErrorBody]`
- **Error**: `CbbV3OddsBettingMarketsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `IncludeOrStr` | `cbb_api/models/enums/include.py` |
| `BettingMarket` | `cbb_api/models/betting_market.py` |
| `CbbV3OddsBettingMarketsByGameErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_markets_by_game_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_markets_by_game_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/BettingMarketsByGameID/{gameid}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_betting_markets_by_game_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByGameSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsBettingMarketsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `IncludeOrStr` | `cbb_api/models/enums/include.py` |
| `BettingMarket` | `cbb_api/models/betting_market.py` |
| `CbbV3OddsBettingMarketsByGameSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_markets_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/cbb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}`
- **Signature**: `def cbb_v3_odds_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `CbbV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `IncludeOrStr` | `cbb_api/models/enums/include.py` |
| `BettingMarket` | `cbb_api/models/betting_market.py` |
| `CbbV3OddsBettingMarketsByMarketTypeErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_betting_markets_by_market_type_sportsbook_group(format: FormatOrStr, event_id: str, market_type_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `IncludeOrStr` | `cbb_api/models/enums/include.py` |
| `BettingMarket` | `cbb_api/models/betting_market.py` |
| `CbbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_metadata

- **Route**: `GET /v3/cbb/odds/{format}/BettingMetadata`
- **Signature**: `def cbb_v3_odds_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `BettingEntityMetadataCollection`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection, CbbV3OddsBettingMetadataErrorBody]`
- **Error**: `CbbV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `BettingEntityMetadataCollection` | `cbb_api/models/betting_entity_metadata_collection.py` |
| `CbbV3OddsBettingMetadataErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_player_props_by_game

- **Route**: `GET /v3/cbb/odds/{format}/BettingPlayerPropsByGameID/{gameId}`
- **Signature**: `def cbb_v3_odds_betting_player_props_by_game(format: FormatOrStr, game_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CbbV3OddsBettingPlayerPropsByGameErrorBody]`
- **Error**: `CbbV3OddsBettingPlayerPropsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `IncludeOrStr` | `cbb_api/models/enums/include.py` |
| `BettingMarket` | `cbb_api/models/betting_market.py` |
| `CbbV3OddsBettingPlayerPropsByGameErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_player_props_by_game_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_player_props_by_game_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_betting_player_props_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`, `sportsbookgroup`
- **Params**: `format` — path · `game_id` — path `gameId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CbbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `IncludeOrStr` | `cbb_api/models/enums/include.py` |
| `BettingMarket` | `cbb_api/models/betting_market.py` |
| `CbbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_player_props_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_results_by_market

- **Route**: `GET /v3/cbb/odds/{format}/BettingMarketResults/{marketId}`
- **Signature**: `def cbb_v3_odds_betting_results_by_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, CbbV3OddsBettingResultsByMarketErrorBody]`
- **Error**: `CbbV3OddsBettingResultsByMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `BettingMarketResult` | `cbb_api/models/betting_market_result.py` |
| `CbbV3OddsBettingResultsByMarketErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_results_by_market_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_results_by_market_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_betting_results_by_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, CbbV3OddsBettingResultsByMarketSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsBettingResultsByMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `BettingMarketResult` | `cbb_api/models/betting_market_result.py` |
| `CbbV3OddsBettingResultsByMarketSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_results_by_market_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_splits_by_betting_market

- **Route**: `GET /v3/cbb/odds/{format}/BettingSplitsByMarketId/{marketId}`
- **Signature**: `def cbb_v3_odds_betting_splits_by_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketSplit`
- **Returns (raw)**: `ApiResult[BettingMarketSplit, CbbV3OddsBettingSplitsByBettingMarketErrorBody]`
- **Error**: `CbbV3OddsBettingSplitsByBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `BettingMarketSplit` | `cbb_api/models/betting_market_split.py` |
| `CbbV3OddsBettingSplitsByBettingMarketErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_splits_by_betting_market_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_splits_by_game

- **Route**: `GET /v3/cbb/odds/{format}/BettingSplitsByGameId/{gameId}`
- **Signature**: `def cbb_v3_odds_betting_splits_by_game(format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameId`
- **Returns (parsed)**: `GameBettingSplit`
- **Returns (raw)**: `ApiResult[GameBettingSplit, CbbV3OddsBettingSplitsByGameErrorBody]`
- **Error**: `CbbV3OddsBettingSplitsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameBettingSplit` | `cbb_api/models/game_betting_split.py` |
| `CbbV3OddsBettingSplitsByGameErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_splits_by_game_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_trends_by_matchup

- **Route**: `GET /v3/cbb/odds/{format}/MatchupTrends/{team}/{opponent}`
- **Signature**: `def cbb_v3_odds_betting_trends_by_matchup(format: FormatOrStr, team: str, opponent: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`, `opponent`
- **Params**: `format` — path · `team` — path · `opponent` — path
- **Returns (parsed)**: `MatchupTrends`
- **Returns (raw)**: `ApiResult[MatchupTrends, CbbV3OddsBettingTrendsByMatchupErrorBody]`
- **Error**: `CbbV3OddsBettingTrendsByMatchupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `MatchupTrends` | `cbb_api/models/matchup_trends.py` |
| `CbbV3OddsBettingTrendsByMatchupErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_trends_by_matchup_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_betting_trends_by_team

- **Route**: `GET /v3/cbb/odds/{format}/TeamTrends/{team}`
- **Signature**: `def cbb_v3_odds_betting_trends_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `TeamTrends`
- **Returns (raw)**: `ApiResult[TeamTrends, CbbV3OddsBettingTrendsByTeamErrorBody]`
- **Error**: `CbbV3OddsBettingTrendsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `TeamTrends` | `cbb_api/models/team_trends.py` |
| `CbbV3OddsBettingTrendsByTeamErrorBody` | `cbb_api/errors/cbb_v3_odds_betting_trends_by_team_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_in_game_odds_by_date

- **Route**: `GET /v3/cbb/odds/{format}/LiveGameOddsByDate/{date}`
- **Signature**: `def cbb_v3_odds_in_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], CbbV3OddsInGameOddsByDateErrorBody]`
- **Error**: `CbbV3OddsInGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfo` | `cbb_api/models/game_info.py` |
| `CbbV3OddsInGameOddsByDateErrorBody` | `cbb_api/errors/cbb_v3_odds_in_game_odds_by_date_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_in_game_odds_by_date_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/InGameOddsByDate/{date}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_in_game_odds_by_date_sportsbook_group(format: FormatOrStr, date: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `sportsbookgroup`
- **Params**: `format` — path · `date` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], CbbV3OddsInGameOddsByDateSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsInGameOddsByDateSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfo` | `cbb_api/models/game_info.py` |
| `CbbV3OddsInGameOddsByDateSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_in_game_odds_by_date_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_in_game_odds_line_movement

- **Route**: `GET /v3/cbb/odds/{format}/LiveGameOddsLineMovement/{gameid}`
- **Signature**: `def cbb_v3_odds_in_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], CbbV3OddsInGameOddsLineMovementErrorBody]`
- **Error**: `CbbV3OddsInGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfo` | `cbb_api/models/game_info.py` |
| `CbbV3OddsInGameOddsLineMovementErrorBody` | `cbb_api/errors/cbb_v3_odds_in_game_odds_line_movement_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_in_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/InGameLineMovement/{gameid}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_in_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], CbbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfo` | `cbb_api/models/game_info.py` |
| `CbbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_in_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/InGameLineMovementWithResulting/{gameid}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult], CbbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfoResult` | `cbb_api/models/game_info_result.py` |
| `CbbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/PreGameOddsByDate/{date}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(format: FormatOrStr, date: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `sportsbookgroup`
- **Params**: `format` — path · `date` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], CbbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfo` | `cbb_api/models/game_info.py` |
| `CbbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/PreGameOddsLineMovement/{gameid}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfo` | `cbb_api/models/game_info.py` |
| `CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/cbb/odds/{format}/PreGameOddsLineMovementWithResulting/{gameid}/{sportsbookgroup}`
- **Signature**: `def cbb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult], CbbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `CbbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfoResult` | `cbb_api/models/game_info_result.py` |
| `CbbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `cbb_api/errors/cbb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_pre_game_odds_by_date

- **Route**: `GET /v3/cbb/odds/{format}/GameOddsByDate/{date}`
- **Signature**: `def cbb_v3_odds_pre_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], CbbV3OddsPreGameOddsByDateErrorBody]`
- **Error**: `CbbV3OddsPreGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfo` | `cbb_api/models/game_info.py` |
| `CbbV3OddsPreGameOddsByDateErrorBody` | `cbb_api/errors/cbb_v3_odds_pre_game_odds_by_date_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_pre_game_odds_line_movement

- **Route**: `GET /v3/cbb/odds/{format}/GameOddsLineMovement/{gameid}`
- **Signature**: `def cbb_v3_odds_pre_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], CbbV3OddsPreGameOddsLineMovementErrorBody]`
- **Error**: `CbbV3OddsPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `GameInfo` | `cbb_api/models/game_info.py` |
| `CbbV3OddsPreGameOddsLineMovementErrorBody` | `cbb_api/errors/cbb_v3_odds_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_odds.cbb_v3_odds_sportsbooks_by_active

- **Route**: `GET /v3/cbb/odds/{format}/ActiveSportsbooks`
- **Signature**: `def cbb_v3_odds_sportsbooks_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], CbbV3OddsSportsbooksByActiveErrorBody]`
- **Error**: `CbbV3OddsSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Sportsbook` | `cbb_api/models/sportsbook.py` |
| `CbbV3OddsSportsbooksByActiveErrorBody` | `cbb_api/errors/cbb_v3_odds_sportsbooks_by_active_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

