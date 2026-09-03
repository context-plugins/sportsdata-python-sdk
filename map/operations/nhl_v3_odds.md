<!-- Generated file — do not edit; regenerated with the SDK. -->

# NhlV3Odds — operations

Accessor: `client.nhl_v3_odds` · Source: `sports_data_io/apis/nhl_v3_odds.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nhl_v3_odds.nhl_v3_odds_betting_events_by_date

- **Route**: `GET /v3/nhl/odds/{format}/BettingEventsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_events_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BettingEvent1]`
- **Returns (raw)**: `ApiResult[list[BettingEvent1], NhlV3OddsBettingEventsByDateErrorBody]`
- **Error**: `NhlV3OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent1` | `sports_data_io/models/betting_event1.py` |
| `NhlV3OddsBettingEventsByDateErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_events_by_season

- **Route**: `GET /v3/nhl/odds/{format}/BettingEvents/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_events_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent1]`
- **Returns (raw)**: `ApiResult[list[BettingEvent1], NhlV3OddsBettingEventsBySeasonErrorBody]`
- **Error**: `NhlV3OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent1` | `sports_data_io/models/betting_event1.py` |
| `NhlV3OddsBettingEventsBySeasonErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_futures_by_season

- **Route**: `GET /v3/nhl/odds/{format}/BettingFuturesBySeason/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_futures_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent1]`
- **Returns (raw)**: `ApiResult[list[BettingEvent1], NhlV3OddsBettingFuturesBySeasonErrorBody]`
- **Error**: `NhlV3OddsBettingFuturesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent1` | `sports_data_io/models/betting_event1.py` |
| `NhlV3OddsBettingFuturesBySeasonErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_futures_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_futures_by_season_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_futures_by_season_sportsbook_group(format: FormatOrStr, season: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `sportsbookgroup`
- **Params**: `format` — path · `season` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingEvent1]`
- **Returns (raw)**: `ApiResult[list[BettingEvent1], NhlV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent1` | `sports_data_io/models/betting_event1.py` |
| `NhlV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_futures_by_season_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_market

- **Route**: `GET /v3/nhl/odds/{format}/BettingMarket/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, NhlV3OddsBettingMarketErrorBody]`
- **Error**: `NhlV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NhlV3OddsBettingMarketErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_market_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, NhlV3OddsBettingMarketSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NhlV3OddsBettingMarketSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/nhl/odds/{format}/BettingMarkets/{eventId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_markets_by_event(format: FormatOrStr, event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NhlV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `NhlV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NhlV3OddsBettingMarketsByEventErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_markets_by_event_sportsbook_group(format: FormatOrStr, event_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NhlV3OddsBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NhlV3OddsBettingMarketsByEventSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_markets_by_game

- **Route**: `GET /v3/nhl/odds/{format}/BettingMarketsByGameID/{gameID}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_markets_by_game(format: FormatOrStr, game_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NhlV3OddsBettingMarketsByGameErrorBody]`
- **Error**: `NhlV3OddsBettingMarketsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NhlV3OddsBettingMarketsByGameErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_markets_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_markets_by_game_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/BettingMarketsByGameID/{gameID}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_markets_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`, `sportsbookgroup`
- **Params**: `format` — path · `game_id` — path `gameID` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NhlV3OddsBettingMarketsByGameSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsBettingMarketsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NhlV3OddsBettingMarketsByGameSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_markets_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/nhl/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NhlV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `NhlV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NhlV3OddsBettingMarketsByMarketTypeErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_markets_by_market_type_sportsbook_group(format: FormatOrStr, event_id: str, market_type_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NhlV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NhlV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_metadata

- **Route**: `GET /v3/nhl/odds/{format}/Bettingmetadata`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `BettingEntityMetadataCollection`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection, NhlV3OddsBettingMetadataErrorBody]`
- **Error**: `NhlV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEntityMetadataCollection` | `sports_data_io/models/betting_entity_metadata_collection.py` |
| `NhlV3OddsBettingMetadataErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_player_props_by_game

- **Route**: `GET /v3/nhl/odds/{format}/BettingPlayerPropsByGameID/{gameId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_player_props_by_game(format: FormatOrStr, game_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NhlV3OddsBettingPlayerPropsByGameErrorBody]`
- **Error**: `NhlV3OddsBettingPlayerPropsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NhlV3OddsBettingPlayerPropsByGameErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_player_props_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_player_props_by_game_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_player_props_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`, `sportsbookgroup`
- **Params**: `format` — path · `game_id` — path `gameId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NhlV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NhlV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_player_props_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_results_by_market

- **Route**: `GET /v3/nhl/odds/{format}/BettingMarketResults/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_results_by_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, NhlV3OddsBettingResultsByMarketErrorBody]`
- **Error**: `NhlV3OddsBettingResultsByMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketResult` | `sports_data_io/models/betting_market_result.py` |
| `NhlV3OddsBettingResultsByMarketErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_results_by_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_results_by_market_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_results_by_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, NhlV3OddsBettingResultsByMarketSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsBettingResultsByMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketResult` | `sports_data_io/models/betting_market_result.py` |
| `NhlV3OddsBettingResultsByMarketSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_results_by_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_splits_by_betting_market

- **Route**: `GET /v3/nhl/odds/{format}/BettingSplitsByMarketId/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_splits_by_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketSplit`
- **Returns (raw)**: `ApiResult[BettingMarketSplit, NhlV3OddsBettingSplitsByBettingMarketErrorBody]`
- **Error**: `NhlV3OddsBettingSplitsByBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketSplit` | `sports_data_io/models/betting_market_split.py` |
| `NhlV3OddsBettingSplitsByBettingMarketErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_splits_by_betting_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_splits_by_game

- **Route**: `GET /v3/nhl/odds/{format}/BettingSplitsByGameId/{gameId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_splits_by_game(format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameId`
- **Returns (parsed)**: `GameBettingSplit1`
- **Returns (raw)**: `ApiResult[GameBettingSplit1, NhlV3OddsBettingSplitsByGameErrorBody]`
- **Error**: `NhlV3OddsBettingSplitsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameBettingSplit1` | `sports_data_io/models/game_betting_split1.py` |
| `NhlV3OddsBettingSplitsByGameErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_splits_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_trends_by_matchup

- **Route**: `GET /v3/nhl/odds/{format}/MatchupTrends/{team}/{opponent}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_trends_by_matchup(format: FormatOrStr, team: str, opponent: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`, `opponent`
- **Params**: `format` — path · `team` — path · `opponent` — path
- **Returns (parsed)**: `MatchupTrends3`
- **Returns (raw)**: `ApiResult[MatchupTrends3, NhlV3OddsBettingTrendsByMatchupErrorBody]`
- **Error**: `NhlV3OddsBettingTrendsByMatchupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `MatchupTrends3` | `sports_data_io/models/matchup_trends3.py` |
| `NhlV3OddsBettingTrendsByMatchupErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_trends_by_matchup_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_betting_trends_by_team

- **Route**: `GET /v3/nhl/odds/{format}/TeamTrends/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_betting_trends_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `TeamTrends1`
- **Returns (raw)**: `ApiResult[TeamTrends1, NhlV3OddsBettingTrendsByTeamErrorBody]`
- **Error**: `NhlV3OddsBettingTrendsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamTrends1` | `sports_data_io/models/team_trends1.py` |
| `NhlV3OddsBettingTrendsByTeamErrorBody` | `sports_data_io/errors/nhl_v3_odds_betting_trends_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_in_game_odds_by_date

- **Route**: `GET /v3/nhl/odds/{format}/LiveGameOddsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_in_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo3]`
- **Returns (raw)**: `ApiResult[list[GameInfo3], NhlV3OddsInGameOddsByDateErrorBody]`
- **Error**: `NhlV3OddsInGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo3` | `sports_data_io/models/game_info3.py` |
| `NhlV3OddsInGameOddsByDateErrorBody` | `sports_data_io/errors/nhl_v3_odds_in_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_in_game_odds_by_date_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/InGameOddsByDate/{date}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_in_game_odds_by_date_sportsbook_group(format: FormatOrStr, date: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `sportsbookgroup`
- **Params**: `format` — path · `date` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo3]`
- **Returns (raw)**: `ApiResult[list[GameInfo3], NhlV3OddsInGameOddsByDateSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsInGameOddsByDateSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo3` | `sports_data_io/models/game_info3.py` |
| `NhlV3OddsInGameOddsByDateSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_in_game_odds_by_date_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_in_game_odds_line_movement

- **Route**: `GET /v3/nhl/odds/{format}/LiveGameOddsLineMovement/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_in_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo3]`
- **Returns (raw)**: `ApiResult[list[GameInfo3], NhlV3OddsInGameOddsLineMovementErrorBody]`
- **Error**: `NhlV3OddsInGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo3` | `sports_data_io/models/game_info3.py` |
| `NhlV3OddsInGameOddsLineMovementErrorBody` | `sports_data_io/errors/nhl_v3_odds_in_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_in_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/InGameLineMovement/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_in_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo3]`
- **Returns (raw)**: `ApiResult[list[GameInfo3], NhlV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo3` | `sports_data_io/models/game_info3.py` |
| `NhlV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_in_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/InGameLineMovementWithResulting/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult3]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult3], NhlV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfoResult3` | `sports_data_io/models/game_info_result3.py` |
| `NhlV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_period_game_odds_by_date

- **Route**: `GET /v3/nhl/odds/{format}/AlternateMarketGameOddsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_period_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo3]`
- **Returns (raw)**: `ApiResult[list[GameInfo3], NhlV3OddsPeriodGameOddsByDateErrorBody]`
- **Error**: `NhlV3OddsPeriodGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo3` | `sports_data_io/models/game_info3.py` |
| `NhlV3OddsPeriodGameOddsByDateErrorBody` | `sports_data_io/errors/nhl_v3_odds_period_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_period_game_odds_line_movement

- **Route**: `GET /v3/nhl/odds/{format}/AlternateMarketGameOddsLineMovement/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_period_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo3]`
- **Returns (raw)**: `ApiResult[list[GameInfo3], NhlV3OddsPeriodGameOddsLineMovementErrorBody]`
- **Error**: `NhlV3OddsPeriodGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo3` | `sports_data_io/models/game_info3.py` |
| `NhlV3OddsPeriodGameOddsLineMovementErrorBody` | `sports_data_io/errors/nhl_v3_odds_period_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/PreGameOddsByDate/{date}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(format: FormatOrStr, date: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `sportsbookgroup`
- **Params**: `format` — path · `date` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo3]`
- **Returns (raw)**: `ApiResult[list[GameInfo3], NhlV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo3` | `sports_data_io/models/game_info3.py` |
| `NhlV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/PreGameOddsLineMovement/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo3]`
- **Returns (raw)**: `ApiResult[list[GameInfo3], NhlV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo3` | `sports_data_io/models/game_info3.py` |
| `NhlV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/nhl/odds/{format}/PreGameOddsLineMovementWithResulting/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult3]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult3], NhlV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `NhlV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfoResult3` | `sports_data_io/models/game_info_result3.py` |
| `NhlV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data_io/errors/nhl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_pre_game_odds_by_date

- **Route**: `GET /v3/nhl/odds/{format}/GameOddsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_pre_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo3]`
- **Returns (raw)**: `ApiResult[list[GameInfo3], NhlV3OddsPreGameOddsByDateErrorBody]`
- **Error**: `NhlV3OddsPreGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo3` | `sports_data_io/models/game_info3.py` |
| `NhlV3OddsPreGameOddsByDateErrorBody` | `sports_data_io/errors/nhl_v3_odds_pre_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_pre_game_odds_line_movement

- **Route**: `GET /v3/nhl/odds/{format}/GameOddsLineMovement/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_pre_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo3]`
- **Returns (raw)**: `ApiResult[list[GameInfo3], NhlV3OddsPreGameOddsLineMovementErrorBody]`
- **Error**: `NhlV3OddsPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo3` | `sports_data_io/models/game_info3.py` |
| `NhlV3OddsPreGameOddsLineMovementErrorBody` | `sports_data_io/errors/nhl_v3_odds_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_odds.nhl_v3_odds_sportsbooks_by_active

- **Route**: `GET /v3/nhl/odds/{format}/ActiveSportsbooks`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_odds_sportsbooks_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], NhlV3OddsSportsbooksByActiveErrorBody]`
- **Error**: `NhlV3OddsSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Sportsbook` | `sports_data_io/models/sportsbook.py` |
| `NhlV3OddsSportsbooksByActiveErrorBody` | `sports_data_io/errors/nhl_v3_odds_sportsbooks_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

