<!-- Generated file — do not edit; regenerated with the SDK. -->

# MmaV3Stats — operations

Accessor: `client.mma_v3_stats` · Source: `sports_data_io/apis/mma_v3_stats.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mma_v3_stats.mma_v3_stats_fight_basic_final

- **Route**: `GET /v3/mma/stats/{format}/FightBasicFinal/{fightid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mma_v3_stats_fight_basic_final(format: FormatOrStr, fightid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `fightid`
- **Params**: `format` — path · `fightid` — path
- **Returns (parsed)**: `FightBasic`
- **Returns (raw)**: `ApiResult[FightBasic, MmaV3StatsFightBasicFinalErrorBody]`
- **Error**: `MmaV3StatsFightBasicFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FightBasic` | `sports_data_io/models/fight_basic.py` |
| `MmaV3StatsFightBasicFinalErrorBody` | `sports_data_io/errors/mma_v3_stats_fight_basic_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mma_v3_stats.mma_v3_stats_fight_basic_live_final

- **Route**: `GET /v3/mma/stats/{format}/FightBasic/{fightid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mma_v3_stats_fight_basic_live_final(format: FormatOrStr, fightid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `fightid`
- **Params**: `format` — path · `fightid` — path
- **Returns (parsed)**: `FightBasic`
- **Returns (raw)**: `ApiResult[FightBasic, MmaV3StatsFightBasicLiveFinalErrorBody]`
- **Error**: `MmaV3StatsFightBasicLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FightBasic` | `sports_data_io/models/fight_basic.py` |
| `MmaV3StatsFightBasicLiveFinalErrorBody` | `sports_data_io/errors/mma_v3_stats_fight_basic_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mma_v3_stats.mma_v3_stats_fight_final

- **Route**: `GET /v3/mma/stats/{format}/FightFinal/{fightid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mma_v3_stats_fight_final(format: FormatOrStr, fightid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `fightid`
- **Params**: `format` — path · `fightid` — path
- **Returns (parsed)**: `FightDetail`
- **Returns (raw)**: `ApiResult[FightDetail, MmaV3StatsFightFinalErrorBody]`
- **Error**: `MmaV3StatsFightFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FightDetail` | `sports_data_io/models/fight_detail.py` |
| `MmaV3StatsFightFinalErrorBody` | `sports_data_io/errors/mma_v3_stats_fight_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mma_v3_stats.mma_v3_stats_fight_live_final

- **Route**: `GET /v3/mma/stats/{format}/Fight/{fightid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mma_v3_stats_fight_live_final(format: FormatOrStr, fightid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `fightid`
- **Params**: `format` — path · `fightid` — path
- **Returns (parsed)**: `FightDetail`
- **Returns (raw)**: `ApiResult[FightDetail, MmaV3StatsFightLiveFinalErrorBody]`
- **Error**: `MmaV3StatsFightLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FightDetail` | `sports_data_io/models/fight_detail.py` |
| `MmaV3StatsFightLiveFinalErrorBody` | `sports_data_io/errors/mma_v3_stats_fight_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

