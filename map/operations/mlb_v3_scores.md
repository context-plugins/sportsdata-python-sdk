<!-- Generated file — do not edit; regenerated with the SDK. -->

# MlbV3Scores — operations

Accessor: `client.mlb_v3_scores` · Source: `sports_data/apis/mlb_v3_scores.py` · 26 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mlb_v3_scores.mlb_v3_scores_are_games_in_progress

- **Route**: `GET /v3/mlb/scores/{format}/AreAnyGamesInProgress`
- **Signature**: `def mlb_v3_scores_are_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, MlbV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `MlbV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `MlbV3ScoresAreGamesInProgressErrorBody` | `sports_data/errors/mlb_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_games_by_date_final

- **Route**: `GET /v3/mlb/scores/{format}/GamesByDateFinal/{date}`
- **Signature**: `def mlb_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game6]`
- **Returns (raw)**: `ApiResult[list[Game6], MlbV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `MlbV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game6` | `sports_data/models/game6.py` |
| `MlbV3ScoresGamesByDateFinalErrorBody` | `sports_data/errors/mlb_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/mlb/scores/{format}/GamesByDate/{date}`
- **Signature**: `def mlb_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game6]`
- **Returns (raw)**: `ApiResult[list[Game6], MlbV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `MlbV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game6` | `sports_data/models/game6.py` |
| `MlbV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data/errors/mlb_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_games_basic_by_date_final

- **Route**: `GET /v3/mlb/scores/{format}/ScoresBasicFinal/{date}`
- **Signature**: `def mlb_v3_scores_games_basic_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic2]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic2], MlbV3ScoresGamesBasicByDateFinalErrorBody]`
- **Error**: `MlbV3ScoresGamesBasicByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic2` | `sports_data/models/score_basic2.py` |
| `MlbV3ScoresGamesBasicByDateFinalErrorBody` | `sports_data/errors/mlb_v3_scores_games_basic_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_games_basic_by_date_live_final

- **Route**: `GET /v3/mlb/scores/{format}/ScoresBasic/{date}`
- **Signature**: `def mlb_v3_scores_games_basic_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic2]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic2], MlbV3ScoresGamesBasicByDateLiveFinalErrorBody]`
- **Error**: `MlbV3ScoresGamesBasicByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic2` | `sports_data/models/score_basic2.py` |
| `MlbV3ScoresGamesBasicByDateLiveFinalErrorBody` | `sports_data/errors/mlb_v3_scores_games_basic_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_news

- **Route**: `GET /v3/mlb/scores/{format}/News`
- **Signature**: `def mlb_v3_scores_news(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], MlbV3ScoresNewsErrorBody]`
- **Error**: `MlbV3ScoresNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News1` | `sports_data/models/news1.py` |
| `MlbV3ScoresNewsErrorBody` | `sports_data/errors/mlb_v3_scores_news_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_news_by_date

- **Route**: `GET /v3/mlb/scores/{format}/NewsByDate/{date}`
- **Signature**: `def mlb_v3_scores_news_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], MlbV3ScoresNewsByDateErrorBody]`
- **Error**: `MlbV3ScoresNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News1` | `sports_data/models/news1.py` |
| `MlbV3ScoresNewsByDateErrorBody` | `sports_data/errors/mlb_v3_scores_news_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_player_details_by_active

- **Route**: `GET /v3/mlb/scores/{format}/Players`
- **Signature**: `def mlb_v3_scores_player_details_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player3]`
- **Returns (raw)**: `ApiResult[list[Player3], MlbV3ScoresPlayerDetailsByActiveErrorBody]`
- **Error**: `MlbV3ScoresPlayerDetailsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player3` | `sports_data/models/player3.py` |
| `MlbV3ScoresPlayerDetailsByActiveErrorBody` | `sports_data/errors/mlb_v3_scores_player_details_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_player_details_by_free_agents

- **Route**: `GET /v3/mlb/scores/{format}/FreeAgents`
- **Signature**: `def mlb_v3_scores_player_details_by_free_agents(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player3]`
- **Returns (raw)**: `ApiResult[list[Player3], MlbV3ScoresPlayerDetailsByFreeAgentsErrorBody]`
- **Error**: `MlbV3ScoresPlayerDetailsByFreeAgentsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player3` | `sports_data/models/player3.py` |
| `MlbV3ScoresPlayerDetailsByFreeAgentsErrorBody` | `sports_data/errors/mlb_v3_scores_player_details_by_free_agents_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_player_profiles_by_active

- **Route**: `GET /v3/mlb/scores/{format}/PlayersByActive`
- **Signature**: `def mlb_v3_scores_player_profiles_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic2]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByActiveErrorBody]`
- **Error**: `MlbV3ScoresPlayerProfilesByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic2` | `sports_data/models/player_basic2.py` |
| `MlbV3ScoresPlayerProfilesByActiveErrorBody` | `sports_data/errors/mlb_v3_scores_player_profiles_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_player_profiles_by_free_agents

- **Route**: `GET /v3/mlb/scores/{format}/PlayersByFreeAgents`
- **Signature**: `def mlb_v3_scores_player_profiles_by_free_agents(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic2]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByFreeAgentsErrorBody]`
- **Error**: `MlbV3ScoresPlayerProfilesByFreeAgentsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic2` | `sports_data/models/player_basic2.py` |
| `MlbV3ScoresPlayerProfilesByFreeAgentsErrorBody` | `sports_data/errors/mlb_v3_scores_player_profiles_by_free_agents_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_player_profiles_by_team

- **Route**: `GET /v3/mlb/scores/{format}/PlayersBasic/{team}`
- **Signature**: `def mlb_v3_scores_player_profiles_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[PlayerBasic2]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByTeamErrorBody]`
- **Error**: `MlbV3ScoresPlayerProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic2` | `sports_data/models/player_basic2.py` |
| `MlbV3ScoresPlayerProfilesByTeamErrorBody` | `sports_data/errors/mlb_v3_scores_player_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_players_details_by_team

- **Route**: `GET /v3/mlb/scores/{format}/Players/{team}`
- **Signature**: `def mlb_v3_scores_players_details_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[Player3]`
- **Returns (raw)**: `ApiResult[list[Player3], MlbV3ScoresPlayersDetailsByTeamErrorBody]`
- **Error**: `MlbV3ScoresPlayersDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player3` | `sports_data/models/player3.py` |
| `MlbV3ScoresPlayersDetailsByTeamErrorBody` | `sports_data/errors/mlb_v3_scores_players_details_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_schedules

- **Route**: `GET /v3/mlb/scores/{format}/Games/{season}`
- **Signature**: `def mlb_v3_scores_schedules(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Game6]`
- **Returns (raw)**: `ApiResult[list[Game6], MlbV3ScoresSchedulesErrorBody]`
- **Error**: `MlbV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game6` | `sports_data/models/game6.py` |
| `MlbV3ScoresSchedulesErrorBody` | `sports_data/errors/mlb_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_schedules_basic

- **Route**: `GET /v3/mlb/scores/{format}/SchedulesBasic/{season}`
- **Signature**: `def mlb_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic3]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic3], MlbV3ScoresSchedulesBasicErrorBody]`
- **Error**: `MlbV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScheduleBasic3` | `sports_data/models/schedule_basic3.py` |
| `MlbV3ScoresSchedulesBasicErrorBody` | `sports_data/errors/mlb_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_season_current

- **Route**: `GET /v3/mlb/scores/{format}/CurrentSeason`
- **Signature**: `def mlb_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `Season4`
- **Returns (raw)**: `ApiResult[Season4, MlbV3ScoresSeasonCurrentErrorBody]`
- **Error**: `MlbV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Season4` | `sports_data/models/season4.py` |
| `MlbV3ScoresSeasonCurrentErrorBody` | `sports_data/errors/mlb_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_stadiums

- **Route**: `GET /v3/mlb/scores/{format}/Stadiums`
- **Signature**: `def mlb_v3_scores_stadiums(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Stadium4]`
- **Returns (raw)**: `ApiResult[list[Stadium4], MlbV3ScoresStadiumsErrorBody]`
- **Error**: `MlbV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Stadium4` | `sports_data/models/stadium4.py` |
| `MlbV3ScoresStadiumsErrorBody` | `sports_data/errors/mlb_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_standings

- **Route**: `GET /v3/mlb/scores/{format}/Standings/{season}`
- **Signature**: `def mlb_v3_scores_standings(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Standing]`
- **Returns (raw)**: `ApiResult[list[Standing], MlbV3ScoresStandingsErrorBody]`
- **Error**: `MlbV3ScoresStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Standing` | `sports_data/models/standing.py` |
| `MlbV3ScoresStandingsErrorBody` | `sports_data/errors/mlb_v3_scores_standings_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_game_logs_by_season

- **Route**: `GET /v3/mlb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Signature**: `def mlb_v3_scores_team_game_logs_by_season(format: FormatOrStr, season: str, teamid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `teamid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame2]`
- **Returns (raw)**: `ApiResult[list[TeamGame2], MlbV3ScoresTeamGameLogsBySeasonErrorBody]`
- **Error**: `MlbV3ScoresTeamGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame2` | `sports_data/models/team_game2.py` |
| `MlbV3ScoresTeamGameLogsBySeasonErrorBody` | `sports_data/errors/mlb_v3_scores_team_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_game_stats_by_date_final

- **Route**: `GET /v3/mlb/scores/{format}/TeamGameStatsByDateFinal/{date}`
- **Signature**: `def mlb_v3_scores_team_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame2]`
- **Returns (raw)**: `ApiResult[list[TeamGame2], MlbV3ScoresTeamGameStatsByDateFinalErrorBody]`
- **Error**: `MlbV3ScoresTeamGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame2` | `sports_data/models/team_game2.py` |
| `MlbV3ScoresTeamGameStatsByDateFinalErrorBody` | `sports_data/errors/mlb_v3_scores_team_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_game_stats_by_date_live_final

- **Route**: `GET /v3/mlb/scores/{format}/TeamGameStatsByDate/{date}`
- **Signature**: `def mlb_v3_scores_team_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame2]`
- **Returns (raw)**: `ApiResult[list[TeamGame2], MlbV3ScoresTeamGameStatsByDateLiveFinalErrorBody]`
- **Error**: `MlbV3ScoresTeamGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame2` | `sports_data/models/team_game2.py` |
| `MlbV3ScoresTeamGameStatsByDateLiveFinalErrorBody` | `sports_data/errors/mlb_v3_scores_team_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_profiles_all

- **Route**: `GET /v3/mlb/scores/{format}/AllTeams`
- **Signature**: `def mlb_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team3]`
- **Returns (raw)**: `ApiResult[list[Team3], MlbV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `MlbV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team3` | `sports_data/models/team3.py` |
| `MlbV3ScoresTeamProfilesAllErrorBody` | `sports_data/errors/mlb_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_profiles_by_active

- **Route**: `GET /v3/mlb/scores/{format}/teams`
- **Signature**: `def mlb_v3_scores_team_profiles_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team3]`
- **Returns (raw)**: `ApiResult[list[Team3], MlbV3ScoresTeamProfilesByActiveErrorBody]`
- **Error**: `MlbV3ScoresTeamProfilesByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team3` | `sports_data/models/team3.py` |
| `MlbV3ScoresTeamProfilesByActiveErrorBody` | `sports_data/errors/mlb_v3_scores_team_profiles_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_profiles_by_season

- **Route**: `GET /v3/mlb/scores/{format}/teams/{season}`
- **Signature**: `def mlb_v3_scores_team_profiles_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Team3]`
- **Returns (raw)**: `ApiResult[list[Team3], MlbV3ScoresTeamProfilesBySeasonErrorBody]`
- **Error**: `MlbV3ScoresTeamProfilesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team3` | `sports_data/models/team3.py` |
| `MlbV3ScoresTeamProfilesBySeasonErrorBody` | `sports_data/errors/mlb_v3_scores_team_profiles_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_season_stats

- **Route**: `GET /v3/mlb/scores/{format}/TeamSeasonStats/{season}`
- **Signature**: `def mlb_v3_scores_team_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamSeason2]`
- **Returns (raw)**: `ApiResult[list[TeamSeason2], MlbV3ScoresTeamSeasonStatsErrorBody]`
- **Error**: `MlbV3ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamSeason2` | `sports_data/models/team_season2.py` |
| `MlbV3ScoresTeamSeasonStatsErrorBody` | `sports_data/errors/mlb_v3_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_transactions

- **Route**: `GET /v3/mlb/scores/{format}/TransactionsByDate/{date}`
- **Signature**: `def mlb_v3_scores_transactions(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Transaction]`
- **Returns (raw)**: `ApiResult[list[Transaction], MlbV3ScoresTransactionsErrorBody]`
- **Error**: `MlbV3ScoresTransactionsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Transaction` | `sports_data/models/transaction.py` |
| `MlbV3ScoresTransactionsErrorBody` | `sports_data/errors/mlb_v3_scores_transactions_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

