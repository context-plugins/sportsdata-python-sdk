<!-- Generated file — do not edit; regenerated with the SDK. -->

# NflV3Stats — operations

Accessor: `client.nfl_v3_stats` · Source: `sports_data/apis/nfl_v3_stats.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nfl_v3_stats.nfl_v3_stats_box_score_by_team_final

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoreByTeamFinal/{season}/{week}/{hometeam}`
- **Signature**: `def nfl_v3_stats_box_score_by_team_final(format: FormatOrStr, season: str, week: str, hometeam: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `hometeam`
- **Params**: `format` — path · `season` — path · `week` — path · `hometeam` — path
- **Returns (parsed)**: `BoxScoreV3`
- **Returns (raw)**: `ApiResult[BoxScoreV3, NflV3StatsBoxScoreByTeamFinalErrorBody]`
- **Error**: `NflV3StatsBoxScoreByTeamFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScoreV3` | `sports_data/models/box_score_v3.py` |
| `NflV3StatsBoxScoreByTeamFinalErrorBody` | `sports_data/errors/nfl_v3_stats_box_score_by_team_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_score_by_team_live_final

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoreV3/{season}/{week}/{hometeam}`
- **Signature**: `def nfl_v3_stats_box_score_by_team_live_final(format: FormatOrStr, season: str, week: str, hometeam: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `hometeam`
- **Params**: `format` — path · `season` — path · `week` — path · `hometeam` — path
- **Returns (parsed)**: `BoxScoreV3`
- **Returns (raw)**: `ApiResult[BoxScoreV3, NflV3StatsBoxScoreByTeamLiveFinalErrorBody]`
- **Error**: `NflV3StatsBoxScoreByTeamLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScoreV3` | `sports_data/models/box_score_v3.py` |
| `NflV3StatsBoxScoreByTeamLiveFinalErrorBody` | `sports_data/errors/nfl_v3_stats_box_score_by_team_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_score_final

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoreFinal/{scoreid}`
- **Signature**: `def nfl_v3_stats_box_score_final(format: FormatOrStr, scoreid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`
- **Params**: `format` — path · `scoreid` — path
- **Returns (parsed)**: `BoxScoreV3`
- **Returns (raw)**: `ApiResult[BoxScoreV3, NflV3StatsBoxScoreFinalErrorBody]`
- **Error**: `NflV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScoreV3` | `sports_data/models/box_score_v3.py` |
| `NflV3StatsBoxScoreFinalErrorBody` | `sports_data/errors/nfl_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_score_live_final

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoreByScoreIDV3/{scoreid}`
- **Signature**: `def nfl_v3_stats_box_score_live_final(format: FormatOrStr, scoreid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `scoreid`
- **Params**: `format` — path · `scoreid` — path
- **Returns (parsed)**: `BoxScoreV3`
- **Returns (raw)**: `ApiResult[BoxScoreV3, NflV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `NflV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScoreV3` | `sports_data/models/box_score_v3.py` |
| `NflV3StatsBoxScoreLiveFinalErrorBody` | `sports_data/errors/nfl_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_scores_by_week_final

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoresFinal/{season}/{week}`
- **Signature**: `def nfl_v3_stats_box_scores_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[BoxScoreV3]`
- **Returns (raw)**: `ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresByWeekFinalErrorBody]`
- **Error**: `NflV3StatsBoxScoresByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScoreV3` | `sports_data/models/box_score_v3.py` |
| `NflV3StatsBoxScoresByWeekFinalErrorBody` | `sports_data/errors/nfl_v3_stats_box_scores_by_week_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_scores_delta_by_week

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoresDeltaV3/{season}/{week}/{playerstoinclude}/{minutes}`
- **Signature**: `def nfl_v3_stats_box_scores_delta_by_week(format: FormatOrStr, season: str, week: str, playerstoinclude: PlayerstoincludeOrStr, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `playerstoinclude`, `minutes`
- **Params**: `format` — path · `season` — path · `week` — path · `playerstoinclude` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScoreV3]`
- **Returns (raw)**: `ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresDeltaByWeekErrorBody]`
- **Error**: `NflV3StatsBoxScoresDeltaByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerstoincludeOrStr` | `sports_data/models/enums/playerstoinclude.py` |
| `BoxScoreV3` | `sports_data/models/box_score_v3.py` |
| `NflV3StatsBoxScoresDeltaByWeekErrorBody` | `sports_data/errors/nfl_v3_stats_box_scores_delta_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_scores_simulation

- **Route**: `GET /v3/nfl/stats/{format}/SimulatedBoxScoresV3/{numberofplays}`
- **Signature**: `def nfl_v3_stats_box_scores_simulation(format: FormatOrStr, numberofplays: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `numberofplays`
- **Params**: `format` — path · `numberofplays` — path
- **Returns (parsed)**: `list[BoxScoreV3]`
- **Returns (raw)**: `ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresSimulationErrorBody]`
- **Error**: `NflV3StatsBoxScoresSimulationErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScoreV3` | `sports_data/models/box_score_v3.py` |
| `NflV3StatsBoxScoresSimulationErrorBody` | `sports_data/errors/nfl_v3_stats_box_scores_simulation_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_defense_game_stats_all

- **Route**: `GET /v3/nfl/stats/{format}/FantasyDefenseByGame/{season}/{week}`
- **Signature**: `def nfl_v3_stats_fantasy_defense_game_stats_all(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[FantasyDefenseGame]`
- **Returns (raw)**: `ApiResult[list[FantasyDefenseGame], NflV3StatsFantasyDefenseGameStatsAllErrorBody]`
- **Error**: `NflV3StatsFantasyDefenseGameStatsAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyDefenseGame` | `sports_data/models/fantasy_defense_game.py` |
| `NflV3StatsFantasyDefenseGameStatsAllErrorBody` | `sports_data/errors/nfl_v3_stats_fantasy_defense_game_stats_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_defense_game_stats_by_team

- **Route**: `GET /v3/nfl/stats/{format}/FantasyDefenseByGameByTeam/{season}/{week}/{team}`
- **Signature**: `def nfl_v3_stats_fantasy_defense_game_stats_by_team(format: FormatOrStr, season: str, week: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `team`
- **Params**: `format` — path · `season` — path · `week` — path · `team` — path
- **Returns (parsed)**: `FantasyDefenseGame`
- **Returns (raw)**: `ApiResult[FantasyDefenseGame, NflV3StatsFantasyDefenseGameStatsByTeamErrorBody]`
- **Error**: `NflV3StatsFantasyDefenseGameStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyDefenseGame` | `sports_data/models/fantasy_defense_game.py` |
| `NflV3StatsFantasyDefenseGameStatsByTeamErrorBody` | `sports_data/errors/nfl_v3_stats_fantasy_defense_game_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_defense_season_stats_all

- **Route**: `GET /v3/nfl/stats/{format}/FantasyDefenseBySeason/{season}`
- **Signature**: `def nfl_v3_stats_fantasy_defense_season_stats_all(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[FantasyDefenseSeason]`
- **Returns (raw)**: `ApiResult[list[FantasyDefenseSeason], NflV3StatsFantasyDefenseSeasonStatsAllErrorBody]`
- **Error**: `NflV3StatsFantasyDefenseSeasonStatsAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyDefenseSeason` | `sports_data/models/fantasy_defense_season.py` |
| `NflV3StatsFantasyDefenseSeasonStatsAllErrorBody` | `sports_data/errors/nfl_v3_stats_fantasy_defense_season_stats_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_defense_season_stats_by_team

- **Route**: `GET /v3/nfl/stats/{format}/FantasyDefenseBySeasonByTeam/{season}/{team}`
- **Signature**: `def nfl_v3_stats_fantasy_defense_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `FantasyDefenseSeason`
- **Returns (raw)**: `ApiResult[FantasyDefenseSeason, NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody]`
- **Error**: `NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyDefenseSeason` | `sports_data/models/fantasy_defense_season.py` |
| `NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody` | `sports_data/errors/nfl_v3_stats_fantasy_defense_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week

- **Route**: `GET /v3/nfl/stats/{format}/PlayerOwnership/{season}/{week}`
- **Signature**: `def nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerOwnership]`
- **Returns (raw)**: `ApiResult[list[PlayerOwnership], NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody]`
- **Error**: `NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerOwnership` | `sports_data/models/player_ownership.py` |
| `NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody` | `sports_data/errors/nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_points_by_week

- **Route**: `GET /v3/nfl/stats/{format}/FantasyGameStatsByWeek/{season}/{week}`
- **Signature**: `def nfl_v3_stats_fantasy_points_by_week(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[FantasyGame2]`
- **Returns (raw)**: `ApiResult[list[FantasyGame2], NflV3StatsFantasyPointsByWeekErrorBody]`
- **Error**: `NflV3StatsFantasyPointsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyGame2` | `sports_data/models/fantasy_game2.py` |
| `NflV3StatsFantasyPointsByWeekErrorBody` | `sports_data/errors/nfl_v3_stats_fantasy_points_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_games_by_season_final

- **Route**: `GET /v3/nfl/stats/{format}/ScoresFinal/{season}`
- **Signature**: `def nfl_v3_stats_games_by_season_final(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3StatsGamesBySeasonFinalErrorBody]`
- **Error**: `NflV3StatsGamesBySeasonFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Score` | `sports_data/models/score.py` |
| `NflV3StatsGamesBySeasonFinalErrorBody` | `sports_data/errors/nfl_v3_stats_games_by_season_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_injuries_all

- **Route**: `GET /v3/nfl/stats/{format}/Injuries/{season}/{week}`
- **Signature**: `def nfl_v3_stats_injuries_all(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[Injury]`
- **Returns (raw)**: `ApiResult[list[Injury], NflV3StatsInjuriesAllErrorBody]`
- **Error**: `NflV3StatsInjuriesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Injury` | `sports_data/models/injury.py` |
| `NflV3StatsInjuriesAllErrorBody` | `sports_data/errors/nfl_v3_stats_injuries_all_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_injuries_by_team

- **Route**: `GET /v3/nfl/stats/{format}/Injuries/{season}/{week}/{team}`
- **Signature**: `def nfl_v3_stats_injuries_by_team(format: FormatOrStr, season: str, week: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `team`
- **Params**: `format` — path · `season` — path · `week` — path · `team` — path
- **Returns (parsed)**: `list[Injury]`
- **Returns (raw)**: `ApiResult[list[Injury], NflV3StatsInjuriesByTeamErrorBody]`
- **Error**: `NflV3StatsInjuriesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Injury` | `sports_data/models/injury.py` |
| `NflV3StatsInjuriesByTeamErrorBody` | `sports_data/errors/nfl_v3_stats_injuries_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Signature**: `def nfl_v3_stats_player_game_logs_by_season(format: FormatOrStr, season: str, playerid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `playerid`, `numberofgames`
- **Params**: `format` — path · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame4]`
- **Returns (raw)**: `ApiResult[list[PlayerGame4], NflV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `NflV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame4` | `sports_data/models/player_game4.py` |
| `NflV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data/errors/nfl_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_red_zone_stats

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameRedZoneStats/{season}/{week}`
- **Signature**: `def nfl_v3_stats_player_game_red_zone_stats(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGameRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsErrorBody]`
- **Error**: `NflV3StatsPlayerGameRedZoneStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameRedZone` | `sports_data/models/player_game_red_zone.py` |
| `NflV3StatsPlayerGameRedZoneStatsErrorBody` | `sports_data/errors/nfl_v3_stats_player_game_red_zone_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_red_zone_stats_inside_five

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameRedZoneInsideFiveStats/{season}/{week}`
- **Signature**: `def nfl_v3_stats_player_game_red_zone_stats_inside_five(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGameRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsInsideFiveErrorBody]`
- **Error**: `NflV3StatsPlayerGameRedZoneStatsInsideFiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameRedZone` | `sports_data/models/player_game_red_zone.py` |
| `NflV3StatsPlayerGameRedZoneStatsInsideFiveErrorBody` | `sports_data/errors/nfl_v3_stats_player_game_red_zone_stats_inside_five_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_red_zone_stats_inside_ten

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameRedZoneInsideTenStats/{season}/{week}`
- **Signature**: `def nfl_v3_stats_player_game_red_zone_stats_inside_ten(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGameRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsInsideTenErrorBody]`
- **Error**: `NflV3StatsPlayerGameRedZoneStatsInsideTenErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameRedZone` | `sports_data/models/player_game_red_zone.py` |
| `NflV3StatsPlayerGameRedZoneStatsInsideTenErrorBody` | `sports_data/errors/nfl_v3_stats_player_game_red_zone_stats_inside_ten_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_by_team_final

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsByTeamFinal/{season}/{week}/{team}`
- **Signature**: `def nfl_v3_stats_player_game_stats_by_team_final(format: FormatOrStr, season: str, week: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `team`
- **Params**: `format` — path · `season` — path · `week` — path · `team` — path
- **Returns (parsed)**: `list[PlayerGame4]`
- **Returns (raw)**: `ApiResult[list[PlayerGame4], NflV3StatsPlayerGameStatsByTeamFinalErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsByTeamFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame4` | `sports_data/models/player_game4.py` |
| `NflV3StatsPlayerGameStatsByTeamFinalErrorBody` | `sports_data/errors/nfl_v3_stats_player_game_stats_by_team_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_by_team_live_final

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsByTeam/{season}/{week}/{team}`
- **Signature**: `def nfl_v3_stats_player_game_stats_by_team_live_final(format: FormatOrStr, season: str, week: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `team`
- **Params**: `format` — path · `season` — path · `week` — path · `team` — path
- **Returns (parsed)**: `list[PlayerGame4]`
- **Returns (raw)**: `ApiResult[list[PlayerGame4], NflV3StatsPlayerGameStatsByTeamLiveFinalErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsByTeamLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame4` | `sports_data/models/player_game4.py` |
| `NflV3StatsPlayerGameStatsByTeamLiveFinalErrorBody` | `sports_data/errors/nfl_v3_stats_player_game_stats_by_team_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_by_week_final

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsByWeekFinal/{season}/{week}`
- **Signature**: `def nfl_v3_stats_player_game_stats_by_week_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGame4]`
- **Returns (raw)**: `ApiResult[list[PlayerGame4], NflV3StatsPlayerGameStatsByWeekFinalErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame4` | `sports_data/models/player_game4.py` |
| `NflV3StatsPlayerGameStatsByWeekFinalErrorBody` | `sports_data/errors/nfl_v3_stats_player_game_stats_by_week_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_by_week_live_final

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsByWeek/{season}/{week}`
- **Signature**: `def nfl_v3_stats_player_game_stats_by_week_live_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGame4]`
- **Returns (raw)**: `ApiResult[list[PlayerGame4], NflV3StatsPlayerGameStatsByWeekLiveFinalErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame4` | `sports_data/models/player_game4.py` |
| `NflV3StatsPlayerGameStatsByWeekLiveFinalErrorBody` | `sports_data/errors/nfl_v3_stats_player_game_stats_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_delta

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsDelta/{minutes}`
- **Signature**: `def nfl_v3_stats_player_game_stats_delta(format: FormatOrStr, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `minutes`
- **Params**: `format` — path · `minutes` — path
- **Returns (parsed)**: `list[PlayerGame4]`
- **Returns (raw)**: `ApiResult[list[PlayerGame4], NflV3StatsPlayerGameStatsDeltaErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsDeltaErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame4` | `sports_data/models/player_game4.py` |
| `NflV3StatsPlayerGameStatsDeltaErrorBody` | `sports_data/errors/nfl_v3_stats_player_game_stats_delta_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_delta_by_week

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsByWeekDelta/{season}/{week}/{minutes}`
- **Signature**: `def nfl_v3_stats_player_game_stats_delta_by_week(format: FormatOrStr, season: str, week: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`, `minutes`
- **Params**: `format` — path · `season` — path · `week` — path · `minutes` — path
- **Returns (parsed)**: `list[PlayerGame4]`
- **Returns (raw)**: `ApiResult[list[PlayerGame4], NflV3StatsPlayerGameStatsDeltaByWeekErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsDeltaByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame4` | `sports_data/models/player_game4.py` |
| `NflV3StatsPlayerGameStatsDeltaByWeekErrorBody` | `sports_data/errors/nfl_v3_stats_player_game_stats_delta_by_week_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_red_zone_stats

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonRedZoneStats/{season}`
- **Signature**: `def nfl_v3_stats_player_season_red_zone_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonRedZoneStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeasonRedZone` | `sports_data/models/player_season_red_zone.py` |
| `NflV3StatsPlayerSeasonRedZoneStatsErrorBody` | `sports_data/errors/nfl_v3_stats_player_season_red_zone_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_red_zone_stats_inside_five

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonRedZoneInsideFiveStats/{season}`
- **Signature**: `def nfl_v3_stats_player_season_red_zone_stats_inside_five(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsInsideFiveErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonRedZoneStatsInsideFiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeasonRedZone` | `sports_data/models/player_season_red_zone.py` |
| `NflV3StatsPlayerSeasonRedZoneStatsInsideFiveErrorBody` | `sports_data/errors/nfl_v3_stats_player_season_red_zone_stats_inside_five_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_red_zone_stats_inside_ten

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonRedZoneInsideTenStats/{season}`
- **Signature**: `def nfl_v3_stats_player_season_red_zone_stats_inside_ten(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeasonRedZone` | `sports_data/models/player_season_red_zone.py` |
| `NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody` | `sports_data/errors/nfl_v3_stats_player_season_red_zone_stats_inside_ten_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_stats

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonStats/{season}`
- **Signature**: `def nfl_v3_stats_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason5]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason5], NflV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason5` | `sports_data/models/player_season5.py` |
| `NflV3StatsPlayerSeasonStatsErrorBody` | `sports_data/errors/nfl_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Signature**: `def nfl_v3_stats_player_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `team`
- **Params**: `format` — path · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason5]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason5], NflV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeason5` | `sports_data/models/player_season5.py` |
| `NflV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data/errors/nfl_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_third_down_stats

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonThirdDownStats/{season}`
- **Signature**: `def nfl_v3_stats_player_season_third_down_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonThirdDown]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonThirdDown], NflV3StatsPlayerSeasonThirdDownStatsErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonThirdDownStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerSeasonThirdDown` | `sports_data/models/player_season_third_down.py` |
| `NflV3StatsPlayerSeasonThirdDownStatsErrorBody` | `sports_data/errors/nfl_v3_stats_player_season_third_down_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_pro_bowlers

- **Route**: `GET /v3/nfl/stats/{format}/ProBowlers/{season}`
- **Signature**: `def nfl_v3_stats_pro_bowlers(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerInfo]`
- **Returns (raw)**: `ApiResult[list[PlayerInfo], NflV3StatsProBowlersErrorBody]`
- **Error**: `NflV3StatsProBowlersErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerInfo` | `sports_data/models/player_info.py` |
| `NflV3StatsProBowlersErrorBody` | `sports_data/errors/nfl_v3_stats_pro_bowlers_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_team_game_stats_by_game_final

- **Route**: `GET /v3/nfl/stats/{format}/TeamGameStatsFinal/{season}/{week}`
- **Signature**: `def nfl_v3_stats_team_game_stats_by_game_final(format: FormatOrStr, season: str, week: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`, `week`
- **Params**: `format` — path · `season` — path · `week` — path
- **Returns (parsed)**: `list[TeamGame4]`
- **Returns (raw)**: `ApiResult[list[TeamGame4], NflV3StatsTeamGameStatsByGameFinalErrorBody]`
- **Error**: `NflV3StatsTeamGameStatsByGameFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame4` | `sports_data/models/team_game4.py` |
| `NflV3StatsTeamGameStatsByGameFinalErrorBody` | `sports_data/errors/nfl_v3_stats_team_game_stats_by_game_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

