<!-- Generated file — do not edit; regenerated with the SDK. -->

# MmaV3Scores — operations

Accessor: `client.mma_v3_scores` · Source: `sports_data/apis/mma_v3_scores.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mma_v3_scores.mma_v3_scores_event

- **Route**: `GET /v3/mma/scores/{format}/Event/{eventid}`
- **Signature**: `def mma_v3_scores_event(format: FormatOrStr, eventid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `eventid`
- **Params**: `format` — path · `eventid` — path
- **Returns (parsed)**: `EventDetail`
- **Returns (raw)**: `ApiResult[EventDetail, MmaV3ScoresEventErrorBody]`
- **Error**: `MmaV3ScoresEventErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `EventDetail` | `sports_data/models/event_detail.py` |
| `MmaV3ScoresEventErrorBody` | `sports_data/errors/mma_v3_scores_event_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_scores.mma_v3_scores_fighter_profile_by_fighter

- **Route**: `GET /v3/mma/scores/{format}/Fighter/{fighterid}`
- **Signature**: `def mma_v3_scores_fighter_profile_by_fighter(format: FormatOrStr, fighterid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `fighterid`
- **Params**: `format` — path · `fighterid` — path
- **Returns (parsed)**: `Fighter`
- **Returns (raw)**: `ApiResult[Fighter, MmaV3ScoresFighterProfileByFighterErrorBody]`
- **Error**: `MmaV3ScoresFighterProfileByFighterErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Fighter` | `sports_data/models/fighter.py` |
| `MmaV3ScoresFighterProfileByFighterErrorBody` | `sports_data/errors/mma_v3_scores_fighter_profile_by_fighter_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_scores.mma_v3_scores_fighter_profiles_all

- **Route**: `GET /v3/mma/scores/{format}/Fighters`
- **Signature**: `def mma_v3_scores_fighter_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Fighter]`
- **Returns (raw)**: `ApiResult[list[Fighter], MmaV3ScoresFighterProfilesAllErrorBody]`
- **Error**: `MmaV3ScoresFighterProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Fighter` | `sports_data/models/fighter.py` |
| `MmaV3ScoresFighterProfilesAllErrorBody` | `sports_data/errors/mma_v3_scores_fighter_profiles_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_scores.mma_v3_scores_fighter_profiles_basic_all

- **Route**: `GET /v3/mma/scores/{format}/FightersBasic`
- **Signature**: `def mma_v3_scores_fighter_profiles_basic_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[FighterBasic]`
- **Returns (raw)**: `ApiResult[list[FighterBasic], MmaV3ScoresFighterProfilesBasicAllErrorBody]`
- **Error**: `MmaV3ScoresFighterProfilesBasicAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FighterBasic` | `sports_data/models/fighter_basic.py` |
| `MmaV3ScoresFighterProfilesBasicAllErrorBody` | `sports_data/errors/mma_v3_scores_fighter_profiles_basic_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_scores.mma_v3_scores_leagues

- **Route**: `GET /v3/mma/scores/{format}/Leagues`
- **Signature**: `def mma_v3_scores_leagues(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[League]`
- **Returns (raw)**: `ApiResult[list[League], MmaV3ScoresLeaguesErrorBody]`
- **Error**: `MmaV3ScoresLeaguesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `League` | `sports_data/models/league.py` |
| `MmaV3ScoresLeaguesErrorBody` | `sports_data/errors/mma_v3_scores_leagues_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mma_v3_scores.mma_v3_scores_schedules

- **Route**: `GET /v3/mma/scores/{format}/Schedule/{league}/{season}`
- **Signature**: `def mma_v3_scores_schedules(format: FormatOrStr, league: str, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `league`, `season`
- **Params**: `format` — path · `league` — path · `season` — path
- **Returns (parsed)**: `list[Event]`
- **Returns (raw)**: `ApiResult[list[Event], MmaV3ScoresSchedulesErrorBody]`
- **Error**: `MmaV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Event` | `sports_data/models/event.py` |
| `MmaV3ScoresSchedulesErrorBody` | `sports_data/errors/mma_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

