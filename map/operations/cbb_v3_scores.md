<!-- Generated file — do not edit; regenerated with the SDK. -->

# CbbV3Scores — operations

Accessor: `client.cbb_v3_scores` · Source: `sports_data_io/apis/cbb_v3_scores.py` · 22 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cbb_v3_scores.cbb_v3_scores_are_games_in_progress

- **Route**: `GET /v3/cbb/scores/{format}/AreAnyGamesInProgress`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_are_games_in_progress(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, CbbV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `CbbV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `CbbV3ScoresAreGamesInProgressErrorBody` | `sports_data_io/errors/cbb_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_games_by_date_final

- **Route**: `GET /v3/cbb/scores/{format}/GamesByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_games_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[Game9]`
- **Returns (raw)**: `ApiResult[list[Game9], CbbV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `CbbV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game9` | `sports_data_io/models/game9.py` |
| `CbbV3ScoresGamesByDateFinalErrorBody` | `sports_data_io/errors/cbb_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/cbb/scores/{format}/GamesByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_games_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[Game9]`
- **Returns (raw)**: `ApiResult[list[Game9], CbbV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `CbbV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game9` | `sports_data_io/models/game9.py` |
| `CbbV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data_io/errors/cbb_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_games_by_season

- **Route**: `GET /v3/cbb/scores/{format}/Games/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_games_by_season(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[Game9]`
- **Returns (raw)**: `ApiResult[list[Game9], CbbV3ScoresGamesBySeasonErrorBody]`
- **Error**: `CbbV3ScoresGamesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game9` | `sports_data_io/models/game9.py` |
| `CbbV3ScoresGamesBySeasonErrorBody` | `sports_data_io/errors/cbb_v3_scores_games_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_games_by_season_final

- **Route**: `GET /v3/cbb/scores/{format}/GamesFinal/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_games_by_season_final(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[Game9]`
- **Returns (raw)**: `ApiResult[list[Game9], CbbV3ScoresGamesBySeasonFinalErrorBody]`
- **Error**: `CbbV3ScoresGamesBySeasonFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game9` | `sports_data_io/models/game9.py` |
| `CbbV3ScoresGamesBySeasonFinalErrorBody` | `sports_data_io/errors/cbb_v3_scores_games_by_season_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_games_basic_by_date

- **Route**: `GET /v3/cbb/scores/{format}/ScoresBasic/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_games_basic_by_date(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[ScoreBasic5]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic5], CbbV3ScoresGamesBasicByDateErrorBody]`
- **Error**: `CbbV3ScoresGamesBasicByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic5` | `sports_data_io/models/score_basic5.py` |
| `CbbV3ScoresGamesBasicByDateErrorBody` | `sports_data_io/errors/cbb_v3_scores_games_basic_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_league_hierarchy

- **Route**: `GET /v3/cbb/scores/{format}/LeagueHierarchy`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_league_hierarchy(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Conference1]`
- **Returns (raw)**: `ApiResult[list[Conference1], CbbV3ScoresLeagueHierarchyErrorBody]`
- **Error**: `CbbV3ScoresLeagueHierarchyErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Conference1` | `sports_data_io/models/conference1.py` |
| `CbbV3ScoresLeagueHierarchyErrorBody` | `sports_data_io/errors/cbb_v3_scores_league_hierarchy_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_player_details_by_active

- **Route**: `GET /v3/cbb/scores/{format}/Players`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_player_details_by_active(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Player5]`
- **Returns (raw)**: `ApiResult[list[Player5], CbbV3ScoresPlayerDetailsByActiveErrorBody]`
- **Error**: `CbbV3ScoresPlayerDetailsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player5` | `sports_data_io/models/player5.py` |
| `CbbV3ScoresPlayerDetailsByActiveErrorBody` | `sports_data_io/errors/cbb_v3_scores_player_details_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_player_details_by_active2

- **Route**: `GET /v3/cbb/scores/{format}/PlayersByActive`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_player_details_by_active2(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[PlayerBasic5]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic5], CbbV3ScoresPlayerDetailsByActive2ErrorBody]`
- **Error**: `CbbV3ScoresPlayerDetailsByActive2ErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic5` | `sports_data_io/models/player_basic5.py` |
| `CbbV3ScoresPlayerDetailsByActive2ErrorBody` | `sports_data_io/errors/cbb_v3_scores_player_details_by_active2_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_player_details_by_injured

- **Route**: `GET /v3/cbb/scores/{format}/InjuredPlayers`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_player_details_by_injured(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Player5]`
- **Returns (raw)**: `ApiResult[list[Player5], CbbV3ScoresPlayerDetailsByInjuredErrorBody]`
- **Error**: `CbbV3ScoresPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player5` | `sports_data_io/models/player5.py` |
| `CbbV3ScoresPlayerDetailsByInjuredErrorBody` | `sports_data_io/errors/cbb_v3_scores_player_details_by_injured_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_player_details_by_team

- **Route**: `GET /v3/cbb/scores/{format}/Players/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_player_details_by_team(team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`
- **Params**: `format_` — path `format` · `team` — path
- **Returns (parsed)**: `list[Player5]`
- **Returns (raw)**: `ApiResult[list[Player5], CbbV3ScoresPlayerDetailsByTeamErrorBody]`
- **Error**: `CbbV3ScoresPlayerDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player5` | `sports_data_io/models/player5.py` |
| `CbbV3ScoresPlayerDetailsByTeamErrorBody` | `sports_data_io/errors/cbb_v3_scores_player_details_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_player_profiles_by_team

- **Route**: `GET /v3/cbb/scores/{format}/PlayersBasic/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_player_profiles_by_team(team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`
- **Params**: `format_` — path `format` · `team` — path
- **Returns (parsed)**: `list[PlayerBasic5]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic5], CbbV3ScoresPlayerProfilesByTeamErrorBody]`
- **Error**: `CbbV3ScoresPlayerProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic5` | `sports_data_io/models/player_basic5.py` |
| `CbbV3ScoresPlayerProfilesByTeamErrorBody` | `sports_data_io/errors/cbb_v3_scores_player_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_schedules_by_team

- **Route**: `GET /v3/cbb/scores/{format}/TeamSchedule/{season}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_schedules_by_team(season: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `team`
- **Params**: `format_` — path `format` · `season` — path · `team` — path
- **Returns (parsed)**: `list[Game9]`
- **Returns (raw)**: `ApiResult[list[Game9], CbbV3ScoresSchedulesByTeamErrorBody]`
- **Error**: `CbbV3ScoresSchedulesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game9` | `sports_data_io/models/game9.py` |
| `CbbV3ScoresSchedulesByTeamErrorBody` | `sports_data_io/errors/cbb_v3_scores_schedules_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_schedules_basic

- **Route**: `GET /v3/cbb/scores/{format}/SchedulesBasic/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_schedules_basic(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic5]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic5], CbbV3ScoresSchedulesBasicErrorBody]`
- **Error**: `CbbV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScheduleBasic5` | `sports_data_io/models/schedule_basic5.py` |
| `CbbV3ScoresSchedulesBasicErrorBody` | `sports_data_io/errors/cbb_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_season_current

- **Route**: `GET /v3/cbb/scores/{format}/CurrentSeason`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_season_current(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `Season3`
- **Returns (raw)**: `ApiResult[Season3, CbbV3ScoresSeasonCurrentErrorBody]`
- **Error**: `CbbV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Season3` | `sports_data_io/models/season3.py` |
| `CbbV3ScoresSeasonCurrentErrorBody` | `sports_data_io/errors/cbb_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_stadiums

- **Route**: `GET /v3/cbb/scores/{format}/Stadiums`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_stadiums(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Stadium1]`
- **Returns (raw)**: `ApiResult[list[Stadium1], CbbV3ScoresStadiumsErrorBody]`
- **Error**: `CbbV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Stadium1` | `sports_data_io/models/stadium1.py` |
| `CbbV3ScoresStadiumsErrorBody` | `sports_data_io/errors/cbb_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_team_game_logs_by_season

- **Route**: `GET /v3/cbb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_team_game_logs_by_season(season: str, teamid: str, numberofgames: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `teamid`, `numberofgames`
- **Params**: `format_` — path `format` · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame5]`
- **Returns (raw)**: `ApiResult[list[TeamGame5], CbbV3ScoresTeamGameLogsBySeasonErrorBody]`
- **Error**: `CbbV3ScoresTeamGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame5` | `sports_data_io/models/team_game5.py` |
| `CbbV3ScoresTeamGameLogsBySeasonErrorBody` | `sports_data_io/errors/cbb_v3_scores_team_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_team_game_stats_by_date_live_final

- **Route**: `GET /v3/cbb/scores/{format}/TeamGameStatsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_team_game_stats_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[TeamGame5]`
- **Returns (raw)**: `ApiResult[list[TeamGame5], CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody]`
- **Error**: `CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame5` | `sports_data_io/models/team_game5.py` |
| `CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody` | `sports_data_io/errors/cbb_v3_scores_team_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_team_profiles_all

- **Route**: `GET /v3/cbb/scores/{format}/teams`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_team_profiles_all(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Team5]`
- **Returns (raw)**: `ApiResult[list[Team5], CbbV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `CbbV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team5` | `sports_data_io/models/team5.py` |
| `CbbV3ScoresTeamProfilesAllErrorBody` | `sports_data_io/errors/cbb_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_team_season_stats

- **Route**: `GET /v3/cbb/scores/{format}/TeamSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_team_season_stats(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[TeamSeason5]`
- **Returns (raw)**: `ApiResult[list[TeamSeason5], CbbV3ScoresTeamSeasonStatsErrorBody]`
- **Error**: `CbbV3ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamSeason5` | `sports_data_io/models/team_season5.py` |
| `CbbV3ScoresTeamSeasonStatsErrorBody` | `sports_data_io/errors/cbb_v3_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_teams_basic_all

- **Route**: `GET /v3/cbb/scores/{format}/TeamsBasic`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_teams_basic_all(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[TeamBasic2]`
- **Returns (raw)**: `ApiResult[list[TeamBasic2], CbbV3ScoresTeamsBasicAllErrorBody]`
- **Error**: `CbbV3ScoresTeamsBasicAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamBasic2` | `sports_data_io/models/team_basic2.py` |
| `CbbV3ScoresTeamsBasicAllErrorBody` | `sports_data_io/errors/cbb_v3_scores_teams_basic_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_tournament_hierarchy

- **Route**: `GET /v3/cbb/scores/{format}/Tournament/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_scores_tournament_hierarchy(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `Tournament`
- **Returns (raw)**: `ApiResult[Tournament, CbbV3ScoresTournamentHierarchyErrorBody]`
- **Error**: `CbbV3ScoresTournamentHierarchyErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Tournament` | `sports_data_io/models/tournament.py` |
| `CbbV3ScoresTournamentHierarchyErrorBody` | `sports_data_io/errors/cbb_v3_scores_tournament_hierarchy_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

