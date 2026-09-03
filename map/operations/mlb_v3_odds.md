<!-- Generated file — do not edit; regenerated with the SDK. -->

# MlbV3Odds — operations

Accessor: `client.mlb_v3_odds` · Source: `sports_data_io/apis/mlb_v3_odds.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mlb_v3_odds.mlb_v3_odds_betting_events_by_date

- **Route**: `GET /v3/mlb/odds/{format}/BettingEventsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_events_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BettingEvent1]`
- **Returns (raw)**: `ApiResult[list[BettingEvent1], MlbV3OddsBettingEventsByDateErrorBody]`
- **Error**: `MlbV3OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent1` | `sports_data_io/models/betting_event1.py` |
| `MlbV3OddsBettingEventsByDateErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_events_by_season

- **Route**: `GET /v3/mlb/odds/{format}/BettingEvents/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_events_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent1]`
- **Returns (raw)**: `ApiResult[list[BettingEvent1], MlbV3OddsBettingEventsBySeasonErrorBody]`
- **Error**: `MlbV3OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent1` | `sports_data_io/models/betting_event1.py` |
| `MlbV3OddsBettingEventsBySeasonErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_futures_by_season

- **Route**: `GET /v3/mlb/odds/{format}/BettingFuturesBySeason/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_futures_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent1]`
- **Returns (raw)**: `ApiResult[list[BettingEvent1], MlbV3OddsBettingFuturesBySeasonErrorBody]`
- **Error**: `MlbV3OddsBettingFuturesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent1` | `sports_data_io/models/betting_event1.py` |
| `MlbV3OddsBettingFuturesBySeasonErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_futures_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_futures_by_season_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_futures_by_season_sportsbook_group(format: FormatOrStr, season: str, sportsbook_group: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `sportsbook_group`
- **Params**: `format` — path · `season` — path · `sportsbook_group` — path `sportsbookGroup`
- **Returns (parsed)**: `list[BettingEvent1]`
- **Returns (raw)**: `ApiResult[list[BettingEvent1], MlbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent1` | `sports_data_io/models/betting_event1.py` |
| `MlbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_futures_by_season_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_market

- **Route**: `GET /v3/mlb/odds/{format}/BettingMarket/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, MlbV3OddsBettingMarketErrorBody]`
- **Error**: `MlbV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `MlbV3OddsBettingMarketErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_market_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/BettingMarket/{marketId}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbook_group: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbook_group`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbook_group` — path `sportsbookGroup` · `include` — query
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, MlbV3OddsBettingMarketSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `MlbV3OddsBettingMarketSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/mlb/odds/{format}/BettingMarkets/{eventId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_markets_by_event(format: FormatOrStr, event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `MlbV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `MlbV3OddsBettingMarketsByEventErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_markets_by_event_sportsbook_group(format: FormatOrStr, event_id: str, sportsbook_group: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `sportsbook_group`
- **Params**: `format` — path · `event_id` — path `eventId` · `sportsbook_group` — path `sportsbookGroup` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `MlbV3OddsBettingMarketsByEventSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_markets_by_game

- **Route**: `GET /v3/mlb/odds/{format}/BettingMarketsByGameID/{gameID}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_markets_by_game(format: FormatOrStr, game_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByGameErrorBody]`
- **Error**: `MlbV3OddsBettingMarketsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `MlbV3OddsBettingMarketsByGameErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_markets_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_markets_by_game_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/BettingMarketsByGameID/{gameID}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_markets_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbook_group: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`, `sportsbook_group`
- **Params**: `format` — path · `game_id` — path `gameID` · `sportsbook_group` — path `sportsbookGroup` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByGameSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsBettingMarketsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `MlbV3OddsBettingMarketsByGameSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_markets_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/mlb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `MlbV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `MlbV3OddsBettingMarketsByMarketTypeErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/BettingMarketsByMarketType/{eventID}/{marketTypeID}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_markets_by_market_type_sportsbook_group(format: FormatOrStr, event_id: str, market_type_id: str, sportsbook_group: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`, `sportsbook_group`
- **Params**: `format` — path · `event_id` — path `eventID` · `market_type_id` — path `marketTypeID` · `sportsbook_group` — path `sportsbookGroup` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], MlbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `MlbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_metadata

- **Route**: `GET /v3/mlb/odds/{format}/BettingMetadata`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `BettingEntityMetadataCollection`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection, MlbV3OddsBettingMetadataErrorBody]`
- **Error**: `MlbV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEntityMetadataCollection` | `sports_data_io/models/betting_entity_metadata_collection.py` |
| `MlbV3OddsBettingMetadataErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_player_props_by_game

- **Route**: `GET /v3/mlb/odds/{format}/BettingPlayerPropsByGameID/{gameId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_player_props_by_game(format: FormatOrStr, game_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], MlbV3OddsBettingPlayerPropsByGameErrorBody]`
- **Error**: `MlbV3OddsBettingPlayerPropsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `MlbV3OddsBettingPlayerPropsByGameErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_player_props_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_player_props_by_game_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_player_props_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbook_group: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`, `sportsbook_group`
- **Params**: `format` — path · `game_id` — path `gameId` · `sportsbook_group` — path `sportsbookGroup` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], MlbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `MlbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_player_props_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_results_by_market

- **Route**: `GET /v3/mlb/odds/{format}/BettingMarketResults/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_results_by_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, MlbV3OddsBettingResultsByMarketErrorBody]`
- **Error**: `MlbV3OddsBettingResultsByMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketResult` | `sports_data_io/models/betting_market_result.py` |
| `MlbV3OddsBettingResultsByMarketErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_results_by_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_results_by_market_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/BettingResultsByMarket/{marketID}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_results_by_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbook_group: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbook_group`
- **Params**: `format` — path · `market_id` — path `marketID` · `sportsbook_group` — path `sportsbookGroup`
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, MlbV3OddsBettingResultsByMarketSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsBettingResultsByMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketResult` | `sports_data_io/models/betting_market_result.py` |
| `MlbV3OddsBettingResultsByMarketSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_results_by_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_splits_by_game

- **Route**: `GET /v3/mlb/odds/{format}/BettingSplitsByGameId/{gameId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_splits_by_game(format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameId`
- **Returns (parsed)**: `GameBettingSplit1`
- **Returns (raw)**: `ApiResult[GameBettingSplit1, MlbV3OddsBettingSplitsByGameErrorBody]`
- **Error**: `MlbV3OddsBettingSplitsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameBettingSplit1` | `sports_data_io/models/game_betting_split1.py` |
| `MlbV3OddsBettingSplitsByGameErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_splits_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_splits_by_betting_market

- **Route**: `GET /v3/mlb/odds/{format}/BettingSplitsByMarketId/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_splits_by_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketSplit`
- **Returns (raw)**: `ApiResult[BettingMarketSplit, MlbV3OddsBettingSplitsByBettingMarketErrorBody]`
- **Error**: `MlbV3OddsBettingSplitsByBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketSplit` | `sports_data_io/models/betting_market_split.py` |
| `MlbV3OddsBettingSplitsByBettingMarketErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_splits_by_betting_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_trends_by_matchup

- **Route**: `GET /v3/mlb/odds/{format}/MatchupTrends/{team}/{opponent}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_trends_by_matchup(format: FormatOrStr, team: str, opponent: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`, `opponent`
- **Params**: `format` — path · `team` — path · `opponent` — path
- **Returns (parsed)**: `MatchupTrends2`
- **Returns (raw)**: `ApiResult[MatchupTrends2, MlbV3OddsBettingTrendsByMatchupErrorBody]`
- **Error**: `MlbV3OddsBettingTrendsByMatchupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `MatchupTrends2` | `sports_data_io/models/matchup_trends2.py` |
| `MlbV3OddsBettingTrendsByMatchupErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_trends_by_matchup_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_betting_trends_by_team

- **Route**: `GET /v3/mlb/odds/{format}/TeamTrends/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_betting_trends_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `TeamTrends1`
- **Returns (raw)**: `ApiResult[TeamTrends1, MlbV3OddsBettingTrendsByTeamErrorBody]`
- **Error**: `MlbV3OddsBettingTrendsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamTrends1` | `sports_data_io/models/team_trends1.py` |
| `MlbV3OddsBettingTrendsByTeamErrorBody` | `sports_data_io/errors/mlb_v3_odds_betting_trends_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_in_game_odds_by_date

- **Route**: `GET /v3/mlb/odds/{format}/LiveGameOddsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_in_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], MlbV3OddsInGameOddsByDateErrorBody]`
- **Error**: `MlbV3OddsInGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo2` | `sports_data_io/models/game_info2.py` |
| `MlbV3OddsInGameOddsByDateErrorBody` | `sports_data_io/errors/mlb_v3_odds_in_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_in_game_odds_by_date_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/InGameOddsByDate/{date}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_in_game_odds_by_date_sportsbook_group(format: FormatOrStr, date: str, sportsbook_group: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `sportsbook_group`
- **Params**: `format` — path · `date` — path · `sportsbook_group` — path `sportsbookGroup`
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], MlbV3OddsInGameOddsByDateSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsInGameOddsByDateSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo2` | `sports_data_io/models/game_info2.py` |
| `MlbV3OddsInGameOddsByDateSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_in_game_odds_by_date_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_in_game_odds_line_movement

- **Route**: `GET /v3/mlb/odds/{format}/LiveGameOddsLineMovement/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_in_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], MlbV3OddsInGameOddsLineMovementErrorBody]`
- **Error**: `MlbV3OddsInGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo2` | `sports_data_io/models/game_info2.py` |
| `MlbV3OddsInGameOddsLineMovementErrorBody` | `sports_data_io/errors/mlb_v3_odds_in_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_in_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/InGameOddsLineMovement/{gameid}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_in_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbook_group: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbook_group`
- **Params**: `format` — path · `gameid` — path · `sportsbook_group` — path `sportsbookGroup`
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo2` | `sports_data_io/models/game_info2.py` |
| `MlbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_in_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/InGameOddsLineMovementWithResulting/{gameid}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbook_group: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbook_group`
- **Params**: `format` — path · `gameid` — path · `sportsbook_group` — path `sportsbookGroup`
- **Returns (parsed)**: `list[GameInfoResult2]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult2], MlbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfoResult2` | `sports_data_io/models/game_info_result2.py` |
| `MlbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_period_game_odds_by_date

- **Route**: `GET /v3/mlb/odds/{format}/AlternateMarketGameOddsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_period_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], MlbV3OddsPeriodGameOddsByDateErrorBody]`
- **Error**: `MlbV3OddsPeriodGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo2` | `sports_data_io/models/game_info2.py` |
| `MlbV3OddsPeriodGameOddsByDateErrorBody` | `sports_data_io/errors/mlb_v3_odds_period_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_period_game_odds_line_movement

- **Route**: `GET /v3/mlb/odds/{format}/AlternateMarketGameOddsLineMovement/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_period_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], MlbV3OddsPeriodGameOddsLineMovementErrorBody]`
- **Error**: `MlbV3OddsPeriodGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo2` | `sports_data_io/models/game_info2.py` |
| `MlbV3OddsPeriodGameOddsLineMovementErrorBody` | `sports_data_io/errors/mlb_v3_odds_period_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/PreGameOddsByDate/{date}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(format: FormatOrStr, date: str, sportsbook_group: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `sportsbook_group`
- **Params**: `format` — path · `date` — path · `sportsbook_group` — path `sportsbookGroup`
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo2` | `sports_data_io/models/game_info2.py` |
| `MlbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/PreGameOddsLineMovement/{gameid}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbook_group: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbook_group`
- **Params**: `format` — path · `gameid` — path · `sportsbook_group` — path `sportsbookGroup`
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], MlbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo2` | `sports_data_io/models/game_info2.py` |
| `MlbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/mlb/odds/{format}/PreGameOddsLineMovementWithResulting/{gameid}/{sportsbookGroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbook_group: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbook_group`
- **Params**: `format` — path · `gameid` — path · `sportsbook_group` — path `sportsbookGroup`
- **Returns (parsed)**: `list[GameInfoResult2]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult2], MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfoResult2` | `sports_data_io/models/game_info_result2.py` |
| `MlbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data_io/errors/mlb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_pre_game_odds_by_date

- **Route**: `GET /v3/mlb/odds/{format}/GameOddsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_pre_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], MlbV3OddsPreGameOddsByDateErrorBody]`
- **Error**: `MlbV3OddsPreGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo2` | `sports_data_io/models/game_info2.py` |
| `MlbV3OddsPreGameOddsByDateErrorBody` | `sports_data_io/errors/mlb_v3_odds_pre_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_pre_game_odds_line_movement

- **Route**: `GET /v3/mlb/odds/{format}/GameOddsLineMovement/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_pre_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], MlbV3OddsPreGameOddsLineMovementErrorBody]`
- **Error**: `MlbV3OddsPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo2` | `sports_data_io/models/game_info2.py` |
| `MlbV3OddsPreGameOddsLineMovementErrorBody` | `sports_data_io/errors/mlb_v3_odds_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_odds.mlb_v3_odds_sportsbooks_by_active

- **Route**: `GET /v3/mlb/odds/{format}/ActiveSportsbooks`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_odds_sportsbooks_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], MlbV3OddsSportsbooksByActiveErrorBody]`
- **Error**: `MlbV3OddsSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Sportsbook` | `sports_data_io/models/sportsbook.py` |
| `MlbV3OddsSportsbooksByActiveErrorBody` | `sports_data_io/errors/mlb_v3_odds_sportsbooks_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

