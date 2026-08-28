<!-- Generated file — do not edit; regenerated with the SDK. -->

# CfbV3Scores — operations

Accessor: `client.cfb_v3_scores` · Source: `sports_data/apis/cfb_v3_scores.py` · 26 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cfb_v3_scores.cfb_v3_scores_are_games_in_progress

- **Route**: `GET /v3/cfb/scores/{format}/AreAnyGamesInProgress`
- **Signature**: `def cfb_v3_scores_are_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, CfbV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `CfbV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `CfbV3ScoresAreGamesInProgressErrorBody` | `sports_data/errors/cfb_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_conference_hierarchy

- **Route**: `GET /v3/cfb/scores/{format}/LeagueHierarchy`
- **Signature**: `def cfb_v3_scores_conference_hierarchy(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Conference1]`
- **Returns (raw)**: `ApiResult[list[Conference1], CfbV3ScoresConferenceHierarchyErrorBody]`
- **Error**: `CfbV3ScoresConferenceHierarchyErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Conference1` | `sports_data/models/conference1.py` |
| `CfbV3ScoresConferenceHierarchyErrorBody` | `sports_data/errors/cfb_v3_scores_conference_hierarchy_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/cfb/scores/{format}/GamesByDate/{date}`
- **Signature**: `def cfb_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game4]`
- **Returns (raw)**: `ApiResult[list[Game4], CfbV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game4` | `sports_data/models/game4.py` |
| `CfbV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data/errors/cfb_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_by_week_final

- **Route**: `GET /v3/cfb/scores/{format}/GamesByWeekFinal/{season}/{week}`
- **Signature**: `def cfb_v3_scores_games_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[Game4]`
- **Returns (raw)**: `ApiResult[list[Game4], CfbV3ScoresGamesByWeekFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game4` | `sports_data/models/game4.py` |
| `CfbV3ScoresGamesByWeekFinalErrorBody` | `sports_data/errors/cfb_v3_scores_games_by_week_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_by_week_live_final

- **Route**: `GET /v3/cfb/scores/{format}/GamesByWeek/{season}/{week}`
- **Signature**: `def cfb_v3_scores_games_by_week_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[Game4]`
- **Returns (raw)**: `ApiResult[list[Game4], CfbV3ScoresGamesByWeekLiveFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game4` | `sports_data/models/game4.py` |
| `CfbV3ScoresGamesByWeekLiveFinalErrorBody` | `sports_data/errors/cfb_v3_scores_games_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_basic_by_date_live_final

- **Route**: `GET /v3/cfb/scores/{format}/ScoresBasic/{date}`
- **Signature**: `def cfb_v3_scores_games_basic_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic1]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic1], CfbV3ScoresGamesBasicByDateLiveFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesBasicByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic1` | `sports_data/models/score_basic1.py` |
| `CfbV3ScoresGamesBasicByDateLiveFinalErrorBody` | `sports_data/errors/cfb_v3_scores_games_basic_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_basic_by_week_final

- **Route**: `GET /v3/cfb/scores/{format}/ScoresBasicFinal/{season}/{week}`
- **Signature**: `def cfb_v3_scores_games_basic_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[ScoreBasic1]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic1], CfbV3ScoresGamesBasicByWeekFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesBasicByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic1` | `sports_data/models/score_basic1.py` |
| `CfbV3ScoresGamesBasicByWeekFinalErrorBody` | `sports_data/errors/cfb_v3_scores_games_basic_by_week_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_basic_by_date_final

- **Route**: `GET /v3/cfb/scores/{format}/ScoresBasicFinal/{date}`
- **Signature**: `def cfb_v3_scores_games_basic_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic1]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic1], CfbV3ScoresGamesBasicByDateFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesBasicByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic1` | `sports_data/models/score_basic1.py` |
| `CfbV3ScoresGamesBasicByDateFinalErrorBody` | `sports_data/errors/cfb_v3_scores_games_basic_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_games_by_date_final

- **Route**: `GET /v3/cfb/scores/{format}/GamesByDateFinal/{date}`
- **Signature**: `def cfb_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game4]`
- **Returns (raw)**: `ApiResult[list[Game4], CfbV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `CfbV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game4` | `sports_data/models/game4.py` |
| `CfbV3ScoresGamesByDateFinalErrorBody` | `sports_data/errors/cfb_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_player_details_by_active

- **Route**: `GET /v3/cfb/scores/{format}/Players`
- **Signature**: `def cfb_v3_scores_player_details_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player1]`
- **Returns (raw)**: `ApiResult[list[Player1], CfbV3ScoresPlayerDetailsByActiveErrorBody]`
- **Error**: `CfbV3ScoresPlayerDetailsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player1` | `sports_data/models/player1.py` |
| `CfbV3ScoresPlayerDetailsByActiveErrorBody` | `sports_data/errors/cfb_v3_scores_player_details_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_player_details_by_active2

- **Route**: `GET /v3/cfb/scores/{format}/PlayersByActive`
- **Signature**: `def cfb_v3_scores_player_details_by_active2(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic1]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic1], CfbV3ScoresPlayerDetailsByActive2ErrorBody]`
- **Error**: `CfbV3ScoresPlayerDetailsByActive2ErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic1` | `sports_data/models/player_basic1.py` |
| `CfbV3ScoresPlayerDetailsByActive2ErrorBody` | `sports_data/errors/cfb_v3_scores_player_details_by_active2_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_player_details_by_injured

- **Route**: `GET /v3/cfb/scores/{format}/InjuredPlayers`
- **Signature**: `def cfb_v3_scores_player_details_by_injured(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player1]`
- **Returns (raw)**: `ApiResult[list[Player1], CfbV3ScoresPlayerDetailsByInjuredErrorBody]`
- **Error**: `CfbV3ScoresPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player1` | `sports_data/models/player1.py` |
| `CfbV3ScoresPlayerDetailsByInjuredErrorBody` | `sports_data/errors/cfb_v3_scores_player_details_by_injured_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_player_details_by_team

- **Route**: `GET /v3/cfb/scores/{format}/Players/{team}`
- **Signature**: `def cfb_v3_scores_player_details_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[Player1]`
- **Returns (raw)**: `ApiResult[list[Player1], CfbV3ScoresPlayerDetailsByTeamErrorBody]`
- **Error**: `CfbV3ScoresPlayerDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player1` | `sports_data/models/player1.py` |
| `CfbV3ScoresPlayerDetailsByTeamErrorBody` | `sports_data/errors/cfb_v3_scores_player_details_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_player_profiles_by_team

- **Route**: `GET /v3/cfb/scores/{format}/PlayersBasic/{team}`
- **Signature**: `def cfb_v3_scores_player_profiles_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[PlayerBasic1]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic1], CfbV3ScoresPlayerProfilesByTeamErrorBody]`
- **Error**: `CfbV3ScoresPlayerProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic1` | `sports_data/models/player_basic1.py` |
| `CfbV3ScoresPlayerProfilesByTeamErrorBody` | `sports_data/errors/cfb_v3_scores_player_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_schedules

- **Route**: `GET /v3/cfb/scores/{format}/Games/{season}`
- **Signature**: `def cfb_v3_scores_schedules(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Game4]`
- **Returns (raw)**: `ApiResult[list[Game4], CfbV3ScoresSchedulesErrorBody]`
- **Error**: `CfbV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game4` | `sports_data/models/game4.py` |
| `CfbV3ScoresSchedulesErrorBody` | `sports_data/errors/cfb_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_schedules_basic

- **Route**: `GET /v3/cfb/scores/{format}/SchedulesBasic/{season}`
- **Signature**: `def cfb_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic1]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic1], CfbV3ScoresSchedulesBasicErrorBody]`
- **Error**: `CfbV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScheduleBasic1` | `sports_data/models/schedule_basic1.py` |
| `CfbV3ScoresSchedulesBasicErrorBody` | `sports_data/errors/cfb_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_season_current

- **Route**: `GET /v3/cfb/scores/{format}/CurrentSeason`
- **Signature**: `def cfb_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int`
- **Returns (raw)**: `ApiResult[int, CfbV3ScoresSeasonCurrentErrorBody]`
- **Error**: `CfbV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `CfbV3ScoresSeasonCurrentErrorBody` | `sports_data/errors/cfb_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_season_current_details

- **Route**: `GET /v3/cfb/scores/{format}/CurrentSeasonDetails`
- **Signature**: `def cfb_v3_scores_season_current_details(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `Season1`
- **Returns (raw)**: `ApiResult[Season1, CfbV3ScoresSeasonCurrentDetailsErrorBody]`
- **Error**: `CfbV3ScoresSeasonCurrentDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Season1` | `sports_data/models/season1.py` |
| `CfbV3ScoresSeasonCurrentDetailsErrorBody` | `sports_data/errors/cfb_v3_scores_season_current_details_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_season_type_current

- **Route**: `GET /v3/cfb/scores/{format}/CurrentSeasonType`
- **Signature**: `def cfb_v3_scores_season_type_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `str | None`
- **Returns (raw)**: `ApiResult[str | None, CfbV3ScoresSeasonTypeCurrentErrorBody]`
- **Error**: `CfbV3ScoresSeasonTypeCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `CfbV3ScoresSeasonTypeCurrentErrorBody` | `sports_data/errors/cfb_v3_scores_season_type_current_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_stadiums

- **Route**: `GET /v3/cfb/scores/{format}/Stadiums`
- **Signature**: `def cfb_v3_scores_stadiums(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Stadium1]`
- **Returns (raw)**: `ApiResult[list[Stadium1], CfbV3ScoresStadiumsErrorBody]`
- **Error**: `CfbV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Stadium1` | `sports_data/models/stadium1.py` |
| `CfbV3ScoresStadiumsErrorBody` | `sports_data/errors/cfb_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_team_game_logs_by_season

- **Route**: `GET /v3/cfb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Signature**: `def cfb_v3_scores_team_game_logs_by_season(format: FormatOrStr, season: str, teamid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `teamid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame1]`
- **Returns (raw)**: `ApiResult[list[TeamGame1], CfbV3ScoresTeamGameLogsBySeasonErrorBody]`
- **Error**: `CfbV3ScoresTeamGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame1` | `sports_data/models/team_game1.py` |
| `CfbV3ScoresTeamGameLogsBySeasonErrorBody` | `sports_data/errors/cfb_v3_scores_team_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_team_game_stats_by_week_live_final

- **Route**: `GET /v3/cfb/scores/{format}/TeamGameStatsByWeek/{season}/{week}`
- **Signature**: `def cfb_v3_scores_team_game_stats_by_week_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[TeamGame1]`
- **Returns (raw)**: `ApiResult[list[TeamGame1], CfbV3ScoresTeamGameStatsByWeekLiveFinalErrorBody]`
- **Error**: `CfbV3ScoresTeamGameStatsByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame1` | `sports_data/models/team_game1.py` |
| `CfbV3ScoresTeamGameStatsByWeekLiveFinalErrorBody` | `sports_data/errors/cfb_v3_scores_team_game_stats_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_team_profiles_all

- **Route**: `GET /v3/cfb/scores/{format}/Teams`
- **Signature**: `def cfb_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team1]`
- **Returns (raw)**: `ApiResult[list[Team1], CfbV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `CfbV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team1` | `sports_data/models/team1.py` |
| `CfbV3ScoresTeamProfilesAllErrorBody` | `sports_data/errors/cfb_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_team_season_stats_standings

- **Route**: `GET /v3/cfb/scores/{format}/TeamSeasonStats/{season}`
- **Signature**: `def cfb_v3_scores_team_season_stats_standings(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamSeason1]`
- **Returns (raw)**: `ApiResult[list[TeamSeason1], CfbV3ScoresTeamSeasonStatsStandingsErrorBody]`
- **Error**: `CfbV3ScoresTeamSeasonStatsStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamSeason1` | `sports_data/models/team_season1.py` |
| `CfbV3ScoresTeamSeasonStatsStandingsErrorBody` | `sports_data/errors/cfb_v3_scores_team_season_stats_standings_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_teams_basic_all

- **Route**: `GET /v3/cfb/scores/{format}/TeamsBasic`
- **Signature**: `def cfb_v3_scores_teams_basic_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamBasic1]`
- **Returns (raw)**: `ApiResult[list[TeamBasic1], CfbV3ScoresTeamsBasicAllErrorBody]`
- **Error**: `CfbV3ScoresTeamsBasicAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamBasic1` | `sports_data/models/team_basic1.py` |
| `CfbV3ScoresTeamsBasicAllErrorBody` | `sports_data/errors/cfb_v3_scores_teams_basic_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_scores.cfb_v3_scores_week_current

- **Route**: `GET /v3/cfb/scores/{format}/CurrentWeek`
- **Signature**: `def cfb_v3_scores_week_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, CfbV3ScoresWeekCurrentErrorBody]`
- **Error**: `CfbV3ScoresWeekCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `CfbV3ScoresWeekCurrentErrorBody` | `sports_data/errors/cfb_v3_scores_week_current_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

