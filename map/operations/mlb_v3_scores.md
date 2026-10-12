<!-- Generated file — do not edit; regenerated with the SDK. -->

# MlbV3Scores — operations

Accessor: `client.mlb_v3_scores` · Source: `sports_data_io/apis/mlb_v3_scores.py` · 26 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mlb_v3_scores.mlb_v3_scores_are_games_in_progress

- **Route**: `GET /v3/mlb/scores/{format}/AreAnyGamesInProgress`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_are_games_in_progress(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `bool`
- **Returns (raw)**: `ApiResult[bool, MlbV3ScoresAreGamesInProgressErrorBody]`
- **Error**: `MlbV3ScoresAreGamesInProgressErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `MlbV3ScoresAreGamesInProgressErrorBody` | `sports_data_io/errors/mlb_v3_scores_are_games_in_progress_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_games_by_date_final

- **Route**: `GET /v3/mlb/scores/{format}/GamesByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_games_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[Game6]`
- **Returns (raw)**: `ApiResult[list[Game6], MlbV3ScoresGamesByDateFinalErrorBody]`
- **Error**: `MlbV3ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game6` | `sports_data_io/models/game6.py` |
| `MlbV3ScoresGamesByDateFinalErrorBody` | `sports_data_io/errors/mlb_v3_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_games_by_date_live_final

- **Route**: `GET /v3/mlb/scores/{format}/GamesByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_games_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[Game6]`
- **Returns (raw)**: `ApiResult[list[Game6], MlbV3ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `MlbV3ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game6` | `sports_data_io/models/game6.py` |
| `MlbV3ScoresGamesByDateLiveFinalErrorBody` | `sports_data_io/errors/mlb_v3_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_games_basic_by_date_final

- **Route**: `GET /v3/mlb/scores/{format}/ScoresBasicFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_games_basic_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[ScoreBasic2]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic2], MlbV3ScoresGamesBasicByDateFinalErrorBody]`
- **Error**: `MlbV3ScoresGamesBasicByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic2` | `sports_data_io/models/score_basic2.py` |
| `MlbV3ScoresGamesBasicByDateFinalErrorBody` | `sports_data_io/errors/mlb_v3_scores_games_basic_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_games_basic_by_date_live_final

- **Route**: `GET /v3/mlb/scores/{format}/ScoresBasic/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_games_basic_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[ScoreBasic2]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic2], MlbV3ScoresGamesBasicByDateLiveFinalErrorBody]`
- **Error**: `MlbV3ScoresGamesBasicByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic2` | `sports_data_io/models/score_basic2.py` |
| `MlbV3ScoresGamesBasicByDateLiveFinalErrorBody` | `sports_data_io/errors/mlb_v3_scores_games_basic_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_news

- **Route**: `GET /v3/mlb/scores/{format}/News`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_news(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[News]`
- **Returns (raw)**: `ApiResult[list[News], MlbV3ScoresNewsErrorBody]`
- **Error**: `MlbV3ScoresNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News` | `sports_data_io/models/news.py` |
| `MlbV3ScoresNewsErrorBody` | `sports_data_io/errors/mlb_v3_scores_news_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_news_by_date

- **Route**: `GET /v3/mlb/scores/{format}/NewsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_news_by_date(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[News]`
- **Returns (raw)**: `ApiResult[list[News], MlbV3ScoresNewsByDateErrorBody]`
- **Error**: `MlbV3ScoresNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News` | `sports_data_io/models/news.py` |
| `MlbV3ScoresNewsByDateErrorBody` | `sports_data_io/errors/mlb_v3_scores_news_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_player_details_by_active

- **Route**: `GET /v3/mlb/scores/{format}/Players`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_player_details_by_active(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Player2]`
- **Returns (raw)**: `ApiResult[list[Player2], MlbV3ScoresPlayerDetailsByActiveErrorBody]`
- **Error**: `MlbV3ScoresPlayerDetailsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player2` | `sports_data_io/models/player2.py` |
| `MlbV3ScoresPlayerDetailsByActiveErrorBody` | `sports_data_io/errors/mlb_v3_scores_player_details_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_player_details_by_free_agents

- **Route**: `GET /v3/mlb/scores/{format}/FreeAgents`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_player_details_by_free_agents(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Player2]`
- **Returns (raw)**: `ApiResult[list[Player2], MlbV3ScoresPlayerDetailsByFreeAgentsErrorBody]`
- **Error**: `MlbV3ScoresPlayerDetailsByFreeAgentsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player2` | `sports_data_io/models/player2.py` |
| `MlbV3ScoresPlayerDetailsByFreeAgentsErrorBody` | `sports_data_io/errors/mlb_v3_scores_player_details_by_free_agents_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_player_profiles_by_active

- **Route**: `GET /v3/mlb/scores/{format}/PlayersByActive`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_player_profiles_by_active(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[PlayerBasic2]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByActiveErrorBody]`
- **Error**: `MlbV3ScoresPlayerProfilesByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic2` | `sports_data_io/models/player_basic2.py` |
| `MlbV3ScoresPlayerProfilesByActiveErrorBody` | `sports_data_io/errors/mlb_v3_scores_player_profiles_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_player_profiles_by_free_agents

- **Route**: `GET /v3/mlb/scores/{format}/PlayersByFreeAgents`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_player_profiles_by_free_agents(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[PlayerBasic2]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByFreeAgentsErrorBody]`
- **Error**: `MlbV3ScoresPlayerProfilesByFreeAgentsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic2` | `sports_data_io/models/player_basic2.py` |
| `MlbV3ScoresPlayerProfilesByFreeAgentsErrorBody` | `sports_data_io/errors/mlb_v3_scores_player_profiles_by_free_agents_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_player_profiles_by_team

- **Route**: `GET /v3/mlb/scores/{format}/PlayersBasic/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_player_profiles_by_team(team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`
- **Params**: `format_` — path `format` · `team` — path
- **Returns (parsed)**: `list[PlayerBasic2]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic2], MlbV3ScoresPlayerProfilesByTeamErrorBody]`
- **Error**: `MlbV3ScoresPlayerProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic2` | `sports_data_io/models/player_basic2.py` |
| `MlbV3ScoresPlayerProfilesByTeamErrorBody` | `sports_data_io/errors/mlb_v3_scores_player_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_players_details_by_team

- **Route**: `GET /v3/mlb/scores/{format}/Players/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_players_details_by_team(team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team`
- **Params**: `format_` — path `format` · `team` — path
- **Returns (parsed)**: `list[Player2]`
- **Returns (raw)**: `ApiResult[list[Player2], MlbV3ScoresPlayersDetailsByTeamErrorBody]`
- **Error**: `MlbV3ScoresPlayersDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player2` | `sports_data_io/models/player2.py` |
| `MlbV3ScoresPlayersDetailsByTeamErrorBody` | `sports_data_io/errors/mlb_v3_scores_players_details_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_schedules

- **Route**: `GET /v3/mlb/scores/{format}/Games/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_schedules(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[Game6]`
- **Returns (raw)**: `ApiResult[list[Game6], MlbV3ScoresSchedulesErrorBody]`
- **Error**: `MlbV3ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game6` | `sports_data_io/models/game6.py` |
| `MlbV3ScoresSchedulesErrorBody` | `sports_data_io/errors/mlb_v3_scores_schedules_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_schedules_basic

- **Route**: `GET /v3/mlb/scores/{format}/SchedulesBasic/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_schedules_basic(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic2]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic2], MlbV3ScoresSchedulesBasicErrorBody]`
- **Error**: `MlbV3ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScheduleBasic2` | `sports_data_io/models/schedule_basic2.py` |
| `MlbV3ScoresSchedulesBasicErrorBody` | `sports_data_io/errors/mlb_v3_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_season_current

- **Route**: `GET /v3/mlb/scores/{format}/CurrentSeason`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_season_current(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `Season1`
- **Returns (raw)**: `ApiResult[Season1, MlbV3ScoresSeasonCurrentErrorBody]`
- **Error**: `MlbV3ScoresSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Season1` | `sports_data_io/models/season1.py` |
| `MlbV3ScoresSeasonCurrentErrorBody` | `sports_data_io/errors/mlb_v3_scores_season_current_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_stadiums

- **Route**: `GET /v3/mlb/scores/{format}/Stadiums`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_stadiums(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Stadium3]`
- **Returns (raw)**: `ApiResult[list[Stadium3], MlbV3ScoresStadiumsErrorBody]`
- **Error**: `MlbV3ScoresStadiumsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Stadium3` | `sports_data_io/models/stadium3.py` |
| `MlbV3ScoresStadiumsErrorBody` | `sports_data_io/errors/mlb_v3_scores_stadiums_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_standings

- **Route**: `GET /v3/mlb/scores/{format}/Standings/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_standings(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[Standing2]`
- **Returns (raw)**: `ApiResult[list[Standing2], MlbV3ScoresStandingsErrorBody]`
- **Error**: `MlbV3ScoresStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Standing2` | `sports_data_io/models/standing2.py` |
| `MlbV3ScoresStandingsErrorBody` | `sports_data_io/errors/mlb_v3_scores_standings_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_game_logs_by_season

- **Route**: `GET /v3/mlb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_team_game_logs_by_season(season: str, teamid: str, numberofgames: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `teamid`, `numberofgames`
- **Params**: `format_` — path `format` · `season` — path · `teamid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[TeamGame2]`
- **Returns (raw)**: `ApiResult[list[TeamGame2], MlbV3ScoresTeamGameLogsBySeasonErrorBody]`
- **Error**: `MlbV3ScoresTeamGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame2` | `sports_data_io/models/team_game2.py` |
| `MlbV3ScoresTeamGameLogsBySeasonErrorBody` | `sports_data_io/errors/mlb_v3_scores_team_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_game_stats_by_date_final

- **Route**: `GET /v3/mlb/scores/{format}/TeamGameStatsByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_team_game_stats_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[TeamGame2]`
- **Returns (raw)**: `ApiResult[list[TeamGame2], MlbV3ScoresTeamGameStatsByDateFinalErrorBody]`
- **Error**: `MlbV3ScoresTeamGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame2` | `sports_data_io/models/team_game2.py` |
| `MlbV3ScoresTeamGameStatsByDateFinalErrorBody` | `sports_data_io/errors/mlb_v3_scores_team_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_game_stats_by_date_live_final

- **Route**: `GET /v3/mlb/scores/{format}/TeamGameStatsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_team_game_stats_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[TeamGame2]`
- **Returns (raw)**: `ApiResult[list[TeamGame2], MlbV3ScoresTeamGameStatsByDateLiveFinalErrorBody]`
- **Error**: `MlbV3ScoresTeamGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame2` | `sports_data_io/models/team_game2.py` |
| `MlbV3ScoresTeamGameStatsByDateLiveFinalErrorBody` | `sports_data_io/errors/mlb_v3_scores_team_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_profiles_all

- **Route**: `GET /v3/mlb/scores/{format}/AllTeams`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_team_profiles_all(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Team2]`
- **Returns (raw)**: `ApiResult[list[Team2], MlbV3ScoresTeamProfilesAllErrorBody]`
- **Error**: `MlbV3ScoresTeamProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team2` | `sports_data_io/models/team2.py` |
| `MlbV3ScoresTeamProfilesAllErrorBody` | `sports_data_io/errors/mlb_v3_scores_team_profiles_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_profiles_by_active

- **Route**: `GET /v3/mlb/scores/{format}/teams`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_team_profiles_by_active(*, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `format_` — path `format`
- **Returns (parsed)**: `list[Team2]`
- **Returns (raw)**: `ApiResult[list[Team2], MlbV3ScoresTeamProfilesByActiveErrorBody]`
- **Error**: `MlbV3ScoresTeamProfilesByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team2` | `sports_data_io/models/team2.py` |
| `MlbV3ScoresTeamProfilesByActiveErrorBody` | `sports_data_io/errors/mlb_v3_scores_team_profiles_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_profiles_by_season

- **Route**: `GET /v3/mlb/scores/{format}/teams/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_team_profiles_by_season(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[Team2]`
- **Returns (raw)**: `ApiResult[list[Team2], MlbV3ScoresTeamProfilesBySeasonErrorBody]`
- **Error**: `MlbV3ScoresTeamProfilesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team2` | `sports_data_io/models/team2.py` |
| `MlbV3ScoresTeamProfilesBySeasonErrorBody` | `sports_data_io/errors/mlb_v3_scores_team_profiles_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_team_season_stats

- **Route**: `GET /v3/mlb/scores/{format}/TeamSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_team_season_stats(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[TeamSeason2]`
- **Returns (raw)**: `ApiResult[list[TeamSeason2], MlbV3ScoresTeamSeasonStatsErrorBody]`
- **Error**: `MlbV3ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamSeason2` | `sports_data_io/models/team_season2.py` |
| `MlbV3ScoresTeamSeasonStatsErrorBody` | `sports_data_io/errors/mlb_v3_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.mlb_v3_scores.mlb_v3_scores_transactions

- **Route**: `GET /v3/mlb/scores/{format}/TransactionsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def mlb_v3_scores_transactions(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[Transaction]`
- **Returns (raw)**: `ApiResult[list[Transaction], MlbV3ScoresTransactionsErrorBody]`
- **Error**: `MlbV3ScoresTransactionsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Transaction` | `sports_data_io/models/transaction.py` |
| `MlbV3ScoresTransactionsErrorBody` | `sports_data_io/errors/mlb_v3_scores_transactions_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

