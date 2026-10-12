<!-- Generated file — do not edit; regenerated with the SDK. -->

# NhlV3Scores — operations

Accessor: `client.nhl_v3_scores` · Source: `sports_data_io/apis/nhl_v3_scores.py` · 27 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nhl_v3_scores.nhl_v3_scores_are_games_in_progress

- **Route**: `GET /v3/nhl/scores/{format}/AreAnyGamesInProgress`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_are_games_in_progress(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, NhlV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `NhlV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `NhlV3ScoresAreGamesInProgressErrorBody` | `sports_data_io/errors/nhl_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_depth_charts_goalies

- **Route**: `GET /v3/nhl/scores/{format}/GoalieDepthCharts`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_depth_charts_goalies(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[TeamGoalieDepthChart]`
- **Returns (raw)**: `ApiResult[list[TeamGoalieDepthChart], NhlV3ScoresDepthChartsGoaliesErrorBody]`
- **Error**: `NhlV3ScoresDepthChartsGoaliesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGoalieDepthChart` | `sports_data_io/models/team_goalie_depth_chart.py` |
| `NhlV3ScoresDepthChartsGoaliesErrorBody` | `sports_data_io/errors/nhl_v3_scores_depth_charts_goalies_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_games_by_date_final

- **Route**: `GET /v3/nhl/scores/{format}/GamesByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_games_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[Game7]`
- **Returns (raw)**: `ApiResult[list[Game7], NhlV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `NhlV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game7` | `sports_data_io/models/game7.py` |
| `NhlV3ScoresGamesByDateFinalErrorBody` | `sports_data_io/errors/nhl_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/nhl/scores/{format}/GamesByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_games_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[Game7]`
- **Returns (raw)**: `ApiResult[list[Game7], NhlV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `NhlV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game7` | `sports_data_io/models/game7.py` |
| `NhlV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data_io/errors/nhl_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_games_basic_by_date_final

- **Route**: `GET /v3/nhl/scores/{format}/ScoresBasicFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_games_basic_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[ScoreBasic3]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic3], NhlV3ScoresGamesBasicByDateFinalErrorBody]`
- **Error**: `NhlV3ScoresGamesBasicByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic3` | `sports_data_io/models/score_basic3.py` |
| `NhlV3ScoresGamesBasicByDateFinalErrorBody` | `sports_data_io/errors/nhl_v3_scores_games_basic_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_games_basic_by_date_live_final

- **Route**: `GET /v3/nhl/scores/{format}/ScoresBasic/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_games_basic_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[ScoreBasic3]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic3], NhlV3ScoresGamesBasicByDateLiveFinalErrorBody]`
- **Error**: `NhlV3ScoresGamesBasicByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic3` | `sports_data_io/models/score_basic3.py` |
| `NhlV3ScoresGamesBasicByDateLiveFinalErrorBody` | `sports_data_io/errors/nhl_v3_scores_games_basic_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_news

- **Route**: `GET /v3/nhl/scores/{format}/News`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_news(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], NhlV3ScoresNewsErrorBody]`
- **Error**: `NhlV3ScoresNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News1` | `sports_data_io/models/news1.py` |
| `NhlV3ScoresNewsErrorBody` | `sports_data_io/errors/nhl_v3_scores_news_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_news_by_date

- **Route**: `GET /v3/nhl/scores/{format}/NewsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_news_by_date(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], NhlV3ScoresNewsByDateErrorBody]`
- **Error**: `NhlV3ScoresNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News1` | `sports_data_io/models/news1.py` |
| `NhlV3ScoresNewsByDateErrorBody` | `sports_data_io/errors/nhl_v3_scores_news_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_player_details_by_active

- **Route**: `GET /v3/nhl/scores/{format}/Players`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_player_details_by_active(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Player3]`
- **Returns (raw)**: `ApiResult[list[Player3], NhlV3ScoresPlayerDetailsByActiveErrorBody]`
- **Error**: `NhlV3ScoresPlayerDetailsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player3` | `sports_data_io/models/player3.py` |
| `NhlV3ScoresPlayerDetailsByActiveErrorBody` | `sports_data_io/errors/nhl_v3_scores_player_details_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_player_details_by_active2

- **Route**: `GET /v3/nhl/scores/{format}/PlayersByActive`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_player_details_by_active2(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[PlayerBasic3]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic3], NhlV3ScoresPlayerDetailsByActive2ErrorBody]`
- **Error**: `NhlV3ScoresPlayerDetailsByActive2ErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic3` | `sports_data_io/models/player_basic3.py` |
| `NhlV3ScoresPlayerDetailsByActive2ErrorBody` | `sports_data_io/errors/nhl_v3_scores_player_details_by_active2_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_player_details_by_free_agents

- **Route**: `GET /v3/nhl/scores/{format}/FreeAgents`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_player_details_by_free_agents(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Player3]`
- **Returns (raw)**: `ApiResult[list[Player3], NhlV3ScoresPlayerDetailsByFreeAgentsErrorBody]`
- **Error**: `NhlV3ScoresPlayerDetailsByFreeAgentsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player3` | `sports_data_io/models/player3.py` |
| `NhlV3ScoresPlayerDetailsByFreeAgentsErrorBody` | `sports_data_io/errors/nhl_v3_scores_player_details_by_free_agents_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_player_details_by_free_agents2

- **Route**: `GET /v3/nhl/scores/{format}/PlayersByFreeAgents`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_player_details_by_free_agents2(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[PlayerBasic3]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic3], NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody]`
- **Error**: `NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic3` | `sports_data_io/models/player_basic3.py` |
| `NhlV3ScoresPlayerDetailsByFreeAgents2ErrorBody` | `sports_data_io/errors/nhl_v3_scores_player_details_by_free_agents2_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_players_details_by_team

- **Route**: `GET /v3/nhl/scores/{format}/Players/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_players_details_by_team(team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`
- **Params**: `format_` — path `format` · `team` — path
- **Returns (parsed)**: `list[Player3]`
- **Returns (raw)**: `ApiResult[list[Player3], NhlV3ScoresPlayersDetailsByTeamErrorBody]`
- **Error**: `NhlV3ScoresPlayersDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player3` | `sports_data_io/models/player3.py` |
| `NhlV3ScoresPlayersDetailsByTeamErrorBody` | `sports_data_io/errors/nhl_v3_scores_players_details_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_players_profiles_by_team

- **Route**: `GET /v3/nhl/scores/{format}/PlayersBasic/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_players_profiles_by_team(team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`
- **Params**: `format_` — path `format` · `team` — path
- **Returns (parsed)**: `list[PlayerBasic3]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic3], NhlV3ScoresPlayersProfilesByTeamErrorBody]`
- **Error**: `NhlV3ScoresPlayersProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic3` | `sports_data_io/models/player_basic3.py` |
| `NhlV3ScoresPlayersProfilesByTeamErrorBody` | `sports_data_io/errors/nhl_v3_scores_players_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_referees

- **Route**: `GET /v3/nhl/scores/{format}/Referees`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_referees(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Referee1]`
- **Returns (raw)**: `ApiResult[list[Referee1], NhlV3ScoresRefereesErrorBody]`
- **Error**: `NhlV3ScoresRefereesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Referee1` | `sports_data_io/models/referee1.py` |
| `NhlV3ScoresRefereesErrorBody` | `sports_data_io/errors/nhl_v3_scores_referees_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_schedules

- **Route**: `GET /v3/nhl/scores/{format}/Games/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_schedules(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[Game7]`
- **Returns (raw)**: `ApiResult[list[Game7], NhlV3ScoresSchedulesErrorBody]`
- **Error**: `NhlV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game7` | `sports_data_io/models/game7.py` |
| `NhlV3ScoresSchedulesErrorBody` | `sports_data_io/errors/nhl_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_schedules_basic

- **Route**: `GET /v3/nhl/scores/{format}/SchedulesBasic/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_schedules_basic(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic3]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic3], NhlV3ScoresSchedulesBasicErrorBody]`
- **Error**: `NhlV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScheduleBasic3` | `sports_data_io/models/schedule_basic3.py` |
| `NhlV3ScoresSchedulesBasicErrorBody` | `sports_data_io/errors/nhl_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_season_current

- **Route**: `GET /v3/nhl/scores/{format}/CurrentSeason`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_season_current(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `Season`
- **Returns (raw)**: `ApiResult[Season, NhlV3ScoresSeasonCurrentErrorBody]`
- **Error**: `NhlV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Season` | `sports_data_io/models/season.py` |
| `NhlV3ScoresSeasonCurrentErrorBody` | `sports_data_io/errors/nhl_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_stadiums

- **Route**: `GET /v3/nhl/scores/{format}/Stadiums`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_stadiums(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Stadium1]`
- **Returns (raw)**: `ApiResult[list[Stadium1], NhlV3ScoresStadiumsErrorBody]`
- **Error**: `NhlV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Stadium1` | `sports_data_io/models/stadium1.py` |
| `NhlV3ScoresStadiumsErrorBody` | `sports_data_io/errors/nhl_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_standings

- **Route**: `GET /v3/nhl/scores/{format}/Standings/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_standings(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[Standing3]`
- **Returns (raw)**: `ApiResult[list[Standing3], NhlV3ScoresStandingsErrorBody]`
- **Error**: `NhlV3ScoresStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Standing3` | `sports_data_io/models/standing3.py` |
| `NhlV3ScoresStandingsErrorBody` | `sports_data_io/errors/nhl_v3_scores_standings_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_game_logs_by_season

- **Route**: `GET /v3/nhl/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_team_game_logs_by_season(season: str, teamid: str, numberofgames: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `teamid`, `numberofgames`
- **Params**: `format_` — path `format` · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame3]`
- **Returns (raw)**: `ApiResult[list[TeamGame3], NhlV3ScoresTeamGameLogsBySeasonErrorBody]`
- **Error**: `NhlV3ScoresTeamGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame3` | `sports_data_io/models/team_game3.py` |
| `NhlV3ScoresTeamGameLogsBySeasonErrorBody` | `sports_data_io/errors/nhl_v3_scores_team_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_game_stats_by_date_live_final

- **Route**: `GET /v3/nhl/scores/{format}/TeamGameStatsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_team_game_stats_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[TeamGame3]`
- **Returns (raw)**: `ApiResult[list[TeamGame3], NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody]`
- **Error**: `NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame3` | `sports_data_io/models/team_game3.py` |
| `NhlV3ScoresTeamGameStatsByDateLiveFinalErrorBody` | `sports_data_io/errors/nhl_v3_scores_team_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_profiles_all

- **Route**: `GET /v3/nhl/scores/{format}/AllTeams`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_team_profiles_all(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Team3]`
- **Returns (raw)**: `ApiResult[list[Team3], NhlV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `NhlV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team3` | `sports_data_io/models/team3.py` |
| `NhlV3ScoresTeamProfilesAllErrorBody` | `sports_data_io/errors/nhl_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_profiles_by_active

- **Route**: `GET /v3/nhl/scores/{format}/teams`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_team_profiles_by_active(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Team3]`
- **Returns (raw)**: `ApiResult[list[Team3], NhlV3ScoresTeamProfilesByActiveErrorBody]`
- **Error**: `NhlV3ScoresTeamProfilesByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team3` | `sports_data_io/models/team3.py` |
| `NhlV3ScoresTeamProfilesByActiveErrorBody` | `sports_data_io/errors/nhl_v3_scores_team_profiles_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_profiles_by_season

- **Route**: `GET /v3/nhl/scores/{format}/teams/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_team_profiles_by_season(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[Team3]`
- **Returns (raw)**: `ApiResult[list[Team3], NhlV3ScoresTeamProfilesBySeasonErrorBody]`
- **Error**: `NhlV3ScoresTeamProfilesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team3` | `sports_data_io/models/team3.py` |
| `NhlV3ScoresTeamProfilesBySeasonErrorBody` | `sports_data_io/errors/nhl_v3_scores_team_profiles_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_team_season_stats

- **Route**: `GET /v3/nhl/scores/{format}/TeamSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_team_season_stats(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[TeamSeason3]`
- **Returns (raw)**: `ApiResult[list[TeamSeason3], NhlV3ScoresTeamSeasonStatsErrorBody]`
- **Error**: `NhlV3ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamSeason3` | `sports_data_io/models/team_season3.py` |
| `NhlV3ScoresTeamSeasonStatsErrorBody` | `sports_data_io/errors/nhl_v3_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_scores.nhl_v3_scores_transactions

- **Route**: `GET /v3/nhl/scores/{format}/TransactionsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_scores_transactions(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[Transaction]`
- **Returns (raw)**: `ApiResult[list[Transaction], NhlV3ScoresTransactionsErrorBody]`
- **Error**: `NhlV3ScoresTransactionsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Transaction` | `sports_data_io/models/transaction.py` |
| `NhlV3ScoresTransactionsErrorBody` | `sports_data_io/errors/nhl_v3_scores_transactions_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

