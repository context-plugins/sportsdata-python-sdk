<!-- Generated file — do not edit; regenerated with the SDK. -->

# CfbV3Stats — operations

Accessor: `client.cfb_v3_stats` · Source: `sports_data/apis/cfb_v3_stats.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cfb_v3_stats.cfb_v3_stats_box_score_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoreFinal/{gameid}`
- **Signature**: `def cfb_v3_stats_box_score_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[BoxScore1]`
- **Returns (raw)**: `ApiResult[list[BoxScore1], CfbV3StatsBoxScoreFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore1` | `sports_data/models/box_score1.py` |
| `CfbV3StatsBoxScoreFinalErrorBody` | `sports_data/errors/cfb_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_score_live_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScore/{gameid}`
- **Signature**: `def cfb_v3_stats_box_score_live_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `list[BoxScore1]`
- **Returns (raw)**: `ApiResult[list[BoxScore1], CfbV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore1` | `sports_data/models/box_score1.py` |
| `CfbV3StatsBoxScoreLiveFinalErrorBody` | `sports_data/errors/cfb_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_scores_by_date_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoresFinal/{date}`
- **Signature**: `def cfb_v3_stats_box_scores_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore1]`
- **Returns (raw)**: `ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByDateFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore1` | `sports_data/models/box_score1.py` |
| `CfbV3StatsBoxScoresByDateFinalErrorBody` | `sports_data/errors/cfb_v3_stats_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_scores_by_date_live_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoresByDate/{date}`
- **Signature**: `def cfb_v3_stats_box_scores_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore1]`
- **Returns (raw)**: `ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore1` | `sports_data/models/box_score1.py` |
| `CfbV3StatsBoxScoresByDateLiveFinalErrorBody` | `sports_data/errors/cfb_v3_stats_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_scores_by_week_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoresByWeekFinal/{season}/{week}`
- **Signature**: `def cfb_v3_stats_box_scores_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[BoxScore1]`
- **Returns (raw)**: `ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByWeekFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoresByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore1` | `sports_data/models/box_score1.py` |
| `CfbV3StatsBoxScoresByWeekFinalErrorBody` | `sports_data/errors/cfb_v3_stats_box_scores_by_week_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_scores_by_week_live_final

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoresByWeek/{season}/{week}`
- **Signature**: `def cfb_v3_stats_box_scores_by_week_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[BoxScore1]`
- **Returns (raw)**: `ApiResult[list[BoxScore1], CfbV3StatsBoxScoresByWeekLiveFinalErrorBody]`
- **Error**: `CfbV3StatsBoxScoresByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore1` | `sports_data/models/box_score1.py` |
| `CfbV3StatsBoxScoresByWeekLiveFinalErrorBody` | `sports_data/errors/cfb_v3_stats_box_scores_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_box_scores_delta_by_week

- **Route**: `GET /v3/cfb/stats/{format}/BoxScoresByWeekDelta/{season}/{week}/{minutes}`
- **Signature**: `def cfb_v3_stats_box_scores_delta_by_week(format: FormatOrStr, season: str, week: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `minutes`
- **Params**: `format` — path · `season` — path · `week` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScore1]`
- **Returns (raw)**: `ApiResult[list[BoxScore1], CfbV3StatsBoxScoresDeltaByWeekErrorBody]`
- **Error**: `CfbV3StatsBoxScoresDeltaByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore1` | `sports_data/models/box_score1.py` |
| `CfbV3StatsBoxScoresDeltaByWeekErrorBody` | `sports_data/errors/cfb_v3_stats_box_scores_delta_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/cfb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Signature**: `def cfb_v3_stats_player_game_logs_by_season(format: FormatOrStr, season: str, playerid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `playerid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame1]`
- **Returns (raw)**: `ApiResult[list[PlayerGame1], CfbV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `CfbV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame1` | `sports_data/models/player_game1.py` |
| `CfbV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data/errors/cfb_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_player_game_stats_by_week_final

- **Route**: `GET /v3/cfb/stats/{format}/PlayerGameStatsByWeekFinal/{season}/{week}`
- **Signature**: `def cfb_v3_stats_player_game_stats_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGame1]`
- **Returns (raw)**: `ApiResult[list[PlayerGame1], CfbV3StatsPlayerGameStatsByWeekFinalErrorBody]`
- **Error**: `CfbV3StatsPlayerGameStatsByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame1` | `sports_data/models/player_game1.py` |
| `CfbV3StatsPlayerGameStatsByWeekFinalErrorBody` | `sports_data/errors/cfb_v3_stats_player_game_stats_by_week_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_player_game_stats_by_week_live_final

- **Route**: `GET /v3/cfb/stats/{format}/PlayerGameStatsByWeek/{season}/{week}`
- **Signature**: `def cfb_v3_stats_player_game_stats_by_week_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGame1]`
- **Returns (raw)**: `ApiResult[list[PlayerGame1], CfbV3StatsPlayerGameStatsByWeekLiveFinalErrorBody]`
- **Error**: `CfbV3StatsPlayerGameStatsByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame1` | `sports_data/models/player_game1.py` |
| `CfbV3StatsPlayerGameStatsByWeekLiveFinalErrorBody` | `sports_data/errors/cfb_v3_stats_player_game_stats_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_player_season_stats

- **Route**: `GET /v3/cfb/stats/{format}/PlayerSeasonStats/{season}`
- **Signature**: `def cfb_v3_stats_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason1]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason1], CfbV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `CfbV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason1` | `sports_data/models/player_season1.py` |
| `CfbV3StatsPlayerSeasonStatsErrorBody` | `sports_data/errors/cfb_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/cfb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Signature**: `def cfb_v3_stats_player_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason1]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason1], CfbV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `CfbV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason1` | `sports_data/models/player_season1.py` |
| `CfbV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data/errors/cfb_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cfb_v3_stats.cfb_v3_stats_team_game_stats_by_week_final

- **Route**: `GET /v3/cfb/stats/{format}/TeamGameStatsByWeekFinal/{season}/{week}`
- **Signature**: `def cfb_v3_stats_team_game_stats_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[TeamGame1]`
- **Returns (raw)**: `ApiResult[list[TeamGame1], CfbV3StatsTeamGameStatsByWeekFinalErrorBody]`
- **Error**: `CfbV3StatsTeamGameStatsByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame1` | `sports_data/models/team_game1.py` |
| `CfbV3StatsTeamGameStatsByWeekFinalErrorBody` | `sports_data/errors/cfb_v3_stats_team_game_stats_by_week_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

