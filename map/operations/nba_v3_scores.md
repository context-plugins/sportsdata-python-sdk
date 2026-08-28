<!-- Generated file — do not edit; regenerated with the SDK. -->

# NbaV3Scores — operations

Accessor: `client.nba_v3_scores` · Source: `sports_data/apis/nba_v3_scores.py` · 27 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nba_v3_scores.nba_v3_scores_are_games_in_progress

- **Route**: `GET /v3/nba/scores/{format}/AreAnyGamesInProgress`
- **Signature**: `def nba_v3_scores_are_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, NbaV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `NbaV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `NbaV3ScoresAreGamesInProgressErrorBody` | `sports_data/errors/nba_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_depth_charts

- **Route**: `GET /v3/nba/scores/{format}/DepthCharts`
- **Signature**: `def nba_v3_scores_depth_charts(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamDepthChart]`
- **Returns (raw)**: `ApiResult[list[TeamDepthChart], NbaV3ScoresDepthChartsErrorBody]`
- **Error**: `NbaV3ScoresDepthChartsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamDepthChart` | `sports_data/models/team_depth_chart.py` |
| `NbaV3ScoresDepthChartsErrorBody` | `sports_data/errors/nba_v3_scores_depth_charts_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_games_by_date_final

- **Route**: `GET /v3/nba/scores/{format}/GamesByDateFinal/{date}`
- **Signature**: `def nba_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game7]`
- **Returns (raw)**: `ApiResult[list[Game7], NbaV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `NbaV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game7` | `sports_data/models/game7.py` |
| `NbaV3ScoresGamesByDateFinalErrorBody` | `sports_data/errors/nba_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/nba/scores/{format}/GamesByDate/{date}`
- **Signature**: `def nba_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Game7]`
- **Returns (raw)**: `ApiResult[list[Game7], NbaV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `NbaV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game7` | `sports_data/models/game7.py` |
| `NbaV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data/errors/nba_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_games_basic_by_date_final

- **Route**: `GET /v3/nba/scores/{format}/ScoresBasicFinal/{date}`
- **Signature**: `def nba_v3_scores_games_basic_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic3]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic3], NbaV3ScoresGamesBasicByDateFinalErrorBody]`
- **Error**: `NbaV3ScoresGamesBasicByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic3` | `sports_data/models/score_basic3.py` |
| `NbaV3ScoresGamesBasicByDateFinalErrorBody` | `sports_data/errors/nba_v3_scores_games_basic_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_games_basic_by_date_live_final

- **Route**: `GET /v3/nba/scores/{format}/ScoresBasic/{date}`
- **Signature**: `def nba_v3_scores_games_basic_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic3]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic3], NbaV3ScoresGamesBasicByDateLiveFinalErrorBody]`
- **Error**: `NbaV3ScoresGamesBasicByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic3` | `sports_data/models/score_basic3.py` |
| `NbaV3ScoresGamesBasicByDateLiveFinalErrorBody` | `sports_data/errors/nba_v3_scores_games_basic_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_news

- **Route**: `GET /v3/nba/scores/{format}/News`
- **Signature**: `def nba_v3_scores_news(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], NbaV3ScoresNewsErrorBody]`
- **Error**: `NbaV3ScoresNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News1` | `sports_data/models/news1.py` |
| `NbaV3ScoresNewsErrorBody` | `sports_data/errors/nba_v3_scores_news_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_news_by_date

- **Route**: `GET /v3/nba/scores/{format}/NewsByDate/{date}`
- **Signature**: `def nba_v3_scores_news_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], NbaV3ScoresNewsByDateErrorBody]`
- **Error**: `NbaV3ScoresNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News1` | `sports_data/models/news1.py` |
| `NbaV3ScoresNewsByDateErrorBody` | `sports_data/errors/nba_v3_scores_news_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_player_details_by_active

- **Route**: `GET /v3/nba/scores/{format}/Players`
- **Signature**: `def nba_v3_scores_player_details_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player4]`
- **Returns (raw)**: `ApiResult[list[Player4], NbaV3ScoresPlayerDetailsByActiveErrorBody]`
- **Error**: `NbaV3ScoresPlayerDetailsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player4` | `sports_data/models/player4.py` |
| `NbaV3ScoresPlayerDetailsByActiveErrorBody` | `sports_data/errors/nba_v3_scores_player_details_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_player_details_by_free_agent

- **Route**: `GET /v3/nba/scores/{format}/FreeAgents`
- **Signature**: `def nba_v3_scores_player_details_by_free_agent(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player4]`
- **Returns (raw)**: `ApiResult[list[Player4], NbaV3ScoresPlayerDetailsByFreeAgentErrorBody]`
- **Error**: `NbaV3ScoresPlayerDetailsByFreeAgentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player4` | `sports_data/models/player4.py` |
| `NbaV3ScoresPlayerDetailsByFreeAgentErrorBody` | `sports_data/errors/nba_v3_scores_player_details_by_free_agent_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_player_details_by_team

- **Route**: `GET /v3/nba/scores/{format}/Players/{team}`
- **Signature**: `def nba_v3_scores_player_details_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[Player4]`
- **Returns (raw)**: `ApiResult[list[Player4], NbaV3ScoresPlayerDetailsByTeamErrorBody]`
- **Error**: `NbaV3ScoresPlayerDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player4` | `sports_data/models/player4.py` |
| `NbaV3ScoresPlayerDetailsByTeamErrorBody` | `sports_data/errors/nba_v3_scores_player_details_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_player_profiles_by_active

- **Route**: `GET /v3/nba/scores/{format}/PlayersActiveBasic`
- **Signature**: `def nba_v3_scores_player_profiles_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic3]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic3], NbaV3ScoresPlayerProfilesByActiveErrorBody]`
- **Error**: `NbaV3ScoresPlayerProfilesByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic3` | `sports_data/models/player_basic3.py` |
| `NbaV3ScoresPlayerProfilesByActiveErrorBody` | `sports_data/errors/nba_v3_scores_player_profiles_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_player_profiles_by_free_agent

- **Route**: `GET /v3/nba/scores/{format}/PlayersByFreeAgents`
- **Signature**: `def nba_v3_scores_player_profiles_by_free_agent(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic3]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic3], NbaV3ScoresPlayerProfilesByFreeAgentErrorBody]`
- **Error**: `NbaV3ScoresPlayerProfilesByFreeAgentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic3` | `sports_data/models/player_basic3.py` |
| `NbaV3ScoresPlayerProfilesByFreeAgentErrorBody` | `sports_data/errors/nba_v3_scores_player_profiles_by_free_agent_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_players_profiles_by_team

- **Route**: `GET /v3/nba/scores/{format}/PlayersBasic/{team}`
- **Signature**: `def nba_v3_scores_players_profiles_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[PlayerBasic3]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic3], NbaV3ScoresPlayersProfilesByTeamErrorBody]`
- **Error**: `NbaV3ScoresPlayersProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic3` | `sports_data/models/player_basic3.py` |
| `NbaV3ScoresPlayersProfilesByTeamErrorBody` | `sports_data/errors/nba_v3_scores_players_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_referees

- **Route**: `GET /v3/nba/scores/{format}/Referees`
- **Signature**: `def nba_v3_scores_referees(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Referee]`
- **Returns (raw)**: `ApiResult[list[Referee], NbaV3ScoresRefereesErrorBody]`
- **Error**: `NbaV3ScoresRefereesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Referee` | `sports_data/models/referee.py` |
| `NbaV3ScoresRefereesErrorBody` | `sports_data/errors/nba_v3_scores_referees_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_schedules

- **Route**: `GET /v3/nba/scores/{format}/Games/{season}`
- **Signature**: `def nba_v3_scores_schedules(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Game7]`
- **Returns (raw)**: `ApiResult[list[Game7], NbaV3ScoresSchedulesErrorBody]`
- **Error**: `NbaV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game7` | `sports_data/models/game7.py` |
| `NbaV3ScoresSchedulesErrorBody` | `sports_data/errors/nba_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_schedules_basic

- **Route**: `GET /v3/nba/scores/{format}/SchedulesBasic/{season}`
- **Signature**: `def nba_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic4]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic4], NbaV3ScoresSchedulesBasicErrorBody]`
- **Error**: `NbaV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScheduleBasic4` | `sports_data/models/schedule_basic4.py` |
| `NbaV3ScoresSchedulesBasicErrorBody` | `sports_data/errors/nba_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_season_current

- **Route**: `GET /v3/nba/scores/{format}/CurrentSeason`
- **Signature**: `def nba_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `Season5`
- **Returns (raw)**: `ApiResult[Season5, NbaV3ScoresSeasonCurrentErrorBody]`
- **Error**: `NbaV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Season5` | `sports_data/models/season5.py` |
| `NbaV3ScoresSeasonCurrentErrorBody` | `sports_data/errors/nba_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_stadiums

- **Route**: `GET /v3/nba/scores/{format}/Stadiums`
- **Signature**: `def nba_v3_scores_stadiums(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Stadium]`
- **Returns (raw)**: `ApiResult[list[Stadium], NbaV3ScoresStadiumsErrorBody]`
- **Error**: `NbaV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Stadium` | `sports_data/models/stadium.py` |
| `NbaV3ScoresStadiumsErrorBody` | `sports_data/errors/nba_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_standings

- **Route**: `GET /v3/nba/scores/{format}/Standings/{season}`
- **Signature**: `def nba_v3_scores_standings(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Standing1]`
- **Returns (raw)**: `ApiResult[list[Standing1], NbaV3ScoresStandingsErrorBody]`
- **Error**: `NbaV3ScoresStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Standing1` | `sports_data/models/standing1.py` |
| `NbaV3ScoresStandingsErrorBody` | `sports_data/errors/nba_v3_scores_standings_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_team_game_logs_by_season

- **Route**: `GET /v3/nba/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Signature**: `def nba_v3_scores_team_game_logs_by_season(format: FormatOrStr, season: str, teamid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `teamid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame3]`
- **Returns (raw)**: `ApiResult[list[TeamGame3], NbaV3ScoresTeamGameLogsBySeasonErrorBody]`
- **Error**: `NbaV3ScoresTeamGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame3` | `sports_data/models/team_game3.py` |
| `NbaV3ScoresTeamGameLogsBySeasonErrorBody` | `sports_data/errors/nba_v3_scores_team_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_team_game_stats_by_date_live_final

- **Route**: `GET /v3/nba/scores/{format}/TeamGameStatsByDate/{date}`
- **Signature**: `def nba_v3_scores_team_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame3]`
- **Returns (raw)**: `ApiResult[list[TeamGame3], NbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody]`
- **Error**: `NbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame3` | `sports_data/models/team_game3.py` |
| `NbaV3ScoresTeamGameStatsByDateLiveFinalErrorBody` | `sports_data/errors/nba_v3_scores_team_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_team_profiles_all

- **Route**: `GET /v3/nba/scores/{format}/AllTeams`
- **Signature**: `def nba_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team4]`
- **Returns (raw)**: `ApiResult[list[Team4], NbaV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `NbaV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team4` | `sports_data/models/team4.py` |
| `NbaV3ScoresTeamProfilesAllErrorBody` | `sports_data/errors/nba_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_team_profiles_by_active

- **Route**: `GET /v3/nba/scores/{format}/teams`
- **Signature**: `def nba_v3_scores_team_profiles_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team4]`
- **Returns (raw)**: `ApiResult[list[Team4], NbaV3ScoresTeamProfilesByActiveErrorBody]`
- **Error**: `NbaV3ScoresTeamProfilesByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team4` | `sports_data/models/team4.py` |
| `NbaV3ScoresTeamProfilesByActiveErrorBody` | `sports_data/errors/nba_v3_scores_team_profiles_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_team_profiles_by_season

- **Route**: `GET /v3/nba/scores/{format}/teams/{season}`
- **Signature**: `def nba_v3_scores_team_profiles_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Team4]`
- **Returns (raw)**: `ApiResult[list[Team4], NbaV3ScoresTeamProfilesBySeasonErrorBody]`
- **Error**: `NbaV3ScoresTeamProfilesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team4` | `sports_data/models/team4.py` |
| `NbaV3ScoresTeamProfilesBySeasonErrorBody` | `sports_data/errors/nba_v3_scores_team_profiles_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_team_season_stats

- **Route**: `GET /v3/nba/scores/{format}/TeamSeasonStats/{season}`
- **Signature**: `def nba_v3_scores_team_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamSeason3]`
- **Returns (raw)**: `ApiResult[list[TeamSeason3], NbaV3ScoresTeamSeasonStatsErrorBody]`
- **Error**: `NbaV3ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamSeason3` | `sports_data/models/team_season3.py` |
| `NbaV3ScoresTeamSeasonStatsErrorBody` | `sports_data/errors/nba_v3_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_scores.nba_v3_scores_transactions

- **Route**: `GET /v3/nba/scores/{format}/TransactionsByDate/{date}`
- **Signature**: `def nba_v3_scores_transactions(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Transaction]`
- **Returns (raw)**: `ApiResult[list[Transaction], NbaV3ScoresTransactionsErrorBody]`
- **Error**: `NbaV3ScoresTransactionsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Transaction` | `sports_data/models/transaction.py` |
| `NbaV3ScoresTransactionsErrorBody` | `sports_data/errors/nba_v3_scores_transactions_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

