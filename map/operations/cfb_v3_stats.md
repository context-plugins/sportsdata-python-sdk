<!-- Generated file — do not edit; regenerated with the SDK. -->

# CfbV3Stats — operations

Accessor: `client.cfb_v3_stats` · Source: `sports_data_io/apis/cfb_v3_stats.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cfb_v3_stats.cfb_v3_stats_box_score_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoreFinal/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_box_score_final(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `list[BoxScore3]`
- **Returns (raw)**: `ApiResult[list[BoxScore3], CfbV3StatsBoxScoreFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore3` | `sports_data_io/models/box_score3.py` |
| `CfbV3StatsBoxScoreFinalErrorBody` | `sports_data_io/errors/cfb_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_score_live_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScore/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_box_score_live_final(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `list[BoxScore3]`
- **Returns (raw)**: `ApiResult[list[BoxScore3], CfbV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore3` | `sports_data_io/models/box_score3.py` |
| `CfbV3StatsBoxScoreLiveFinalErrorBody` | `sports_data_io/errors/cfb_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_scores_by_date_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoresFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_box_scores_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[BoxScore3]`
- **Returns (raw)**: `ApiResult[list[BoxScore3], CfbV3StatsBoxScoresByDateFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore3` | `sports_data_io/models/box_score3.py` |
| `CfbV3StatsBoxScoresByDateFinalErrorBody` | `sports_data_io/errors/cfb_v3_stats_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_scores_by_date_live_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoresByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_box_scores_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[BoxScore3]`
- **Returns (raw)**: `ApiResult[list[BoxScore3], CfbV3StatsBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore3` | `sports_data_io/models/box_score3.py` |
| `CfbV3StatsBoxScoresByDateLiveFinalErrorBody` | `sports_data_io/errors/cfb_v3_stats_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_scores_by_week_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoresByWeekFinal/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_box_scores_by_week_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[BoxScore3]`
- **Returns (raw)**: `ApiResult[list[BoxScore3], CfbV3StatsBoxScoresByWeekFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoresByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore3` | `sports_data_io/models/box_score3.py` |
| `CfbV3StatsBoxScoresByWeekFinalErrorBody` | `sports_data_io/errors/cfb_v3_stats_box_scores_by_week_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_scores_by_week_live_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoresByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_box_scores_by_week_live_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[BoxScore3]`
- **Returns (raw)**: `ApiResult[list[BoxScore3], CfbV3StatsBoxScoresByWeekLiveFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoresByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore3` | `sports_data_io/models/box_score3.py` |
| `CfbV3StatsBoxScoresByWeekLiveFinalErrorBody` | `sports_data_io/errors/cfb_v3_stats_box_scores_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_scores_delta_by_week

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoresByWeekDelta/{season}/{week}/{minutes}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_box_scores_delta_by_week(season: str, week: str, minutes: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `minutes`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScore3]`
- **Returns (raw)**: `ApiResult[list[BoxScore3], CfbV3StatsBoxScoresDeltaByWeekErrorBody]`
- **Error**: `CfbV3StatsBoxScoresDeltaByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore3` | `sports_data_io/models/box_score3.py` |
| `CfbV3StatsBoxScoresDeltaByWeekErrorBody` | `sports_data_io/errors/cfb_v3_stats_box_scores_delta_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/cfb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_player_game_logs_by_season(season: str, playerid: str, numberofgames: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `playerid`, `numberofgames`
- **Params**: `format_` — path `format` · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame4]`
- **Returns (raw)**: `ApiResult[list[PlayerGame4], CfbV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `CfbV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame4` | `sports_data_io/models/player_game4.py` |
| `CfbV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data_io/errors/cfb_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_player_game_stats_by_week_final

- **Route**: `GET /v3/cfb/stats/{format}/PlayerGameStatsByWeekFinal/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_player_game_stats_by_week_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGame4]`
- **Returns (raw)**: `ApiResult[list[PlayerGame4], CfbV3StatsPlayerGameStatsByWeekFinalErrorBody]`
- **Error**: `CfbV3StatsPlayerGameStatsByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame4` | `sports_data_io/models/player_game4.py` |
| `CfbV3StatsPlayerGameStatsByWeekFinalErrorBody` | `sports_data_io/errors/cfb_v3_stats_player_game_stats_by_week_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_player_game_stats_by_week_live_final

- **Route**: `GET /v3/cfb/stats/{format}/PlayerGameStatsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_player_game_stats_by_week_live_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGame4]`
- **Returns (raw)**: `ApiResult[list[PlayerGame4], CfbV3StatsPlayerGameStatsByWeekLiveFinalErrorBody]`
- **Error**: `CfbV3StatsPlayerGameStatsByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame4` | `sports_data_io/models/player_game4.py` |
| `CfbV3StatsPlayerGameStatsByWeekLiveFinalErrorBody` | `sports_data_io/errors/cfb_v3_stats_player_game_stats_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_player_season_stats

- **Route**: `GET /v3/cfb/stats/{format}/PlayerSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_player_season_stats(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerSeason5]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason5], CfbV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `CfbV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason5` | `sports_data_io/models/player_season5.py` |
| `CfbV3StatsPlayerSeasonStatsErrorBody` | `sports_data_io/errors/cfb_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/cfb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_player_season_stats_by_team(season: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `team`
- **Params**: `format_` — path `format` · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason5]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason5], CfbV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `CfbV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason5` | `sports_data_io/models/player_season5.py` |
| `CfbV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data_io/errors/cfb_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_team_game_stats_by_week_final

- **Route**: `GET /v3/cfb/stats/{format}/TeamGameStatsByWeekFinal/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cfb_v3_stats_team_game_stats_by_week_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[TeamGame4]`
- **Returns (raw)**: `ApiResult[list[TeamGame4], CfbV3StatsTeamGameStatsByWeekFinalErrorBody]`
- **Error**: `CfbV3StatsTeamGameStatsByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame4` | `sports_data_io/models/team_game4.py` |
| `CfbV3StatsTeamGameStatsByWeekFinalErrorBody` | `sports_data_io/errors/cfb_v3_stats_team_game_stats_by_week_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

