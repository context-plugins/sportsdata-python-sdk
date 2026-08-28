<!-- Generated file — do not edit; regenerated with the SDK. -->

# MlbV3PlayByPlay — operations

Accessor: `client.mlb_v3_play_by_play` · Source: `sports_data/apis/mlb_v3_play_by_play.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mlb_v3_play_by_play.mlb_v3_pbp_play_by_play_final

- **Route**: `GET /v3/mlb/pbp/{format}/PlayByPlayFinal/{gameid}`
- **Signature**: `def mlb_v3_pbp_play_by_play_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `PlayByPlay`
- **Returns (raw)**: `ApiResult[PlayByPlay, MlbV3PbpPlayByPlayFinalErrorBody]`
- **Error**: `MlbV3PbpPlayByPlayFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayByPlay` | `sports_data/models/play_by_play.py` |
| `MlbV3PbpPlayByPlayFinalErrorBody` | `sports_data/errors/mlb_v3_pbp_play_by_play_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_play_by_play.mlb_v3_pbp_play_by_play_live_final

- **Route**: `GET /v3/mlb/pbp/{format}/PlayByPlay/{gameid}`
- **Signature**: `def mlb_v3_pbp_play_by_play_live_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `PlayByPlay`
- **Returns (raw)**: `ApiResult[PlayByPlay, MlbV3PbpPlayByPlayLiveFinalErrorBody]`
- **Error**: `MlbV3PbpPlayByPlayLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayByPlay` | `sports_data/models/play_by_play.py` |
| `MlbV3PbpPlayByPlayLiveFinalErrorBody` | `sports_data/errors/mlb_v3_pbp_play_by_play_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_play_by_play.mlb_v3_pbp_play_by_play_delta

- **Route**: `GET /v3/mlb/pbp/{format}/PlayByPlayDelta/{date}/{minutes}`
- **Signature**: `def mlb_v3_pbp_play_by_play_delta(format: FormatOrStr, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `minutes`
- **Params**: `format` — path · `date` — path · `minutes` — path
- **Returns (parsed)**: `list[PlayByPlay]`
- **Returns (raw)**: `ApiResult[list[PlayByPlay], MlbV3PbpPlayByPlayDeltaErrorBody]`
- **Error**: `MlbV3PbpPlayByPlayDeltaErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayByPlay` | `sports_data/models/play_by_play.py` |
| `MlbV3PbpPlayByPlayDeltaErrorBody` | `sports_data/errors/mlb_v3_pbp_play_by_play_delta_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

