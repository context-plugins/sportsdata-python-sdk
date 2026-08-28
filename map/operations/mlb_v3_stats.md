<!-- Generated file — do not edit; regenerated with the SDK. -->

# MlbV3Stats — operations

Accessor: `client.mlb_v3_stats` · Source: `sports_data/apis/mlb_v3_stats.py` · 17 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.mlb_v3_stats.mlb_v3_stats_batter_vs_pitcher_stats

- **Route**: `GET /v3/mlb/stats/{format}/HitterVsPitcher/{hitterid}/{pitcherid}`
- **Signature**: `def mlb_v3_stats_batter_vs_pitcher_stats(format: FormatOrStr, hitterid: str, pitcherid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `hitterid`, `pitcherid`
- **Params**: `format` — path · `hitterid` — path · `pitcherid` — path
- **Returns (parsed)**: `list[PlayerSeason3]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason3], MlbV3StatsBatterVsPitcherStatsErrorBody]`
- **Error**: `MlbV3StatsBatterVsPitcherStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason3` | `sports_data/models/player_season3.py` |
| `MlbV3StatsBatterVsPitcherStatsErrorBody` | `sports_data/errors/mlb_v3_stats_batter_vs_pitcher_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_box_score_final

- **Route**: `GET /v3/mlb/stats/{format}/BoxScoreFinal/{gameid}`
- **Signature**: `def mlb_v3_stats_box_score_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `BoxScore2`
- **Returns (raw)**: `ApiResult[BoxScore2, MlbV3StatsBoxScoreFinalErrorBody]`
- **Error**: `MlbV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore2` | `sports_data/models/box_score2.py` |
| `MlbV3StatsBoxScoreFinalErrorBody` | `sports_data/errors/mlb_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_box_score_live_final

- **Route**: `GET /v3/mlb/stats/{format}/BoxScore/{gameid}`
- **Signature**: `def mlb_v3_stats_box_score_live_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`
- **Params**: `format` — path · `gameid` — path
- **Returns (parsed)**: `BoxScore2`
- **Returns (raw)**: `ApiResult[BoxScore2, MlbV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `MlbV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore2` | `sports_data/models/box_score2.py` |
| `MlbV3StatsBoxScoreLiveFinalErrorBody` | `sports_data/errors/mlb_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_box_scores_by_date_final

- **Route**: `GET /v3/mlb/stats/{format}/BoxScoresFinal/{date}`
- **Signature**: `def mlb_v3_stats_box_scores_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore2]`
- **Returns (raw)**: `ApiResult[list[BoxScore2], MlbV3StatsBoxScoresByDateFinalErrorBody]`
- **Error**: `MlbV3StatsBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore2` | `sports_data/models/box_score2.py` |
| `MlbV3StatsBoxScoresByDateFinalErrorBody` | `sports_data/errors/mlb_v3_stats_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_box_scores_by_date_live_final

- **Route**: `GET /v3/mlb/stats/{format}/BoxScores/{date}`
- **Signature**: `def mlb_v3_stats_box_scores_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore2]`
- **Returns (raw)**: `ApiResult[list[BoxScore2], MlbV3StatsBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `MlbV3StatsBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore2` | `sports_data/models/box_score2.py` |
| `MlbV3StatsBoxScoresByDateLiveFinalErrorBody` | `sports_data/errors/mlb_v3_stats_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_box_scores_delta_by_date

- **Route**: `GET /v3/mlb/stats/{format}/BoxScoresDelta/{date}/{minutes}`
- **Signature**: `def mlb_v3_stats_box_scores_delta_by_date(format: FormatOrStr, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`, `minutes`
- **Params**: `format` — path · `date` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScore2]`
- **Returns (raw)**: `ApiResult[list[BoxScore2], MlbV3StatsBoxScoresDeltaByDateErrorBody]`
- **Error**: `MlbV3StatsBoxScoresDeltaByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore2` | `sports_data/models/box_score2.py` |
| `MlbV3StatsBoxScoresDeltaByDateErrorBody` | `sports_data/errors/mlb_v3_stats_box_scores_delta_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_fantasy_points_by_date

- **Route**: `GET /v3/mlb/stats/{format}/FantasyGameStatsByDate/{date}`
- **Signature**: `def mlb_v3_stats_fantasy_points_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[FantasyGame]`
- **Returns (raw)**: `ApiResult[list[FantasyGame], MlbV3StatsFantasyPointsByDateErrorBody]`
- **Error**: `MlbV3StatsFantasyPointsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyGame` | `sports_data/models/fantasy_game.py` |
| `MlbV3StatsFantasyPointsByDateErrorBody` | `sports_data/errors/mlb_v3_stats_fantasy_points_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/mlb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Signature**: `def mlb_v3_stats_player_game_logs_by_season(format: FormatOrStr, season: str, playerid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `playerid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame2]`
- **Returns (raw)**: `ApiResult[list[PlayerGame2], MlbV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `MlbV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame2` | `sports_data/models/player_game2.py` |
| `MlbV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data/errors/mlb_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_player_game_stats_by_date_final

- **Route**: `GET /v3/mlb/stats/{format}/PlayerGameStatsByDateFinal/{date}`
- **Signature**: `def mlb_v3_stats_player_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGame2]`
- **Returns (raw)**: `ApiResult[list[PlayerGame2], MlbV3StatsPlayerGameStatsByDateFinalErrorBody]`
- **Error**: `MlbV3StatsPlayerGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame2` | `sports_data/models/player_game2.py` |
| `MlbV3StatsPlayerGameStatsByDateFinalErrorBody` | `sports_data/errors/mlb_v3_stats_player_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_player_game_stats_by_date_live_final

- **Route**: `GET /v3/mlb/stats/{format}/PlayerGameStatsByDate/{date}`
- **Signature**: `def mlb_v3_stats_player_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGame2]`
- **Returns (raw)**: `ApiResult[list[PlayerGame2], MlbV3StatsPlayerGameStatsByDateLiveFinalErrorBody]`
- **Error**: `MlbV3StatsPlayerGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame2` | `sports_data/models/player_game2.py` |
| `MlbV3StatsPlayerGameStatsByDateLiveFinalErrorBody` | `sports_data/errors/mlb_v3_stats_player_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_player_season_split_stats

- **Route**: `GET /v3/mlb/stats/{format}/PlayerSeasonSplitStats/{season}/{split}`
- **Signature**: `def mlb_v3_stats_player_season_split_stats(format: FormatOrStr, season: str, split: SplitOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `split`
- **Params**: `format` — path · `season` — path · `split` — path
- **Returns (parsed)**: `list[PlayerSeason3]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonSplitStatsErrorBody]`
- **Error**: `MlbV3StatsPlayerSeasonSplitStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `SplitOrStr` | `sports_data/models/enums/split.py` |
| `PlayerSeason3` | `sports_data/models/player_season3.py` |
| `MlbV3StatsPlayerSeasonSplitStatsErrorBody` | `sports_data/errors/mlb_v3_stats_player_season_split_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_player_season_stats

- **Route**: `GET /v3/mlb/stats/{format}/PlayerSeasonStats/{season}`
- **Signature**: `def mlb_v3_stats_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason3]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `MlbV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason3` | `sports_data/models/player_season3.py` |
| `MlbV3StatsPlayerSeasonStatsErrorBody` | `sports_data/errors/mlb_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_player_season_stats_by_away

- **Route**: `GET /v3/mlb/stats/{format}/PlayerSeasonAwayStats/{season}`
- **Signature**: `def mlb_v3_stats_player_season_stats_by_away(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason3]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsByAwayErrorBody]`
- **Error**: `MlbV3StatsPlayerSeasonStatsByAwayErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason3` | `sports_data/models/player_season3.py` |
| `MlbV3StatsPlayerSeasonStatsByAwayErrorBody` | `sports_data/errors/mlb_v3_stats_player_season_stats_by_away_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_player_season_stats_by_home

- **Route**: `GET /v3/mlb/stats/{format}/PlayerSeasonHomeStats/{season}`
- **Signature**: `def mlb_v3_stats_player_season_stats_by_home(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason3]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsByHomeErrorBody]`
- **Error**: `MlbV3StatsPlayerSeasonStatsByHomeErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason3` | `sports_data/models/player_season3.py` |
| `MlbV3StatsPlayerSeasonStatsByHomeErrorBody` | `sports_data/errors/mlb_v3_stats_player_season_stats_by_home_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/mlb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Signature**: `def mlb_v3_stats_player_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason3]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `MlbV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason3` | `sports_data/models/player_season3.py` |
| `MlbV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data/errors/mlb_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_player_season_stats_split_by_team

- **Route**: `GET /v3/mlb/stats/{format}/PlayerSeasonStatsSplitByTeam/{season}`
- **Signature**: `def mlb_v3_stats_player_season_stats_split_by_team(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason3]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason3], MlbV3StatsPlayerSeasonStatsSplitByTeamErrorBody]`
- **Error**: `MlbV3StatsPlayerSeasonStatsSplitByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason3` | `sports_data/models/player_season3.py` |
| `MlbV3StatsPlayerSeasonStatsSplitByTeamErrorBody` | `sports_data/errors/mlb_v3_stats_player_season_stats_split_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.mlb_v3_stats.mlb_v3_stats_team_hitting_vs_starting_pitcher

- **Route**: `GET /v3/mlb/stats/{format}/TeamHittersVsPitcher/{gameid}/{team}`
- **Signature**: `def mlb_v3_stats_team_hitting_vs_starting_pitcher(format: FormatOrStr, gameid: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `gameid`, `team`
- **Params**: `format` — path · `gameid` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason3]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason3], MlbV3StatsTeamHittingVsStartingPitcherErrorBody]`
- **Error**: `MlbV3StatsTeamHittingVsStartingPitcherErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason3` | `sports_data/models/player_season3.py` |
| `MlbV3StatsTeamHittingVsStartingPitcherErrorBody` | `sports_data/errors/mlb_v3_stats_team_hitting_vs_starting_pitcher_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

