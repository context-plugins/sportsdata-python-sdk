<!-- Generated file — do not edit; regenerated with the SDK. -->

# MlbV3Projections — operations

Accessor: `client.mlb_v3_projections` · Source: `sports_data_io/apis/mlb_v3_projections.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mlb_v3_projections.mlb_v3_projections_depth_charts

- **Route**: `GET /v3/mlb/projections/{format}/DepthCharts`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_projections_depth_charts(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamDepthChart1]`
- **Returns (raw)**: `ApiResult[list[TeamDepthChart1], MlbV3ProjectionsDepthChartsErrorBody]`
- **Error**: `MlbV3ProjectionsDepthChartsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamDepthChart1` | `sports_data_io/models/team_depth_chart1.py` |
| `MlbV3ProjectionsDepthChartsErrorBody` | `sports_data_io/errors/mlb_v3_projections_depth_charts_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_projections.mlb_v3_projections_dfs_slate_ownership_projections_by_slate

- **Route**: `GET /v3/mlb/projections/{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_projections_dfs_slate_ownership_projections_by_slate(format: FormatOrStr, slate_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `slate_id`
- **Params**: `format` — path · `slate_id` — path `slateId`
- **Returns (parsed)**: `DfsSlateWithOwnershipProjection`
- **Returns (raw)**: `ApiResult[DfsSlateWithOwnershipProjection, MlbV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody]`
- **Error**: `MlbV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DfsSlateWithOwnershipProjection` | `sports_data_io/models/dfs_slate_with_ownership_projection.py` |
| `MlbV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody` | `sports_data_io/errors/mlb_v3_projections_dfs_slate_ownership_projections_by_slate_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_projections.mlb_v3_projections_dfs_slate_ownership_projections_upcoming

- **Route**: `GET /v3/mlb/projections/{format}/UpcomingDfsSlateOwnershipProjections`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_projections_dfs_slate_ownership_projections_upcoming(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[DfsSlateWithOwnershipProjection]`
- **Returns (raw)**: `ApiResult[list[DfsSlateWithOwnershipProjection], MlbV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody]`
- **Error**: `MlbV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DfsSlateWithOwnershipProjection` | `sports_data_io/models/dfs_slate_with_ownership_projection.py` |
| `MlbV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody` | `sports_data_io/errors/mlb_v3_projections_dfs_slate_ownership_projections_upcoming_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_projections.mlb_v3_projections_dfs_slates_by_date

- **Route**: `GET /v3/mlb/projections/{format}/DfsSlatesByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_projections_dfs_slates_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[DfsSlate]`
- **Returns (raw)**: `ApiResult[list[DfsSlate], MlbV3ProjectionsDfsSlatesByDateErrorBody]`
- **Error**: `MlbV3ProjectionsDfsSlatesByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DfsSlate` | `sports_data_io/models/dfs_slate.py` |
| `MlbV3ProjectionsDfsSlatesByDateErrorBody` | `sports_data_io/errors/mlb_v3_projections_dfs_slates_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_projections.mlb_v3_projections_player_details_by_injured

- **Route**: `GET /v3/mlb/projections/{format}/InjuredPlayers`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_projections_player_details_by_injured(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player2]`
- **Returns (raw)**: `ApiResult[list[Player2], MlbV3ProjectionsPlayerDetailsByInjuredErrorBody]`
- **Error**: `MlbV3ProjectionsPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player2` | `sports_data_io/models/player2.py` |
| `MlbV3ProjectionsPlayerDetailsByInjuredErrorBody` | `sports_data_io/errors/mlb_v3_projections_player_details_by_injured_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_projections.mlb_v3_projections_projected_player_game_stats_by_date

- **Route**: `GET /v3/mlb/projections/{format}/PlayerGameProjectionStatsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_projections_projected_player_game_stats_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGameProjection2]`
- **Returns (raw)**: `ApiResult[list[PlayerGameProjection2], MlbV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]`
- **Error**: `MlbV3ProjectionsProjectedPlayerGameStatsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGameProjection2` | `sports_data_io/models/player_game_projection2.py` |
| `MlbV3ProjectionsProjectedPlayerGameStatsByDateErrorBody` | `sports_data_io/errors/mlb_v3_projections_projected_player_game_stats_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_projections.mlb_v3_projections_projected_player_season_stats_with_adp

- **Route**: `GET /v3/mlb/projections/{format}/PlayerSeasonProjectionStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_projections_projected_player_season_stats_with_adp(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonProjection2]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonProjection2], MlbV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody]`
- **Error**: `MlbV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeasonProjection2` | `sports_data_io/models/player_season_projection2.py` |
| `MlbV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody` | `sports_data_io/errors/mlb_v3_projections_projected_player_season_stats_with_adp_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_projections.mlb_v3_projections_starting_lineups_by_date

- **Route**: `GET /v3/mlb/projections/{format}/StartingLineupsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_projections_starting_lineups_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[StartingLineups1]`
- **Returns (raw)**: `ApiResult[list[StartingLineups1], MlbV3ProjectionsStartingLineupsByDateErrorBody]`
- **Error**: `MlbV3ProjectionsStartingLineupsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `StartingLineups1` | `sports_data_io/models/starting_lineups1.py` |
| `MlbV3ProjectionsStartingLineupsByDateErrorBody` | `sports_data_io/errors/mlb_v3_projections_starting_lineups_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

