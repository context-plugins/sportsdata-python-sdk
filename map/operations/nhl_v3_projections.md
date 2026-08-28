<!-- Generated file — do not edit; regenerated with the SDK. -->

# NhlV3Projections — operations

Accessor: `client.nhl_v3_projections` · Source: `sports_data/apis/nhl_v3_projections.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nhl_v3_projections.nhl_v3_projections_dfs_slates_by_date

- **Route**: `GET /v3/nhl/projections/{format}/DfsSlatesByDate/{date}`
- **Signature**: `def nhl_v3_projections_dfs_slates_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[DfsSlate4]`
- **Returns (raw)**: `ApiResult[list[DfsSlate4], NhlV3ProjectionsDfsSlatesByDateErrorBody]`
- **Error**: `NhlV3ProjectionsDfsSlatesByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `DfsSlate4` | `sports_data/models/dfs_slate4.py` |
| `NhlV3ProjectionsDfsSlatesByDateErrorBody` | `sports_data/errors/nhl_v3_projections_dfs_slates_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_projections.nhl_v3_projections_player_details_by_injured

- **Route**: `GET /v3/nhl/projections/{format}/InjuredPlayers`
- **Signature**: `def nhl_v3_projections_player_details_by_injured(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player6]`
- **Returns (raw)**: `ApiResult[list[Player6], NhlV3ProjectionsPlayerDetailsByInjuredErrorBody]`
- **Error**: `NhlV3ProjectionsPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player6` | `sports_data/models/player6.py` |
| `NhlV3ProjectionsPlayerDetailsByInjuredErrorBody` | `sports_data/errors/nhl_v3_projections_player_details_by_injured_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_projections.nhl_v3_projections_projected_player_game_stats_by_date

- **Route**: `GET /v3/nhl/projections/{format}/PlayerGameProjectionStatsByDate/{date}`
- **Signature**: `def nhl_v3_projections_projected_player_game_stats_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGameProjection3]`
- **Returns (raw)**: `ApiResult[list[PlayerGameProjection3], NhlV3ProjectionsProjectedPlayerGameStatsByDateErrorBody]`
- **Error**: `NhlV3ProjectionsProjectedPlayerGameStatsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameProjection3` | `sports_data/models/player_game_projection3.py` |
| `NhlV3ProjectionsProjectedPlayerGameStatsByDateErrorBody` | `sports_data/errors/nhl_v3_projections_projected_player_game_stats_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_projections.nhl_v3_projections_starting_goaltenders_by_date

- **Route**: `GET /v3/nhl/projections/{format}/StartingGoaltendersByDate/{date}`
- **Signature**: `def nhl_v3_projections_starting_goaltenders_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[StartingGoaltenders]`
- **Returns (raw)**: `ApiResult[list[StartingGoaltenders], NhlV3ProjectionsStartingGoaltendersByDateErrorBody]`
- **Error**: `NhlV3ProjectionsStartingGoaltendersByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `StartingGoaltenders` | `sports_data/models/starting_goaltenders.py` |
| `NhlV3ProjectionsStartingGoaltendersByDateErrorBody` | `sports_data/errors/nhl_v3_projections_starting_goaltenders_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

