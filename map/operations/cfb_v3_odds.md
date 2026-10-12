<!-- Generated file — do not edit; regenerated with the SDK. -->

# CfbV3Odds — operations

Accessor: `client.cfb_v3_odds` · Source: `sports_data_io/apis/cfb_v3_odds.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cfb_v3_odds.cfb_v3_odds_betting_events_by_date

- **Route**: `GET /v3/cfb/odds/{format}/BettingEventsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_events_by_date(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], CfbV3OddsBettingEventsByDateErrorBody]`
- **Error**: `CfbV3OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent2` | `sports_data_io/models/betting_event2.py` |
| `CfbV3OddsBettingEventsByDateErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_events_by_season

- **Route**: `GET /v3/cfb/odds/{format}/BettingEvents/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_events_by_season(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], CfbV3OddsBettingEventsBySeasonErrorBody]`
- **Error**: `CfbV3OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent2` | `sports_data_io/models/betting_event2.py` |
| `CfbV3OddsBettingEventsBySeasonErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_futures_by_season

- **Route**: `GET /v3/cfb/odds/{format}/BettingFuturesBySeason/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_futures_by_season(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], CfbV3OddsBettingFuturesBySeasonErrorBody]`
- **Error**: `CfbV3OddsBettingFuturesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent2` | `sports_data_io/models/betting_event2.py` |
| `CfbV3OddsBettingFuturesBySeasonErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_futures_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_futures_by_season_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_futures_by_season_sportsbook_group(season: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `season` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], CfbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent2` | `sports_data_io/models/betting_event2.py` |
| `CfbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_futures_by_season_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_market

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarket/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_market(market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `market_id`
- **Params**: `format_` — path `format` · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, CfbV3OddsBettingMarketErrorBody]`
- **Error**: `CfbV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `CfbV3OddsBettingMarketErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_market_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_market_sportsbook_group(market_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `market_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, CfbV3OddsBettingMarketSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `CfbV3OddsBettingMarketSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarkets/{eventId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_markets_by_event(event_id: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `event_id`
- **Params**: `format_` — path `format` · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByEventErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_markets_by_event_sportsbook_group(event_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `event_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `event_id` — path `eventId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_game

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketsByGameID/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_markets_by_game(gameid: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByGameErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByGameErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_markets_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_game_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketsByGameID/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_markets_by_game_sportsbook_group(gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `gameid` — path · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByGameSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByGameSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_markets_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_markets_by_market_type(event_id: str, market_type_id: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `event_id`, `market_type_id`
- **Params**: `format_` — path `format` · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByMarketTypeErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_markets_by_market_type_sportsbook_group(event_id: str, market_type_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `event_id`, `market_type_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_metadata

- **Route**: `GET /v3/cfb/odds/{format}/BettingMetadata`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_metadata(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `BettingEntityMetadataCollection`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection, CfbV3OddsBettingMetadataErrorBody]`
- **Error**: `CfbV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEntityMetadataCollection` | `sports_data_io/models/betting_entity_metadata_collection.py` |
| `CfbV3OddsBettingMetadataErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_player_props_by_game

- **Route**: `GET /v3/cfb/odds/{format}/BettingPlayerPropsByGameID/{gameId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_player_props_by_game(game_id: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `game_id`
- **Params**: `format_` — path `format` · `game_id` — path `gameId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingPlayerPropsByGameErrorBody]`
- **Error**: `CfbV3OddsBettingPlayerPropsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `CfbV3OddsBettingPlayerPropsByGameErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_player_props_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_player_props_by_game_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_player_props_by_game_sportsbook_group(game_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, include: IncludeOrStr | None = Include.AVAILABLE, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `game_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `game_id` — path `gameId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `IncludeOrStr` | `sports_data_io/models/enums/include.py` |
| `BettingMarket` | `sports_data_io/models/betting_market.py` |
| `CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_player_props_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_results_by_market

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketResults/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_results_by_market(market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `market_id`
- **Params**: `format_` — path `format` · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, CfbV3OddsBettingResultsByMarketErrorBody]`
- **Error**: `CfbV3OddsBettingResultsByMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketResult` | `sports_data_io/models/betting_market_result.py` |
| `CfbV3OddsBettingResultsByMarketErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_results_by_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_results_by_market_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_results_by_market_sportsbook_group(market_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `market_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketResult` | `sports_data_io/models/betting_market_result.py` |
| `CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_results_by_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_splits_by_betting_market

- **Route**: `GET /v3/cfb/odds/{format}/BettingSplitsByMarketId/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_splits_by_betting_market(market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `market_id`
- **Params**: `format_` — path `format` · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketSplit`
- **Returns (raw)**: `ApiResult[BettingMarketSplit, CfbV3OddsBettingSplitsByBettingMarketErrorBody]`
- **Error**: `CfbV3OddsBettingSplitsByBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarketSplit` | `sports_data_io/models/betting_market_split.py` |
| `CfbV3OddsBettingSplitsByBettingMarketErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_splits_by_betting_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_splits_by_game

- **Route**: `GET /v3/cfb/odds/{format}/BettingSplitsByGameId/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_splits_by_game(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `GameBettingSplit2`
- **Returns (raw)**: `ApiResult[GameBettingSplit2, CfbV3OddsBettingSplitsByGameErrorBody]`
- **Error**: `CfbV3OddsBettingSplitsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameBettingSplit2` | `sports_data_io/models/game_betting_split2.py` |
| `CfbV3OddsBettingSplitsByGameErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_splits_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_trends_by_matchup

- **Route**: `GET /v3/cfb/odds/{format}/MatchupTrends/{team}/{opponent}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_trends_by_matchup(team: str, opponent: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`, `opponent`
- **Params**: `format_` — path `format` · `team` — path · `opponent` — path
- **Returns (parsed)**: `MatchupTrends4`
- **Returns (raw)**: `ApiResult[MatchupTrends4, CfbV3OddsBettingTrendsByMatchupErrorBody]`
- **Error**: `CfbV3OddsBettingTrendsByMatchupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `MatchupTrends4` | `sports_data_io/models/matchup_trends4.py` |
| `CfbV3OddsBettingTrendsByMatchupErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_trends_by_matchup_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_trends_by_team

- **Route**: `GET /v3/cfb/odds/{format}/TeamTrends/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_betting_trends_by_team(team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`
- **Params**: `format_` — path `format` · `team` — path
- **Returns (parsed)**: `TeamTrends2`
- **Returns (raw)**: `ApiResult[TeamTrends2, CfbV3OddsBettingTrendsByTeamErrorBody]`
- **Error**: `CfbV3OddsBettingTrendsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamTrends2` | `sports_data_io/models/team_trends2.py` |
| `CfbV3OddsBettingTrendsByTeamErrorBody` | `sports_data_io/errors/cfb_v3_odds_betting_trends_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_in_game_odds_by_week

- **Route**: `GET /v3/cfb/odds/{format}/LiveGameOddsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_in_game_odds_by_week(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], CfbV3OddsInGameOddsByWeekErrorBody]`
- **Error**: `CfbV3OddsInGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo4` | `sports_data_io/models/game_info4.py` |
| `CfbV3OddsInGameOddsByWeekErrorBody` | `sports_data_io/errors/cfb_v3_odds_in_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_in_game_odds_by_week_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/InGameOddsByWeek/{season}/{week}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_in_game_odds_by_week_sportsbook_group(season: str, week: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], CfbV3OddsInGameOddsByWeekSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsInGameOddsByWeekSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo4` | `sports_data_io/models/game_info4.py` |
| `CfbV3OddsInGameOddsByWeekSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_in_game_odds_by_week_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_in_game_odds_line_movement

- **Route**: `GET /v3/cfb/odds/{format}/LiveGameOddsLineMovement/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_in_game_odds_line_movement(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], CfbV3OddsInGameOddsLineMovementErrorBody]`
- **Error**: `CfbV3OddsInGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo4` | `sports_data_io/models/game_info4.py` |
| `CfbV3OddsInGameOddsLineMovementErrorBody` | `sports_data_io/errors/cfb_v3_odds_in_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_in_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/InGameLineMovement/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_in_game_odds_line_movement_sportsbook_group(gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo4` | `sports_data_io/models/game_info4.py` |
| `CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_in_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/InGameLineMovementWithResulting/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult4]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult4], CfbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfoResult4` | `sports_data_io/models/game_info_result4.py` |
| `CfbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_period_game_odds_by_week

- **Route**: `GET /v3/cfb/odds/{format}/AlternateMarketGameOddsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_period_game_odds_by_week(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], CfbV3OddsPeriodGameOddsByWeekErrorBody]`
- **Error**: `CfbV3OddsPeriodGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo4` | `sports_data_io/models/game_info4.py` |
| `CfbV3OddsPeriodGameOddsByWeekErrorBody` | `sports_data_io/errors/cfb_v3_odds_period_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_period_game_odds_line_movement

- **Route**: `GET /v3/cfb/odds/{format}/AlternateMarketGameOddsLineMovement/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_period_game_odds_line_movement(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], CfbV3OddsPeriodGameOddsLineMovementErrorBody]`
- **Error**: `CfbV3OddsPeriodGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo4` | `sports_data_io/models/game_info4.py` |
| `CfbV3OddsPeriodGameOddsLineMovementErrorBody` | `sports_data_io/errors/cfb_v3_odds_period_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/PreGameOddsByWeek/{season}/{week}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(season: str, week: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo4` | `sports_data_io/models/game_info4.py` |
| `CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/PreGameOddsLineMovement/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], CfbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo4` | `sports_data_io/models/game_info4.py` |
| `CfbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/PreGameOddsLineMovementWithResulting/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult4]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult4], CfbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfoResult4` | `sports_data_io/models/game_info_result4.py` |
| `CfbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data_io/errors/cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_pre_game_odds_by_week

- **Route**: `GET /v3/cfb/odds/{format}/GameOddsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_pre_game_odds_by_week(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], CfbV3OddsPreGameOddsByWeekErrorBody]`
- **Error**: `CfbV3OddsPreGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo4` | `sports_data_io/models/game_info4.py` |
| `CfbV3OddsPreGameOddsByWeekErrorBody` | `sports_data_io/errors/cfb_v3_odds_pre_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_pre_game_odds_line_movement

- **Route**: `GET /v3/cfb/odds/{format}/GameOddsLineMovement/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_pre_game_odds_line_movement(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], CfbV3OddsPreGameOddsLineMovementErrorBody]`
- **Error**: `CfbV3OddsPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo4` | `sports_data_io/models/game_info4.py` |
| `CfbV3OddsPreGameOddsLineMovementErrorBody` | `sports_data_io/errors/cfb_v3_odds_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_sportsbooks_by_active

- **Route**: `GET /v3/cfb/odds/{format}/ActiveSportsbooks`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_odds_sportsbooks_by_active(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], CfbV3OddsSportsbooksByActiveErrorBody]`
- **Error**: `CfbV3OddsSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Sportsbook` | `sports_data_io/models/sportsbook.py` |
| `CfbV3OddsSportsbooksByActiveErrorBody` | `sports_data_io/errors/cfb_v3_odds_sportsbooks_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

