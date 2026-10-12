<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoccerV4Odds — operations

Accessor: `client.soccer_v4_odds` · Source: `sports_data_io/apis/soccer_v4_odds.py` · 28 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.soccer_v4_odds.soccer_v4_odds_betting_events_by_date

- **Route**: `GET /v4/soccer/odds/{format}/BettingEventsByDate/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_events_by_date(competition: str, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `date`
- **Params**: `format_` — path `format` · `competition` — path · `date` — path
- **Returns (parsed)**: `list[BettingEvent3]`
- **Returns (raw)**: `ApiResult[list[BettingEvent3], SoccerV4OddsBettingEventsByDateErrorBody]`
- **Error**: `SoccerV4OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent3` | `sports_data_io/models/betting_event3.py` |
| `SoccerV4OddsBettingEventsByDateErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_events_by_season

- **Route**: `GET /v4/soccer/odds/{format}/BettingEventsBySeason/{competition}/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_events_by_season(competition: str, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `season`
- **Params**: `format_` — path `format` · `competition` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent3]`
- **Returns (raw)**: `ApiResult[list[BettingEvent3], SoccerV4OddsBettingEventsBySeasonErrorBody]`
- **Error**: `SoccerV4OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent3` | `sports_data_io/models/betting_event3.py` |
| `SoccerV4OddsBettingEventsBySeasonErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_futures_by_season

- **Route**: `GET /v4/soccer/odds/{format}/BettingFuturesBySeason/{competition}/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_futures_by_season(competition: str, season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `season`
- **Params**: `format_` — path `format` · `competition` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent3]`
- **Returns (raw)**: `ApiResult[list[BettingEvent3], SoccerV4OddsBettingFuturesBySeasonErrorBody]`
- **Error**: `SoccerV4OddsBettingFuturesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent3` | `sports_data_io/models/betting_event3.py` |
| `SoccerV4OddsBettingFuturesBySeasonErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_futures_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_futures_by_season_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/BettingFuturesBySeason/{competition}/{season}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_futures_by_season_sportsbook_group(competition: str, season: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `season`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `season` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingEvent3]`
- **Returns (raw)**: `ApiResult[list[BettingEvent3], SoccerV4OddsBettingFuturesBySeasonSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsBettingFuturesBySeasonSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEvent3` | `sports_data_io/models/betting_event3.py` |
| `SoccerV4OddsBettingFuturesBySeasonSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_futures_by_season_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_market

- **Route**: `GET /v4/soccer/odds/{format}/BettingMarket/{competition}/{marketId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_market(competition: str, market_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `market_id`
- **Params**: `format_` — path `format` · `competition` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket1`
- **Returns (raw)**: `ApiResult[BettingMarket1, SoccerV4OddsBettingMarketErrorBody]`
- **Error**: `SoccerV4OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket1` | `sports_data_io/models/betting_market1.py` |
| `SoccerV4OddsBettingMarketErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_market_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/BettingMarket/{competition}/{marketId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_market_sportsbook_group(competition: str, market_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `market_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarket1`
- **Returns (raw)**: `ApiResult[BettingMarket1, SoccerV4OddsBettingMarketSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket1` | `sports_data_io/models/betting_market1.py` |
| `SoccerV4OddsBettingMarketSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_markets_by_event

- **Route**: `GET /v4/soccer/odds/{format}/BettingMarkets/{competition}/{eventId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_markets_by_event(competition: str, event_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `event_id`
- **Params**: `format_` — path `format` · `competition` — path · `event_id` — path `eventId`
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByEventErrorBody]`
- **Error**: `SoccerV4OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket1` | `sports_data_io/models/betting_market1.py` |
| `SoccerV4OddsBettingMarketsByEventErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/BettingMarketsByEvent/{competition}/{eventId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_markets_by_event_sportsbook_group(competition: str, event_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `event_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `event_id` — path `eventId` · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket1` | `sports_data_io/models/betting_market1.py` |
| `SoccerV4OddsBettingMarketsByEventSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_markets_by_game

- **Route**: `GET /v4/soccer/odds/{format}/BettingMarketsByGameID/{competition}/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_markets_by_game(competition: str, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `gameid`
- **Params**: `format_` — path `format` · `competition` — path · `gameid` — path
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByGameErrorBody]`
- **Error**: `SoccerV4OddsBettingMarketsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket1` | `sports_data_io/models/betting_market1.py` |
| `SoccerV4OddsBettingMarketsByGameErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_markets_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_markets_by_game_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/BettingMarketsByGameID/{competition}/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_markets_by_game_sportsbook_group(competition: str, gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByGameSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsBettingMarketsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket1` | `sports_data_io/models/betting_market1.py` |
| `SoccerV4OddsBettingMarketsByGameSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_markets_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_markets_by_market_type

- **Route**: `GET /v4/soccer/odds/{format}/BettingMarketsByMarketType/{competition}/{eventId}/{marketTypeID}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_markets_by_market_type(competition: str, event_id: str, market_type_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `event_id`, `market_type_id`
- **Params**: `format_` — path `format` · `competition` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID`
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `SoccerV4OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket1` | `sports_data_io/models/betting_market1.py` |
| `SoccerV4OddsBettingMarketsByMarketTypeErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/BettingMarketsByMarketType/{competition}/{eventId}/{marketTypeID}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_markets_by_market_type_sportsbook_group(competition: str, event_id: str, market_type_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `event_id`, `market_type_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], SoccerV4OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket1` | `sports_data_io/models/betting_market1.py` |
| `SoccerV4OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_metadata

- **Route**: `GET /v4/soccer/odds/{format}/BettingMetadata`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_metadata(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `BettingEntityMetadataCollection1`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection1, SoccerV4OddsBettingMetadataErrorBody]`
- **Error**: `SoccerV4OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingEntityMetadataCollection1` | `sports_data_io/models/betting_entity_metadata_collection1.py` |
| `SoccerV4OddsBettingMetadataErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_player_props_by_game

- **Route**: `GET /v4/soccer/odds/{format}/BettingPlayerPropsByGameID/{competition}/{gameId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_player_props_by_game(competition: str, game_id: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `game_id`
- **Params**: `format_` — path `format` · `competition` — path · `game_id` — path `gameId`
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], SoccerV4OddsBettingPlayerPropsByGameErrorBody]`
- **Error**: `SoccerV4OddsBettingPlayerPropsByGameErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket1` | `sports_data_io/models/betting_market1.py` |
| `SoccerV4OddsBettingPlayerPropsByGameErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_player_props_by_game_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_betting_player_props_by_game_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/BettingPlayerPropsByGameID/{competition}/{gameId}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_betting_player_props_by_game_sportsbook_group(competition: str, game_id: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `game_id`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `game_id` — path `gameId` · `sportsbookgroup` — path
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], SoccerV4OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BettingMarket1` | `sports_data_io/models/betting_market1.py` |
| `SoccerV4OddsBettingPlayerPropsByGameSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_betting_player_props_by_game_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_in_game_odds_by_date

- **Route**: `GET /v4/soccer/odds/{format}/LiveGameOddsByDate/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_in_game_odds_by_date(competition: str, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `date`
- **Params**: `format_` — path `format` · `competition` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo7]`
- **Returns (raw)**: `ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsByDateErrorBody]`
- **Error**: `SoccerV4OddsInGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo7` | `sports_data_io/models/game_info7.py` |
| `SoccerV4OddsInGameOddsByDateErrorBody` | `sports_data_io/errors/soccer_v4_odds_in_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_in_game_odds_by_date_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/InGameOddsByDate/{competition}/{date}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_in_game_odds_by_date_sportsbook_group(competition: str, date: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `date`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `date` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo7]`
- **Returns (raw)**: `ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsByDateSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsInGameOddsByDateSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo7` | `sports_data_io/models/game_info7.py` |
| `SoccerV4OddsInGameOddsByDateSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_in_game_odds_by_date_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_in_game_odds_line_movement

- **Route**: `GET /v4/soccer/odds/{format}/LiveGameOddsLineMovement/{competition}/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_in_game_odds_line_movement(competition: str, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `gameid`
- **Params**: `format_` — path `format` · `competition` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo7]`
- **Returns (raw)**: `ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsLineMovementErrorBody]`
- **Error**: `SoccerV4OddsInGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo7` | `sports_data_io/models/game_info7.py` |
| `SoccerV4OddsInGameOddsLineMovementErrorBody` | `sports_data_io/errors/soccer_v4_odds_in_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_in_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/InGameOddsLineMovement/{competition}/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_in_game_odds_line_movement_sportsbook_group(competition: str, gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo7]`
- **Returns (raw)**: `ApiResult[list[GameInfo7], SoccerV4OddsInGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsInGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo7` | `sports_data_io/models/game_info7.py` |
| `SoccerV4OddsInGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_in_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/InGameOddsLineMovementWithResulting/{competition}/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(competition: str, gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult6]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult6], SoccerV4OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfoResult6` | `sports_data_io/models/game_info_result6.py` |
| `SoccerV4OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_period_game_odds_by_date

- **Route**: `GET /v4/soccer/odds/{format}/AlternateMarketGameOddsByDate/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_period_game_odds_by_date(competition: str, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `date`
- **Params**: `format_` — path `format` · `competition` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo7]`
- **Returns (raw)**: `ApiResult[list[GameInfo7], SoccerV4OddsPeriodGameOddsByDateErrorBody]`
- **Error**: `SoccerV4OddsPeriodGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo7` | `sports_data_io/models/game_info7.py` |
| `SoccerV4OddsPeriodGameOddsByDateErrorBody` | `sports_data_io/errors/soccer_v4_odds_period_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_period_game_odds_line_movement

- **Route**: `GET /v4/soccer/odds/{format}/AlternateMarketGameOddsLineMovement/{competition}/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_period_game_odds_line_movement(competition: str, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `gameid`
- **Params**: `format_` — path `format` · `competition` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo7]`
- **Returns (raw)**: `ApiResult[list[GameInfo7], SoccerV4OddsPeriodGameOddsLineMovementErrorBody]`
- **Error**: `SoccerV4OddsPeriodGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo7` | `sports_data_io/models/game_info7.py` |
| `SoccerV4OddsPeriodGameOddsLineMovementErrorBody` | `sports_data_io/errors/soccer_v4_odds_period_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/PreGameOddsByDate/{competition}/{date}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(competition: str, date: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `date`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `date` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo7]`
- **Returns (raw)**: `ApiResult[list[GameInfo7], SoccerV4OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo7` | `sports_data_io/models/game_info7.py` |
| `SoccerV4OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/PreGameOddsLineMovement/{competition}/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(competition: str, gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfo7]`
- **Returns (raw)**: `ApiResult[list[GameInfo7], SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo7` | `sports_data_io/models/game_info7.py` |
| `SoccerV4OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group

- **Route**: `GET /v4/soccer/odds/{format}/PreGameOddsLineMovementWithResulting/{competition}/{gameid}/{sportsbookgroup}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(competition: str, gameid: str, sportsbookgroup: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `gameid`, `sportsbookgroup`
- **Params**: `format_` — path `format` · `competition` — path · `gameid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `list[GameInfoResult6]`
- **Returns (raw)**: `ApiResult[list[GameInfoResult6], SoccerV4OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]`
- **Error**: `SoccerV4OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfoResult6` | `sports_data_io/models/game_info_result6.py` |
| `SoccerV4OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody` | `sports_data_io/errors/soccer_v4_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_pre_game_odds_by_date

- **Route**: `GET /v4/soccer/odds/{format}/GameOddsByDate/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_pre_game_odds_by_date(competition: str, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `date`
- **Params**: `format_` — path `format` · `competition` — path · `date` — path
- **Returns (parsed)**: `list[GameInfo7]`
- **Returns (raw)**: `ApiResult[list[GameInfo7], SoccerV4OddsPreGameOddsByDateErrorBody]`
- **Error**: `SoccerV4OddsPreGameOddsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo7` | `sports_data_io/models/game_info7.py` |
| `SoccerV4OddsPreGameOddsByDateErrorBody` | `sports_data_io/errors/soccer_v4_odds_pre_game_odds_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_pre_game_odds_line_movement

- **Route**: `GET /v4/soccer/odds/{format}/GameOddsLineMovement/{competition}/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_pre_game_odds_line_movement(competition: str, gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `gameid`
- **Params**: `format_` — path `format` · `competition` — path · `gameid` — path
- **Returns (parsed)**: `list[GameInfo7]`
- **Returns (raw)**: `ApiResult[list[GameInfo7], SoccerV4OddsPreGameOddsLineMovementErrorBody]`
- **Error**: `SoccerV4OddsPreGameOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `GameInfo7` | `sports_data_io/models/game_info7.py` |
| `SoccerV4OddsPreGameOddsLineMovementErrorBody` | `sports_data_io/errors/soccer_v4_odds_pre_game_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_odds.soccer_v4_odds_sportsbooks_by_active

- **Route**: `GET /v4/soccer/odds/{format}/ActiveSportsbooks`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_odds_sportsbooks_by_active(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], SoccerV4OddsSportsbooksByActiveErrorBody]`
- **Error**: `SoccerV4OddsSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Sportsbook` | `sports_data_io/models/sportsbook.py` |
| `SoccerV4OddsSportsbooksByActiveErrorBody` | `sports_data_io/errors/soccer_v4_odds_sportsbooks_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

