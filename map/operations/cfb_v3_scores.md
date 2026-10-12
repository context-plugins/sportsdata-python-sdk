<!-- Generated file — do not edit; regenerated with the SDK. -->

# CfbV3Scores — operations

Accessor: `client.cfb_v3_scores` · Source: `sports_data_io/apis/cfb_v3_scores.py` · 26 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cfb_v3_scores.cfb_v3_scores_are_games_in_progress

- **Route**: `GET /v3/cfb/scores/{format}/AreAnyGamesInProgress`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_are_games_in_progress(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, CfbV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `CfbV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `CfbV3ScoresAreGamesInProgressErrorBody` | `sports_data_io/errors/cfb_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_conference_hierarchy

- **Route**: `GET /v3/cfb/scores/{format}/LeagueHierarchy`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_conference_hierarchy(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Conference]`
- **Returns (raw)**: `ApiResult[list[Conference], CfbV3ScoresConferenceHierarchyErrorBody]`
- **Error**: `CfbV3ScoresConferenceHierarchyErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Conference` | `sports_data_io/models/conference.py` |
| `CfbV3ScoresConferenceHierarchyErrorBody` | `sports_data_io/errors/cfb_v3_scores_conference_hierarchy_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/cfb/scores/{format}/GamesByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_games_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[Game8]`
- **Returns (raw)**: `ApiResult[list[Game8], CfbV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game8` | `sports_data_io/models/game8.py` |
| `CfbV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data_io/errors/cfb_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_by_week_final

- **Route**: `GET /v3/cfb/scores/{format}/GamesByWeekFinal/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_games_by_week_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[Game8]`
- **Returns (raw)**: `ApiResult[list[Game8], CfbV3ScoresGamesByWeekFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game8` | `sports_data_io/models/game8.py` |
| `CfbV3ScoresGamesByWeekFinalErrorBody` | `sports_data_io/errors/cfb_v3_scores_games_by_week_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_by_week_live_final

- **Route**: `GET /v3/cfb/scores/{format}/GamesByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_games_by_week_live_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[Game8]`
- **Returns (raw)**: `ApiResult[list[Game8], CfbV3ScoresGamesByWeekLiveFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game8` | `sports_data_io/models/game8.py` |
| `CfbV3ScoresGamesByWeekLiveFinalErrorBody` | `sports_data_io/errors/cfb_v3_scores_games_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_basic_by_date_live_final

- **Route**: `GET /v3/cfb/scores/{format}/ScoresBasic/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_games_basic_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[ScoreBasic4]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic4], CfbV3ScoresGamesBasicByDateLiveFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesBasicByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic4` | `sports_data_io/models/score_basic4.py` |
| `CfbV3ScoresGamesBasicByDateLiveFinalErrorBody` | `sports_data_io/errors/cfb_v3_scores_games_basic_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_basic_by_week_final

- **Route**: `GET /v3/cfb/scores/{format}/ScoresBasicFinal/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_games_basic_by_week_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[ScoreBasic4]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic4], CfbV3ScoresGamesBasicByWeekFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesBasicByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic4` | `sports_data_io/models/score_basic4.py` |
| `CfbV3ScoresGamesBasicByWeekFinalErrorBody` | `sports_data_io/errors/cfb_v3_scores_games_basic_by_week_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_basic_by_date_final

- **Route**: `GET /v3/cfb/scores/{format}/ScoresBasicFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_games_basic_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[ScoreBasic4]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic4], CfbV3ScoresGamesBasicByDateFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesBasicByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic4` | `sports_data_io/models/score_basic4.py` |
| `CfbV3ScoresGamesBasicByDateFinalErrorBody` | `sports_data_io/errors/cfb_v3_scores_games_basic_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_by_date_final

- **Route**: `GET /v3/cfb/scores/{format}/GamesByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_games_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[Game8]`
- **Returns (raw)**: `ApiResult[list[Game8], CfbV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game8` | `sports_data_io/models/game8.py` |
| `CfbV3ScoresGamesByDateFinalErrorBody` | `sports_data_io/errors/cfb_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_player_details_by_active

- **Route**: `GET /v3/cfb/scores/{format}/Players`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_player_details_by_active(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Player4]`
- **Returns (raw)**: `ApiResult[list[Player4], CfbV3ScoresPlayerDetailsByActiveErrorBody]`
- **Error**: `CfbV3ScoresPlayerDetailsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player4` | `sports_data_io/models/player4.py` |
| `CfbV3ScoresPlayerDetailsByActiveErrorBody` | `sports_data_io/errors/cfb_v3_scores_player_details_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_player_details_by_active2

- **Route**: `GET /v3/cfb/scores/{format}/PlayersByActive`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_player_details_by_active2(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[PlayerBasic4]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic4], CfbV3ScoresPlayerDetailsByActive2ErrorBody]`
- **Error**: `CfbV3ScoresPlayerDetailsByActive2ErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic4` | `sports_data_io/models/player_basic4.py` |
| `CfbV3ScoresPlayerDetailsByActive2ErrorBody` | `sports_data_io/errors/cfb_v3_scores_player_details_by_active2_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_player_details_by_injured

- **Route**: `GET /v3/cfb/scores/{format}/InjuredPlayers`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_player_details_by_injured(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Player4]`
- **Returns (raw)**: `ApiResult[list[Player4], CfbV3ScoresPlayerDetailsByInjuredErrorBody]`
- **Error**: `CfbV3ScoresPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player4` | `sports_data_io/models/player4.py` |
| `CfbV3ScoresPlayerDetailsByInjuredErrorBody` | `sports_data_io/errors/cfb_v3_scores_player_details_by_injured_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_player_details_by_team

- **Route**: `GET /v3/cfb/scores/{format}/Players/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_player_details_by_team(team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`
- **Params**: `format_` — path `format` · `team` — path
- **Returns (parsed)**: `list[Player4]`
- **Returns (raw)**: `ApiResult[list[Player4], CfbV3ScoresPlayerDetailsByTeamErrorBody]`
- **Error**: `CfbV3ScoresPlayerDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player4` | `sports_data_io/models/player4.py` |
| `CfbV3ScoresPlayerDetailsByTeamErrorBody` | `sports_data_io/errors/cfb_v3_scores_player_details_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_player_profiles_by_team

- **Route**: `GET /v3/cfb/scores/{format}/PlayersBasic/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_player_profiles_by_team(team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`
- **Params**: `format_` — path `format` · `team` — path
- **Returns (parsed)**: `list[PlayerBasic4]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic4], CfbV3ScoresPlayerProfilesByTeamErrorBody]`
- **Error**: `CfbV3ScoresPlayerProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic4` | `sports_data_io/models/player_basic4.py` |
| `CfbV3ScoresPlayerProfilesByTeamErrorBody` | `sports_data_io/errors/cfb_v3_scores_player_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_schedules

- **Route**: `GET /v3/cfb/scores/{format}/Games/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_schedules(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[Game8]`
- **Returns (raw)**: `ApiResult[list[Game8], CfbV3ScoresSchedulesErrorBody]`
- **Error**: `CfbV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game8` | `sports_data_io/models/game8.py` |
| `CfbV3ScoresSchedulesErrorBody` | `sports_data_io/errors/cfb_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_schedules_basic

- **Route**: `GET /v3/cfb/scores/{format}/SchedulesBasic/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_schedules_basic(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic4]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic4], CfbV3ScoresSchedulesBasicErrorBody]`
- **Error**: `CfbV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScheduleBasic4` | `sports_data_io/models/schedule_basic4.py` |
| `CfbV3ScoresSchedulesBasicErrorBody` | `sports_data_io/errors/cfb_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_season_current

- **Route**: `GET /v3/cfb/scores/{format}/CurrentSeason`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_season_current(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `int`
- **Returns (raw)**: `ApiResult[int, CfbV3ScoresSeasonCurrentErrorBody]`
- **Error**: `CfbV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `CfbV3ScoresSeasonCurrentErrorBody` | `sports_data_io/errors/cfb_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_season_current_details

- **Route**: `GET /v3/cfb/scores/{format}/CurrentSeasonDetails`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_season_current_details(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `Season2`
- **Returns (raw)**: `ApiResult[Season2, CfbV3ScoresSeasonCurrentDetailsErrorBody]`
- **Error**: `CfbV3ScoresSeasonCurrentDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Season2` | `sports_data_io/models/season2.py` |
| `CfbV3ScoresSeasonCurrentDetailsErrorBody` | `sports_data_io/errors/cfb_v3_scores_season_current_details_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_season_type_current

- **Route**: `GET /v3/cfb/scores/{format}/CurrentSeasonType`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_season_type_current(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `str | None`
- **Returns (raw)**: `ApiResult[str | None, CfbV3ScoresSeasonTypeCurrentErrorBody]`
- **Error**: `CfbV3ScoresSeasonTypeCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `CfbV3ScoresSeasonTypeCurrentErrorBody` | `sports_data_io/errors/cfb_v3_scores_season_type_current_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_stadiums

- **Route**: `GET /v3/cfb/scores/{format}/Stadiums`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_stadiums(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Stadium5]`
- **Returns (raw)**: `ApiResult[list[Stadium5], CfbV3ScoresStadiumsErrorBody]`
- **Error**: `CfbV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Stadium5` | `sports_data_io/models/stadium5.py` |
| `CfbV3ScoresStadiumsErrorBody` | `sports_data_io/errors/cfb_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_team_game_logs_by_season

- **Route**: `GET /v3/cfb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_team_game_logs_by_season(season: str, teamid: str, numberofgames: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `teamid`, `numberofgames`
- **Params**: `format_` — path `format` · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame4]`
- **Returns (raw)**: `ApiResult[list[TeamGame4], CfbV3ScoresTeamGameLogsBySeasonErrorBody]`
- **Error**: `CfbV3ScoresTeamGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame4` | `sports_data_io/models/team_game4.py` |
| `CfbV3ScoresTeamGameLogsBySeasonErrorBody` | `sports_data_io/errors/cfb_v3_scores_team_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_team_game_stats_by_week_live_final

- **Route**: `GET /v3/cfb/scores/{format}/TeamGameStatsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_team_game_stats_by_week_live_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[TeamGame4]`
- **Returns (raw)**: `ApiResult[list[TeamGame4], CfbV3ScoresTeamGameStatsByWeekLiveFinalErrorBody]`
- **Error**: `CfbV3ScoresTeamGameStatsByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame4` | `sports_data_io/models/team_game4.py` |
| `CfbV3ScoresTeamGameStatsByWeekLiveFinalErrorBody` | `sports_data_io/errors/cfb_v3_scores_team_game_stats_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_team_profiles_all

- **Route**: `GET /v3/cfb/scores/{format}/Teams`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_team_profiles_all(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Team4]`
- **Returns (raw)**: `ApiResult[list[Team4], CfbV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `CfbV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team4` | `sports_data_io/models/team4.py` |
| `CfbV3ScoresTeamProfilesAllErrorBody` | `sports_data_io/errors/cfb_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_team_season_stats_standings

- **Route**: `GET /v3/cfb/scores/{format}/TeamSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_team_season_stats_standings(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[TeamSeason4]`
- **Returns (raw)**: `ApiResult[list[TeamSeason4], CfbV3ScoresTeamSeasonStatsStandingsErrorBody]`
- **Error**: `CfbV3ScoresTeamSeasonStatsStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamSeason4` | `sports_data_io/models/team_season4.py` |
| `CfbV3ScoresTeamSeasonStatsStandingsErrorBody` | `sports_data_io/errors/cfb_v3_scores_team_season_stats_standings_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_teams_basic_all

- **Route**: `GET /v3/cfb/scores/{format}/TeamsBasic`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_teams_basic_all(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[TeamBasic1]`
- **Returns (raw)**: `ApiResult[list[TeamBasic1], CfbV3ScoresTeamsBasicAllErrorBody]`
- **Error**: `CfbV3ScoresTeamsBasicAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamBasic1` | `sports_data_io/models/team_basic1.py` |
| `CfbV3ScoresTeamsBasicAllErrorBody` | `sports_data_io/errors/cfb_v3_scores_teams_basic_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_week_current

- **Route**: `GET /v3/cfb/scores/{format}/CurrentWeek`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_scores_week_current(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, CfbV3ScoresWeekCurrentErrorBody]`
- **Error**: `CfbV3ScoresWeekCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `CfbV3ScoresWeekCurrentErrorBody` | `sports_data_io/errors/cfb_v3_scores_week_current_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

