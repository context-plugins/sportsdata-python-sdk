<!-- Generated file — do not edit; regenerated with the SDK. -->

# NhlV3Scores — operations

Accessor: `client.nhl_v3_scores` · Source: `sports_data/apis/nhl_v3_scores.py` · 27 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nhl_v3_scores.nhl_v3_scores_are_games_in_progress

- **Route**: `GET /v3/nhl/scores/{format}/AreAnyGamesInProgress`
- **Signature**: `def nhl_v3_scores_are_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, NhlV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `NhlV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `NhlV3ScoresAreGamesInProgressErrorBody` | `sports_data/errors/nhl_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_depth_charts_goalies

- **Route**: `GET /v3/nhl/scores/{format}/GoalieDepthCharts`
- **Signature**: `def nhl_v3_scores_depth_charts_goalies(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamGoalieDepthChart]`
- **Returns (raw)**: `ApiResult[list[TeamGoalieDepthChart], NhlV3ScoresDepthChartsGoaliesErrorBody]`
- **Error**: `NhlV3ScoresDepthChartsGoaliesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGoalieDepthChart` | `sports_data/models/team_goalie_depth_chart.py` |
| `NhlV3ScoresDepthChartsGoaliesErrorBody` | `sports_data/errors/nhl_v3_scores_depth_charts_goalies_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_games_by_date_final

- **Route**: `GET /v3/nhl/scores/{format}/GamesByDateFinal/{date}`
- **Signature**: `def nhl_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game8]`
- **Returns (raw)**: `ApiResult[list[Game8], NhlV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `NhlV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game8` | `sports_data/models/game8.py` |
| `NhlV3ScoresGamesByDateFinalErrorBody` | `sports_data/errors/nhl_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/nhl/scores/{format}/GamesByDate/{date}`
- **Signature**: `def nhl_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game8]`
- **Returns (raw)**: `ApiResult[list[Game8], NhlV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `NhlV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game8` | `sports_data/models/game8.py` |
| `NhlV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data/errors/nhl_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_games_basic_by_date_final

- **Route**: `GET /v3/nhl/scores/{format}/ScoresBasicFinal/{date}`
- **Signature**: `def nhl_v3_scores_games_basic_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic5]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic5], NhlV3ScoresGamesBasicByDateFinalErrorBody]`
- **Error**: `NhlV3ScoresGamesBasicByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic5` | `sports_data/models/score_basic5.py` |
| `NhlV3ScoresGamesBasicByDateFinalErrorBody` | `sports_data/errors/nhl_v3_scores_games_basic_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_games_basic_by_date_live_final

- **Route**: `GET /v3/nhl/scores/{format}/ScoresBasic/{date}`
- **Signature**: `def nhl_v3_scores_games_basic_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic5]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic5], NhlV3ScoresGamesBasicByDateLiveFinalErrorBody]`
- **Error**: `NhlV3ScoresGamesBasicByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic5` | `sports_data/models/score_basic5.py` |
| `NhlV3ScoresGamesBasicByDateLiveFinalErrorBody` | `sports_data/errors/nhl_v3_scores_games_basic_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_news

- **Route**: `GET /v3/nhl/scores/{format}/News`
- **Signature**: `def nhl_v3_scores_news(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[News2]`
- **Returns (raw)**: `ApiResult[list[News2], NhlV3ScoresNewsErrorBody]`
- **Error**: `NhlV3ScoresNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News2` | `sports_data/models/news2.py` |
| `NhlV3ScoresNewsErrorBody` | `sports_data/errors/nhl_v3_scores_news_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_news_by_date

- **Route**: `GET /v3/nhl/scores/{format}/NewsByDate/{date}`
- **Signature**: `def nhl_v3_scores_news_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[News2]`
- **Returns (raw)**: `ApiResult[list[News2], NhlV3ScoresNewsByDateErrorBody]`
- **Error**: `NhlV3ScoresNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News2` | `sports_data/models/news2.py` |
| `NhlV3ScoresNewsByDateErrorBody` | `sports_data/errors/nhl_v3_scores_news_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_player_details_by_active

- **Route**: `GET /v3/nhl/scores/{format}/Players`
- **Signature**: `def nhl_v3_scores_player_details_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player6]`
- **Returns (raw)**: `ApiResult[list[Player6], NhlV3ScoresPlayerDetailsByActiveErrorBody]`
- **Error**: `NhlV3ScoresPlayerDetailsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player6` | `sports_data/models/player6.py` |
| `NhlV3ScoresPlayerDetailsByActiveErrorBody` | `sports_data/errors/nhl_v3_scores_player_details_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_player_details_by_active2

- **Route**: `GET /v3/nhl/scores/{format}/PlayersByActive`
- **Signature**: `def nhl_v3_scores_player_details_by_active2(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic5]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic5], NhlV3ScoresPlayerDetailsByActive2ErrorBody]`
- **Error**: `NhlV3ScoresPlayerDetailsByActive2ErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic5` | `sports_data/models/player_basic5.py` |
| `NhlV3ScoresPlayerDetailsByActive2ErrorBody` | `sports_data/errors/nhl_v3_scores_player_details_by_active2_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_player_details_by_free_agents

- **Route**: `GET /v3/nhl/scores/{format}/FreeAgents`
- **Signature**: `def nhl_v3_scores_player_details_by_free_agents(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player6]`
- **Returns (raw)**: `ApiResult[list[Player6], NhlV3ScoresPlayerDetailsByFreeAgentsErrorBody]`
- **Error**: `NhlV3ScoresPlayerDetailsByFreeAgentsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player6` | `sports_data/models/player6.py` |
| `NhlV3ScoresPlayerDetailsByFreeAgentsErrorBody` | `sports_data/errors/nhl_v3_scores_player_details_by_free_agents_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_player_details_by_free_agents2

- **Route**: `GET /v3/nhl/scores/{format}/PlayersByFreeAgents`
- **Signature**: `def nhl_v3_scores_player_details_by_free_agents2(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic5]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic5], NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody]`
- **Error**: `NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic5` | `sports_data/models/player_basic5.py` |
| `NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody` | `sports_data/errors/nhl_v3_scores_player_details_by_free_agents2_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_players_details_by_team

- **Route**: `GET /v3/nhl/scores/{format}/Players/{team}`
- **Signature**: `def nhl_v3_scores_players_details_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[Player6]`
- **Returns (raw)**: `ApiResult[list[Player6], NhlV3ScoresPlayersDetailsByTeamErrorBody]`
- **Error**: `NhlV3ScoresPlayersDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player6` | `sports_data/models/player6.py` |
| `NhlV3ScoresPlayersDetailsByTeamErrorBody` | `sports_data/errors/nhl_v3_scores_players_details_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_players_profiles_by_team

- **Route**: `GET /v3/nhl/scores/{format}/PlayersBasic/{team}`
- **Signature**: `def nhl_v3_scores_players_profiles_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[PlayerBasic5]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic5], NhlV3ScoresPlayersProfilesByTeamErrorBody]`
- **Error**: `NhlV3ScoresPlayersProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic5` | `sports_data/models/player_basic5.py` |
| `NhlV3ScoresPlayersProfilesByTeamErrorBody` | `sports_data/errors/nhl_v3_scores_players_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_referees

- **Route**: `GET /v3/nhl/scores/{format}/Referees`
- **Signature**: `def nhl_v3_scores_referees(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Referee]`
- **Returns (raw)**: `ApiResult[list[Referee], NhlV3ScoresRefereesErrorBody]`
- **Error**: `NhlV3ScoresRefereesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Referee` | `sports_data/models/referee.py` |
| `NhlV3ScoresRefereesErrorBody` | `sports_data/errors/nhl_v3_scores_referees_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_schedules

- **Route**: `GET /v3/nhl/scores/{format}/Games/{season}`
- **Signature**: `def nhl_v3_scores_schedules(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Game8]`
- **Returns (raw)**: `ApiResult[list[Game8], NhlV3ScoresSchedulesErrorBody]`
- **Error**: `NhlV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game8` | `sports_data/models/game8.py` |
| `NhlV3ScoresSchedulesErrorBody` | `sports_data/errors/nhl_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_schedules_basic

- **Route**: `GET /v3/nhl/scores/{format}/SchedulesBasic/{season}`
- **Signature**: `def nhl_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic6]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic6], NhlV3ScoresSchedulesBasicErrorBody]`
- **Error**: `NhlV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScheduleBasic6` | `sports_data/models/schedule_basic6.py` |
| `NhlV3ScoresSchedulesBasicErrorBody` | `sports_data/errors/nhl_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_season_current

- **Route**: `GET /v3/nhl/scores/{format}/CurrentSeason`
- **Signature**: `def nhl_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `Season5`
- **Returns (raw)**: `ApiResult[Season5, NhlV3ScoresSeasonCurrentErrorBody]`
- **Error**: `NhlV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Season5` | `sports_data/models/season5.py` |
| `NhlV3ScoresSeasonCurrentErrorBody` | `sports_data/errors/nhl_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_stadiums

- **Route**: `GET /v3/nhl/scores/{format}/Stadiums`
- **Signature**: `def nhl_v3_scores_stadiums(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Stadium]`
- **Returns (raw)**: `ApiResult[list[Stadium], NhlV3ScoresStadiumsErrorBody]`
- **Error**: `NhlV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Stadium` | `sports_data/models/stadium.py` |
| `NhlV3ScoresStadiumsErrorBody` | `sports_data/errors/nhl_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_standings

- **Route**: `GET /v3/nhl/scores/{format}/Standings/{season}`
- **Signature**: `def nhl_v3_scores_standings(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Standing3]`
- **Returns (raw)**: `ApiResult[list[Standing3], NhlV3ScoresStandingsErrorBody]`
- **Error**: `NhlV3ScoresStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Standing3` | `sports_data/models/standing3.py` |
| `NhlV3ScoresStandingsErrorBody` | `sports_data/errors/nhl_v3_scores_standings_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_game_logs_by_season

- **Route**: `GET /v3/nhl/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Signature**: `def nhl_v3_scores_team_game_logs_by_season(format: FormatOrStr, season: str, teamid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `teamid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame5]`
- **Returns (raw)**: `ApiResult[list[TeamGame5], NhlV3ScoresTeamGameLogsBySeasonErrorBody]`
- **Error**: `NhlV3ScoresTeamGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame5` | `sports_data/models/team_game5.py` |
| `NhlV3ScoresTeamGameLogsBySeasonErrorBody` | `sports_data/errors/nhl_v3_scores_team_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_game_stats_by_date_live_final

- **Route**: `GET /v3/nhl/scores/{format}/TeamGameStatsByDate/{date}`
- **Signature**: `def nhl_v3_scores_team_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame5]`
- **Returns (raw)**: `ApiResult[list[TeamGame5], NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody]`
- **Error**: `NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame5` | `sports_data/models/team_game5.py` |
| `NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody` | `sports_data/errors/nhl_v3_scores_team_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_profiles_all

- **Route**: `GET /v3/nhl/scores/{format}/AllTeams`
- **Signature**: `def nhl_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team6]`
- **Returns (raw)**: `ApiResult[list[Team6], NhlV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `NhlV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team6` | `sports_data/models/team6.py` |
| `NhlV3ScoresTeamProfilesAllErrorBody` | `sports_data/errors/nhl_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_profiles_by_active

- **Route**: `GET /v3/nhl/scores/{format}/teams`
- **Signature**: `def nhl_v3_scores_team_profiles_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team6]`
- **Returns (raw)**: `ApiResult[list[Team6], NhlV3ScoresTeamProfilesByActiveErrorBody]`
- **Error**: `NhlV3ScoresTeamProfilesByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team6` | `sports_data/models/team6.py` |
| `NhlV3ScoresTeamProfilesByActiveErrorBody` | `sports_data/errors/nhl_v3_scores_team_profiles_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_profiles_by_season

- **Route**: `GET /v3/nhl/scores/{format}/teams/{season}`
- **Signature**: `def nhl_v3_scores_team_profiles_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Team6]`
- **Returns (raw)**: `ApiResult[list[Team6], NhlV3ScoresTeamProfilesBySeasonErrorBody]`
- **Error**: `NhlV3ScoresTeamProfilesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team6` | `sports_data/models/team6.py` |
| `NhlV3ScoresTeamProfilesBySeasonErrorBody` | `sports_data/errors/nhl_v3_scores_team_profiles_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_season_stats

- **Route**: `GET /v3/nhl/scores/{format}/TeamSeasonStats/{season}`
- **Signature**: `def nhl_v3_scores_team_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamSeason5]`
- **Returns (raw)**: `ApiResult[list[TeamSeason5], NhlV3ScoresTeamSeasonStatsErrorBody]`
- **Error**: `NhlV3ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamSeason5` | `sports_data/models/team_season5.py` |
| `NhlV3ScoresTeamSeasonStatsErrorBody` | `sports_data/errors/nhl_v3_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_transactions

- **Route**: `GET /v3/nhl/scores/{format}/TransactionsByDate/{date}`
- **Signature**: `def nhl_v3_scores_transactions(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Transaction]`
- **Returns (raw)**: `ApiResult[list[Transaction], NhlV3ScoresTransactionsErrorBody]`
- **Error**: `NhlV3ScoresTransactionsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Transaction` | `sports_data/models/transaction.py` |
| `NhlV3ScoresTransactionsErrorBody` | `sports_data/errors/nhl_v3_scores_transactions_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

