<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoccerV4Projections — operations

Accessor: `client.soccer_v4_projections` · Source: `sports_data_io/apis/soccer_v4_projections.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.soccer_v4_projections.soccer_v4_projections_dfs_slates_by_date

- **Route**: `GET /v4/soccer/projections/{format}/DfsSlatesByDate/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_projections_dfs_slates_by_date(competition: str, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `date`
- **Params**: `format_` — path `format` · `competition` — path · `date` — path
- **Returns (parsed)**: `list[DfsSlate1]`
- **Returns (raw)**: `ApiResult[list[DfsSlate1], SoccerV4ProjectionsDfsSlatesByDateErrorBody]`
- **Error**: `SoccerV4ProjectionsDfsSlatesByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DfsSlate1` | `sports_data_io/models/dfs_slate1.py` |
| `SoccerV4ProjectionsDfsSlatesByDateErrorBody` | `sports_data_io/errors/soccer_v4_projections_dfs_slates_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_projections.soccer_v4_projections_player_details_by_injured

- **Route**: `GET /v4/soccer/projections/{format}/InjuredPlayers/{competition}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_projections_player_details_by_injured(competition: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`
- **Params**: `format_` — path `format` · `competition` — path
- **Returns (parsed)**: `list[Player7]`
- **Returns (raw)**: `ApiResult[list[Player7], SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody]`
- **Error**: `SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player7` | `sports_data_io/models/player7.py` |
| `SoccerV4ProjectionsPlayerDetailsByInjuredErrorBody` | `sports_data_io/errors/soccer_v4_projections_player_details_by_injured_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_projections.soccer_v4_projections_projected_player_game_stats_by_date

- **Route**: `GET /v4/soccer/projections/{format}/PlayerGameProjectionStatsByDate/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_projections_projected_player_game_stats_by_date(competition: str, date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`, `date`
- **Params**: `format_` — path `format` · `competition` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGameProjection4]`
- **Returns (raw)**: `ApiResult[list[PlayerGameProjection4], SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody]`
- **Error**: `SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGameProjection4` | `sports_data_io/models/player_game_projection4.py` |
| `SoccerV4ProjectionsProjectedPlayerGameStatsByDateErrorBody` | `sports_data_io/errors/soccer_v4_projections_projected_player_game_stats_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_projections.soccer_v4_projections_upcoming_dfs_slates_by_competition

- **Route**: `GET /v4/soccer/projections/{format}/UpcomingDfsSlatesByCompetition/{competition}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_projections_upcoming_dfs_slates_by_competition(competition: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `competition`
- **Params**: `format_` — path `format` · `competition` — path
- **Returns (parsed)**: `list[DfsSlate1]`
- **Returns (raw)**: `ApiResult[list[DfsSlate1], SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody]`
- **Error**: `SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DfsSlate1` | `sports_data_io/models/dfs_slate1.py` |
| `SoccerV4ProjectionsUpcomingDfsSlatesByCompetitionErrorBody` | `sports_data_io/errors/soccer_v4_projections_upcoming_dfs_slates_by_competition_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

