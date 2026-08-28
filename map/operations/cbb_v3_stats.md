<!-- Generated file — do not edit; regenerated with the SDK. -->

# CbbV3Stats — operations

Accessor: `client.cbb_v3_stats` · Source: `sports_data/apis/cbb_v3_stats.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cbb_v3_stats.cbb_v3_stats_box_score_final

- **Route**: `GET /v3/cbb/stats/{format}/BoxScoreFinal/{gameid}`
- **Signature**: `def cbb_v3_stats_box_score_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `BoxScore`
- **Returns (raw)**: `ApiResult[BoxScore, CbbV3StatsBoxScoreFinalErrorBody]`
- **Error**: `CbbV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore` | `sports_data/models/box_score.py` |
| `CbbV3StatsBoxScoreFinalErrorBody` | `sports_data/errors/cbb_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_box_score_live_final

- **Route**: `GET /v3/cbb/stats/{format}/BoxScore/{gameid}`
- **Signature**: `def cbb_v3_stats_box_score_live_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `BoxScore`
- **Returns (raw)**: `ApiResult[BoxScore, CbbV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `CbbV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore` | `sports_data/models/box_score.py` |
| `CbbV3StatsBoxScoreLiveFinalErrorBody` | `sports_data/errors/cbb_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_box_scores_by_date_final

- **Route**: `GET /v3/cbb/stats/{format}/BoxScoresFinal/{date}`
- **Signature**: `def cbb_v3_stats_box_scores_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore]`
- **Returns (raw)**: `ApiResult[list[BoxScore], CbbV3StatsBoxScoresByDateFinalErrorBody]`
- **Error**: `CbbV3StatsBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore` | `sports_data/models/box_score.py` |
| `CbbV3StatsBoxScoresByDateFinalErrorBody` | `sports_data/errors/cbb_v3_stats_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_box_scores_by_date_live_final

- **Route**: `GET /v3/cbb/stats/{format}/BoxScores/{date}`
- **Signature**: `def cbb_v3_stats_box_scores_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore]`
- **Returns (raw)**: `ApiResult[list[BoxScore], CbbV3StatsBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `CbbV3StatsBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore` | `sports_data/models/box_score.py` |
| `CbbV3StatsBoxScoresByDateLiveFinalErrorBody` | `sports_data/errors/cbb_v3_stats_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_box_scores_delta_by_date

- **Route**: `GET /v3/cbb/stats/{format}/BoxScoresDelta/{date}/{minutes}`
- **Signature**: `def cbb_v3_stats_box_scores_delta_by_date(format: FormatOrStr, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `minutes`
- **Params**: `format` — path · `date` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScore]`
- **Returns (raw)**: `ApiResult[list[BoxScore], CbbV3StatsBoxScoresDeltaByDateErrorBody]`
- **Error**: `CbbV3StatsBoxScoresDeltaByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore` | `sports_data/models/box_score.py` |
| `CbbV3StatsBoxScoresDeltaByDateErrorBody` | `sports_data/errors/cbb_v3_stats_box_scores_delta_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/cbb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Signature**: `def cbb_v3_stats_player_game_logs_by_season(format: FormatOrStr, season: str, playerid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `playerid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame]`
- **Returns (raw)**: `ApiResult[list[PlayerGame], CbbV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `CbbV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame` | `sports_data/models/player_game.py` |
| `CbbV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data/errors/cbb_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_player_game_stats_by_date_final

- **Route**: `GET /v3/cbb/stats/{format}/PlayerGameStatsByDateFinal/{date}`
- **Signature**: `def cbb_v3_stats_player_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGame]`
- **Returns (raw)**: `ApiResult[list[PlayerGame], CbbV3StatsPlayerGameStatsByDateFinalErrorBody]`
- **Error**: `CbbV3StatsPlayerGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame` | `sports_data/models/player_game.py` |
| `CbbV3StatsPlayerGameStatsByDateFinalErrorBody` | `sports_data/errors/cbb_v3_stats_player_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_player_game_stats_by_date_live_final

- **Route**: `GET /v3/cbb/stats/{format}/PlayerGameStatsByDate/{date}`
- **Signature**: `def cbb_v3_stats_player_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGame]`
- **Returns (raw)**: `ApiResult[list[PlayerGame], CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody]`
- **Error**: `CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame` | `sports_data/models/player_game.py` |
| `CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody` | `sports_data/errors/cbb_v3_stats_player_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_player_season_stats

- **Route**: `GET /v3/cbb/stats/{format}/PlayerSeasonStats/{season}`
- **Signature**: `def cbb_v3_stats_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason], CbbV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `CbbV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason` | `sports_data/models/player_season.py` |
| `CbbV3StatsPlayerSeasonStatsErrorBody` | `sports_data/errors/cbb_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/cbb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Signature**: `def cbb_v3_stats_player_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason], CbbV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `CbbV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason` | `sports_data/models/player_season.py` |
| `CbbV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data/errors/cbb_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_team_game_stats_by_date_final

- **Route**: `GET /v3/cbb/stats/{format}/TeamGameStatsByDateFinal/{date}`
- **Signature**: `def cbb_v3_stats_team_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame]`
- **Returns (raw)**: `ApiResult[list[TeamGame], CbbV3StatsTeamGameStatsByDateFinalErrorBody]`
- **Error**: `CbbV3StatsTeamGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame` | `sports_data/models/team_game.py` |
| `CbbV3StatsTeamGameStatsByDateFinalErrorBody` | `sports_data/errors/cbb_v3_stats_team_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

