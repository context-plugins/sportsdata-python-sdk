<!-- Generated file — do not edit; regenerated with the SDK. -->

# CwbbV3Scores — operations

Accessor: `client.cwbb_v3_scores` · Source: `sports_data/apis/cwbb_v3_scores.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cwbb_v3_scores.cwbb_v3_scores_are_any_games_in_progress

- **Route**: `GET /v3/cwbb/scores/{format}/AreAnyGamesInProgress`
- **Signature**: `def cwbb_v3_scores_are_any_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, CwbbV3ScoresAreAnyGamesInProgressErrorBody]`
- **Error**: `CwbbV3ScoresAreAnyGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `CwbbV3ScoresAreAnyGamesInProgressErrorBody` | `sports_data/errors/cwbb_v3_scores_are_any_games_in_progress_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_games_by_date_final

- **Route**: `GET /v3/cwbb/scores/{format}/GamesByDateFinal/{date}`
- **Signature**: `def cwbb_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game5]`
- **Returns (raw)**: `ApiResult[list[Game5], CwbbV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `CwbbV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game5` | `sports_data/models/game5.py` |
| `CwbbV3ScoresGamesByDateFinalErrorBody` | `sports_data/errors/cwbb_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/cwbb/scores/{format}/GamesByDate/{date}`
- **Signature**: `def cwbb_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game5]`
- **Returns (raw)**: `ApiResult[list[Game5], CwbbV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `CwbbV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game5` | `sports_data/models/game5.py` |
| `CwbbV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data/errors/cwbb_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_league_hierarchy

- **Route**: `GET /v3/cwbb/scores/{format}/LeagueHierarchy`
- **Signature**: `def cwbb_v3_scores_league_hierarchy(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Conference]`
- **Returns (raw)**: `ApiResult[list[Conference], CwbbV3ScoresLeagueHierarchyErrorBody]`
- **Error**: `CwbbV3ScoresLeagueHierarchyErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Conference` | `sports_data/models/conference.py` |
| `CwbbV3ScoresLeagueHierarchyErrorBody` | `sports_data/errors/cwbb_v3_scores_league_hierarchy_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_schedules

- **Route**: `GET /v3/cwbb/scores/{format}/Games/{season}`
- **Signature**: `def cwbb_v3_scores_schedules(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Game5]`
- **Returns (raw)**: `ApiResult[list[Game5], CwbbV3ScoresSchedulesErrorBody]`
- **Error**: `CwbbV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game5` | `sports_data/models/game5.py` |
| `CwbbV3ScoresSchedulesErrorBody` | `sports_data/errors/cwbb_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_schedules_basic

- **Route**: `GET /v3/cwbb/scores/{format}/SchedulesBasic/{season}`
- **Signature**: `def cwbb_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic2]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic2], CwbbV3ScoresSchedulesBasicErrorBody]`
- **Error**: `CwbbV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScheduleBasic2` | `sports_data/models/schedule_basic2.py` |
| `CwbbV3ScoresSchedulesBasicErrorBody` | `sports_data/errors/cwbb_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_season_current

- **Route**: `GET /v3/cwbb/scores/{format}/CurrentSeason`
- **Signature**: `def cwbb_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `Season2`
- **Returns (raw)**: `ApiResult[Season2, CwbbV3ScoresSeasonCurrentErrorBody]`
- **Error**: `CwbbV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Season2` | `sports_data/models/season2.py` |
| `CwbbV3ScoresSeasonCurrentErrorBody` | `sports_data/errors/cwbb_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cwbb_v3_scores.cwbb_v3_scores_team_profiles_all

- **Route**: `GET /v3/cwbb/scores/{format}/Teams`
- **Signature**: `def cwbb_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team2]`
- **Returns (raw)**: `ApiResult[list[Team2], CwbbV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `CwbbV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team2` | `sports_data/models/team2.py` |
| `CwbbV3ScoresTeamProfilesAllErrorBody` | `sports_data/errors/cwbb_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

