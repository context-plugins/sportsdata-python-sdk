<!-- Generated file — do not edit; regenerated with the SDK. -->

# NhlV3Stats — operations

Accessor: `client.nhl_v3_stats` · Source: `sports_data/apis/nhl_v3_stats.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nhl_v3_stats.nhl_v3_stats_box_score_final

- **Route**: `GET /v3/nhl/stats/{format}/BoxScoreFinal/{gameid}`
- **Signature**: `def nhl_v3_stats_box_score_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `BoxScore4`
- **Returns (raw)**: `ApiResult[BoxScore4, NhlV3StatsBoxScoreFinalErrorBody]`
- **Error**: `NhlV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore4` | `sports_data/models/box_score4.py` |
| `NhlV3StatsBoxScoreFinalErrorBody` | `sports_data/errors/nhl_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_box_score_live_final

- **Route**: `GET /v3/nhl/stats/{format}/BoxScore/{gameid}`
- **Signature**: `def nhl_v3_stats_box_score_live_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `BoxScore4`
- **Returns (raw)**: `ApiResult[BoxScore4, NhlV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `NhlV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore4` | `sports_data/models/box_score4.py` |
| `NhlV3StatsBoxScoreLiveFinalErrorBody` | `sports_data/errors/nhl_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_box_scores_by_date_final

- **Route**: `GET /v3/nhl/stats/{format}/BoxScoresFinal/{date}`
- **Signature**: `def nhl_v3_stats_box_scores_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore4]`
- **Returns (raw)**: `ApiResult[list[BoxScore4], NhlV3StatsBoxScoresByDateFinalErrorBody]`
- **Error**: `NhlV3StatsBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore4` | `sports_data/models/box_score4.py` |
| `NhlV3StatsBoxScoresByDateFinalErrorBody` | `sports_data/errors/nhl_v3_stats_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_box_scores_by_date_live_final

- **Route**: `GET /v3/nhl/stats/{format}/BoxScores/{date}`
- **Signature**: `def nhl_v3_stats_box_scores_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore4]`
- **Returns (raw)**: `ApiResult[list[BoxScore4], NhlV3StatsBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `NhlV3StatsBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore4` | `sports_data/models/box_score4.py` |
| `NhlV3StatsBoxScoresByDateLiveFinalErrorBody` | `sports_data/errors/nhl_v3_stats_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_box_scores_delta_by_date

- **Route**: `GET /v3/nhl/stats/{format}/BoxScoresDelta/{date}/{minutes}`
- **Signature**: `def nhl_v3_stats_box_scores_delta_by_date(format: FormatOrStr, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `minutes`
- **Params**: `format` — path · `date` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScore4]`
- **Returns (raw)**: `ApiResult[list[BoxScore4], NhlV3StatsBoxScoresDeltaByDateErrorBody]`
- **Error**: `NhlV3StatsBoxScoresDeltaByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore4` | `sports_data/models/box_score4.py` |
| `NhlV3StatsBoxScoresDeltaByDateErrorBody` | `sports_data/errors/nhl_v3_stats_box_scores_delta_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_fantasy_points_by_date

- **Route**: `GET /v3/nhl/stats/{format}/FantasyGameStatsByDate/{date}`
- **Signature**: `def nhl_v3_stats_fantasy_points_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[FantasyGame3]`
- **Returns (raw)**: `ApiResult[list[FantasyGame3], NhlV3StatsFantasyPointsByDateErrorBody]`
- **Error**: `NhlV3StatsFantasyPointsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyGame3` | `sports_data/models/fantasy_game3.py` |
| `NhlV3StatsFantasyPointsByDateErrorBody` | `sports_data/errors/nhl_v3_stats_fantasy_points_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_line_combinations_by_season

- **Route**: `GET /v3/nhl/stats/{format}/LinesBySeason/{season}`
- **Signature**: `def nhl_v3_stats_line_combinations_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamLine]`
- **Returns (raw)**: `ApiResult[list[TeamLine], NhlV3StatsLineCombinationsBySeasonErrorBody]`
- **Error**: `NhlV3StatsLineCombinationsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamLine` | `sports_data/models/team_line.py` |
| `NhlV3StatsLineCombinationsBySeasonErrorBody` | `sports_data/errors/nhl_v3_stats_line_combinations_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/nhl/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Signature**: `def nhl_v3_stats_player_game_logs_by_season(format: FormatOrStr, season: str, playerid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `playerid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame5]`
- **Returns (raw)**: `ApiResult[list[PlayerGame5], NhlV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `NhlV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame5` | `sports_data/models/player_game5.py` |
| `NhlV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data/errors/nhl_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_player_game_stats_by_date_final

- **Route**: `GET /v3/nhl/stats/{format}/PlayerGameStatsByDateFinal/{date}`
- **Signature**: `def nhl_v3_stats_player_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGame5]`
- **Returns (raw)**: `ApiResult[list[PlayerGame5], NhlV3StatsPlayerGameStatsByDateFinalErrorBody]`
- **Error**: `NhlV3StatsPlayerGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame5` | `sports_data/models/player_game5.py` |
| `NhlV3StatsPlayerGameStatsByDateFinalErrorBody` | `sports_data/errors/nhl_v3_stats_player_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_player_game_stats_by_date_live_final

- **Route**: `GET /v3/nhl/stats/{format}/PlayerGameStatsByDate/{date}`
- **Signature**: `def nhl_v3_stats_player_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGame5]`
- **Returns (raw)**: `ApiResult[list[PlayerGame5], NhlV3StatsPlayerGameStatsByDateLiveFinalErrorBody]`
- **Error**: `NhlV3StatsPlayerGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame5` | `sports_data/models/player_game5.py` |
| `NhlV3StatsPlayerGameStatsByDateLiveFinalErrorBody` | `sports_data/errors/nhl_v3_stats_player_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_player_season_stats

- **Route**: `GET /v3/nhl/stats/{format}/PlayerSeasonStats/{season}`
- **Signature**: `def nhl_v3_stats_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason6]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason6], NhlV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `NhlV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason6` | `sports_data/models/player_season6.py` |
| `NhlV3StatsPlayerSeasonStatsErrorBody` | `sports_data/errors/nhl_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/nhl/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Signature**: `def nhl_v3_stats_player_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason6]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason6], NhlV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `NhlV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason6` | `sports_data/models/player_season6.py` |
| `NhlV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data/errors/nhl_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_team_game_stats_by_date_final

- **Route**: `GET /v3/nhl/stats/{format}/TeamGameStatsByDateFinal/{date}`
- **Signature**: `def nhl_v3_stats_team_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame5]`
- **Returns (raw)**: `ApiResult[list[TeamGame5], NhlV3StatsTeamGameStatsByDateFinalErrorBody]`
- **Error**: `NhlV3StatsTeamGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame5` | `sports_data/models/team_game5.py` |
| `NhlV3StatsTeamGameStatsByDateFinalErrorBody` | `sports_data/errors/nhl_v3_stats_team_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_team_stats_allowed_by_position

- **Route**: `GET /v3/nhl/stats/{format}/TeamStatsAllowedByPosition/{season}`
- **Signature**: `def nhl_v3_stats_team_stats_allowed_by_position(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamSeason5]`
- **Returns (raw)**: `ApiResult[list[TeamSeason5], NhlV3StatsTeamStatsAllowedByPositionErrorBody]`
- **Error**: `NhlV3StatsTeamStatsAllowedByPositionErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamSeason5` | `sports_data/models/team_season5.py` |
| `NhlV3StatsTeamStatsAllowedByPositionErrorBody` | `sports_data/errors/nhl_v3_stats_team_stats_allowed_by_position_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

