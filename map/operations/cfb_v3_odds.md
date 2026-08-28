<!-- Generated file — do not edit; regenerated with the SDK. -->

# CfbV3Odds — operations

Accessor: `client.cfb_v3_odds` · Source: `sports_data/apis/cfb_v3_odds.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cfb_v3_odds.cfb_v3_odds_betting_events_by_date

- **Route**: `GET /v3/cfb/odds/{format}/BettingEventsByDate/{date}`
- **Signature**: `def cfb_v3_odds_betting_events_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], CfbV3OddsBettingEventsByDateErrorBody]`
- **Error**: `CfbV3OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent` | `sports_data/models/betting_event.py` |
| `CfbV3OddsBettingEventsByDateErrorBody` | `sports_data/errors/cfb_v3_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_events_by_season

- **Route**: `GET /v3/cfb/odds/{format}/BettingEvents/{season}`
- **Signature**: `def cfb_v3_odds_betting_events_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], CfbV3OddsBettingEventsBySeasonErrorBody]`
- **Error**: `CfbV3OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent` | `sports_data/models/betting_event.py` |
| `CfbV3OddsBettingEventsBySeasonErrorBody` | `sports_data/errors/cfb_v3_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_futures_by_season

- **Route**: `GET /v3/cfb/odds/{format}/BettingFuturesBySeason/{season}`
- **Signature**: `def cfb_v3_odds_betting_futures_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], CfbV3OddsBettingFuturesBySeasonErrorBody]`
- **Error**: `CfbV3OddsBettingFuturesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent` | `sports_data/models/betting_event.py` |
| `CfbV3OddsBettingFuturesBySeasonErrorBody` | `sports_data/errors/cfb_v3_odds_betting_futures_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_futures_by_season_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_betting_futures_by_season_sportsbook_group(format: FormatOrStr, season: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `sportsbookgroup`
- **Params**: `format` — path · `season` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingEvent]`
- **Returns (raw)**: `ApiResult[list[BettingEvent], CfbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent` | `sports_data/models/betting_event.py` |
| `CfbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_betting_futures_by_season_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_market

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarket/{marketId}`
- **Signature**: `def cfb_v3_odds_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, CfbV3OddsBettingMarketErrorBody]`
- **Error**: `CfbV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `CfbV3OddsBettingMarketErrorBody` | `sports_data/errors/cfb_v3_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_market_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_betting_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, CfbV3OddsBettingMarketSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `CfbV3OddsBettingMarketSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarkets/{eventId}`
- **Signature**: `def cfb_v3_odds_betting_markets_by_event(format: FormatOrStr, event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByEventErrorBody` | `sports_data/errors/cfb_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_betting_markets_by_event_sportsbook_group(format: FormatOrStr, event_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByEventSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_game

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketsByGameID/{gameid}`
- **Signature**: `def cfb_v3_odds_betting_markets_by_game(format: FormatOrStr, gameid: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByGameErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByGameErrorBody` | `sports_data/errors/cfb_v3_odds_betting_markets_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_game_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketsByGameID/{gameid}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_betting_markets_by_game_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByGameSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByGameSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_betting_markets_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}`
- **Signature**: `def cfb_v3_odds_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByMarketTypeErrorBody` | `sports_data/errors/cfb_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_betting_markets_by_market_type_sportsbook_group(format: FormatOrStr, event_id: str, market_type_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `CfbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_metadata

- **Route**: `GET /v3/cfb/odds/{format}/BettingMetadata`
- **Signature**: `def cfb_v3_odds_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `BettingEntityMetadataCollection`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection, CfbV3OddsBettingMetadataErrorBody]`
- **Error**: `CfbV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEntityMetadataCollection` | `sports_data/models/betting_entity_metadata_collection.py` |
| `CfbV3OddsBettingMetadataErrorBody` | `sports_data/errors/cfb_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_player_props_by_game

- **Route**: `GET /v3/cfb/odds/{format}/BettingPlayerPropsByGameID/{gameId}`
- **Signature**: `def cfb_v3_odds_betting_player_props_by_game(format: FormatOrStr, game_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingPlayerPropsByGameErrorBody]`
- **Error**: `CfbV3OddsBettingPlayerPropsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `CfbV3OddsBettingPlayerPropsByGameErrorBody` | `sports_data/errors/cfb_v3_odds_betting_player_props_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_player_props_by_game_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_betting_player_props_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`, `sportsbookgroup`
- **Params**: `format` — path · `game_id` — path `gameId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_betting_player_props_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_results_by_market

- **Route**: `GET /v3/cfb/odds/{format}/BettingMarketResults/{marketId}`
- **Signature**: `def cfb_v3_odds_betting_results_by_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, CfbV3OddsBettingResultsByMarketErrorBody]`
- **Error**: `CfbV3OddsBettingResultsByMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarketResult` | `sports_data/models/betting_market_result.py` |
| `CfbV3OddsBettingResultsByMarketErrorBody` | `sports_data/errors/cfb_v3_odds_betting_results_by_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_results_by_market_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_betting_results_by_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarketResult` | `sports_data/models/betting_market_result.py` |
| `CfbV3OddsBettingResultsByMarketSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_betting_results_by_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_splits_by_betting_market

- **Route**: `GET /v3/cfb/odds/{format}/BettingSplitsByMarketId/{marketId}`
- **Signature**: `def cfb_v3_odds_betting_splits_by_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketSplit`
- **Returns (raw)**: `ApiResult[BettingMarketSplit, CfbV3OddsBettingSplitsByBettingMarketErrorBody]`
- **Error**: `CfbV3OddsBettingSplitsByBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarketSplit` | `sports_data/models/betting_market_split.py` |
| `CfbV3OddsBettingSplitsByBettingMarketErrorBody` | `sports_data/errors/cfb_v3_odds_betting_splits_by_betting_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_splits_by_game

- **Route**: `GET /v3/cfb/odds/{format}/BettingSplitsByGameId/{gameid}`
- **Signature**: `def cfb_v3_odds_betting_splits_by_game(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `GameBettingSplit1`
- **Returns (raw)**: `ApiResult[GameBettingSplit1, CfbV3OddsBettingSplitsByGameErrorBody]`
- **Error**: `CfbV3OddsBettingSplitsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameBettingSplit1` | `sports_data/models/game_betting_split1.py` |
| `CfbV3OddsBettingSplitsByGameErrorBody` | `sports_data/errors/cfb_v3_odds_betting_splits_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_trends_by_matchup

- **Route**: `GET /v3/cfb/odds/{format}/MatchupTrends/{team}/{opponent}`
- **Signature**: `def cfb_v3_odds_betting_trends_by_matchup(format: FormatOrStr, team: str, opponent: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`, `opponent`
- **Params**: `format` — path · `team` — path · `opponent` — path
- **Returns (parsed)**: `MatchupTrends`
- **Returns (raw)**: `ApiResult[MatchupTrends, CfbV3OddsBettingTrendsByMatchupErrorBody]`
- **Error**: `CfbV3OddsBettingTrendsByMatchupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `MatchupTrends` | `sports_data/models/matchup_trends.py` |
| `CfbV3OddsBettingTrendsByMatchupErrorBody` | `sports_data/errors/cfb_v3_odds_betting_trends_by_matchup_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_betting_trends_by_team

- **Route**: `GET /v3/cfb/odds/{format}/TeamTrends/{team}`
- **Signature**: `def cfb_v3_odds_betting_trends_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `TeamTrends`
- **Returns (raw)**: `ApiResult[TeamTrends, CfbV3OddsBettingTrendsByTeamErrorBody]`
- **Error**: `CfbV3OddsBettingTrendsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamTrends` | `sports_data/models/team_trends.py` |
| `CfbV3OddsBettingTrendsByTeamErrorBody` | `sports_data/errors/cfb_v3_odds_betting_trends_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_in_game_odds_by_week

- **Route**: `GET /v3/cfb/odds/{format}/LiveGameOddsByWeek/{season}/{week}`
- **Signature**: `def cfb_v3_odds_in_game_odds_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo1]`
- **Returns (raw)**: `ApiResult[list[GameInfo1], CfbV3OddsInGameOddsByWeekErrorBody]`
- **Error**: `CfbV3OddsInGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo1` | `sports_data/models/game_info1.py` |
| `CfbV3OddsInGameOddsByWeekErrorBody` | `sports_data/errors/cfb_v3_odds_in_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_in_game_odds_by_week_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/InGameOddsByWeek/{season}/{week}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_in_game_odds_by_week_sportsbook_group(format: FormatOrStr, season: str, week: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `sportsbookgroup`
- **Params**: `format` — path · `season` — path · `week` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo1]`
- **Returns (raw)**: `ApiResult[list[GameInfo1], CfbV3OddsInGameOddsByWeekSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsInGameOddsByWeekSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo1` | `sports_data/models/game_info1.py` |
| `CfbV3OddsInGameOddsByWeekSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_in_game_odds_by_week_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_in_game_odds_line_movement

- **Route**: `GET /v3/cfb/odds/{format}/LiveGameOddsLineMovement/{gameid}`
- **Signature**: `def cfb_v3_odds_in_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo1]`
- **Returns (raw)**: `ApiResult[list[GameInfo1], CfbV3OddsInGameOddsLineMovementErrorBody]`
- **Error**: `CfbV3OddsInGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo1` | `sports_data/models/game_info1.py` |
| `CfbV3OddsInGameOddsLineMovementErrorBody` | `sports_data/errors/cfb_v3_odds_in_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_in_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/InGameLineMovement/{gameid}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_in_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo1]`
- **Returns (raw)**: `ApiResult[list[GameInfo1], CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo1` | `sports_data/models/game_info1.py` |
| `CfbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_in_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/InGameLineMovementWithResulting/{gameid}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult1]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult1], CfbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfoResult1` | `sports_data/models/game_info_result1.py` |
| `CfbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_period_game_odds_by_week

- **Route**: `GET /v3/cfb/odds/{format}/AlternateMarketGameOddsByWeek/{season}/{week}`
- **Signature**: `def cfb_v3_odds_period_game_odds_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo1]`
- **Returns (raw)**: `ApiResult[list[GameInfo1], CfbV3OddsPeriodGameOddsByWeekErrorBody]`
- **Error**: `CfbV3OddsPeriodGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo1` | `sports_data/models/game_info1.py` |
| `CfbV3OddsPeriodGameOddsByWeekErrorBody` | `sports_data/errors/cfb_v3_odds_period_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_period_game_odds_line_movement

- **Route**: `GET /v3/cfb/odds/{format}/AlternateMarketGameOddsLineMovement/{gameid}`
- **Signature**: `def cfb_v3_odds_period_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo1]`
- **Returns (raw)**: `ApiResult[list[GameInfo1], CfbV3OddsPeriodGameOddsLineMovementErrorBody]`
- **Error**: `CfbV3OddsPeriodGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo1` | `sports_data/models/game_info1.py` |
| `CfbV3OddsPeriodGameOddsLineMovementErrorBody` | `sports_data/errors/cfb_v3_odds_period_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/PreGameOddsByWeek/{season}/{week}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(format: FormatOrStr, season: str, week: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `sportsbookgroup`
- **Params**: `format` — path · `season` — path · `week` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo1]`
- **Returns (raw)**: `ApiResult[list[GameInfo1], CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo1` | `sports_data/models/game_info1.py` |
| `CfbV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/PreGameOddsLineMovement/{gameid}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo1]`
- **Returns (raw)**: `ApiResult[list[GameInfo1], CfbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo1` | `sports_data/models/game_info1.py` |
| `CfbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/cfb/odds/{format}/PreGameOddsLineMovementWithResulting/{gameid}/{sportsbookgroup}`
- **Signature**: `def cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult1]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult1], CfbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `CfbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfoResult1` | `sports_data/models/game_info_result1.py` |
| `CfbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data/errors/cfb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_pre_game_odds_by_week

- **Route**: `GET /v3/cfb/odds/{format}/GameOddsByWeek/{season}/{week}`
- **Signature**: `def cfb_v3_odds_pre_game_odds_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo1]`
- **Returns (raw)**: `ApiResult[list[GameInfo1], CfbV3OddsPreGameOddsByWeekErrorBody]`
- **Error**: `CfbV3OddsPreGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo1` | `sports_data/models/game_info1.py` |
| `CfbV3OddsPreGameOddsByWeekErrorBody` | `sports_data/errors/cfb_v3_odds_pre_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_pre_game_odds_line_movement

- **Route**: `GET /v3/cfb/odds/{format}/GameOddsLineMovement/{gameid}`
- **Signature**: `def cfb_v3_odds_pre_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo1]`
- **Returns (raw)**: `ApiResult[list[GameInfo1], CfbV3OddsPreGameOddsLineMovementErrorBody]`
- **Error**: `CfbV3OddsPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo1` | `sports_data/models/game_info1.py` |
| `CfbV3OddsPreGameOddsLineMovementErrorBody` | `sports_data/errors/cfb_v3_odds_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_odds.cfb_v3_odds_sportsbooks_by_active

- **Route**: `GET /v3/cfb/odds/{format}/ActiveSportsbooks`
- **Signature**: `def cfb_v3_odds_sportsbooks_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], CfbV3OddsSportsbooksByActiveErrorBody]`
- **Error**: `CfbV3OddsSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Sportsbook` | `sports_data/models/sportsbook.py` |
| `CfbV3OddsSportsbooksByActiveErrorBody` | `sports_data/errors/cfb_v3_odds_sportsbooks_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

