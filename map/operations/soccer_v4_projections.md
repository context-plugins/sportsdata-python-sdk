<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoccerV4Projections — operations

Accessor: `client.soccer_v4_projections` · Source: `sports_data/apis/soccer_v4_projections.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.soccer_v4_projections.soccer_v4_projections_dfs_slates_by_date

- **Route**: `GET /v4/soccer/projections/{format}/DfsSlatesByDate/{competition}/{date}`
- **Signature**: `def soccer_v4_projections_dfs_slates_by_date(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[DfsSlate5]`
- **Returns (raw)**: `ApiResult[list[DfsSlate5], SoccerV4ProjectionsDfsSlatesByDateErrorBody]`
- **Error**: `SoccerV4ProjectionsDfsSlatesByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `DfsSlate5` | `sports_data/models/dfs_slate5.py` |
| `SoccerV4ProjectionsDfsSlatesByDateErrorBody` | `sports_data/errors/soccer_v4_projections_dfs_slates_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_projections.soccer_v4_projections_player_details_by_injured

- **Route**: `GET /v4/soccer/projections/{format}/InjuredPlayers/{competition}`
- **Signature**: `def soccer_v4_projections_player_details_by_injured(format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`
- **Params**: `format` — path · `competition` — path
- **Returns (parsed)**: `list[Player7]`
- **Returns (raw)**: `ApiResult[list[Player7], SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody]`
- **Error**: `SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player7` | `sports_data/models/player7.py` |
| `SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody` | `sports_data/errors/soccer_v4_projections_player_details_by_injured_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_projections.soccer_v4_projections_projected_player_game_stats_by_date

- **Route**: `GET /v4/soccer/projections/{format}/PlayerGameProjectionStatsByDate/{competition}/{date}`
- **Signature**: `def soccer_v4_projections_projected_player_game_stats_by_date(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGameProjection4]`
- **Returns (raw)**: `ApiResult[list[PlayerGameProjection4], SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody]`
- **Error**: `SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameProjection4` | `sports_data/models/player_game_projection4.py` |
| `SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody` | `sports_data/errors/soccer_v4_projections_projected_player_game_stats_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_projections.soccer_v4_projections_upcoming_dfs_slates_by_competition

- **Route**: `GET /v4/soccer/projections/{format}/UpcomingDfsSlatesByCompetition/{competition}`
- **Signature**: `def soccer_v4_projections_upcoming_dfs_slates_by_competition(format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`
- **Params**: `format` — path · `competition` — path
- **Returns (parsed)**: `list[DfsSlate5]`
- **Returns (raw)**: `ApiResult[list[DfsSlate5], SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody]`
- **Error**: `SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `DfsSlate5` | `sports_data/models/dfs_slate5.py` |
| `SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody` | `sports_data/errors/soccer_v4_projections_upcoming_dfs_slates_by_competition_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

