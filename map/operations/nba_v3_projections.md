<!-- Generated file — do not edit; regenerated with the SDK. -->

# NbaV3Projections — operations

Accessor: `client.nba_v3_projections` · Source: `sports_data/apis/nba_v3_projections.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nba_v3_projections.nba_v3_projections_dfs_slates_by_date

- **Route**: `GET /v3/nba/projections/{format}/DfsSlatesByDate/{date}`
- **Signature**: `def nba_v3_projections_dfs_slates_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[DfsSlate2]`
- **Returns (raw)**: `ApiResult[list[DfsSlate2], NbaV3ProjectionsDfsSlatesByDateErrorBody]`
- **Error**: `NbaV3ProjectionsDfsSlatesByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `DfsSlate2` | `sports_data/models/dfs_slate2.py` |
| `NbaV3ProjectionsDfsSlatesByDateErrorBody` | `sports_data/errors/nba_v3_projections_dfs_slates_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_projections.nba_v3_projections_player_details_by_injured

- **Route**: `GET /v3/nba/projections/{format}/InjuredPlayers`
- **Signature**: `def nba_v3_projections_player_details_by_injured(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player4]`
- **Returns (raw)**: `ApiResult[list[Player4], NbaV3ProjectionsPlayerDetailsByInjuredErrorBody]`
- **Error**: `NbaV3ProjectionsPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player4` | `sports_data/models/player4.py` |
| `NbaV3ProjectionsPlayerDetailsByInjuredErrorBody` | `sports_data/errors/nba_v3_projections_player_details_by_injured_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_projections.nba_v3_projections_projected_player_game_stats_by_date

- **Route**: `GET /v3/nba/projections/{format}/PlayerGameProjectionStatsByDate/{date}`
- **Signature**: `def nba_v3_projections_projected_player_game_stats_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGameProjection1]`
- **Returns (raw)**: `ApiResult[list[PlayerGameProjection1], NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]`
- **Error**: `NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameProjection1` | `sports_data/models/player_game_projection1.py` |
| `NbaV3ProjectionsProjectedPlayerGameStatsByDateErrorBody` | `sports_data/errors/nba_v3_projections_projected_player_game_stats_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_projections.nba_v3_projections_projected_player_season_stats

- **Route**: `GET /v3/nba/projections/{format}/PlayerSeasonProjectionStats/{season}`
- **Signature**: `def nba_v3_projections_projected_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonProjection1]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonProjection1], NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody]`
- **Error**: `NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeasonProjection1` | `sports_data/models/player_season_projection1.py` |
| `NbaV3ProjectionsProjectedPlayerSeasonStatsErrorBody` | `sports_data/errors/nba_v3_projections_projected_player_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_projections.nba_v3_projections_projected_player_season_stats_by_team

- **Route**: `GET /v3/nba/projections/{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team}`
- **Signature**: `def nba_v3_projections_projected_player_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeasonProjection1]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonProjection1], NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeasonProjection1` | `sports_data/models/player_season_projection1.py` |
| `NbaV3ProjectionsProjectedPlayerSeasonStatsByTeamErrorBody` | `sports_data/errors/nba_v3_projections_projected_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_projections.nba_v3_projections_starting_lineups_by_date

- **Route**: `GET /v3/nba/projections/{format}/StartingLineupsByDate/{date}`
- **Signature**: `def nba_v3_projections_starting_lineups_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[StartingLineups1]`
- **Returns (raw)**: `ApiResult[list[StartingLineups1], NbaV3ProjectionsStartingLineupsByDateErrorBody]`
- **Error**: `NbaV3ProjectionsStartingLineupsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `StartingLineups1` | `sports_data/models/starting_lineups1.py` |
| `NbaV3ProjectionsStartingLineupsByDateErrorBody` | `sports_data/errors/nba_v3_projections_starting_lineups_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

