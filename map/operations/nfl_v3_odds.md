<!-- Generated file — do not edit; regenerated with the SDK. -->

# NflV3Odds — operations

Accessor: `client.nfl_v3_odds` · Source: `sports_data/apis/nfl_v3_odds.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nfl_v3_odds.nfl_v3_odds_betting_events_by_date

- **Route**: `GET /v3/nfl/odds/{format}/BettingEventsByDate/{date}`
- **Signature**: `def nfl_v3_odds_betting_events_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BettingEvent5]`
- **Returns (raw)**: `ApiResult[list[BettingEvent5], NflV3OddsBettingEventsByDateErrorBody]`
- **Error**: `NflV3OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent5` | `sports_data/models/betting_event5.py` |
| `NflV3OddsBettingEventsByDateErrorBody` | `sports_data/errors/nfl_v3_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_events_by_season

- **Route**: `GET /v3/nfl/odds/{format}/BettingEvents/{season}`
- **Signature**: `def nfl_v3_odds_betting_events_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent5]`
- **Returns (raw)**: `ApiResult[list[BettingEvent5], NflV3OddsBettingEventsBySeasonErrorBody]`
- **Error**: `NflV3OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent5` | `sports_data/models/betting_event5.py` |
| `NflV3OddsBettingEventsBySeasonErrorBody` | `sports_data/errors/nfl_v3_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_futures_by_season

- **Route**: `GET /v3/nfl/odds/{format}/BettingFuturesBySeason/{season}`
- **Signature**: `def nfl_v3_odds_betting_futures_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent5]`
- **Returns (raw)**: `ApiResult[list[BettingEvent5], NflV3OddsBettingFuturesBySeasonErrorBody]`
- **Error**: `NflV3OddsBettingFuturesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent5` | `sports_data/models/betting_event5.py` |
| `NflV3OddsBettingFuturesBySeasonErrorBody` | `sports_data/errors/nfl_v3_odds_betting_futures_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_futures_by_season_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_betting_futures_by_season_sportsbook_group(format: FormatOrStr, season: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `sportsbookgroup`
- **Params**: `format` — path · `season` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingEvent5]`
- **Returns (raw)**: `ApiResult[list[BettingEvent5], NflV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent5` | `sports_data/models/betting_event5.py` |
| `NflV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_betting_futures_by_season_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_market

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarket/{marketId}`
- **Signature**: `def nfl_v3_odds_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, NflV3OddsBettingMarketErrorBody]`
- **Error**: `NflV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NflV3OddsBettingMarketErrorBody` | `sports_data/errors/nfl_v3_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_market_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_betting_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, NflV3OddsBettingMarketSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NflV3OddsBettingMarketSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarkets/{eventId}`
- **Signature**: `def nfl_v3_odds_betting_markets_by_event(format: FormatOrStr, event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NflV3OddsBettingMarketsByEventErrorBody` | `sports_data/errors/nfl_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_betting_markets_by_event_sportsbook_group(format: FormatOrStr, event_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NflV3OddsBettingMarketsByEventSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_game

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketsByScoreID/{scoreid}`
- **Signature**: `def nfl_v3_odds_betting_markets_by_game(format: FormatOrStr, scoreid: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`
- **Params**: `format` — path · `scoreid` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByGameErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NflV3OddsBettingMarketsByGameErrorBody` | `sports_data/errors/nfl_v3_odds_betting_markets_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_game_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketsByGameID/{gameid}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_betting_markets_by_game_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `sportsbookgroup`
- **Params**: `format` — path · `gameid` — path · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByGameSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NflV3OddsBettingMarketsByGameSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_betting_markets_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}`
- **Signature**: `def nfl_v3_odds_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NflV3OddsBettingMarketsByMarketTypeErrorBody` | `sports_data/errors/nfl_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_betting_markets_by_market_type_sportsbook_group(format: FormatOrStr, event_id: str, market_type_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NflV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_metadata

- **Route**: `GET /v3/nfl/odds/{format}/BettingMetadata`
- **Signature**: `def nfl_v3_odds_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `BettingEntityMetadataCollection`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection, NflV3OddsBettingMetadataErrorBody]`
- **Error**: `NflV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEntityMetadataCollection` | `sports_data/models/betting_entity_metadata_collection.py` |
| `NflV3OddsBettingMetadataErrorBody` | `sports_data/errors/nfl_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_player_props_by_game

- **Route**: `GET /v3/nfl/odds/{format}/BettingPlayerPropsByScoreID/{scoreid}`
- **Signature**: `def nfl_v3_odds_betting_player_props_by_game(format: FormatOrStr, scoreid: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`
- **Params**: `format` — path · `scoreid` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingPlayerPropsByGameErrorBody]`
- **Error**: `NflV3OddsBettingPlayerPropsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NflV3OddsBettingPlayerPropsByGameErrorBody` | `sports_data/errors/nfl_v3_odds_betting_player_props_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_player_props_by_game_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingPlayerPropsByScoreID/{scoreid}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_betting_player_props_by_game_sportsbook_group(format: FormatOrStr, scoreid: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`, `sportsbookgroup`
- **Params**: `format` — path · `scoreid` — path · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], NflV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `NflV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_betting_player_props_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_results_by_market

- **Route**: `GET /v3/nfl/odds/{format}/BettingMarketResults/{marketId}`
- **Signature**: `def nfl_v3_odds_betting_results_by_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, NflV3OddsBettingResultsByMarketErrorBody]`
- **Error**: `NflV3OddsBettingResultsByMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarketResult` | `sports_data/models/betting_market_result.py` |
| `NflV3OddsBettingResultsByMarketErrorBody` | `sports_data/errors/nfl_v3_odds_betting_results_by_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_results_by_market_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/BettingResultsByMarket/{marketId}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_betting_results_by_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarketResult`
- **Returns (raw)**: `ApiResult[BettingMarketResult, NflV3OddsBettingResultsByMarketSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsBettingResultsByMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarketResult` | `sports_data/models/betting_market_result.py` |
| `NflV3OddsBettingResultsByMarketSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_betting_results_by_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_splits_by_betting_market

- **Route**: `GET /v3/nfl/odds/{format}/BettingSplitsByMarketId/{marketId}`
- **Signature**: `def nfl_v3_odds_betting_splits_by_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarketSplit`
- **Returns (raw)**: `ApiResult[BettingMarketSplit, NflV3OddsBettingSplitsByBettingMarketErrorBody]`
- **Error**: `NflV3OddsBettingSplitsByBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarketSplit` | `sports_data/models/betting_market_split.py` |
| `NflV3OddsBettingSplitsByBettingMarketErrorBody` | `sports_data/errors/nfl_v3_odds_betting_splits_by_betting_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_splits_by_game

- **Route**: `GET /v3/nfl/odds/{format}/BettingSplitsByScoreId/{scoreId}`
- **Signature**: `def nfl_v3_odds_betting_splits_by_game(format: FormatOrStr, score_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `score_id`
- **Params**: `format` — path · `score_id` — path `scoreId`
- **Returns (parsed)**: `GameBettingSplit2`
- **Returns (raw)**: `ApiResult[GameBettingSplit2, NflV3OddsBettingSplitsByGameErrorBody]`
- **Error**: `NflV3OddsBettingSplitsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameBettingSplit2` | `sports_data/models/game_betting_split2.py` |
| `NflV3OddsBettingSplitsByGameErrorBody` | `sports_data/errors/nfl_v3_odds_betting_splits_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_trends_by_matchup

- **Route**: `GET /v3/nfl/odds/{format}/MatchupTrends/{team}/{opponent}`
- **Signature**: `def nfl_v3_odds_betting_trends_by_matchup(format: FormatOrStr, team: str, opponent: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`, `opponent`
- **Params**: `format` — path · `team` — path · `opponent` — path
- **Returns (parsed)**: `MatchupTrends3`
- **Returns (raw)**: `ApiResult[MatchupTrends3, NflV3OddsBettingTrendsByMatchupErrorBody]`
- **Error**: `NflV3OddsBettingTrendsByMatchupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `MatchupTrends3` | `sports_data/models/matchup_trends3.py` |
| `NflV3OddsBettingTrendsByMatchupErrorBody` | `sports_data/errors/nfl_v3_odds_betting_trends_by_matchup_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_betting_trends_by_team

- **Route**: `GET /v3/nfl/odds/{format}/TeamTrends/{team}`
- **Signature**: `def nfl_v3_odds_betting_trends_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `TeamTrends3`
- **Returns (raw)**: `ApiResult[TeamTrends3, NflV3OddsBettingTrendsByTeamErrorBody]`
- **Error**: `NflV3OddsBettingTrendsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamTrends3` | `sports_data/models/team_trends3.py` |
| `NflV3OddsBettingTrendsByTeamErrorBody` | `sports_data/errors/nfl_v3_odds_betting_trends_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_in_game_odds_by_week

- **Route**: `GET /v3/nfl/odds/{format}/LiveGameOddsByWeek/{season}/{week}`
- **Signature**: `def nfl_v3_odds_in_game_odds_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], NflV3OddsInGameOddsByWeekErrorBody]`
- **Error**: `NflV3OddsInGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo2` | `sports_data/models/game_info2.py` |
| `NflV3OddsInGameOddsByWeekErrorBody` | `sports_data/errors/nfl_v3_odds_in_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_in_game_odds_by_week_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/InGameOddsByWeek/{season}/{week}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_in_game_odds_by_week_sportsbook_group(format: FormatOrStr, season: str, week: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `sportsbookgroup`
- **Params**: `format` — path · `season` — path · `week` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo2` | `sports_data/models/game_info2.py` |
| `NflV3OddsInGameOddsByWeekSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_in_game_odds_by_week_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_in_game_odds_line_movement

- **Route**: `GET /v3/nfl/odds/{format}/LiveGameOddsLineMovement/{scoreid}`
- **Signature**: `def nfl_v3_odds_in_game_odds_line_movement(format: FormatOrStr, scoreid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`
- **Params**: `format` — path · `scoreid` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], NflV3OddsInGameOddsLineMovementErrorBody]`
- **Error**: `NflV3OddsInGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo2` | `sports_data/models/game_info2.py` |
| `NflV3OddsInGameOddsLineMovementErrorBody` | `sports_data/errors/nfl_v3_odds_in_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_in_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/InGameLineMovement/{scoreid}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_in_game_odds_line_movement_sportsbook_group(format: FormatOrStr, scoreid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`, `sportsbookgroup`
- **Params**: `format` — path · `scoreid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], NflV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo2` | `sports_data/models/game_info2.py` |
| `NflV3OddsInGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_in_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/InGameLineMovementWithResulting/{scoreid}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, scoreid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`, `sportsbookgroup`
- **Params**: `format` — path · `scoreid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult4]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult4], NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfoResult4` | `sports_data/models/game_info_result4.py` |
| `NflV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_period_game_odds_by_week

- **Route**: `GET /v3/nfl/odds/{format}/AlternateMarketGameOddsByWeek/{season}/{week}`
- **Signature**: `def nfl_v3_odds_period_game_odds_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], NflV3OddsPeriodGameOddsByWeekErrorBody]`
- **Error**: `NflV3OddsPeriodGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo2` | `sports_data/models/game_info2.py` |
| `NflV3OddsPeriodGameOddsByWeekErrorBody` | `sports_data/errors/nfl_v3_odds_period_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_period_game_odds_line_movement

- **Route**: `GET /v3/nfl/odds/{format}/AlternateMarketGameOddsLineMovement/{scoreid}`
- **Signature**: `def nfl_v3_odds_period_game_odds_line_movement(format: FormatOrStr, scoreid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`
- **Params**: `format` — path · `scoreid` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], NflV3OddsPeriodGameOddsLineMovementErrorBody]`
- **Error**: `NflV3OddsPeriodGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo2` | `sports_data/models/game_info2.py` |
| `NflV3OddsPeriodGameOddsLineMovementErrorBody` | `sports_data/errors/nfl_v3_odds_period_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/PreGameOddsByWeek/{season}/{week}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group(format: FormatOrStr, season: str, week: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `sportsbookgroup`
- **Params**: `format` — path · `season` — path · `week` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], NflV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo2` | `sports_data/models/game_info2.py` |
| `NflV3OddsPreGameAndPeriodGameOddsByWeekSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_pre_game_and_period_game_odds_by_week_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/PreGameOddsLineMovement/{scoreid}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(format: FormatOrStr, scoreid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`, `sportsbookgroup`
- **Params**: `format` — path · `scoreid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], NflV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo2` | `sports_data/models/game_info2.py` |
| `NflV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v3/nfl/odds/{format}/PreGameOddsLineMovementWithResulting/{scoreid}/{sportsbookgroup}`
- **Signature**: `def nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, scoreid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`, `sportsbookgroup`
- **Params**: `format` — path · `scoreid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult4]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult4], NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfoResult4` | `sports_data/models/game_info_result4.py` |
| `NflV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data/errors/nfl_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_pre_game_odds_by_week

- **Route**: `GET /v3/nfl/odds/{format}/GameOddsByWeek/{season}/{week}`
- **Signature**: `def nfl_v3_odds_pre_game_odds_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], NflV3OddsPreGameOddsByWeekErrorBody]`
- **Error**: `NflV3OddsPreGameOddsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo2` | `sports_data/models/game_info2.py` |
| `NflV3OddsPreGameOddsByWeekErrorBody` | `sports_data/errors/nfl_v3_odds_pre_game_odds_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_pre_game_odds_line_movement

- **Route**: `GET /v3/nfl/odds/{format}/GameOddsLineMovement/{scoreid}`
- **Signature**: `def nfl_v3_odds_pre_game_odds_line_movement(format: FormatOrStr, scoreid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`
- **Params**: `format` — path · `scoreid` — path
- **Returns (parsed)**: `list[GameInfo2]`
- **Returns (raw)**: `ApiResult[list[GameInfo2], NflV3OddsPreGameOddsLineMovementErrorBody]`
- **Error**: `NflV3OddsPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo2` | `sports_data/models/game_info2.py` |
| `NflV3OddsPreGameOddsLineMovementErrorBody` | `sports_data/errors/nfl_v3_odds_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_odds.nfl_v3_odds_sportsbooks_active

- **Route**: `GET /v3/nfl/odds/{format}/ActiveSportsbooks`
- **Signature**: `def nfl_v3_odds_sportsbooks_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], NflV3OddsSportsbooksActiveErrorBody]`
- **Error**: `NflV3OddsSportsbooksActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Sportsbook` | `sports_data/models/sportsbook.py` |
| `NflV3OddsSportsbooksActiveErrorBody` | `sports_data/errors/nfl_v3_odds_sportsbooks_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

