<!-- Generated file — do not edit; regenerated with the SDK. -->

# NbaV3Stats — operations

Accessor: `client.nba_v3_stats` · Source: `sports_data/apis/nba_v3_stats.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nba_v3_stats.nba_v3_stats_all_stars

- **Route**: `GET /v3/nba/stats/{format}/AllStars/{season}`
- **Signature**: `def nba_v3_stats_all_stars(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerInfo]`
- **Returns (raw)**: `ApiResult[list[PlayerInfo], NbaV3StatsAllStarsErrorBody]`
- **Error**: `NbaV3StatsAllStarsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerInfo` | `sports_data/models/player_info.py` |
| `NbaV3StatsAllStarsErrorBody` | `sports_data/errors/nba_v3_stats_all_stars_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_box_score_final

- **Route**: `GET /v3/nba/stats/{format}/BoxScoreFinal/{gameid}`
- **Signature**: `def nba_v3_stats_box_score_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `BoxScore3`
- **Returns (raw)**: `ApiResult[BoxScore3, NbaV3StatsBoxScoreFinalErrorBody]`
- **Error**: `NbaV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore3` | `sports_data/models/box_score3.py` |
| `NbaV3StatsBoxScoreFinalErrorBody` | `sports_data/errors/nba_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_box_score_live_final

- **Route**: `GET /v3/nba/stats/{format}/BoxScore/{gameid}`
- **Signature**: `def nba_v3_stats_box_score_live_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `BoxScore3`
- **Returns (raw)**: `ApiResult[BoxScore3, NbaV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `NbaV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore3` | `sports_data/models/box_score3.py` |
| `NbaV3StatsBoxScoreLiveFinalErrorBody` | `sports_data/errors/nba_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_box_scores_by_date_final

- **Route**: `GET /v3/nba/stats/{format}/BoxScoresFinal/{date}`
- **Signature**: `def nba_v3_stats_box_scores_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore3]`
- **Returns (raw)**: `ApiResult[list[BoxScore3], NbaV3StatsBoxScoresByDateFinalErrorBody]`
- **Error**: `NbaV3StatsBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore3` | `sports_data/models/box_score3.py` |
| `NbaV3StatsBoxScoresByDateFinalErrorBody` | `sports_data/errors/nba_v3_stats_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_box_scores_by_date_live_final

- **Route**: `GET /v3/nba/stats/{format}/BoxScores/{date}`
- **Signature**: `def nba_v3_stats_box_scores_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore3]`
- **Returns (raw)**: `ApiResult[list[BoxScore3], NbaV3StatsBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `NbaV3StatsBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore3` | `sports_data/models/box_score3.py` |
| `NbaV3StatsBoxScoresByDateLiveFinalErrorBody` | `sports_data/errors/nba_v3_stats_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_box_scores_delta_by_date

- **Route**: `GET /v3/nba/stats/{format}/BoxScoresDelta/{date}/{minutes}`
- **Signature**: `def nba_v3_stats_box_scores_delta_by_date(format: FormatOrStr, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `minutes`
- **Params**: `format` — path · `date` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScore3]`
- **Returns (raw)**: `ApiResult[list[BoxScore3], NbaV3StatsBoxScoresDeltaByDateErrorBody]`
- **Error**: `NbaV3StatsBoxScoresDeltaByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore3` | `sports_data/models/box_score3.py` |
| `NbaV3StatsBoxScoresDeltaByDateErrorBody` | `sports_data/errors/nba_v3_stats_box_scores_delta_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_fantasy_points_by_date

- **Route**: `GET /v3/nba/stats/{format}/FantasyGameStatsByDate/{date}`
- **Signature**: `def nba_v3_stats_fantasy_points_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[FantasyGame1]`
- **Returns (raw)**: `ApiResult[list[FantasyGame1], NbaV3StatsFantasyPointsByDateErrorBody]`
- **Error**: `NbaV3StatsFantasyPointsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyGame1` | `sports_data/models/fantasy_game1.py` |
| `NbaV3StatsFantasyPointsByDateErrorBody` | `sports_data/errors/nba_v3_stats_fantasy_points_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/nba/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Signature**: `def nba_v3_stats_player_game_logs_by_season(format: FormatOrStr, season: str, playerid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `playerid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame3]`
- **Returns (raw)**: `ApiResult[list[PlayerGame3], NbaV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `NbaV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame3` | `sports_data/models/player_game3.py` |
| `NbaV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data/errors/nba_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_player_game_stats_by_date_final

- **Route**: `GET /v3/nba/stats/{format}/PlayerGameStatsByDateFinal/{date}`
- **Signature**: `def nba_v3_stats_player_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGame3]`
- **Returns (raw)**: `ApiResult[list[PlayerGame3], NbaV3StatsPlayerGameStatsByDateFinalErrorBody]`
- **Error**: `NbaV3StatsPlayerGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame3` | `sports_data/models/player_game3.py` |
| `NbaV3StatsPlayerGameStatsByDateFinalErrorBody` | `sports_data/errors/nba_v3_stats_player_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_player_game_stats_by_date_live_final

- **Route**: `GET /v3/nba/stats/{format}/PlayerGameStatsByDate/{date}`
- **Signature**: `def nba_v3_stats_player_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGame3]`
- **Returns (raw)**: `ApiResult[list[PlayerGame3], NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody]`
- **Error**: `NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame3` | `sports_data/models/player_game3.py` |
| `NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody` | `sports_data/errors/nba_v3_stats_player_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_player_season_stats

- **Route**: `GET /v3/nba/stats/{format}/PlayerSeasonStats/{season}`
- **Signature**: `def nba_v3_stats_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason4]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason4], NbaV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `NbaV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason4` | `sports_data/models/player_season4.py` |
| `NbaV3StatsPlayerSeasonStatsErrorBody` | `sports_data/errors/nba_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/nba/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Signature**: `def nba_v3_stats_player_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason4]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason4], NbaV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `NbaV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason4` | `sports_data/models/player_season4.py` |
| `NbaV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data/errors/nba_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_team_game_stats_by_date_final

- **Route**: `GET /v3/nba/stats/{format}/TeamGameStatsByDateFinal/{date}`
- **Signature**: `def nba_v3_stats_team_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame3]`
- **Returns (raw)**: `ApiResult[list[TeamGame3], NbaV3StatsTeamGameStatsByDateFinalErrorBody]`
- **Error**: `NbaV3StatsTeamGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame3` | `sports_data/models/team_game3.py` |
| `NbaV3StatsTeamGameStatsByDateFinalErrorBody` | `sports_data/errors/nba_v3_stats_team_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_team_stats_allowed_by_position

- **Route**: `GET /v3/nba/stats/{format}/TeamStatsAllowedByPosition/{season}`
- **Signature**: `def nba_v3_stats_team_stats_allowed_by_position(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[TeamSeason3]`
- **Returns (raw)**: `ApiResult[list[TeamSeason3], NbaV3StatsTeamStatsAllowedByPositionErrorBody]`
- **Error**: `NbaV3StatsTeamStatsAllowedByPositionErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamSeason3` | `sports_data/models/team_season3.py` |
| `NbaV3StatsTeamStatsAllowedByPositionErrorBody` | `sports_data/errors/nba_v3_stats_team_stats_allowed_by_position_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

