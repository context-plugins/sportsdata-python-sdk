<!-- Generated file — do not edit; regenerated with the SDK. -->

# NbaV3Odds — operations

Accessor: `client.nba_v3_odds` · Source: `sports_data/apis/nba_v3_odds.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nba_v3_odds.nba_v3_odds_betting_events_by_date

- **Route**: `GET /v3/nba/odds/{format}/BettingEventsByDate/{date}`
- **Signature**: `def nba_v3_odds_betting_events_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], NbaV3OddsBettingEventsByDateErrorBody]`
- **Error**: `NbaV3OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent2` | `sports_data/models/betting_event2.py` |
| `NbaV3OddsBettingEventsByDateErrorBody` | `sports_data/errors/nba_v3_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_events_by_season

- **Route**: `GET /v3/nba/odds/{format}/BettingEvents/{season}`
- **Signature**: `def nba_v3_odds_betting_events_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], NbaV3OddsBettingEventsBySeasonErrorBody]`
- **Error**: `NbaV3OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent2` | `sports_data/models/betting_event2.py` |
| `NbaV3OddsBettingEventsBySeasonErrorBody` | `sports_data/errors/nba_v3_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_futures_by_season

- **Route**: `GET /v3/nba/odds/{format}/BettingFuturesBySeason/{season}`
- **Signature**: `def nba_v3_odds_betting_futures_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], NbaV3OddsBettingFuturesBySeasonErrorBody]`
- **Error**: `NbaV3OddsBettingFuturesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent2` | `sports_data/models/betting_event2.py` |
| `NbaV3OddsBettingFuturesBySeasonErrorBody` | `sports_data/errors/nba_v3_odds_betting_futures_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_futures_by_season_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_betting_futures_by_season_sportsbook_group(format: FormatOrStr, season: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `sportsbookgroup`
- **Params**: `format` — path · `season` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], NbaV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent2` | `sports_data/models/betting_event2.py` |
| `NbaV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_betting_futures_by_season_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_market

- **Route**: `GET /v3/nba/odds/{format}/BettingMarket/{marketId}`
- **Signature**: `def nba_v3_odds_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, NbaV3OddsBettingMarketErrorBody]`
- **Error**: `NbaV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NbaV3OddsBettingMarketErrorBody` | `sports_data/errors/nba_v3_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_market_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_betting_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, NbaV3OddsBettingMarketSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NbaV3OddsBettingMarketSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/nba/odds/{format}/BettingMarkets/{eventId}`
- **Signature**: `def nba_v3_odds_betting_markets_by_event(format: FormatOrStr, event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NbaV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `NbaV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NbaV3OddsBettingMarketsByEventErrorBody` | `sports_data/errors/nba_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_betting_markets_by_event_sportsbook_group(format: FormatOrStr, event_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NbaV3OddsBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NbaV3OddsBettingMarketsByEventSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_markets_by_game

- **Route**: `GET /v3/nba/odds/{format}/BettingMarketsByGameID/{gameID}`
- **Signature**: `def nba_v3_odds_betting_markets_by_game(format: FormatOrStr, game_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NbaV3OddsBettingMarketsByGameErrorBody]`
- **Error**: `NbaV3OddsBettingMarketsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NbaV3OddsBettingMarketsByGameErrorBody` | `sports_data/errors/nba_v3_odds_betting_markets_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_markets_by_game_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/BettingMarketsByGameID/{gameID}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_betting_markets_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`, `sportsbookgroup`
- **Params**: `format` — path · `game_id` — path `gameID` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NbaV3OddsBettingMarketsByGameSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsBettingMarketsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NbaV3OddsBettingMarketsByGameSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_betting_markets_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/nba/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}`
- **Signature**: `def nba_v3_odds_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NbaV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `NbaV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NbaV3OddsBettingMarketsByMarketTypeErrorBody` | `sports_data/errors/nba_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_betting_markets_by_market_type_sportsbook_group(format: FormatOrStr, event_id: str, market_type_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NbaV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NbaV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_metadata

- **Route**: `GET /v3/nba/odds/{format}/BettingMetadata`
- **Signature**: `def nba_v3_odds_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `BettingEntityMetadataCollection`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection, NbaV3OddsBettingMetadataErrorBody]`
- **Error**: `NbaV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEntityMetadataCollection` | `sports_data/models/betting_entity_metadata_collection.py` |
| `NbaV3OddsBettingMetadataErrorBody` | `sports_data/errors/nba_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_player_props_by_game

- **Route**: `GET /v3/nba/odds/{format}/BettingPlayerPropsByGameID/{gameId}`
- **Signature**: `def nba_v3_odds_betting_player_props_by_game(format: FormatOrStr, game_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NbaV3OddsBettingPlayerPropsByGameErrorBody]`
- **Error**: `NbaV3OddsBettingPlayerPropsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NbaV3OddsBettingPlayerPropsByGameErrorBody` | `sports_data/errors/nba_v3_odds_betting_player_props_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_player_props_by_game_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_betting_player_props_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`, `sportsbookgroup`
- **Params**: `format` — path · `game_id` — path `gameId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NbaV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NbaV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_betting_player_props_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_results_by_market

- **Route**: `GET /v3/nba/odds/{format}/BettingMarketResults/{marketId}`
- **Signature**: `def nba_v3_odds_betting_results_by_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, NbaV3OddsBettingResultsByMarketErrorBody]`
- **Error**: `NbaV3OddsBettingResultsByMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarketResult` | `sports_data/models/betting_market_result.py` |
| `NbaV3OddsBettingResultsByMarketErrorBody` | `sports_data/errors/nba_v3_odds_betting_results_by_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_results_by_market_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_betting_results_by_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, NbaV3OddsBettingResultsByMarketSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsBettingResultsByMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarketResult` | `sports_data/models/betting_market_result.py` |
| `NbaV3OddsBettingResultsByMarketSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_betting_results_by_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_splits_by_betting_market

- **Route**: `GET /v3/nba/odds/{format}/BettingSplitsByMarketId/{marketId}`
- **Signature**: `def nba_v3_odds_betting_splits_by_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketSplit`
- **Returns (raw)**: `ApiResult[BettingMarketSplit, NbaV3OddsBettingSplitsByBettingMarketErrorBody]`
- **Error**: `NbaV3OddsBettingSplitsByBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarketSplit` | `sports_data/models/betting_market_split.py` |
| `NbaV3OddsBettingSplitsByBettingMarketErrorBody` | `sports_data/errors/nba_v3_odds_betting_splits_by_betting_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_splits_by_game

- **Route**: `GET /v3/nba/odds/{format}/BettingSplitsByGameId/{gameId}`
- **Signature**: `def nba_v3_odds_betting_splits_by_game(format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameId`
- **Returns (parsed)**: `GameBettingSplit`
- **Returns (raw)**: `ApiResult[GameBettingSplit, NbaV3OddsBettingSplitsByGameErrorBody]`
- **Error**: `NbaV3OddsBettingSplitsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameBettingSplit` | `sports_data/models/game_betting_split.py` |
| `NbaV3OddsBettingSplitsByGameErrorBody` | `sports_data/errors/nba_v3_odds_betting_splits_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_trends_by_matchup

- **Route**: `GET /v3/nba/odds/{format}/MatchupTrends/{team}/{opponent}`
- **Signature**: `def nba_v3_odds_betting_trends_by_matchup(format: FormatOrStr, team: str, opponent: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`, `opponent`
- **Params**: `format` — path · `team` — path · `opponent` — path
- **Returns (parsed)**: `MatchupTrends2`
- **Returns (raw)**: `ApiResult[MatchupTrends2, NbaV3OddsBettingTrendsByMatchupErrorBody]`
- **Error**: `NbaV3OddsBettingTrendsByMatchupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `MatchupTrends2` | `sports_data/models/matchup_trends2.py` |
| `NbaV3OddsBettingTrendsByMatchupErrorBody` | `sports_data/errors/nba_v3_odds_betting_trends_by_matchup_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_betting_trends_by_team

- **Route**: `GET /v3/nba/odds/{format}/TeamTrends/{team}`
- **Signature**: `def nba_v3_odds_betting_trends_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `TeamTrends2`
- **Returns (raw)**: `ApiResult[TeamTrends2, NbaV3OddsBettingTrendsByTeamErrorBody]`
- **Error**: `NbaV3OddsBettingTrendsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamTrends2` | `sports_data/models/team_trends2.py` |
| `NbaV3OddsBettingTrendsByTeamErrorBody` | `sports_data/errors/nba_v3_odds_betting_trends_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_in_game_odds_by_date

- **Route**: `GET /v3/nba/odds/{format}/LiveGameOddsByDate/{date}`
- **Signature**: `def nba_v3_odds_in_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NbaV3OddsInGameOddsByDateErrorBody]`
- **Error**: `NbaV3OddsInGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo` | `sports_data/models/game_info.py` |
| `NbaV3OddsInGameOddsByDateErrorBody` | `sports_data/errors/nba_v3_odds_in_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_in_game_odds_by_date_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/InGameOddsByDate/{date}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_in_game_odds_by_date_sportsbook_group(format: FormatOrStr, date: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `sportsbookgroup`
- **Params**: `format` — path · `date` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NbaV3OddsInGameOddsByDateSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsInGameOddsByDateSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo` | `sports_data/models/game_info.py` |
| `NbaV3OddsInGameOddsByDateSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_in_game_odds_by_date_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_in_game_odds_line_movement

- **Route**: `GET /v3/nba/odds/{format}/LiveGameOddsLineMovement/{gameid}`
- **Signature**: `def nba_v3_odds_in_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NbaV3OddsInGameOddsLineMovementErrorBody]`
- **Error**: `NbaV3OddsInGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo` | `sports_data/models/game_info.py` |
| `NbaV3OddsInGameOddsLineMovementErrorBody` | `sports_data/errors/nba_v3_odds_in_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_in_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/InGameLineMovement/{gameid}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_in_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NbaV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo` | `sports_data/models/game_info.py` |
| `NbaV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_in_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/InGameLineMovementWithResulting/{gameid}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult3]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult3], NbaV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfoResult3` | `sports_data/models/game_info_result3.py` |
| `NbaV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_period_game_odds_by_date

- **Route**: `GET /v3/nba/odds/{format}/AlternateMarketGameOddsByDate/{date}`
- **Signature**: `def nba_v3_odds_period_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NbaV3OddsPeriodGameOddsByDateErrorBody]`
- **Error**: `NbaV3OddsPeriodGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo` | `sports_data/models/game_info.py` |
| `NbaV3OddsPeriodGameOddsByDateErrorBody` | `sports_data/errors/nba_v3_odds_period_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_period_game_odds_line_movement

- **Route**: `GET /v3/nba/odds/{format}/AlternateMarketGameOddsLineMovement/{gameid}`
- **Signature**: `def nba_v3_odds_period_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NbaV3OddsPeriodGameOddsLineMovementErrorBody]`
- **Error**: `NbaV3OddsPeriodGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo` | `sports_data/models/game_info.py` |
| `NbaV3OddsPeriodGameOddsLineMovementErrorBody` | `sports_data/errors/nba_v3_odds_period_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/PreGameOddsByDate/{date}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(format: FormatOrStr, date: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `sportsbookgroup`
- **Params**: `format` — path · `date` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NbaV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo` | `sports_data/models/game_info.py` |
| `NbaV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/PreGameOddsLineMovement/{gameid}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NbaV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo` | `sports_data/models/game_info.py` |
| `NbaV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/nba/odds/{format}/PreGameOddsLineMovementWithResulting/{gameid}/{sportsbookgroup}`
- **Signature**: `def nba_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult3]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult3], NbaV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `NbaV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfoResult3` | `sports_data/models/game_info_result3.py` |
| `NbaV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data/errors/nba_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_pre_game_odds_by_date

- **Route**: `GET /v3/nba/odds/{format}/GameOddsByDate/{date}`
- **Signature**: `def nba_v3_odds_pre_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NbaV3OddsPreGameOddsByDateErrorBody]`
- **Error**: `NbaV3OddsPreGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo` | `sports_data/models/game_info.py` |
| `NbaV3OddsPreGameOddsByDateErrorBody` | `sports_data/errors/nba_v3_odds_pre_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_pre_game_odds_line_movement

- **Route**: `GET /v3/nba/odds/{format}/GameOddsLineMovement/{gameid}`
- **Signature**: `def nba_v3_odds_pre_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NbaV3OddsPreGameOddsLineMovementErrorBody]`
- **Error**: `NbaV3OddsPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo` | `sports_data/models/game_info.py` |
| `NbaV3OddsPreGameOddsLineMovementErrorBody` | `sports_data/errors/nba_v3_odds_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_odds.nba_v3_odds_sportsbooks_by_active

- **Route**: `GET /v3/nba/odds/{format}/ActiveSportsbooks`
- **Signature**: `def nba_v3_odds_sportsbooks_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], NbaV3OddsSportsbooksByActiveErrorBody]`
- **Error**: `NbaV3OddsSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Sportsbook` | `sports_data/models/sportsbook.py` |
| `NbaV3OddsSportsbooksByActiveErrorBody` | `sports_data/errors/nba_v3_odds_sportsbooks_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

