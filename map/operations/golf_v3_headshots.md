<!-- Generated file — do not edit; regenerated with the SDK. -->

# GolfV3Headshots — operations

Accessor: `client.golf_v3_headshots` · Source: `sports_data_io/apis/golf_v3_headshots.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.golf_v3_headshots.golf_v3_headshots_headshots

- **Route**: `GET /v3/golf/headshots/{format}/Headshots`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v3_headshots_headshots(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Headshot1]`
- **Returns (raw)**: `ApiResult[list[Headshot1], GolfV3HeadshotsHeadshotsErrorBody]`
- **Error**: `GolfV3HeadshotsHeadshotsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Headshot1` | `sports_data_io/models/headshot1.py` |
| `GolfV3HeadshotsHeadshotsErrorBody` | `sports_data_io/errors/golf_v3_headshots_headshots_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

