<!-- Generated file — do not edit; regenerated with the SDK. -->

# NflV3Scores — operations

Accessor: `client.nfl_v3_scores` · Source: `sports_data/apis/nfl_v3_scores.py` · 44 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nfl_v3_scores.nfl_v3_scores_are_games_in_progress

- **Route**: `GET /v3/nfl/scores/{format}/AreAnyGamesInProgress`
- **Signature**: `def nfl_v3_scores_are_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, NflV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `NflV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `NflV3ScoresAreGamesInProgressErrorBody` | `sports_data/errors/nfl_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_bye_weeks

- **Route**: `GET /v3/nfl/scores/{format}/Byes/{season}`
- **Signature**: `def nfl_v3_scores_bye_weeks(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Bye]`
- **Returns (raw)**: `ApiResult[list[Bye], NflV3ScoresByeWeeksErrorBody]`
- **Error**: `NflV3ScoresByeWeeksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Bye` | `sports_data/models/bye.py` |
| `NflV3ScoresByeWeeksErrorBody` | `sports_data/errors/nfl_v3_scores_bye_weeks_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_depth_charts_all

- **Route**: `GET /v3/nfl/scores/{format}/DepthChartsAll`
- **Signature**: `def nfl_v3_scores_depth_charts_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamDepthChart1]`
- **Returns (raw)**: `ApiResult[list[TeamDepthChart1], NflV3ScoresDepthChartsAllErrorBody]`
- **Error**: `NflV3ScoresDepthChartsAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamDepthChart1` | `sports_data/models/team_depth_chart1.py` |
| `NflV3ScoresDepthChartsAllErrorBody` | `sports_data/errors/nfl_v3_scores_depth_charts_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_depth_charts_by_active

- **Route**: `GET /v3/nfl/scores/{format}/DepthCharts`
- **Signature**: `def nfl_v3_scores_depth_charts_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamDepthChart1]`
- **Returns (raw)**: `ApiResult[list[TeamDepthChart1], NflV3ScoresDepthChartsByActiveErrorBody]`
- **Error**: `NflV3ScoresDepthChartsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamDepthChart1` | `sports_data/models/team_depth_chart1.py` |
| `NflV3ScoresDepthChartsByActiveErrorBody` | `sports_data/errors/nfl_v3_scores_depth_charts_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_depth_charts_by_week

- **Route**: `GET /v3/nfl/scores/{format}/DepthChartsByWeek/{season}/{week}`
- **Signature**: `def nfl_v3_scores_depth_charts_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[TeamDepthChartWeekly]`
- **Returns (raw)**: `ApiResult[list[TeamDepthChartWeekly], NflV3ScoresDepthChartsByWeekErrorBody]`
- **Error**: `NflV3ScoresDepthChartsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamDepthChartWeekly` | `sports_data/models/team_depth_chart_weekly.py` |
| `NflV3ScoresDepthChartsByWeekErrorBody` | `sports_data/errors/nfl_v3_scores_depth_charts_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_by_date_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresByDateFinal/{date}`
- **Signature**: `def nfl_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `NflV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Score` | `sports_data/models/score.py` |
| `NflV3ScoresGamesByDateFinalErrorBody` | `sports_data/errors/nfl_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresByDate/{date}`
- **Signature**: `def nfl_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `NflV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Score` | `sports_data/models/score.py` |
| `NflV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data/errors/nfl_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_by_season_live_final

- **Route**: `GET /v3/nfl/scores/{format}/Scores/{season}`
- **Signature**: `def nfl_v3_scores_games_by_season_live_final(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresGamesBySeasonLiveFinalErrorBody]`
- **Error**: `NflV3ScoresGamesBySeasonLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Score` | `sports_data/models/score.py` |
| `NflV3ScoresGamesBySeasonLiveFinalErrorBody` | `sports_data/errors/nfl_v3_scores_games_by_season_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_by_week_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresByWeekFinal/{season}/{week}`
- **Signature**: `def nfl_v3_scores_games_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresGamesByWeekFinalErrorBody]`
- **Error**: `NflV3ScoresGamesByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Score` | `sports_data/models/score.py` |
| `NflV3ScoresGamesByWeekFinalErrorBody` | `sports_data/errors/nfl_v3_scores_games_by_week_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_by_week_live_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresByWeek/{season}/{week}`
- **Signature**: `def nfl_v3_scores_games_by_week_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresGamesByWeekLiveFinalErrorBody]`
- **Error**: `NflV3ScoresGamesByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Score` | `sports_data/models/score.py` |
| `NflV3ScoresGamesByWeekLiveFinalErrorBody` | `sports_data/errors/nfl_v3_scores_games_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_basic_by_week_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresBasicFinal/{season}/{week}`
- **Signature**: `def nfl_v3_scores_games_basic_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[ScoreBasic4]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic4], NflV3ScoresGamesBasicByWeekFinalErrorBody]`
- **Error**: `NflV3ScoresGamesBasicByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic4` | `sports_data/models/score_basic4.py` |
| `NflV3ScoresGamesBasicByWeekFinalErrorBody` | `sports_data/errors/nfl_v3_scores_games_basic_by_week_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_basic_by_week_live_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresBasic/{season}/{week}`
- **Signature**: `def nfl_v3_scores_games_basic_by_week_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[ScoreBasic4]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic4], NflV3ScoresGamesBasicByWeekLiveFinalErrorBody]`
- **Error**: `NflV3ScoresGamesBasicByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic4` | `sports_data/models/score_basic4.py` |
| `NflV3ScoresGamesBasicByWeekLiveFinalErrorBody` | `sports_data/errors/nfl_v3_scores_games_basic_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_news

- **Route**: `GET /v3/nfl/scores/{format}/News`
- **Signature**: `def nfl_v3_scores_news(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], NflV3ScoresNewsErrorBody]`
- **Error**: `NflV3ScoresNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News1` | `sports_data/models/news1.py` |
| `NflV3ScoresNewsErrorBody` | `sports_data/errors/nfl_v3_scores_news_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_news_by_date

- **Route**: `GET /v3/nfl/scores/{format}/NewsByDate/{date}`
- **Signature**: `def nfl_v3_scores_news_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], NflV3ScoresNewsByDateErrorBody]`
- **Error**: `NflV3ScoresNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News1` | `sports_data/models/news1.py` |
| `NflV3ScoresNewsByDateErrorBody` | `sports_data/errors/nfl_v3_scores_news_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_news_by_team

- **Route**: `GET /v3/nfl/scores/{format}/NewsByTeam/{team}`
- **Signature**: `def nfl_v3_scores_news_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], NflV3ScoresNewsByTeamErrorBody]`
- **Error**: `NflV3ScoresNewsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News1` | `sports_data/models/news1.py` |
| `NflV3ScoresNewsByTeamErrorBody` | `sports_data/errors/nfl_v3_scores_news_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_details_all

- **Route**: `GET /v3/nfl/scores/{format}/Players`
- **Signature**: `def nfl_v3_scores_player_details_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player5]`
- **Returns (raw)**: `ApiResult[list[Player5], NflV3ScoresPlayerDetailsAllErrorBody]`
- **Error**: `NflV3ScoresPlayerDetailsAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player5` | `sports_data/models/player5.py` |
| `NflV3ScoresPlayerDetailsAllErrorBody` | `sports_data/errors/nfl_v3_scores_player_details_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_details_by_free_agents

- **Route**: `GET /v3/nfl/scores/{format}/FreeAgents`
- **Signature**: `def nfl_v3_scores_player_details_by_free_agents(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player5]`
- **Returns (raw)**: `ApiResult[list[Player5], NflV3ScoresPlayerDetailsByFreeAgentsErrorBody]`
- **Error**: `NflV3ScoresPlayerDetailsByFreeAgentsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player5` | `sports_data/models/player5.py` |
| `NflV3ScoresPlayerDetailsByFreeAgentsErrorBody` | `sports_data/errors/nfl_v3_scores_player_details_by_free_agents_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_details_by_rookie_draft_year

- **Route**: `GET /v3/nfl/scores/{format}/Rookies/{season}`
- **Signature**: `def nfl_v3_scores_player_details_by_rookie_draft_year(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Player5]`
- **Returns (raw)**: `ApiResult[list[Player5], NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody]`
- **Error**: `NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player5` | `sports_data/models/player5.py` |
| `NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody` | `sports_data/errors/nfl_v3_scores_player_details_by_rookie_draft_year_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_details_by_team

- **Route**: `GET /v3/nfl/scores/{format}/Players/{team}`
- **Signature**: `def nfl_v3_scores_player_details_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[PlayerDetail]`
- **Returns (raw)**: `ApiResult[list[PlayerDetail], NflV3ScoresPlayerDetailsByTeamErrorBody]`
- **Error**: `NflV3ScoresPlayerDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerDetail` | `sports_data/models/player_detail.py` |
| `NflV3ScoresPlayerDetailsByTeamErrorBody` | `sports_data/errors/nfl_v3_scores_player_details_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_game_logs_by_season

- **Route**: `GET /v3/nfl/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Signature**: `def nfl_v3_scores_player_game_logs_by_season(format: FormatOrStr, season: str, teamid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `teamid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame4]`
- **Returns (raw)**: `ApiResult[list[TeamGame4], NflV3ScoresPlayerGameLogsBySeasonErrorBody]`
- **Error**: `NflV3ScoresPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame4` | `sports_data/models/team_game4.py` |
| `NflV3ScoresPlayerGameLogsBySeasonErrorBody` | `sports_data/errors/nfl_v3_scores_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_profiles_all

- **Route**: `GET /v3/nfl/scores/{format}/PlayersByAvailable`
- **Signature**: `def nfl_v3_scores_player_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic4]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic4], NflV3ScoresPlayerProfilesAllErrorBody]`
- **Error**: `NflV3ScoresPlayerProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic4` | `sports_data/models/player_basic4.py` |
| `NflV3ScoresPlayerProfilesAllErrorBody` | `sports_data/errors/nfl_v3_scores_player_profiles_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_profiles_by_free_agent

- **Route**: `GET /v3/nfl/scores/{format}/PlayersByFreeAgents`
- **Signature**: `def nfl_v3_scores_player_profiles_by_free_agent(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic4]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic4], NflV3ScoresPlayerProfilesByFreeAgentErrorBody]`
- **Error**: `NflV3ScoresPlayerProfilesByFreeAgentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic4` | `sports_data/models/player_basic4.py` |
| `NflV3ScoresPlayerProfilesByFreeAgentErrorBody` | `sports_data/errors/nfl_v3_scores_player_profiles_by_free_agent_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_profiles_by_rookie_draft_year

- **Route**: `GET /v3/nfl/scores/{format}/PlayersByRookieDraftYear/{season}`
- **Signature**: `def nfl_v3_scores_player_profiles_by_rookie_draft_year(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerBasic4]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic4], NflV3ScoresPlayerProfilesByRookieDraftYearErrorBody]`
- **Error**: `NflV3ScoresPlayerProfilesByRookieDraftYearErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic4` | `sports_data/models/player_basic4.py` |
| `NflV3ScoresPlayerProfilesByRookieDraftYearErrorBody` | `sports_data/errors/nfl_v3_scores_player_profiles_by_rookie_draft_year_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_profiles_by_team

- **Route**: `GET /v3/nfl/scores/{format}/PlayersBasic/{team}`
- **Signature**: `def nfl_v3_scores_player_profiles_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[PlayerBasic4]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic4], NflV3ScoresPlayerProfilesByTeamErrorBody]`
- **Error**: `NflV3ScoresPlayerProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic4` | `sports_data/models/player_basic4.py` |
| `NflV3ScoresPlayerProfilesByTeamErrorBody` | `sports_data/errors/nfl_v3_scores_player_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_referees

- **Route**: `GET /v3/nfl/scores/{format}/Referees`
- **Signature**: `def nfl_v3_scores_referees(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Referee1]`
- **Returns (raw)**: `ApiResult[list[Referee1], NflV3ScoresRefereesErrorBody]`
- **Error**: `NflV3ScoresRefereesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Referee1` | `sports_data/models/referee1.py` |
| `NflV3ScoresRefereesErrorBody` | `sports_data/errors/nfl_v3_scores_referees_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_schedules

- **Route**: `GET /v3/nfl/scores/{format}/Schedules/{season}`
- **Signature**: `def nfl_v3_scores_schedules(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Schedule]`
- **Returns (raw)**: `ApiResult[list[Schedule], NflV3ScoresSchedulesErrorBody]`
- **Error**: `NflV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Schedule` | `sports_data/models/schedule.py` |
| `NflV3ScoresSchedulesErrorBody` | `sports_data/errors/nfl_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_schedules_basic

- **Route**: `GET /v3/nfl/scores/{format}/SchedulesBasic/{season}`
- **Signature**: `def nfl_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic5]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic5], NflV3ScoresSchedulesBasicErrorBody]`
- **Error**: `NflV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScheduleBasic5` | `sports_data/models/schedule_basic5.py` |
| `NflV3ScoresSchedulesBasicErrorBody` | `sports_data/errors/nfl_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_scores_by_week_simulation

- **Route**: `GET /v3/nfl/scores/{format}/SimulatedScores/{numberofplays}`
- **Signature**: `def nfl_v3_scores_scores_by_week_simulation(format: FormatOrStr, numberofplays: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `numberofplays`
- **Params**: `format` — path · `numberofplays` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresScoresByWeekSimulationErrorBody]`
- **Error**: `NflV3ScoresScoresByWeekSimulationErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Score` | `sports_data/models/score.py` |
| `NflV3ScoresScoresByWeekSimulationErrorBody` | `sports_data/errors/nfl_v3_scores_scores_by_week_simulation_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_season_current

- **Route**: `GET /v3/nfl/scores/{format}/CurrentSeason`
- **Signature**: `def nfl_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresSeasonCurrentErrorBody]`
- **Error**: `NflV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `NflV3ScoresSeasonCurrentErrorBody` | `sports_data/errors/nfl_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_season_last_completed

- **Route**: `GET /v3/nfl/scores/{format}/LastCompletedSeason`
- **Signature**: `def nfl_v3_scores_season_last_completed(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresSeasonLastCompletedErrorBody]`
- **Error**: `NflV3ScoresSeasonLastCompletedErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `NflV3ScoresSeasonLastCompletedErrorBody` | `sports_data/errors/nfl_v3_scores_season_last_completed_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_season_upcoming

- **Route**: `GET /v3/nfl/scores/{format}/UpcomingSeason`
- **Signature**: `def nfl_v3_scores_season_upcoming(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresSeasonUpcomingErrorBody]`
- **Error**: `NflV3ScoresSeasonUpcomingErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `NflV3ScoresSeasonUpcomingErrorBody` | `sports_data/errors/nfl_v3_scores_season_upcoming_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_stadiums

- **Route**: `GET /v3/nfl/scores/{format}/Stadiums`
- **Signature**: `def nfl_v3_scores_stadiums(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Stadium5]`
- **Returns (raw)**: `ApiResult[list[Stadium5], NflV3ScoresStadiumsErrorBody]`
- **Error**: `NflV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Stadium5` | `sports_data/models/stadium5.py` |
| `NflV3ScoresStadiumsErrorBody` | `sports_data/errors/nfl_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_standings

- **Route**: `GET /v3/nfl/scores/{format}/Standings/{season}`
- **Signature**: `def nfl_v3_scores_standings(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Standing2]`
- **Returns (raw)**: `ApiResult[list[Standing2], NflV3ScoresStandingsErrorBody]`
- **Error**: `NflV3ScoresStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Standing2` | `sports_data/models/standing2.py` |
| `NflV3ScoresStandingsErrorBody` | `sports_data/errors/nfl_v3_scores_standings_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_game_stats_live_final

- **Route**: `GET /v3/nfl/scores/{format}/TeamGameStats/{season}/{week}`
- **Signature**: `def nfl_v3_scores_team_game_stats_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[TeamGame4]`
- **Returns (raw)**: `ApiResult[list[TeamGame4], NflV3ScoresTeamGameStatsLiveFinalErrorBody]`
- **Error**: `NflV3ScoresTeamGameStatsLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame4` | `sports_data/models/team_game4.py` |
| `NflV3ScoresTeamGameStatsLiveFinalErrorBody` | `sports_data/errors/nfl_v3_scores_team_game_stats_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_profiles_all

- **Route**: `GET /v3/nfl/scores/{format}/AllTeams`
- **Signature**: `def nfl_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team5]`
- **Returns (raw)**: `ApiResult[list[Team5], NflV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `NflV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team5` | `sports_data/models/team5.py` |
| `NflV3ScoresTeamProfilesAllErrorBody` | `sports_data/errors/nfl_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_profiles_by_active

- **Route**: `GET /v3/nfl/scores/{format}/Teams`
- **Signature**: `def nfl_v3_scores_team_profiles_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team5]`
- **Returns (raw)**: `ApiResult[list[Team5], NflV3ScoresTeamProfilesByActiveErrorBody]`
- **Error**: `NflV3ScoresTeamProfilesByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team5` | `sports_data/models/team5.py` |
| `NflV3ScoresTeamProfilesByActiveErrorBody` | `sports_data/errors/nfl_v3_scores_team_profiles_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_profiles_by_season

- **Route**: `GET /v3/nfl/scores/{format}/Teams/{season}`
- **Signature**: `def nfl_v3_scores_team_profiles_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Team5]`
- **Returns (raw)**: `ApiResult[list[Team5], NflV3ScoresTeamProfilesBySeasonErrorBody]`
- **Error**: `NflV3ScoresTeamProfilesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team5` | `sports_data/models/team5.py` |
| `NflV3ScoresTeamProfilesBySeasonErrorBody` | `sports_data/errors/nfl_v3_scores_team_profiles_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_profiles_basic_all

- **Route**: `GET /v3/nfl/scores/{format}/TeamsBasic`
- **Signature**: `def nfl_v3_scores_team_profiles_basic_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamBasic2]`
- **Returns (raw)**: `ApiResult[list[TeamBasic2], NflV3ScoresTeamProfilesBasicAllErrorBody]`
- **Error**: `NflV3ScoresTeamProfilesBasicAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamBasic2` | `sports_data/models/team_basic2.py` |
| `NflV3ScoresTeamProfilesBasicAllErrorBody` | `sports_data/errors/nfl_v3_scores_team_profiles_basic_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_season_stats

- **Route**: `GET /v3/nfl/scores/{format}/TeamSeasonStats/{season}`
- **Signature**: `def nfl_v3_scores_team_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamSeason4]`
- **Returns (raw)**: `ApiResult[list[TeamSeason4], NflV3ScoresTeamSeasonStatsErrorBody]`
- **Error**: `NflV3ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamSeason4` | `sports_data/models/team_season4.py` |
| `NflV3ScoresTeamSeasonStatsErrorBody` | `sports_data/errors/nfl_v3_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_timeframes

- **Route**: `GET /v3/nfl/scores/{format}/Timeframes/{type}`
- **Signature**: `def nfl_v3_scores_timeframes(format: FormatOrStr, type_: TypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `type_`
- **Params**: `format` — path · `type_` — path `type`
- **Returns (parsed)**: `list[Timeframe]`
- **Returns (raw)**: `ApiResult[list[Timeframe], NflV3ScoresTimeframesErrorBody]`
- **Error**: `NflV3ScoresTimeframesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TypeOrStr` | `sports_data/models/enums/type.py` |
| `Timeframe` | `sports_data/models/timeframe.py` |
| `NflV3ScoresTimeframesErrorBody` | `sports_data/errors/nfl_v3_scores_timeframes_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_transactions_by_date

- **Route**: `GET /v3/nfl/scores/{format}/TransactionsByDate/{date}`
- **Signature**: `def nfl_v3_scores_transactions_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Transaction]`
- **Returns (raw)**: `ApiResult[list[Transaction], NflV3ScoresTransactionsByDateErrorBody]`
- **Error**: `NflV3ScoresTransactionsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Transaction` | `sports_data/models/transaction.py` |
| `NflV3ScoresTransactionsByDateErrorBody` | `sports_data/errors/nfl_v3_scores_transactions_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_week_current

- **Route**: `GET /v3/nfl/scores/{format}/CurrentWeek`
- **Signature**: `def nfl_v3_scores_week_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresWeekCurrentErrorBody]`
- **Error**: `NflV3ScoresWeekCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `NflV3ScoresWeekCurrentErrorBody` | `sports_data/errors/nfl_v3_scores_week_current_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_week_last_completed

- **Route**: `GET /v3/nfl/scores/{format}/LastCompletedWeek`
- **Signature**: `def nfl_v3_scores_week_last_completed(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresWeekLastCompletedErrorBody]`
- **Error**: `NflV3ScoresWeekLastCompletedErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `NflV3ScoresWeekLastCompletedErrorBody` | `sports_data/errors/nfl_v3_scores_week_last_completed_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_week_upcoming

- **Route**: `GET /v3/nfl/scores/{format}/UpcomingWeek`
- **Signature**: `def nfl_v3_scores_week_upcoming(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresWeekUpcomingErrorBody]`
- **Error**: `NflV3ScoresWeekUpcomingErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `NflV3ScoresWeekUpcomingErrorBody` | `sports_data/errors/nfl_v3_scores_week_upcoming_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

