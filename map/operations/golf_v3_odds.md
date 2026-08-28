<!-- Generated file — do not edit; regenerated with the SDK. -->

# GolfV3Odds — operations

Accessor: `client.golf_v3_odds` · Source: `sports_data/apis/golf_v3_odds.py` · 21 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.golf_v3_odds.golf_v3_odds_betting_events_by_date

- **Route**: `GET /v3/golf/odds/{format}/BettingEventsByDate/{date}`
- **Signature**: `def golf_v3_odds_betting_events_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BettingEvent1]`
- **Returns (raw)**: `ApiResult[list[BettingEvent1], GolfV3OddsBettingEventsByDateErrorBody]`
- **Error**: `GolfV3OddsBettingEventsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent1` | `sports_data/models/betting_event1.py` |
| `GolfV3OddsBettingEventsByDateErrorBody` | `sports_data/errors/golf_v3_odds_betting_events_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_events_by_season

- **Route**: `GET /v3/golf/odds/{format}/BettingEvents/{season}`
- **Signature**: `def golf_v3_odds_betting_events_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[BettingEvent1]`
- **Returns (raw)**: `ApiResult[list[BettingEvent1], GolfV3OddsBettingEventsBySeasonErrorBody]`
- **Error**: `GolfV3OddsBettingEventsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEvent1` | `sports_data/models/betting_event1.py` |
| `GolfV3OddsBettingEventsBySeasonErrorBody` | `sports_data/errors/golf_v3_odds_betting_events_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_market

- **Route**: `GET /v3/golf/odds/{format}/BettingMarket/{marketId}`
- **Signature**: `def golf_v3_odds_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`
- **Params**: `format` — path · `market_id` — path `marketId`
- **Returns (parsed)**: `BettingMarket1`
- **Returns (raw)**: `ApiResult[BettingMarket1, GolfV3OddsBettingMarketErrorBody]`
- **Error**: `GolfV3OddsBettingMarketErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket1` | `sports_data/models/betting_market1.py` |
| `GolfV3OddsBettingMarketErrorBody` | `sports_data/errors/golf_v3_odds_betting_market_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_market_sportsbook_group

- **Route**: `GET /v3/golf/odds/{format}/BettingMarket/{marketId}/{sportsbookgroup}`
- **Signature**: `def golf_v3_odds_betting_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `market_id`, `sportsbookgroup`
- **Params**: `format` — path · `market_id` — path `marketId` · `sportsbookgroup` — path
- **Returns (parsed)**: `BettingMarket1`
- **Returns (raw)**: `ApiResult[BettingMarket1, GolfV3OddsBettingMarketSportsbookGroupErrorBody]`
- **Error**: `GolfV3OddsBettingMarketSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingMarket1` | `sports_data/models/betting_market1.py` |
| `GolfV3OddsBettingMarketSportsbookGroupErrorBody` | `sports_data/errors/golf_v3_odds_betting_market_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_markets_by_event

- **Route**: `GET /v3/golf/odds/{format}/BettingMarkets/{eventId}`
- **Signature**: `def golf_v3_odds_betting_markets_by_event(format: FormatOrStr, event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `include` — query
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByEventErrorBody]`
- **Error**: `GolfV3OddsBettingMarketsByEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket1` | `sports_data/models/betting_market1.py` |
| `GolfV3OddsBettingMarketsByEventErrorBody` | `sports_data/errors/golf_v3_odds_betting_markets_by_event_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_markets_by_event_sportsbook_group

- **Route**: `GET /v3/golf/odds/{format}/BettingMarketsByEvent/{eventId}/{sportsbookgroup}`
- **Signature**: `def golf_v3_odds_betting_markets_by_event_sportsbook_group(format: FormatOrStr, event_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByEventSportsbookGroupErrorBody]`
- **Error**: `GolfV3OddsBettingMarketsByEventSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket1` | `sports_data/models/betting_market1.py` |
| `GolfV3OddsBettingMarketsByEventSportsbookGroupErrorBody` | `sports_data/errors/golf_v3_odds_betting_markets_by_event_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_markets_by_market_type

- **Route**: `GET /v3/golf/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}`
- **Signature**: `def golf_v3_odds_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `include` — query
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByMarketTypeErrorBody]`
- **Error**: `GolfV3OddsBettingMarketsByMarketTypeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket1` | `sports_data/models/betting_market1.py` |
| `GolfV3OddsBettingMarketsByMarketTypeErrorBody` | `sports_data/errors/golf_v3_odds_betting_markets_by_market_type_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_markets_by_market_type_sportsbook_group

- **Route**: `GET /v3/golf/odds/{format}/BettingMarketsByMarketType/{eventId}/{marketTypeID}/{sportsbookgroup}`
- **Signature**: `def golf_v3_odds_betting_markets_by_market_type_sportsbook_group(format: FormatOrStr, event_id: str, market_type_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `event_id`, `market_type_id`, `sportsbookgroup`
- **Params**: `format` — path · `event_id` — path `eventId` · `market_type_id` — path `marketTypeID` · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]`
- **Error**: `GolfV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket1` | `sports_data/models/betting_market1.py` |
| `GolfV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody` | `sports_data/errors/golf_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_markets_by_tournament

- **Route**: `GET /v3/golf/odds/{format}/BettingMarketsByTournamentID/{tournamentid}`
- **Signature**: `def golf_v3_odds_betting_markets_by_tournament(format: FormatOrStr, tournamentid: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByTournamentErrorBody]`
- **Error**: `GolfV3OddsBettingMarketsByTournamentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket1` | `sports_data/models/betting_market1.py` |
| `GolfV3OddsBettingMarketsByTournamentErrorBody` | `sports_data/errors/golf_v3_odds_betting_markets_by_tournament_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_markets_by_tournament_sportsbook_group

- **Route**: `GET /v3/golf/odds/{format}/BettingMarketsByTournamentID/{tournamentid}/{sportsbookgroup}`
- **Signature**: `def golf_v3_odds_betting_markets_by_tournament_sportsbook_group(format: FormatOrStr, tournamentid: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`, `sportsbookgroup`
- **Params**: `format` — path · `tournamentid` — path · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], GolfV3OddsBettingMarketsByTournamentSportsbookGroupErrorBody]`
- **Error**: `GolfV3OddsBettingMarketsByTournamentSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket1` | `sports_data/models/betting_market1.py` |
| `GolfV3OddsBettingMarketsByTournamentSportsbookGroupErrorBody` | `sports_data/errors/golf_v3_odds_betting_markets_by_tournament_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_metadata

- **Route**: `GET /v3/golf/odds/{format}/BettingMetadata`
- **Signature**: `def golf_v3_odds_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `BettingEntityMetadataCollection1`
- **Returns (raw)**: `ApiResult[BettingEntityMetadataCollection1, GolfV3OddsBettingMetadataErrorBody]`
- **Error**: `GolfV3OddsBettingMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BettingEntityMetadataCollection1` | `sports_data/models/betting_entity_metadata_collection1.py` |
| `GolfV3OddsBettingMetadataErrorBody` | `sports_data/errors/golf_v3_odds_betting_metadata_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_betting_player_props_by_tournament_sportsbook_group

- **Route**: `GET /v3/golf/odds/{format}/BettingPlayerPropsByTournamentID/{tournamentid}/{sportsbookgroup}`
- **Signature**: `def golf_v3_odds_betting_player_props_by_tournament_sportsbook_group(format: FormatOrStr, tournamentid: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`, `sportsbookgroup`
- **Params**: `format` — path · `tournamentid` — path · `sportsbookgroup` — path · `include` — query
- **Returns (parsed)**: `list[BettingMarket1]`
- **Returns (raw)**: `ApiResult[list[BettingMarket1], GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody]`
- **Error**: `GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `IncludeOrStr` | `sports_data/models/enums/include.py` |
| `BettingMarket1` | `sports_data/models/betting_market1.py` |
| `GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody` | `sports_data/errors/golf_v3_odds_betting_player_props_by_tournament_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_in_play_tournament_odds

- **Route**: `GET /v3/golf/odds/{format}/InPlayTournamentOdds/{tournamentid}`
- **Signature**: `def golf_v3_odds_in_play_tournament_odds(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `TournamentOdds`
- **Returns (raw)**: `ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsErrorBody]`
- **Error**: `GolfV3OddsInPlayTournamentOddsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TournamentOdds` | `sports_data/models/tournament_odds.py` |
| `GolfV3OddsInPlayTournamentOddsErrorBody` | `sports_data/errors/golf_v3_odds_in_play_tournament_odds_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_in_play_tournament_odds_sportsbook_group

- **Route**: `GET /v3/golf/odds/{format}/InPlayTournamentOdds/{tournamentid}/{sportsbookgroup}`
- **Signature**: `def golf_v3_odds_in_play_tournament_odds_sportsbook_group(format: FormatOrStr, tournamentid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`, `sportsbookgroup`
- **Params**: `format` — path · `tournamentid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `TournamentOdds`
- **Returns (raw)**: `ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsSportsbookGroupErrorBody]`
- **Error**: `GolfV3OddsInPlayTournamentOddsSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TournamentOdds` | `sports_data/models/tournament_odds.py` |
| `GolfV3OddsInPlayTournamentOddsSportsbookGroupErrorBody` | `sports_data/errors/golf_v3_odds_in_play_tournament_odds_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_in_play_tournament_odds_line_movement

- **Route**: `GET /v3/golf/odds/{format}/InPlayTournamentOddsLineMovement/{tournamentid}`
- **Signature**: `def golf_v3_odds_in_play_tournament_odds_line_movement(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `TournamentOdds`
- **Returns (raw)**: `ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsLineMovementErrorBody]`
- **Error**: `GolfV3OddsInPlayTournamentOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TournamentOdds` | `sports_data/models/tournament_odds.py` |
| `GolfV3OddsInPlayTournamentOddsLineMovementErrorBody` | `sports_data/errors/golf_v3_odds_in_play_tournament_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/golf/odds/{format}/InPlayTournamentOddsLineMovement/{tournamentid}/{sportsbookgroup}`
- **Signature**: `def golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group(format: FormatOrStr, tournamentid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`, `sportsbookgroup`
- **Params**: `format` — path · `tournamentid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `TournamentOdds`
- **Returns (raw)**: `ApiResult[TournamentOdds, GolfV3OddsInPlayTournamentOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `GolfV3OddsInPlayTournamentOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TournamentOdds` | `sports_data/models/tournament_odds.py` |
| `GolfV3OddsInPlayTournamentOddsLineMovementSportsbookGroupErrorBody` | `sports_data/errors/golf_v3_odds_in_play_tournament_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_sportsbooks_by_active

- **Route**: `GET /v3/golf/odds/{format}/ActiveSportsbooks`
- **Signature**: `def golf_v3_odds_sportsbooks_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Sportsbook]`
- **Returns (raw)**: `ApiResult[list[Sportsbook], GolfV3OddsSportsbooksByActiveErrorBody]`
- **Error**: `GolfV3OddsSportsbooksByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Sportsbook` | `sports_data/models/sportsbook.py` |
| `GolfV3OddsSportsbooksByActiveErrorBody` | `sports_data/errors/golf_v3_odds_sportsbooks_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_tournament_odds

- **Route**: `GET /v3/golf/odds/{format}/TournamentOdds/{tournamentid}`
- **Signature**: `def golf_v3_odds_tournament_odds(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `TournamentOdds`
- **Returns (raw)**: `ApiResult[TournamentOdds, GolfV3OddsTournamentOddsErrorBody]`
- **Error**: `GolfV3OddsTournamentOddsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TournamentOdds` | `sports_data/models/tournament_odds.py` |
| `GolfV3OddsTournamentOddsErrorBody` | `sports_data/errors/golf_v3_odds_tournament_odds_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_tournament_odds_sportsbook_group

- **Route**: `GET /v3/golf/odds/{format}/TournamentOdds/{tournamentid}/{sportsbookgroup}`
- **Signature**: `def golf_v3_odds_tournament_odds_sportsbook_group(format: FormatOrStr, tournamentid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`, `sportsbookgroup`
- **Params**: `format` — path · `tournamentid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `TournamentOdds`
- **Returns (raw)**: `ApiResult[TournamentOdds, GolfV3OddsTournamentOddsSportsbookGroupErrorBody]`
- **Error**: `GolfV3OddsTournamentOddsSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TournamentOdds` | `sports_data/models/tournament_odds.py` |
| `GolfV3OddsTournamentOddsSportsbookGroupErrorBody` | `sports_data/errors/golf_v3_odds_tournament_odds_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_tournament_odds_line_movement

- **Route**: `GET /v3/golf/odds/{format}/TournamentOddsLineMovement/{tournamentid}`
- **Signature**: `def golf_v3_odds_tournament_odds_line_movement(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `TournamentOdds`
- **Returns (raw)**: `ApiResult[TournamentOdds, GolfV3OddsTournamentOddsLineMovementErrorBody]`
- **Error**: `GolfV3OddsTournamentOddsLineMovementErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TournamentOdds` | `sports_data/models/tournament_odds.py` |
| `GolfV3OddsTournamentOddsLineMovementErrorBody` | `sports_data/errors/golf_v3_odds_tournament_odds_line_movement_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_odds.golf_v3_odds_tournament_odds_line_movement_sportsbook_group

- **Route**: `GET /v3/golf/odds/{format}/TournamentOddsLineMovement/{tournamentid}/{sportsbookgroup}`
- **Signature**: `def golf_v3_odds_tournament_odds_line_movement_sportsbook_group(format: FormatOrStr, tournamentid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`, `sportsbookgroup`
- **Params**: `format` — path · `tournamentid` — path · `sportsbookgroup` — path
- **Returns (parsed)**: `TournamentOdds`
- **Returns (raw)**: `ApiResult[TournamentOdds, GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody]`
- **Error**: `GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TournamentOdds` | `sports_data/models/tournament_odds.py` |
| `GolfV3OddsTournamentOddsLineMovementSportsbookGroupErrorBody` | `sports_data/errors/golf_v3_odds_tournament_odds_line_movement_sportsbook_group_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

