<!-- Generated file — do not edit; regenerated with the SDK. -->

# NflV3Odds — operations

Accessor: `client.nfl_v3_odds` · Source: `sports_data_io/apis/nfl_v3_odds.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nfl_v3_odds.nfl_v3_odds_betting_events_by_date

- **Route**: `GET /v3/nfl/odds/{format}/BettingEventsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_events_by_date(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], NflV3OddsBettingEventsByDateErrorBody]`
- **Error**: `NflV3OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent` | `sports_data_io/models/betting_event.py` |
| `NflV3OddsBettingEventsByDateErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_events_by_season

- **Route**: `GET /v3/nfl/odds/{format}/BettingEvents/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_events_by_season(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], NflV3OddsBettingEventsBySeasonErrorBody]`
- **Error**: `NflV3OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent` | `sports_data_io/models/betting_event.py` |
| `NflV3OddsBettingEventsBySeasonErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_futures_by_season

- **Route**: `GET /v3/nfl/odds/{format}/BettingFuturesBySeason/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_futures_by_season(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], NflV3OddsBettingFuturesBySeasonErrorBody]`
- **Error**: `NflV3OddsBettingFuturesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent` | `sports_data_io/models/betting_event.py` |
| `NflV3OddsBettingFuturesBySeasonErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_futures_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_futures_by_season_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_futures_by_season_sportsbook_group(season: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `season` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], NflV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent` | `sports_data_io/models/betting_event.py` |
| `NflV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_futures_by_season_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_market

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarket/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_market(market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `market_id`
- **Params**: `format_` — path `format` · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, NflV3OddsBettingMarketErrorBody]`
- **Error**: `NflV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NflV3OddsBettingMarketErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_market_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_market_sportsbook_group(market_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `market_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, NflV3OddsBettingMarketSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NflV3OddsBettingMarketSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarkets/{eventId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_markets_by_event(event_id: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `event_id`
- **Params**: `format_` — path `format` · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NflV3OddsBettingMarketsByEventErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_markets_by_event_sportsbook_group(event_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `event_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `event_id` — path `eventId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NflV3OddsBettingMarketsByEventSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_game

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketsByScoreID/{scoreid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_markets_by_game(scoreid: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`
- **Params**: `format_` — path `format` · `scoreid` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByGameErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NflV3OddsBettingMarketsByGameErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_markets_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_game_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketsByGameID/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_markets_by_game_sportsbook_group(gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `gameid` — path · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByGameSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NflV3OddsBettingMarketsByGameSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_markets_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_markets_by_market_type(event_id: str, market_type_id: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `event_id`, `market_type_id`
- **Params**: `format_` — path `format` · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NflV3OddsBettingMarketsByMarketTypeErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_markets_by_market_type_sportsbook_group(event_id: str, market_type_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `event_id`, `market_type_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NflV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_metadata

- **Route**: `GET /v3/nfl/odds/{format}/BettingMetadata`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_metadata(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `BettingEntityMetadataCollection`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection, NflV3OddsBettingMetadataErrorBody]`
- **Error**: `NflV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEntityMetadataCollection` | `sports_data_io/models/betting_entity_metadata_collection.py` |
| `NflV3OddsBettingMetadataErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_player_props_by_game

- **Route**: `GET /v3/nfl/odds/{format}/BettingPlayerPropsByScoreID/{scoreid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_player_props_by_game(scoreid: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`
- **Params**: `format_` — path `format` · `scoreid` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingPlayerPropsByGameErrorBody]`
- **Error**: `NflV3OddsBettingPlayerPropsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NflV3OddsBettingPlayerPropsByGameErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_player_props_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_player_props_by_game_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingPlayerPropsByScoreID/{scoreid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_player_props_by_game_sportsbook_group(scoreid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `scoreid` — path · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `NflV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_player_props_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_results_by_market

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketResults/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_results_by_market(market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `market_id`
- **Params**: `format_` — path `format` · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, NflV3OddsBettingResultsByMarketErrorBody]`
- **Error**: `NflV3OddsBettingResultsByMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketResult` | `sports_data_io/models/betting_market_result.py` |
| `NflV3OddsBettingResultsByMarketErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_results_by_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_results_by_market_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_results_by_market_sportsbook_group(market_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `market_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, NflV3OddsBettingResultsByMarketSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingResultsByMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketResult` | `sports_data_io/models/betting_market_result.py` |
| `NflV3OddsBettingResultsByMarketSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_results_by_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_splits_by_betting_market

- **Route**: `GET /v3/nfl/odds/{format}/BettingSplitsByMarketId/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_splits_by_betting_market(market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `market_id`
- **Params**: `format_` — path `format` · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketSplit`
- **Returns (raw)**: `ApiResult[BettingMarketSplit, NflV3OddsBettingSplitsByBettingMarketErrorBody]`
- **Error**: `NflV3OddsBettingSplitsByBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketSplit` | `sports_data_io/models/betting_market_split.py` |
| `NflV3OddsBettingSplitsByBettingMarketErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_splits_by_betting_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_splits_by_game

- **Route**: `GET /v3/nfl/odds/{format}/BettingSplitsByScoreId/{scoreId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_splits_by_game(score_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `score_id`
- **Params**: `format_` — path `format` · `score_id` — path `scoreId`
- **Returns (parsed)**: `GameBettingSplit`
- **Returns (raw)**: `ApiResult[GameBettingSplit, NflV3OddsBettingSplitsByGameErrorBody]`
- **Error**: `NflV3OddsBettingSplitsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameBettingSplit` | `sports_data_io/models/game_betting_split.py` |
| `NflV3OddsBettingSplitsByGameErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_splits_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_trends_by_matchup

- **Route**: `GET /v3/nfl/odds/{format}/MatchupTrends/{team}/{opponent}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_trends_by_matchup(team: str, opponent: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`, `opponent`
- **Params**: `format_` — path `format` · `team` — path · `opponent` — path
- **Returns (parsed)**: `MatchupTrends`
- **Returns (raw)**: `ApiResult[MatchupTrends, NflV3OddsBettingTrendsByMatchupErrorBody]`
- **Error**: `NflV3OddsBettingTrendsByMatchupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `MatchupTrends` | `sports_data_io/models/matchup_trends.py` |
| `NflV3OddsBettingTrendsByMatchupErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_trends_by_matchup_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_trends_by_team

- **Route**: `GET /v3/nfl/odds/{format}/TeamTrends/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_betting_trends_by_team(team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`
- **Params**: `format_` — path `format` · `team` — path
- **Returns (parsed)**: `TeamTrends`
- **Returns (raw)**: `ApiResult[TeamTrends, NflV3OddsBettingTrendsByTeamErrorBody]`
- **Error**: `NflV3OddsBettingTrendsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamTrends` | `sports_data_io/models/team_trends.py` |
| `NflV3OddsBettingTrendsByTeamErrorBody` | `sports_data_io/errors/nfl_v3_odds_betting_trends_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_in_game_odds_by_week

- **Route**: `GET /v3/nfl/odds/{format}/LiveGameOddsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_in_game_odds_by_week(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NflV3OddsInGameOddsByWeekErrorBody]`
- **Error**: `NflV3OddsInGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo` | `sports_data_io/models/game_info.py` |
| `NflV3OddsInGameOddsByWeekErrorBody` | `sports_data_io/errors/nfl_v3_odds_in_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_in_game_odds_by_week_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/InGameOddsByWeek/{season}/{week}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_in_game_odds_by_week_sportsbook_group(season: str, week: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo` | `sports_data_io/models/game_info.py` |
| `NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_in_game_odds_by_week_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_in_game_odds_line_movement

- **Route**: `GET /v3/nfl/odds/{format}/LiveGameOddsLineMovement/{scoreid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_in_game_odds_line_movement(scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`
- **Params**: `format_` — path `format` · `scoreid` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NflV3OddsInGameOddsLineMovementErrorBody]`
- **Error**: `NflV3OddsInGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo` | `sports_data_io/models/game_info.py` |
| `NflV3OddsInGameOddsLineMovementErrorBody` | `sports_data_io/errors/nfl_v3_odds_in_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_in_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/InGameLineMovement/{scoreid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_in_game_odds_line_movement_sportsbook_group(scoreid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `scoreid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NflV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo` | `sports_data_io/models/game_info.py` |
| `NflV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_in_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/InGameLineMovementWithResulting/{scoreid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(scoreid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `scoreid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult], NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfoResult` | `sports_data_io/models/game_info_result.py` |
| `NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_period_game_odds_by_week

- **Route**: `GET /v3/nfl/odds/{format}/AlternateMarketGameOddsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_period_game_odds_by_week(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NflV3OddsPeriodGameOddsByWeekErrorBody]`
- **Error**: `NflV3OddsPeriodGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo` | `sports_data_io/models/game_info.py` |
| `NflV3OddsPeriodGameOddsByWeekErrorBody` | `sports_data_io/errors/nfl_v3_odds_period_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_period_game_odds_line_movement

- **Route**: `GET /v3/nfl/odds/{format}/AlternateMarketGameOddsLineMovement/{scoreid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_period_game_odds_line_movement(scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`
- **Params**: `format_` — path `format` · `scoreid` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NflV3OddsPeriodGameOddsLineMovementErrorBody]`
- **Error**: `NflV3OddsPeriodGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo` | `sports_data_io/models/game_info.py` |
| `NflV3OddsPeriodGameOddsLineMovementErrorBody` | `sports_data_io/errors/nfl_v3_odds_period_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/PreGameOddsByWeek/{season}/{week}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(season: str, week: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NflV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo` | `sports_data_io/models/game_info.py` |
| `NflV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/PreGameOddsLineMovement/{scoreid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(scoreid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `scoreid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NflV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo` | `sports_data_io/models/game_info.py` |
| `NflV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/PreGameOddsLineMovementWithResulting/{scoreid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(scoreid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `scoreid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult], NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfoResult` | `sports_data_io/models/game_info_result.py` |
| `NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data_io/errors/nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_pre_game_odds_by_week

- **Route**: `GET /v3/nfl/odds/{format}/GameOddsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_pre_game_odds_by_week(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NflV3OddsPreGameOddsByWeekErrorBody]`
- **Error**: `NflV3OddsPreGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo` | `sports_data_io/models/game_info.py` |
| `NflV3OddsPreGameOddsByWeekErrorBody` | `sports_data_io/errors/nfl_v3_odds_pre_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_pre_game_odds_line_movement

- **Route**: `GET /v3/nfl/odds/{format}/GameOddsLineMovement/{scoreid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_pre_game_odds_line_movement(scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`
- **Params**: `format_` — path `format` · `scoreid` — path
- **Returns (parsed)**: `list[GameInfo]`
- **Returns (raw)**: `ApiResult[list[GameInfo], NflV3OddsPreGameOddsLineMovementErrorBody]`
- **Error**: `NflV3OddsPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo` | `sports_data_io/models/game_info.py` |
| `NflV3OddsPreGameOddsLineMovementErrorBody` | `sports_data_io/errors/nfl_v3_odds_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_sportsbooks_active

- **Route**: `GET /v3/nfl/odds/{format}/ActiveSportsbooks`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_odds_sportsbooks_active(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], NflV3OddsSportsbooksActiveErrorBody]`
- **Error**: `NflV3OddsSportsbooksActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Sportsbook` | `sports_data_io/models/sportsbook.py` |
| `NflV3OddsSportsbooksActiveErrorBody` | `sports_data_io/errors/nfl_v3_odds_sportsbooks_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

