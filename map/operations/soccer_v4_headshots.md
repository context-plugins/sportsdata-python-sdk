<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoccerV4Headshots — operations

Accessor: `client.soccer_v4_headshots` · Source: `sports_data/apis/soccer_v4_headshots.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.soccer_v4_headshots.soccer_v4_headshots_headshots

- **Route**: `GET /v4/soccer/headshots/{format}/Headshots`
- **Signature**: `def soccer_v4_headshots_headshots(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Headshot1]`
- **Returns (raw)**: `ApiResult[list[Headshot1], SoccerV4HeadshotsHeadshotsErrorBody]`
- **Error**: `SoccerV4HeadshotsHeadshotsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Headshot1` | `sports_data/models/headshot1.py` |
| `SoccerV4HeadshotsHeadshotsErrorBody` | `sports_data/errors/soccer_v4_headshots_headshots_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

