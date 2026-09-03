<!-- Generated file — do not edit; regenerated with the SDK. -->

# NflV3Scores — operations

Accessor: `client.nfl_v3_scores` · Source: `sports_data_io/apis/nfl_v3_scores.py` · 44 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nfl_v3_scores.nfl_v3_scores_are_games_in_progress

- **Route**: `GET /v3/nfl/scores/{format}/AreAnyGamesInProgress`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_are_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, NflV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `NflV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `NflV3ScoresAreGamesInProgressErrorBody` | `sports_data_io/errors/nfl_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_bye_weeks

- **Route**: `GET /v3/nfl/scores/{format}/Byes/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_bye_weeks(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Bye]`
- **Returns (raw)**: `ApiResult[list[Bye], NflV3ScoresByeWeeksErrorBody]`
- **Error**: `NflV3ScoresByeWeeksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Bye` | `sports_data_io/models/bye.py` |
| `NflV3ScoresByeWeeksErrorBody` | `sports_data_io/errors/nfl_v3_scores_bye_weeks_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_depth_charts_all

- **Route**: `GET /v3/nfl/scores/{format}/DepthChartsAll`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_depth_charts_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamDepthChart]`
- **Returns (raw)**: `ApiResult[list[TeamDepthChart], NflV3ScoresDepthChartsAllErrorBody]`
- **Error**: `NflV3ScoresDepthChartsAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamDepthChart` | `sports_data_io/models/team_depth_chart.py` |
| `NflV3ScoresDepthChartsAllErrorBody` | `sports_data_io/errors/nfl_v3_scores_depth_charts_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_depth_charts_by_active

- **Route**: `GET /v3/nfl/scores/{format}/DepthCharts`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_depth_charts_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamDepthChart]`
- **Returns (raw)**: `ApiResult[list[TeamDepthChart], NflV3ScoresDepthChartsByActiveErrorBody]`
- **Error**: `NflV3ScoresDepthChartsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamDepthChart` | `sports_data_io/models/team_depth_chart.py` |
| `NflV3ScoresDepthChartsByActiveErrorBody` | `sports_data_io/errors/nfl_v3_scores_depth_charts_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_depth_charts_by_week

- **Route**: `GET /v3/nfl/scores/{format}/DepthChartsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_depth_charts_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[TeamDepthChartWeekly]`
- **Returns (raw)**: `ApiResult[list[TeamDepthChartWeekly], NflV3ScoresDepthChartsByWeekErrorBody]`
- **Error**: `NflV3ScoresDepthChartsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamDepthChartWeekly` | `sports_data_io/models/team_depth_chart_weekly.py` |
| `NflV3ScoresDepthChartsByWeekErrorBody` | `sports_data_io/errors/nfl_v3_scores_depth_charts_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_by_date_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `NflV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Score` | `sports_data_io/models/score.py` |
| `NflV3ScoresGamesByDateFinalErrorBody` | `sports_data_io/errors/nfl_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `NflV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Score` | `sports_data_io/models/score.py` |
| `NflV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_by_season_live_final

- **Route**: `GET /v3/nfl/scores/{format}/Scores/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_games_by_season_live_final(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresGamesBySeasonLiveFinalErrorBody]`
- **Error**: `NflV3ScoresGamesBySeasonLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Score` | `sports_data_io/models/score.py` |
| `NflV3ScoresGamesBySeasonLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_scores_games_by_season_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_by_week_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresByWeekFinal/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_games_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresGamesByWeekFinalErrorBody]`
- **Error**: `NflV3ScoresGamesByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Score` | `sports_data_io/models/score.py` |
| `NflV3ScoresGamesByWeekFinalErrorBody` | `sports_data_io/errors/nfl_v3_scores_games_by_week_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_by_week_live_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_games_by_week_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresGamesByWeekLiveFinalErrorBody]`
- **Error**: `NflV3ScoresGamesByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Score` | `sports_data_io/models/score.py` |
| `NflV3ScoresGamesByWeekLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_scores_games_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_basic_by_week_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresBasicFinal/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_games_basic_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[ScoreBasic]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic], NflV3ScoresGamesBasicByWeekFinalErrorBody]`
- **Error**: `NflV3ScoresGamesBasicByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic` | `sports_data_io/models/score_basic.py` |
| `NflV3ScoresGamesBasicByWeekFinalErrorBody` | `sports_data_io/errors/nfl_v3_scores_games_basic_by_week_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_games_basic_by_week_live_final

- **Route**: `GET /v3/nfl/scores/{format}/ScoresBasic/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_games_basic_by_week_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[ScoreBasic]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic], NflV3ScoresGamesBasicByWeekLiveFinalErrorBody]`
- **Error**: `NflV3ScoresGamesBasicByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic` | `sports_data_io/models/score_basic.py` |
| `NflV3ScoresGamesBasicByWeekLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_scores_games_basic_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_news

- **Route**: `GET /v3/nfl/scores/{format}/News`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_news(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[News]`
- **Returns (raw)**: `ApiResult[list[News], NflV3ScoresNewsErrorBody]`
- **Error**: `NflV3ScoresNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News` | `sports_data_io/models/news.py` |
| `NflV3ScoresNewsErrorBody` | `sports_data_io/errors/nfl_v3_scores_news_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_news_by_date

- **Route**: `GET /v3/nfl/scores/{format}/NewsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_news_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[News]`
- **Returns (raw)**: `ApiResult[list[News], NflV3ScoresNewsByDateErrorBody]`
- **Error**: `NflV3ScoresNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News` | `sports_data_io/models/news.py` |
| `NflV3ScoresNewsByDateErrorBody` | `sports_data_io/errors/nfl_v3_scores_news_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_news_by_team

- **Route**: `GET /v3/nfl/scores/{format}/NewsByTeam/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_news_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[News]`
- **Returns (raw)**: `ApiResult[list[News], NflV3ScoresNewsByTeamErrorBody]`
- **Error**: `NflV3ScoresNewsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News` | `sports_data_io/models/news.py` |
| `NflV3ScoresNewsByTeamErrorBody` | `sports_data_io/errors/nfl_v3_scores_news_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_details_all

- **Route**: `GET /v3/nfl/scores/{format}/Players`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_player_details_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player]`
- **Returns (raw)**: `ApiResult[list[Player], NflV3ScoresPlayerDetailsAllErrorBody]`
- **Error**: `NflV3ScoresPlayerDetailsAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player` | `sports_data_io/models/player.py` |
| `NflV3ScoresPlayerDetailsAllErrorBody` | `sports_data_io/errors/nfl_v3_scores_player_details_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_details_by_free_agents

- **Route**: `GET /v3/nfl/scores/{format}/FreeAgents`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_player_details_by_free_agents(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player]`
- **Returns (raw)**: `ApiResult[list[Player], NflV3ScoresPlayerDetailsByFreeAgentsErrorBody]`
- **Error**: `NflV3ScoresPlayerDetailsByFreeAgentsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player` | `sports_data_io/models/player.py` |
| `NflV3ScoresPlayerDetailsByFreeAgentsErrorBody` | `sports_data_io/errors/nfl_v3_scores_player_details_by_free_agents_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_details_by_rookie_draft_year

- **Route**: `GET /v3/nfl/scores/{format}/Rookies/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_player_details_by_rookie_draft_year(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Player]`
- **Returns (raw)**: `ApiResult[list[Player], NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody]`
- **Error**: `NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player` | `sports_data_io/models/player.py` |
| `NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody` | `sports_data_io/errors/nfl_v3_scores_player_details_by_rookie_draft_year_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_details_by_team

- **Route**: `GET /v3/nfl/scores/{format}/Players/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_player_details_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[PlayerDetail]`
- **Returns (raw)**: `ApiResult[list[PlayerDetail], NflV3ScoresPlayerDetailsByTeamErrorBody]`
- **Error**: `NflV3ScoresPlayerDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerDetail` | `sports_data_io/models/player_detail.py` |
| `NflV3ScoresPlayerDetailsByTeamErrorBody` | `sports_data_io/errors/nfl_v3_scores_player_details_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_game_logs_by_season

- **Route**: `GET /v3/nfl/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_player_game_logs_by_season(format: FormatOrStr, season: str, teamid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `teamid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame]`
- **Returns (raw)**: `ApiResult[list[TeamGame], NflV3ScoresPlayerGameLogsBySeasonErrorBody]`
- **Error**: `NflV3ScoresPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame` | `sports_data_io/models/team_game.py` |
| `NflV3ScoresPlayerGameLogsBySeasonErrorBody` | `sports_data_io/errors/nfl_v3_scores_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_profiles_all

- **Route**: `GET /v3/nfl/scores/{format}/PlayersByAvailable`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_player_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesAllErrorBody]`
- **Error**: `NflV3ScoresPlayerProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic` | `sports_data_io/models/player_basic.py` |
| `NflV3ScoresPlayerProfilesAllErrorBody` | `sports_data_io/errors/nfl_v3_scores_player_profiles_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_profiles_by_free_agent

- **Route**: `GET /v3/nfl/scores/{format}/PlayersByFreeAgents`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_player_profiles_by_free_agent(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[PlayerBasic]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesByFreeAgentErrorBody]`
- **Error**: `NflV3ScoresPlayerProfilesByFreeAgentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic` | `sports_data_io/models/player_basic.py` |
| `NflV3ScoresPlayerProfilesByFreeAgentErrorBody` | `sports_data_io/errors/nfl_v3_scores_player_profiles_by_free_agent_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_profiles_by_rookie_draft_year

- **Route**: `GET /v3/nfl/scores/{format}/PlayersByRookieDraftYear/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_player_profiles_by_rookie_draft_year(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerBasic]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesByRookieDraftYearErrorBody]`
- **Error**: `NflV3ScoresPlayerProfilesByRookieDraftYearErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic` | `sports_data_io/models/player_basic.py` |
| `NflV3ScoresPlayerProfilesByRookieDraftYearErrorBody` | `sports_data_io/errors/nfl_v3_scores_player_profiles_by_rookie_draft_year_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_player_profiles_by_team

- **Route**: `GET /v3/nfl/scores/{format}/PlayersBasic/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_player_profiles_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[PlayerBasic]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic], NflV3ScoresPlayerProfilesByTeamErrorBody]`
- **Error**: `NflV3ScoresPlayerProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic` | `sports_data_io/models/player_basic.py` |
| `NflV3ScoresPlayerProfilesByTeamErrorBody` | `sports_data_io/errors/nfl_v3_scores_player_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_referees

- **Route**: `GET /v3/nfl/scores/{format}/Referees`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_referees(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Referee]`
- **Returns (raw)**: `ApiResult[list[Referee], NflV3ScoresRefereesErrorBody]`
- **Error**: `NflV3ScoresRefereesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Referee` | `sports_data_io/models/referee.py` |
| `NflV3ScoresRefereesErrorBody` | `sports_data_io/errors/nfl_v3_scores_referees_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_schedules

- **Route**: `GET /v3/nfl/scores/{format}/Schedules/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_schedules(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Schedule]`
- **Returns (raw)**: `ApiResult[list[Schedule], NflV3ScoresSchedulesErrorBody]`
- **Error**: `NflV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Schedule` | `sports_data_io/models/schedule.py` |
| `NflV3ScoresSchedulesErrorBody` | `sports_data_io/errors/nfl_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_schedules_basic

- **Route**: `GET /v3/nfl/scores/{format}/SchedulesBasic/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic], NflV3ScoresSchedulesBasicErrorBody]`
- **Error**: `NflV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScheduleBasic` | `sports_data_io/models/schedule_basic.py` |
| `NflV3ScoresSchedulesBasicErrorBody` | `sports_data_io/errors/nfl_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_scores_by_week_simulation

- **Route**: `GET /v3/nfl/scores/{format}/SimulatedScores/{numberofplays}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_scores_by_week_simulation(format: FormatOrStr, numberofplays: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `numberofplays`
- **Params**: `format` — path · `numberofplays` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3ScoresScoresByWeekSimulationErrorBody]`
- **Error**: `NflV3ScoresScoresByWeekSimulationErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Score` | `sports_data_io/models/score.py` |
| `NflV3ScoresScoresByWeekSimulationErrorBody` | `sports_data_io/errors/nfl_v3_scores_scores_by_week_simulation_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_season_current

- **Route**: `GET /v3/nfl/scores/{format}/CurrentSeason`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresSeasonCurrentErrorBody]`
- **Error**: `NflV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `NflV3ScoresSeasonCurrentErrorBody` | `sports_data_io/errors/nfl_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_season_last_completed

- **Route**: `GET /v3/nfl/scores/{format}/LastCompletedSeason`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_season_last_completed(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresSeasonLastCompletedErrorBody]`
- **Error**: `NflV3ScoresSeasonLastCompletedErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `NflV3ScoresSeasonLastCompletedErrorBody` | `sports_data_io/errors/nfl_v3_scores_season_last_completed_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_season_upcoming

- **Route**: `GET /v3/nfl/scores/{format}/UpcomingSeason`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_season_upcoming(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresSeasonUpcomingErrorBody]`
- **Error**: `NflV3ScoresSeasonUpcomingErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `NflV3ScoresSeasonUpcomingErrorBody` | `sports_data_io/errors/nfl_v3_scores_season_upcoming_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_stadiums

- **Route**: `GET /v3/nfl/scores/{format}/Stadiums`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_stadiums(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Stadium]`
- **Returns (raw)**: `ApiResult[list[Stadium], NflV3ScoresStadiumsErrorBody]`
- **Error**: `NflV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Stadium` | `sports_data_io/models/stadium.py` |
| `NflV3ScoresStadiumsErrorBody` | `sports_data_io/errors/nfl_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_standings

- **Route**: `GET /v3/nfl/scores/{format}/Standings/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_standings(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Standing]`
- **Returns (raw)**: `ApiResult[list[Standing], NflV3ScoresStandingsErrorBody]`
- **Error**: `NflV3ScoresStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Standing` | `sports_data_io/models/standing.py` |
| `NflV3ScoresStandingsErrorBody` | `sports_data_io/errors/nfl_v3_scores_standings_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_game_stats_live_final

- **Route**: `GET /v3/nfl/scores/{format}/TeamGameStats/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_team_game_stats_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[TeamGame]`
- **Returns (raw)**: `ApiResult[list[TeamGame], NflV3ScoresTeamGameStatsLiveFinalErrorBody]`
- **Error**: `NflV3ScoresTeamGameStatsLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame` | `sports_data_io/models/team_game.py` |
| `NflV3ScoresTeamGameStatsLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_scores_team_game_stats_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_profiles_all

- **Route**: `GET /v3/nfl/scores/{format}/AllTeams`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team]`
- **Returns (raw)**: `ApiResult[list[Team], NflV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `NflV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team` | `sports_data_io/models/team.py` |
| `NflV3ScoresTeamProfilesAllErrorBody` | `sports_data_io/errors/nfl_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_profiles_by_active

- **Route**: `GET /v3/nfl/scores/{format}/Teams`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_team_profiles_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Team]`
- **Returns (raw)**: `ApiResult[list[Team], NflV3ScoresTeamProfilesByActiveErrorBody]`
- **Error**: `NflV3ScoresTeamProfilesByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team` | `sports_data_io/models/team.py` |
| `NflV3ScoresTeamProfilesByActiveErrorBody` | `sports_data_io/errors/nfl_v3_scores_team_profiles_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_profiles_by_season

- **Route**: `GET /v3/nfl/scores/{format}/Teams/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_team_profiles_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Team]`
- **Returns (raw)**: `ApiResult[list[Team], NflV3ScoresTeamProfilesBySeasonErrorBody]`
- **Error**: `NflV3ScoresTeamProfilesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team` | `sports_data_io/models/team.py` |
| `NflV3ScoresTeamProfilesBySeasonErrorBody` | `sports_data_io/errors/nfl_v3_scores_team_profiles_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_profiles_basic_all

- **Route**: `GET /v3/nfl/scores/{format}/TeamsBasic`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_team_profiles_basic_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[TeamBasic]`
- **Returns (raw)**: `ApiResult[list[TeamBasic], NflV3ScoresTeamProfilesBasicAllErrorBody]`
- **Error**: `NflV3ScoresTeamProfilesBasicAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamBasic` | `sports_data_io/models/team_basic.py` |
| `NflV3ScoresTeamProfilesBasicAllErrorBody` | `sports_data_io/errors/nfl_v3_scores_team_profiles_basic_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_team_season_stats

- **Route**: `GET /v3/nfl/scores/{format}/TeamSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_team_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamSeason]`
- **Returns (raw)**: `ApiResult[list[TeamSeason], NflV3ScoresTeamSeasonStatsErrorBody]`
- **Error**: `NflV3ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamSeason` | `sports_data_io/models/team_season.py` |
| `NflV3ScoresTeamSeasonStatsErrorBody` | `sports_data_io/errors/nfl_v3_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_timeframes

- **Route**: `GET /v3/nfl/scores/{format}/Timeframes/{type}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_timeframes(format: FormatOrStr, type_: TypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `type_`
- **Params**: `format` — path · `type_` — path `type`
- **Returns (parsed)**: `list[Timeframe]`
- **Returns (raw)**: `ApiResult[list[Timeframe], NflV3ScoresTimeframesErrorBody]`
- **Error**: `NflV3ScoresTimeframesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TypeOrStr` | `sports_data_io/models/enums/type.py` |
| `Timeframe` | `sports_data_io/models/timeframe.py` |
| `NflV3ScoresTimeframesErrorBody` | `sports_data_io/errors/nfl_v3_scores_timeframes_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_transactions_by_date

- **Route**: `GET /v3/nfl/scores/{format}/TransactionsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_transactions_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[Transaction]`
- **Returns (raw)**: `ApiResult[list[Transaction], NflV3ScoresTransactionsByDateErrorBody]`
- **Error**: `NflV3ScoresTransactionsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Transaction` | `sports_data_io/models/transaction.py` |
| `NflV3ScoresTransactionsByDateErrorBody` | `sports_data_io/errors/nfl_v3_scores_transactions_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_week_current

- **Route**: `GET /v3/nfl/scores/{format}/CurrentWeek`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_week_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresWeekCurrentErrorBody]`
- **Error**: `NflV3ScoresWeekCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `NflV3ScoresWeekCurrentErrorBody` | `sports_data_io/errors/nfl_v3_scores_week_current_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_week_last_completed

- **Route**: `GET /v3/nfl/scores/{format}/LastCompletedWeek`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_week_last_completed(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresWeekLastCompletedErrorBody]`
- **Error**: `NflV3ScoresWeekLastCompletedErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `NflV3ScoresWeekLastCompletedErrorBody` | `sports_data_io/errors/nfl_v3_scores_week_last_completed_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_scores.nfl_v3_scores_week_upcoming

- **Route**: `GET /v3/nfl/scores/{format}/UpcomingWeek`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_scores_week_upcoming(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `int | None`
- **Returns (raw)**: `ApiResult[int | None, NflV3ScoresWeekUpcomingErrorBody]`
- **Error**: `NflV3ScoresWeekUpcomingErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `NflV3ScoresWeekUpcomingErrorBody` | `sports_data_io/errors/nfl_v3_scores_week_upcoming_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

