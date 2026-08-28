<!-- Generated file — do not edit; regenerated with the SDK. -->

# CbbV3Scores — operations

Accessor: `client.cbb_v3_scores` · Source: `cbb_api/apis/cbb_v3_scores.py` · 22 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cbb_v3_scores.cbb_v3_scores_are_games_in_progress

- **Route**: `GET /v3/cbb/scores/{format}/AreAnyGamesInProgress`
- **Signature**: `def cbb_v3_scores_are_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, CbbV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `CbbV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `CbbV3ScoresAreGamesInProgressErrorBody` | `cbb_api/errors/cbb_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_games_by_date_final

- **Route**: `GET /v3/cbb/scores/{format}/GamesByDateFinal/{date}`
- **Signature**: `def cbb_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game]`
- **Returns (raw)**: `ApiResult[list[Game], CbbV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `CbbV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Game` | `cbb_api/models/game.py` |
| `CbbV3ScoresGamesByDateFinalErrorBody` | `cbb_api/errors/cbb_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/cbb/scores/{format}/GamesByDate/{date}`
- **Signature**: `def cbb_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game]`
- **Returns (raw)**: `ApiResult[list[Game], CbbV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `CbbV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Game` | `cbb_api/models/game.py` |
| `CbbV3ScoresGamesByDateLiveFinalErrorBody` | `cbb_api/errors/cbb_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_games_by_season

- **Route**: `GET /v3/cbb/scores/{format}/Games/{season}`
- **Signature**: `def cbb_v3_scores_games_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Game]`
- **Returns (raw)**: `ApiResult[list[Game], CbbV3ScoresGamesBySeasonErrorBody]`
- **Error**: `CbbV3ScoresGamesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Game` | `cbb_api/models/game.py` |
| `CbbV3ScoresGamesBySeasonErrorBody` | `cbb_api/errors/cbb_v3_scores_games_by_season_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_games_by_season_final

- **Route**: `GET /v3/cbb/scores/{format}/GamesFinal/{season}`
- **Signature**: `def cbb_v3_scores_games_by_season_final(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Game]`
- **Returns (raw)**: `ApiResult[list[Game], CbbV3ScoresGamesBySeasonFinalErrorBody]`
- **Error**: `CbbV3ScoresGamesBySeasonFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Game` | `cbb_api/models/game.py` |
| `CbbV3ScoresGamesBySeasonFinalErrorBody` | `cbb_api/errors/cbb_v3_scores_games_by_season_final_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_games_basic_by_date

- **Route**: `GET /v3/cbb/scores/{format}/ScoresBasic/{date}`
- **Signature**: `def cbb_v3_scores_games_basic_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic], CbbV3ScoresGamesBasicByDateErrorBody]`
- **Error**: `CbbV3ScoresGamesBasicByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `ScoreBasic` | `cbb_api/models/score_basic.py` |
| `CbbV3ScoresGamesBasicByDateErrorBody` | `cbb_api/errors/cbb_v3_scores_games_basic_by_date_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_league_hierarchy

- **Route**: `GET /v3/cbb/scores/{format}/LeagueHierarchy`
- **Signature**: `def cbb_v3_scores_league_hierarchy(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Conference]`
- **Returns (raw)**: `ApiResult[list[Conference], CbbV3ScoresLeagueHierarchyErrorBody]`
- **Error**: `CbbV3ScoresLeagueHierarchyErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Conference` | `cbb_api/models/conference.py` |
| `CbbV3ScoresLeagueHierarchyErrorBody` | `cbb_api/errors/cbb_v3_scores_league_hierarchy_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_player_details_by_active

- **Route**: `GET /v3/cbb/scores/{format}/Players`
- **Signature**: `def cbb_v3_scores_player_details_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player]`
- **Returns (raw)**: `ApiResult[list[Player], CbbV3ScoresPlayerDetailsByActiveErrorBody]`
- **Error**: `CbbV3ScoresPlayerDetailsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Player` | `cbb_api/models/player.py` |
| `CbbV3ScoresPlayerDetailsByActiveErrorBody` | `cbb_api/errors/cbb_v3_scores_player_details_by_active_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_player_details_by_active2

- **Route**: `GET /v3/cbb/scores/{format}/PlayersByActive`
- **Signature**: `def cbb_v3_scores_player_details_by_active2(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic], CbbV3ScoresPlayerDetailsByActive2ErrorBody]`
- **Error**: `CbbV3ScoresPlayerDetailsByActive2ErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `PlayerBasic` | `cbb_api/models/player_basic.py` |
| `CbbV3ScoresPlayerDetailsByActive2ErrorBody` | `cbb_api/errors/cbb_v3_scores_player_details_by_active2_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_player_details_by_injured

- **Route**: `GET /v3/cbb/scores/{format}/InjuredPlayers`
- **Signature**: `def cbb_v3_scores_player_details_by_injured(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player]`
- **Returns (raw)**: `ApiResult[list[Player], CbbV3ScoresPlayerDetailsByInjuredErrorBody]`
- **Error**: `CbbV3ScoresPlayerDetailsByInjuredErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Player` | `cbb_api/models/player.py` |
| `CbbV3ScoresPlayerDetailsByInjuredErrorBody` | `cbb_api/errors/cbb_v3_scores_player_details_by_injured_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_player_details_by_team

- **Route**: `GET /v3/cbb/scores/{format}/Players/{team}`
- **Signature**: `def cbb_v3_scores_player_details_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[Player]`
- **Returns (raw)**: `ApiResult[list[Player], CbbV3ScoresPlayerDetailsByTeamErrorBody]`
- **Error**: `CbbV3ScoresPlayerDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Player` | `cbb_api/models/player.py` |
| `CbbV3ScoresPlayerDetailsByTeamErrorBody` | `cbb_api/errors/cbb_v3_scores_player_details_by_team_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_player_profiles_by_team

- **Route**: `GET /v3/cbb/scores/{format}/PlayersBasic/{team}`
- **Signature**: `def cbb_v3_scores_player_profiles_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[PlayerBasic]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic], CbbV3ScoresPlayerProfilesByTeamErrorBody]`
- **Error**: `CbbV3ScoresPlayerProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `PlayerBasic` | `cbb_api/models/player_basic.py` |
| `CbbV3ScoresPlayerProfilesByTeamErrorBody` | `cbb_api/errors/cbb_v3_scores_player_profiles_by_team_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_schedules_by_team

- **Route**: `GET /v3/cbb/scores/{format}/TeamSchedule/{season}/{team}`
- **Signature**: `def cbb_v3_scores_schedules_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[Game]`
- **Returns (raw)**: `ApiResult[list[Game], CbbV3ScoresSchedulesByTeamErrorBody]`
- **Error**: `CbbV3ScoresSchedulesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Game` | `cbb_api/models/game.py` |
| `CbbV3ScoresSchedulesByTeamErrorBody` | `cbb_api/errors/cbb_v3_scores_schedules_by_team_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_schedules_basic

- **Route**: `GET /v3/cbb/scores/{format}/SchedulesBasic/{season}`
- **Signature**: `def cbb_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic], CbbV3ScoresSchedulesBasicErrorBody]`
- **Error**: `CbbV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `ScheduleBasic` | `cbb_api/models/schedule_basic.py` |
| `CbbV3ScoresSchedulesBasicErrorBody` | `cbb_api/errors/cbb_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_season_current

- **Route**: `GET /v3/cbb/scores/{format}/CurrentSeason`
- **Signature**: `def cbb_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `Season`
- **Returns (raw)**: `ApiResult[Season, CbbV3ScoresSeasonCurrentErrorBody]`
- **Error**: `CbbV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Season` | `cbb_api/models/season.py` |
| `CbbV3ScoresSeasonCurrentErrorBody` | `cbb_api/errors/cbb_v3_scores_season_current_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_stadiums

- **Route**: `GET /v3/cbb/scores/{format}/Stadiums`
- **Signature**: `def cbb_v3_scores_stadiums(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Stadium]`
- **Returns (raw)**: `ApiResult[list[Stadium], CbbV3ScoresStadiumsErrorBody]`
- **Error**: `CbbV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Stadium` | `cbb_api/models/stadium.py` |
| `CbbV3ScoresStadiumsErrorBody` | `cbb_api/errors/cbb_v3_scores_stadiums_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_team_game_logs_by_season

- **Route**: `GET /v3/cbb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Signature**: `def cbb_v3_scores_team_game_logs_by_season(format: FormatOrStr, season: str, teamid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `teamid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame]`
- **Returns (raw)**: `ApiResult[list[TeamGame], CbbV3ScoresTeamGameLogsBySeasonErrorBody]`
- **Error**: `CbbV3ScoresTeamGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `TeamGame` | `cbb_api/models/team_game.py` |
| `CbbV3ScoresTeamGameLogsBySeasonErrorBody` | `cbb_api/errors/cbb_v3_scores_team_game_logs_by_season_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_team_game_stats_by_date_live_final

- **Route**: `GET /v3/cbb/scores/{format}/TeamGameStatsByDate/{date}`
- **Signature**: `def cbb_v3_scores_team_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame]`
- **Returns (raw)**: `ApiResult[list[TeamGame], CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody]`
- **Error**: `CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `TeamGame` | `cbb_api/models/team_game.py` |
| `CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody` | `cbb_api/errors/cbb_v3_scores_team_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_team_profiles_all

- **Route**: `GET /v3/cbb/scores/{format}/teams`
- **Signature**: `def cbb_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team]`
- **Returns (raw)**: `ApiResult[list[Team], CbbV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `CbbV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Team` | `cbb_api/models/team.py` |
| `CbbV3ScoresTeamProfilesAllErrorBody` | `cbb_api/errors/cbb_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_team_season_stats

- **Route**: `GET /v3/cbb/scores/{format}/TeamSeasonStats/{season}`
- **Signature**: `def cbb_v3_scores_team_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamSeason]`
- **Returns (raw)**: `ApiResult[list[TeamSeason], CbbV3ScoresTeamSeasonStatsErrorBody]`
- **Error**: `CbbV3ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `TeamSeason` | `cbb_api/models/team_season.py` |
| `CbbV3ScoresTeamSeasonStatsErrorBody` | `cbb_api/errors/cbb_v3_scores_team_season_stats_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_teams_basic_all

- **Route**: `GET /v3/cbb/scores/{format}/TeamsBasic`
- **Signature**: `def cbb_v3_scores_teams_basic_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamBasic]`
- **Returns (raw)**: `ApiResult[list[TeamBasic], CbbV3ScoresTeamsBasicAllErrorBody]`
- **Error**: `CbbV3ScoresTeamsBasicAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `TeamBasic` | `cbb_api/models/team_basic.py` |
| `CbbV3ScoresTeamsBasicAllErrorBody` | `cbb_api/errors/cbb_v3_scores_teams_basic_all_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

### client.cbb_v3_scores.cbb_v3_scores_tournament_hierarchy

- **Route**: `GET /v3/cbb/scores/{format}/Tournament/{season}`
- **Signature**: `def cbb_v3_scores_tournament_hierarchy(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `Tournament`
- **Returns (raw)**: `ApiResult[Tournament, CbbV3ScoresTournamentHierarchyErrorBody]`
- **Error**: `CbbV3ScoresTournamentHierarchyErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `cbb_api/models/enums/format.py` |
| `Tournament` | `cbb_api/models/tournament.py` |
| `CbbV3ScoresTournamentHierarchyErrorBody` | `cbb_api/errors/cbb_v3_scores_tournament_hierarchy_error.py` |
| `Unauthorized` | `cbb_api/models/unauthorized.py` |

