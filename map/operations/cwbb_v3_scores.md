<!-- Generated file — do not edit; regenerated with the SDK. -->

# CwbbV3Scores — operations

Accessor: `client.cwbb_v3_scores` · Source: `sports_data_io/apis/cwbb_v3_scores.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cwbb_v3_scores.cwbb_v3_scores_are_any_games_in_progress

- **Route**: `GET /v3/cwbb/scores/{format}/AreAnyGamesInProgress`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cwbb_v3_scores_are_any_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, CwbbV3ScoresAreAnyGamesInProgressErrorBody]`
- **Error**: `CwbbV3ScoresAreAnyGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `CwbbV3ScoresAreAnyGamesInProgressErrorBody` | `sports_data_io/errors/cwbb_v3_scores_are_any_games_in_progress_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_games_by_date_final

- **Route**: `GET /v3/cwbb/scores/{format}/GamesByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cwbb_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game16]`
- **Returns (raw)**: `ApiResult[list[Game16], CwbbV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `CwbbV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game16` | `sports_data_io/models/game16.py` |
| `CwbbV3ScoresGamesByDateFinalErrorBody` | `sports_data_io/errors/cwbb_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/cwbb/scores/{format}/GamesByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cwbb_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game16]`
- **Returns (raw)**: `ApiResult[list[Game16], CwbbV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `CwbbV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game16` | `sports_data_io/models/game16.py` |
| `CwbbV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data_io/errors/cwbb_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_league_hierarchy

- **Route**: `GET /v3/cwbb/scores/{format}/LeagueHierarchy`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cwbb_v3_scores_league_hierarchy(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Conference2]`
- **Returns (raw)**: `ApiResult[list[Conference2], CwbbV3ScoresLeagueHierarchyErrorBody]`
- **Error**: `CwbbV3ScoresLeagueHierarchyErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Conference2` | `sports_data_io/models/conference2.py` |
| `CwbbV3ScoresLeagueHierarchyErrorBody` | `sports_data_io/errors/cwbb_v3_scores_league_hierarchy_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_schedules

- **Route**: `GET /v3/cwbb/scores/{format}/Games/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cwbb_v3_scores_schedules(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Game16]`
- **Returns (raw)**: `ApiResult[list[Game16], CwbbV3ScoresSchedulesErrorBody]`
- **Error**: `CwbbV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game16` | `sports_data_io/models/game16.py` |
| `CwbbV3ScoresSchedulesErrorBody` | `sports_data_io/errors/cwbb_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_schedules_basic

- **Route**: `GET /v3/cwbb/scores/{format}/SchedulesBasic/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cwbb_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic6]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic6], CwbbV3ScoresSchedulesBasicErrorBody]`
- **Error**: `CwbbV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScheduleBasic6` | `sports_data_io/models/schedule_basic6.py` |
| `CwbbV3ScoresSchedulesBasicErrorBody` | `sports_data_io/errors/cwbb_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_season_current

- **Route**: `GET /v3/cwbb/scores/{format}/CurrentSeason`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cwbb_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `Season5`
- **Returns (raw)**: `ApiResult[Season5, CwbbV3ScoresSeasonCurrentErrorBody]`
- **Error**: `CwbbV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Season5` | `sports_data_io/models/season5.py` |
| `CwbbV3ScoresSeasonCurrentErrorBody` | `sports_data_io/errors/cwbb_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_team_profiles_all

- **Route**: `GET /v3/cwbb/scores/{format}/Teams`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cwbb_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team7]`
- **Returns (raw)**: `ApiResult[list[Team7], CwbbV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `CwbbV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team7` | `sports_data_io/models/team7.py` |
| `CwbbV3ScoresTeamProfilesAllErrorBody` | `sports_data_io/errors/cwbb_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

