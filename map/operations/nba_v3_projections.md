<!-- Generated file — do not edit; regenerated with the SDK. -->

# NbaV3Projections — operations

Accessor: `client.nba_v3_projections` · Source: `sports_data_io/apis/nba_v3_projections.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nba_v3_projections.nba_v3_projections_dfs_slates_by_date

- **Route**: `GET /v3/nba/projections/{format}/DfsSlatesByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_projections_dfs_slates_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[DfsSlate]`
- **Returns (raw)**: `ApiResult[list[DfsSlate], NbaV3ProjectionsDfsSlatesByDateErrorBody]`
- **Error**: `NbaV3ProjectionsDfsSlatesByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DfsSlate` | `sports_data_io/models/dfs_slate.py` |
| `NbaV3ProjectionsDfsSlatesByDateErrorBody` | `sports_data_io/errors/nba_v3_projections_dfs_slates_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_projections.nba_v3_projections_player_details_by_injured

- **Route**: `GET /v3/nba/projections/{format}/InjuredPlayers`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_projections_player_details_by_injured(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player1]`
- **Returns (raw)**: `ApiResult[list[Player1], NbaV3ProjectionsPlayerDetailsByInjuredErrorBody]`
- **Error**: `NbaV3ProjectionsPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player1` | `sports_data_io/models/player1.py` |
| `NbaV3ProjectionsPlayerDetailsByInjuredErrorBody` | `sports_data_io/errors/nba_v3_projections_player_details_by_injured_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_projections.nba_v3_projections_projected_player_game_stats_by_date

- **Route**: `GET /v3/nba/projections/{format}/PlayerGameProjectionStatsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_projections_projected_player_game_stats_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGameProjection1]`
- **Returns (raw)**: `ApiResult[list[PlayerGameProjection1], NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]`
- **Error**: `NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGameProjection1` | `sports_data_io/models/player_game_projection1.py` |
| `NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody` | `sports_data_io/errors/nba_v3_projections_projected_player_game_stats_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_projections.nba_v3_projections_projected_player_season_stats

- **Route**: `GET /v3/nba/projections/{format}/PlayerSeasonProjectionStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_projections_projected_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonProjection1]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonProjection1], NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody]`
- **Error**: `NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeasonProjection1` | `sports_data_io/models/player_season_projection1.py` |
| `NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody` | `sports_data_io/errors/nba_v3_projections_projected_player_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_projections.nba_v3_projections_projected_player_season_stats_by_team

- **Route**: `GET /v3/nba/projections/{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_projections_projected_player_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeasonProjection1]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonProjection1], NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeasonProjection1` | `sports_data_io/models/player_season_projection1.py` |
| `NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody` | `sports_data_io/errors/nba_v3_projections_projected_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_projections.nba_v3_projections_starting_lineups_by_date

- **Route**: `GET /v3/nba/projections/{format}/StartingLineupsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_projections_starting_lineups_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[StartingLineups]`
- **Returns (raw)**: `ApiResult[list[StartingLineups], NbaV3ProjectionsStartingLineupsByDateErrorBody]`
- **Error**: `NbaV3ProjectionsStartingLineupsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `StartingLineups` | `sports_data_io/models/starting_lineups.py` |
| `NbaV3ProjectionsStartingLineupsByDateErrorBody` | `sports_data_io/errors/nba_v3_projections_starting_lineups_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

