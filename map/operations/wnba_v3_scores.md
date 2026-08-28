<!-- Generated file — do not edit; regenerated with the SDK. -->

# WnbaV3Scores — operations

Accessor: `client.wnba_v3_scores` · Source: `sports_data/apis/wnba_v3_scores.py` · 40 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wnba_v3_scores.wnba_v3_scores_are_games_in_progress

- **Route**: `GET /v3/wnba/scores/{format}/AreAnyGamesInProgress`
- **Signature**: `def wnba_v3_scores_are_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, WnbaV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `WnbaV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `WnbaV3ScoresAreGamesInProgressErrorBody` | `sports_data/errors/wnba_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_events_by_date

- **Route**: `GET /v3/wnba/scores/{format}/BettingEventsByDate/{date}`
- **Signature**: `def wnba_v3_scores_betting_events_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], WnbaV3ScoresBettingEventsByDateErrorBody]`
- **Error**: `WnbaV3ScoresBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent2` | `sports_data/models/betting_event2.py` |
| `WnbaV3ScoresBettingEventsByDateErrorBody` | `sports_data/errors/wnba_v3_scores_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_events_by_season

- **Route**: `GET /v3/wnba/scores/{format}/BettingEvents/{season}`
- **Signature**: `def wnba_v3_scores_betting_events_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], WnbaV3ScoresBettingEventsBySeasonErrorBody]`
- **Error**: `WnbaV3ScoresBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent2` | `sports_data/models/betting_event2.py` |
| `WnbaV3ScoresBettingEventsBySeasonErrorBody` | `sports_data/errors/wnba_v3_scores_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_futures_by_season

- **Route**: `GET /v3/wnba/scores/{format}/BettingFuturesBySeason/{season}`
- **Signature**: `def wnba_v3_scores_betting_futures_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], WnbaV3ScoresBettingFuturesBySeasonErrorBody]`
- **Error**: `WnbaV3ScoresBettingFuturesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent2` | `sports_data/models/betting_event2.py` |
| `WnbaV3ScoresBettingFuturesBySeasonErrorBody` | `sports_data/errors/wnba_v3_scores_betting_futures_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_futures_by_season_sportsbook_group

- **Route**: `GET /v3/wnba/scores/{format}/BettingFuturesBySeason/{season}/{sportsbookgroup}`
- **Signature**: `def wnba_v3_scores_betting_futures_by_season_sportsbook_group(format: FormatOrStr, season: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `sportsbookgroup`
- **Params**: `format` — path · `season` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingEvent2]`
- **Returns (raw)**: `ApiResult[list[BettingEvent2], WnbaV3ScoresBettingFuturesBySeasonSportsbookGroupErrorBody]`
- **Error**: `WnbaV3ScoresBettingFuturesBySeasonSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent2` | `sports_data/models/betting_event2.py` |
| `WnbaV3ScoresBettingFuturesBySeasonSportsbookGroupErrorBody` | `sports_data/errors/wnba_v3_scores_betting_futures_by_season_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_market

- **Route**: `GET /v3/wnba/scores/{format}/BettingMarket/{marketId}`
- **Signature**: `def wnba_v3_scores_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, WnbaV3ScoresBettingMarketErrorBody]`
- **Error**: `WnbaV3ScoresBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `WnbaV3ScoresBettingMarketErrorBody` | `sports_data/errors/wnba_v3_scores_betting_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_market_sportsbook_group

- **Route**: `GET /v3/wnba/scores/{format}/BettingMarket/{marketId}/{sportsbookgroup}`
- **Signature**: `def wnba_v3_scores_betting_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarket`
- **Returns (raw)**: `ApiResult[BettingMarket, WnbaV3ScoresBettingMarketSportsbookGroupErrorBody]`
- **Error**: `WnbaV3ScoresBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `WnbaV3ScoresBettingMarketSportsbookGroupErrorBody` | `sports_data/errors/wnba_v3_scores_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_markets_by_event

- **Route**: `GET /v3/wnba/scores/{format}/BettingMarkets/{eventId}`
- **Signature**: `def wnba_v3_scores_betting_markets_by_event(format: FormatOrStr, event_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId`
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByEventErrorBody]`
- **Error**: `WnbaV3ScoresBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `WnbaV3ScoresBettingMarketsByEventErrorBody` | `sports_data/errors/wnba_v3_scores_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v3/wnba/scores/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}`
- **Signature**: `def wnba_v3_scores_betting_markets_by_event_sportsbook_group(format: FormatOrStr, event_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `WnbaV3ScoresBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `WnbaV3ScoresBettingMarketsByEventSportsbookGroupErrorBody` | `sports_data/errors/wnba_v3_scores_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_markets_by_game

- **Route**: `GET /v3/wnba/scores/{format}/BettingMarketsByGameID/{gameID}`
- **Signature**: `def wnba_v3_scores_betting_markets_by_game(format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameID`
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByGameErrorBody]`
- **Error**: `WnbaV3ScoresBettingMarketsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `WnbaV3ScoresBettingMarketsByGameErrorBody` | `sports_data/errors/wnba_v3_scores_betting_markets_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_markets_by_game_sportsbook_group

- **Route**: `GET /v3/wnba/scores/{format}/BettingMarketsByGameID/{gameID}/{sportsbookgroup}`
- **Signature**: `def wnba_v3_scores_betting_markets_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`, `sportsbookgroup`
- **Params**: `format` — path · `game_id` — path `gameID` · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByGameSportsbookGroupErrorBody]`
- **Error**: `WnbaV3ScoresBettingMarketsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `WnbaV3ScoresBettingMarketsByGameSportsbookGroupErrorBody` | `sports_data/errors/wnba_v3_scores_betting_markets_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_markets_by_market_type

- **Route**: `GET /v3/wnba/scores/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}`
- **Signature**: `def wnba_v3_scores_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID`
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByMarketTypeErrorBody]`
- **Error**: `WnbaV3ScoresBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `WnbaV3ScoresBettingMarketsByMarketTypeErrorBody` | `sports_data/errors/wnba_v3_scores_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v3/wnba/scores/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}`
- **Signature**: `def wnba_v3_scores_betting_markets_by_market_type_sportsbook_group(format: FormatOrStr, event_id: str, market_type_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `WnbaV3ScoresBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `sports_data/errors/wnba_v3_scores_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_metadata

- **Route**: `GET /v3/wnba/scores/{format}/BettingMetadata`
- **Signature**: `def wnba_v3_scores_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `BettingEntityMetadataCollection`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection, WnbaV3ScoresBettingMetadataErrorBody]`
- **Error**: `WnbaV3ScoresBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEntityMetadataCollection` | `sports_data/models/betting_entity_metadata_collection.py` |
| `WnbaV3ScoresBettingMetadataErrorBody` | `sports_data/errors/wnba_v3_scores_betting_metadata_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_player_props_by_game

- **Route**: `GET /v3/wnba/scores/{format}/BettingPlayerPropsByGameID/{gameId}`
- **Signature**: `def wnba_v3_scores_betting_player_props_by_game(format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`
- **Params**: `format` — path · `game_id` — path `gameId`
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], WnbaV3ScoresBettingPlayerPropsByGameErrorBody]`
- **Error**: `WnbaV3ScoresBettingPlayerPropsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `WnbaV3ScoresBettingPlayerPropsByGameErrorBody` | `sports_data/errors/wnba_v3_scores_betting_player_props_by_game_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_betting_player_props_by_game_sportsbook_group

- **Route**: `GET /v3/wnba/scores/{format}/BettingPlayerPropsByGameID/{gameId}/{sportsbookgroup}`
- **Signature**: `def wnba_v3_scores_betting_player_props_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `game_id`, `sportsbookgroup`
- **Params**: `format` — path · `game_id` — path `gameId` · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingMarket]`
- **Returns (raw)**: `ApiResult[list[BettingMarket], WnbaV3ScoresBettingPlayerPropsByGameSportsbookGroupErrorBody]`
- **Error**: `WnbaV3ScoresBettingPlayerPropsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket` | `sports_data/models/betting_market.py` |
| `WnbaV3ScoresBettingPlayerPropsByGameSportsbookGroupErrorBody` | `sports_data/errors/wnba_v3_scores_betting_player_props_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_box_score_final

- **Route**: `GET /v3/wnba/scores/{format}/BoxScoreFinal/{gameid}`
- **Signature**: `def wnba_v3_scores_box_score_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `BoxScore6`
- **Returns (raw)**: `ApiResult[BoxScore6, WnbaV3ScoresBoxScoreFinalErrorBody]`
- **Error**: `WnbaV3ScoresBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore6` | `sports_data/models/box_score6.py` |
| `WnbaV3ScoresBoxScoreFinalErrorBody` | `sports_data/errors/wnba_v3_scores_box_score_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_box_score_live_final

- **Route**: `GET /v3/wnba/scores/{format}/BoxScore/{gameid}`
- **Signature**: `def wnba_v3_scores_box_score_live_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `BoxScore6`
- **Returns (raw)**: `ApiResult[BoxScore6, WnbaV3ScoresBoxScoreLiveFinalErrorBody]`
- **Error**: `WnbaV3ScoresBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore6` | `sports_data/models/box_score6.py` |
| `WnbaV3ScoresBoxScoreLiveFinalErrorBody` | `sports_data/errors/wnba_v3_scores_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_box_scores_by_date_final

- **Route**: `GET /v3/wnba/scores/{format}/BoxScoresFinal/{date}`
- **Signature**: `def wnba_v3_scores_box_scores_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore6]`
- **Returns (raw)**: `ApiResult[list[BoxScore6], WnbaV3ScoresBoxScoresByDateFinalErrorBody]`
- **Error**: `WnbaV3ScoresBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore6` | `sports_data/models/box_score6.py` |
| `WnbaV3ScoresBoxScoresByDateFinalErrorBody` | `sports_data/errors/wnba_v3_scores_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_box_scores_by_date_live_final

- **Route**: `GET /v3/wnba/scores/{format}/BoxScores/{date}`
- **Signature**: `def wnba_v3_scores_box_scores_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore6]`
- **Returns (raw)**: `ApiResult[list[BoxScore6], WnbaV3ScoresBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `WnbaV3ScoresBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore6` | `sports_data/models/box_score6.py` |
| `WnbaV3ScoresBoxScoresByDateLiveFinalErrorBody` | `sports_data/errors/wnba_v3_scores_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_games_by_date_final

- **Route**: `GET /v3/wnba/scores/{format}/GamesByDateFinal/{date}`
- **Signature**: `def wnba_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game10]`
- **Returns (raw)**: `ApiResult[list[Game10], WnbaV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `WnbaV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game10` | `sports_data/models/game10.py` |
| `WnbaV3ScoresGamesByDateFinalErrorBody` | `sports_data/errors/wnba_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/wnba/scores/{format}/GamesByDate/{date}`
- **Signature**: `def wnba_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game10]`
- **Returns (raw)**: `ApiResult[list[Game10], WnbaV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `WnbaV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game10` | `sports_data/models/game10.py` |
| `WnbaV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data/errors/wnba_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_games_basic_by_date_final

- **Route**: `GET /v3/wnba/scores/{format}/ScoresBasicFinal/{date}`
- **Signature**: `def wnba_v3_scores_games_basic_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic7]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic7], WnbaV3ScoresGamesBasicByDateFinalErrorBody]`
- **Error**: `WnbaV3ScoresGamesBasicByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic7` | `sports_data/models/score_basic7.py` |
| `WnbaV3ScoresGamesBasicByDateFinalErrorBody` | `sports_data/errors/wnba_v3_scores_games_basic_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_games_basic_by_date_live_final

- **Route**: `GET /v3/wnba/scores/{format}/ScoresBasic/{date}`
- **Signature**: `def wnba_v3_scores_games_basic_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic7]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic7], WnbaV3ScoresGamesBasicByDateLiveFinalErrorBody]`
- **Error**: `WnbaV3ScoresGamesBasicByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic7` | `sports_data/models/score_basic7.py` |
| `WnbaV3ScoresGamesBasicByDateLiveFinalErrorBody` | `sports_data/errors/wnba_v3_scores_games_basic_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_player_details_by_active

- **Route**: `GET /v3/wnba/scores/{format}/Players`
- **Signature**: `def wnba_v3_scores_player_details_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player8]`
- **Returns (raw)**: `ApiResult[list[Player8], WnbaV3ScoresPlayerDetailsByActiveErrorBody]`
- **Error**: `WnbaV3ScoresPlayerDetailsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player8` | `sports_data/models/player8.py` |
| `WnbaV3ScoresPlayerDetailsByActiveErrorBody` | `sports_data/errors/wnba_v3_scores_player_details_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_player_details_by_team

- **Route**: `GET /v3/wnba/scores/{format}/Players/{team}`
- **Signature**: `def wnba_v3_scores_player_details_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[Player8]`
- **Returns (raw)**: `ApiResult[list[Player8], WnbaV3ScoresPlayerDetailsByTeamErrorBody]`
- **Error**: `WnbaV3ScoresPlayerDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player8` | `sports_data/models/player8.py` |
| `WnbaV3ScoresPlayerDetailsByTeamErrorBody` | `sports_data/errors/wnba_v3_scores_player_details_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_player_season_stats

- **Route**: `GET /v3/wnba/scores/{format}/PlayerSeasonStats/{season}`
- **Signature**: `def wnba_v3_scores_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason8]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason8], WnbaV3ScoresPlayerSeasonStatsErrorBody]`
- **Error**: `WnbaV3ScoresPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason8` | `sports_data/models/player_season8.py` |
| `WnbaV3ScoresPlayerSeasonStatsErrorBody` | `sports_data/errors/wnba_v3_scores_player_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_player_season_stats_by_team

- **Route**: `GET /v3/wnba/scores/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Signature**: `def wnba_v3_scores_player_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason8]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason8], WnbaV3ScoresPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `WnbaV3ScoresPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason8` | `sports_data/models/player_season8.py` |
| `WnbaV3ScoresPlayerSeasonStatsByTeamErrorBody` | `sports_data/errors/wnba_v3_scores_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_pre_game_odds_by_date

- **Route**: `GET /v3/wnba/scores/{format}/GameOddsByDate/{date}`
- **Signature**: `def wnba_v3_scores_pre_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], WnbaV3ScoresPreGameOddsByDateErrorBody]`
- **Error**: `WnbaV3ScoresPreGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo4` | `sports_data/models/game_info4.py` |
| `WnbaV3ScoresPreGameOddsByDateErrorBody` | `sports_data/errors/wnba_v3_scores_pre_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_pre_game_odds_line_movement

- **Route**: `GET /v3/wnba/scores/{format}/GameOddsLineMovement/{gameid}`
- **Signature**: `def wnba_v3_scores_pre_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo4]`
- **Returns (raw)**: `ApiResult[list[GameInfo4], WnbaV3ScoresPreGameOddsLineMovementErrorBody]`
- **Error**: `WnbaV3ScoresPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `GameInfo4` | `sports_data/models/game_info4.py` |
| `WnbaV3ScoresPreGameOddsLineMovementErrorBody` | `sports_data/errors/wnba_v3_scores_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_schedules

- **Route**: `GET /v3/wnba/scores/{format}/Games/{Season}`
- **Signature**: `def wnba_v3_scores_schedules(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path `Season`
- **Returns (parsed)**: `list[Game10]`
- **Returns (raw)**: `ApiResult[list[Game10], WnbaV3ScoresSchedulesErrorBody]`
- **Error**: `WnbaV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game10` | `sports_data/models/game10.py` |
| `WnbaV3ScoresSchedulesErrorBody` | `sports_data/errors/wnba_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_schedules_basic

- **Route**: `GET /v3/wnba/scores/{format}/SchedulesBasic/{Season}`
- **Signature**: `def wnba_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path `Season`
- **Returns (parsed)**: `list[SchedulesBasic]`
- **Returns (raw)**: `ApiResult[list[SchedulesBasic], WnbaV3ScoresSchedulesBasicErrorBody]`
- **Error**: `WnbaV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `SchedulesBasic` | `sports_data/models/schedules_basic.py` |
| `WnbaV3ScoresSchedulesBasicErrorBody` | `sports_data/errors/wnba_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_season_current

- **Route**: `GET /v3/wnba/scores/{format}/CurrentSeason`
- **Signature**: `def wnba_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `Season7`
- **Returns (raw)**: `ApiResult[Season7, WnbaV3ScoresSeasonCurrentErrorBody]`
- **Error**: `WnbaV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Season7` | `sports_data/models/season7.py` |
| `WnbaV3ScoresSeasonCurrentErrorBody` | `sports_data/errors/wnba_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_sportsbooks_by_active

- **Route**: `GET /v3/wnba/scores/{format}/ActiveSportsbooks`
- **Signature**: `def wnba_v3_scores_sportsbooks_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], WnbaV3ScoresSportsbooksByActiveErrorBody]`
- **Error**: `WnbaV3ScoresSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Sportsbook` | `sports_data/models/sportsbook.py` |
| `WnbaV3ScoresSportsbooksByActiveErrorBody` | `sports_data/errors/wnba_v3_scores_sportsbooks_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_stadiums

- **Route**: `GET /v3/wnba/scores/{format}/Stadiums`
- **Signature**: `def wnba_v3_scores_stadiums(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Stadium6]`
- **Returns (raw)**: `ApiResult[list[Stadium6], WnbaV3ScoresStadiumsErrorBody]`
- **Error**: `WnbaV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Stadium6` | `sports_data/models/stadium6.py` |
| `WnbaV3ScoresStadiumsErrorBody` | `sports_data/errors/wnba_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_standings

- **Route**: `GET /v3/wnba/scores/{format}/Standings/{season}`
- **Signature**: `def wnba_v3_scores_standings(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, WnbaV3ScoresStandingsErrorBody]`
- **Error**: `WnbaV3ScoresStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `WnbaV3ScoresStandingsErrorBody` | `sports_data/errors/wnba_v3_scores_standings_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_team_game_stats_by_date_final

- **Route**: `GET /v3/wnba/scores/{format}/TeamGameStatsByDateFinal/{date}`
- **Signature**: `def wnba_v3_scores_team_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame7]`
- **Returns (raw)**: `ApiResult[list[TeamGame7], WnbaV3ScoresTeamGameStatsByDateFinalErrorBody]`
- **Error**: `WnbaV3ScoresTeamGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame7` | `sports_data/models/team_game7.py` |
| `WnbaV3ScoresTeamGameStatsByDateFinalErrorBody` | `sports_data/errors/wnba_v3_scores_team_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_team_game_stats_by_date_live_final

- **Route**: `GET /v3/wnba/scores/{format}/TeamGameStatsByDate/{date}`
- **Signature**: `def wnba_v3_scores_team_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame7]`
- **Returns (raw)**: `ApiResult[list[TeamGame7], WnbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody]`
- **Error**: `WnbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame7` | `sports_data/models/team_game7.py` |
| `WnbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody` | `sports_data/errors/wnba_v3_scores_team_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_team_profiles_all

- **Route**: `GET /v3/wnba/scores/{format}/Teams`
- **Signature**: `def wnba_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team8]`
- **Returns (raw)**: `ApiResult[list[Team8], WnbaV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `WnbaV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team8` | `sports_data/models/team8.py` |
| `WnbaV3ScoresTeamProfilesAllErrorBody` | `sports_data/errors/wnba_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.wnba_v3_scores.wnba_v3_scores_team_season_stats

- **Route**: `GET /v3/wnba/scores/{format}/TeamSeasonStats/{season}`
- **Signature**: `def wnba_v3_scores_team_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamSeason7]`
- **Returns (raw)**: `ApiResult[list[TeamSeason7], WnbaV3ScoresTeamSeasonStatsErrorBody]`
- **Error**: `WnbaV3ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamSeason7` | `sports_data/models/team_season7.py` |
| `WnbaV3ScoresTeamSeasonStatsErrorBody` | `sports_data/errors/wnba_v3_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

