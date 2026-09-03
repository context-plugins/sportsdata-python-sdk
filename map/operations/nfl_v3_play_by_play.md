<!-- Generated file — do not edit; regenerated with the SDK. -->

# NflV3PlayByPlay — operations

Accessor: `client.nfl_v3_play_by_play` · Source: `sports_data_io/apis/nfl_v3_play_by_play.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nfl_v3_play_by_play.nfl_v3_pbp_play_by_play_by_team_final

- **Route**: `GET /v3/nfl/pbp/{format}/PlayByPlayFinal/{season}/{week}/{hometeam}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_pbp_play_by_play_by_team_final(format: FormatOrStr, season: str, week: str, hometeam: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `hometeam`
- **Params**: `format` — path · `season` — path · `week` — path · `hometeam` — path
- **Returns (parsed)**: `PlayByPlay`
- **Returns (raw)**: `ApiResult[PlayByPlay, NflV3PbpPlayByPlayByTeamFinalErrorBody]`
- **Error**: `NflV3PbpPlayByPlayByTeamFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayByPlay` | `sports_data_io/models/play_by_play.py` |
| `NflV3PbpPlayByPlayByTeamFinalErrorBody` | `sports_data_io/errors/nfl_v3_pbp_play_by_play_by_team_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_play_by_play.nfl_v3_pbp_play_by_play_by_team_live_final

- **Route**: `GET /v3/nfl/pbp/{format}/PlayByPlay/{season}/{week}/{hometeam}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_pbp_play_by_play_by_team_live_final(format: FormatOrStr, season: str, week: str, hometeam: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `hometeam`
- **Params**: `format` — path · `season` — path · `week` — path · `hometeam` — path
- **Returns (parsed)**: `PlayByPlay`
- **Returns (raw)**: `ApiResult[PlayByPlay, NflV3PbpPlayByPlayByTeamLiveFinalErrorBody]`
- **Error**: `NflV3PbpPlayByPlayByTeamLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayByPlay` | `sports_data_io/models/play_by_play.py` |
| `NflV3PbpPlayByPlayByTeamLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_pbp_play_by_play_by_team_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_play_by_play.nfl_v3_pbp_play_by_play_final

- **Route**: `GET /v3/nfl/pbp/{format}/PlayByPlayFinal/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_pbp_play_by_play_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `PlayByPlay`
- **Returns (raw)**: `ApiResult[PlayByPlay, NflV3PbpPlayByPlayFinalErrorBody]`
- **Error**: `NflV3PbpPlayByPlayFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayByPlay` | `sports_data_io/models/play_by_play.py` |
| `NflV3PbpPlayByPlayFinalErrorBody` | `sports_data_io/errors/nfl_v3_pbp_play_by_play_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_play_by_play.nfl_v3_pbp_play_by_play_live_final

- **Route**: `GET /v3/nfl/pbp/{format}/PlayByPlay/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_pbp_play_by_play_live_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `PlayByPlay`
- **Returns (raw)**: `ApiResult[PlayByPlay, NflV3PbpPlayByPlayLiveFinalErrorBody]`
- **Error**: `NflV3PbpPlayByPlayLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayByPlay` | `sports_data_io/models/play_by_play.py` |
| `NflV3PbpPlayByPlayLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_pbp_play_by_play_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_play_by_play.nfl_v3_pbp_play_by_play_delta

- **Route**: `GET /v3/nfl/pbp/{format}/PlayByPlayDelta/{season}/{week}/{minutes}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_pbp_play_by_play_delta(format: FormatOrStr, season: str, week: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `minutes`
- **Params**: `format` — path · `season` — path · `week` — path · `minutes` — path
- **Returns (parsed)**: `list[PlayByPlay]`
- **Returns (raw)**: `ApiResult[list[PlayByPlay], NflV3PbpPlayByPlayDeltaErrorBody]`
- **Error**: `NflV3PbpPlayByPlayDeltaErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayByPlay` | `sports_data_io/models/play_by_play.py` |
| `NflV3PbpPlayByPlayDeltaErrorBody` | `sports_data_io/errors/nfl_v3_pbp_play_by_play_delta_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_play_by_play.nfl_v3_pbp_play_by_play_simulation

- **Route**: `GET /v3/nfl/pbp/{format}/SimulatedPlayByPlay/{numberofplays}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_pbp_play_by_play_simulation(format: FormatOrStr, numberofplays: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `numberofplays`
- **Params**: `format` — path · `numberofplays` — path
- **Returns (parsed)**: `list[PlayByPlay]`
- **Returns (raw)**: `ApiResult[list[PlayByPlay], NflV3PbpPlayByPlaySimulationErrorBody]`
- **Error**: `NflV3PbpPlayByPlaySimulationErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayByPlay` | `sports_data_io/models/play_by_play.py` |
| `NflV3PbpPlayByPlaySimulationErrorBody` | `sports_data_io/errors/nfl_v3_pbp_play_by_play_simulation_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

