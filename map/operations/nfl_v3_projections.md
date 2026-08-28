<!-- Generated file — do not edit; regenerated with the SDK. -->

# NflV3Projections — operations

Accessor: `client.nfl_v3_projections` · Source: `sports_data/apis/nfl_v3_projections.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nfl_v3_projections.nfl_v3_projections_dfs_slate_ownership_projections_by_slate

- **Route**: `GET /v3/nfl/projections/{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId}`
- **Signature**: `def nfl_v3_projections_dfs_slate_ownership_projections_by_slate(format: FormatOrStr, slate_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `slate_id`
- **Params**: `format` — path · `slate_id` — path `slateId`
- **Returns (parsed)**: `DfsSlateWithOwnershipProjection`
- **Returns (raw)**: `ApiResult[DfsSlateWithOwnershipProjection, NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody]`
- **Error**: `NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `DfsSlateWithOwnershipProjection` | `sports_data/models/dfs_slate_with_ownership_projection.py` |
| `NflV3ProjectionsDfsSlateOwnershipProjectionsBySlateErrorBody` | `sports_data/errors/nfl_v3_projections_dfs_slate_ownership_projections_by_slate_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_dfs_slate_ownership_projections_upcoming

- **Route**: `GET /v3/nfl/projections/{format}/UpcomingDfsSlateOwnershipProjections`
- **Signature**: `def nfl_v3_projections_dfs_slate_ownership_projections_upcoming(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[DfsSlateWithOwnershipProjection]`
- **Returns (raw)**: `ApiResult[list[DfsSlateWithOwnershipProjection], NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody]`
- **Error**: `NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `DfsSlateWithOwnershipProjection` | `sports_data/models/dfs_slate_with_ownership_projection.py` |
| `NflV3ProjectionsDfsSlateOwnershipProjectionsUpcomingErrorBody` | `sports_data/errors/nfl_v3_projections_dfs_slate_ownership_projections_upcoming_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_dfs_slates_by_date

- **Route**: `GET /v3/nfl/projections/{format}/DfsSlatesByDate/{date}`
- **Signature**: `def nfl_v3_projections_dfs_slates_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[DfsSlate3]`
- **Returns (raw)**: `ApiResult[list[DfsSlate3], NflV3ProjectionsDfsSlatesByDateErrorBody]`
- **Error**: `NflV3ProjectionsDfsSlatesByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `DfsSlate3` | `sports_data/models/dfs_slate3.py` |
| `NflV3ProjectionsDfsSlatesByDateErrorBody` | `sports_data/errors/nfl_v3_projections_dfs_slates_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_dfs_slates_by_week

- **Route**: `GET /v3/nfl/projections/{format}/DfsSlatesByWeek/{season}/{week}`
- **Signature**: `def nfl_v3_projections_dfs_slates_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[DfsSlate3]`
- **Returns (raw)**: `ApiResult[list[DfsSlate3], NflV3ProjectionsDfsSlatesByWeekErrorBody]`
- **Error**: `NflV3ProjectionsDfsSlatesByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `DfsSlate3` | `sports_data/models/dfs_slate3.py` |
| `NflV3ProjectionsDfsSlatesByWeekErrorBody` | `sports_data/errors/nfl_v3_projections_dfs_slates_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_idp_projected_player_game_stats_by_team

- **Route**: `GET /v3/nfl/projections/{format}/IdpPlayerGameProjectionStatsByTeam/{season}/{week}/{team}`
- **Signature**: `def nfl_v3_projections_idp_projected_player_game_stats_by_team(format: FormatOrStr, season: str, week: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `team`
- **Params**: `format` — path · `season` — path · `week` — path · `team` — path
- **Returns (parsed)**: `list[PlayerGameProjection2]`
- **Returns (raw)**: `ApiResult[list[PlayerGameProjection2], NflV3ProjectionsIdpProjectedPlayerGameStatsByTeamErrorBody]`
- **Error**: `NflV3ProjectionsIdpProjectedPlayerGameStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameProjection2` | `sports_data/models/player_game_projection2.py` |
| `NflV3ProjectionsIdpProjectedPlayerGameStatsByTeamErrorBody` | `sports_data/errors/nfl_v3_projections_idp_projected_player_game_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_idp_projected_player_game_stats_by_week

- **Route**: `GET /v3/nfl/projections/{format}/IdpPlayerGameProjectionStatsByWeek/{season}/{week}`
- **Signature**: `def nfl_v3_projections_idp_projected_player_game_stats_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGameProjection2]`
- **Returns (raw)**: `ApiResult[list[PlayerGameProjection2], NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekErrorBody]`
- **Error**: `NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameProjection2` | `sports_data/models/player_game_projection2.py` |
| `NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekErrorBody` | `sports_data/errors/nfl_v3_projections_idp_projected_player_game_stats_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_player_details_by_injured

- **Route**: `GET /v3/nfl/projections/{format}/InjuredPlayers`
- **Signature**: `def nfl_v3_projections_player_details_by_injured(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player5]`
- **Returns (raw)**: `ApiResult[list[Player5], NflV3ProjectionsPlayerDetailsByInjuredErrorBody]`
- **Error**: `NflV3ProjectionsPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player5` | `sports_data/models/player5.py` |
| `NflV3ProjectionsPlayerDetailsByInjuredErrorBody` | `sports_data/errors/nfl_v3_projections_player_details_by_injured_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries

- **Route**: `GET /v3/nfl/projections/{format}/FantasyDefenseProjectionsByGame/{season}/{week}`
- **Signature**: `def nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[FantasyDefenseGameProjection]`
- **Returns (raw)**: `ApiResult[list[FantasyDefenseGameProjection], NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody]`
- **Error**: `NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyDefenseGameProjection` | `sports_data/models/fantasy_defense_game_projection.py` |
| `NflV3ProjectionsProjectedFantasyDefenseGameStatsWithDfsSalariesErrorBody` | `sports_data/errors/nfl_v3_projections_projected_fantasy_defense_game_stats_with_dfs_salaries_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp

- **Route**: `GET /v3/nfl/projections/{format}/FantasyDefenseProjectionsBySeason/{season}`
- **Signature**: `def nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[FantasyDefenseSeasonProjection]`
- **Returns (raw)**: `ApiResult[list[FantasyDefenseSeasonProjection], NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpErrorBody]`
- **Error**: `NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyDefenseSeasonProjection` | `sports_data/models/fantasy_defense_season_projection.py` |
| `NflV3ProjectionsProjectedFantasyDefenseSeasonStatsWithAdpErrorBody` | `sports_data/errors/nfl_v3_projections_projected_fantasy_defense_season_stats_with_adp_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_projected_player_game_stats_by_team

- **Route**: `GET /v3/nfl/projections/{format}/PlayerGameProjectionStatsByTeam/{season}/{week}/{team}`
- **Signature**: `def nfl_v3_projections_projected_player_game_stats_by_team(format: FormatOrStr, season: str, week: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `team`
- **Params**: `format` — path · `season` — path · `week` — path · `team` — path
- **Returns (parsed)**: `list[PlayerGameProjection2]`
- **Returns (raw)**: `ApiResult[list[PlayerGameProjection2], NflV3ProjectionsProjectedPlayerGameStatsByTeamErrorBody]`
- **Error**: `NflV3ProjectionsProjectedPlayerGameStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameProjection2` | `sports_data/models/player_game_projection2.py` |
| `NflV3ProjectionsProjectedPlayerGameStatsByTeamErrorBody` | `sports_data/errors/nfl_v3_projections_projected_player_game_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_projected_player_game_stats_by_week

- **Route**: `GET /v3/nfl/projections/{format}/PlayerGameProjectionStatsByWeek/{season}/{week}`
- **Signature**: `def nfl_v3_projections_projected_player_game_stats_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGameProjection2]`
- **Returns (raw)**: `ApiResult[list[PlayerGameProjection2], NflV3ProjectionsProjectedPlayerGameStatsByWeekErrorBody]`
- **Error**: `NflV3ProjectionsProjectedPlayerGameStatsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameProjection2` | `sports_data/models/player_game_projection2.py` |
| `NflV3ProjectionsProjectedPlayerGameStatsByWeekErrorBody` | `sports_data/errors/nfl_v3_projections_projected_player_game_stats_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_projected_player_season_stats_with_adp

- **Route**: `GET /v3/nfl/projections/{format}/PlayerSeasonProjectionStats/{season}`
- **Signature**: `def nfl_v3_projections_projected_player_season_stats_with_adp(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonProjection2]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonProjection2], NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody]`
- **Error**: `NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeasonProjection2` | `sports_data/models/player_season_projection2.py` |
| `NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpErrorBody` | `sports_data/errors/nfl_v3_projections_projected_player_season_stats_with_adp_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_projections.nfl_v3_projections_projected_player_season_stats_with_adp_by_team

- **Route**: `GET /v3/nfl/projections/{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team}`
- **Signature**: `def nfl_v3_projections_projected_player_season_stats_with_adp_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeasonProjection2]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonProjection2], NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamErrorBody]`
- **Error**: `NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeasonProjection2` | `sports_data/models/player_season_projection2.py` |
| `NflV3ProjectionsProjectedPlayerSeasonStatsWithAdpByTeamErrorBody` | `sports_data/errors/nfl_v3_projections_projected_player_season_stats_with_adp_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

