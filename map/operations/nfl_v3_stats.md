<!-- Generated file — do not edit; regenerated with the SDK. -->

# NflV3Stats — operations

Accessor: `client.nfl_v3_stats` · Source: `sports_data_io/apis/nfl_v3_stats.py` · 34 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nfl_v3_stats.nfl_v3_stats_box_score_by_team_final

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoreByTeamFinal/{season}/{week}/{hometeam}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_box_score_by_team_final(season: str, week: str, hometeam: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `hometeam`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `hometeam` — path
- **Returns (parsed)**: `BoxScoreV3`
- **Returns (raw)**: `ApiResult[BoxScoreV3, NflV3StatsBoxScoreByTeamFinalErrorBody]`
- **Error**: `NflV3StatsBoxScoreByTeamFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScoreV3` | `sports_data_io/models/box_score_v3.py` |
| `NflV3StatsBoxScoreByTeamFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_box_score_by_team_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_score_by_team_live_final

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoreV3/{season}/{week}/{hometeam}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_box_score_by_team_live_final(season: str, week: str, hometeam: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `hometeam`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `hometeam` — path
- **Returns (parsed)**: `BoxScoreV3`
- **Returns (raw)**: `ApiResult[BoxScoreV3, NflV3StatsBoxScoreByTeamLiveFinalErrorBody]`
- **Error**: `NflV3StatsBoxScoreByTeamLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScoreV3` | `sports_data_io/models/box_score_v3.py` |
| `NflV3StatsBoxScoreByTeamLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_box_score_by_team_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_score_final

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoreFinal/{scoreid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_box_score_final(scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`
- **Params**: `format_` — path `format` · `scoreid` — path
- **Returns (parsed)**: `BoxScoreV3`
- **Returns (raw)**: `ApiResult[BoxScoreV3, NflV3StatsBoxScoreFinalErrorBody]`
- **Error**: `NflV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScoreV3` | `sports_data_io/models/box_score_v3.py` |
| `NflV3StatsBoxScoreFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_score_live_final

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoreByScoreIDV3/{scoreid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_box_score_live_final(scoreid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `scoreid`
- **Params**: `format_` — path `format` · `scoreid` — path
- **Returns (parsed)**: `BoxScoreV3`
- **Returns (raw)**: `ApiResult[BoxScoreV3, NflV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `NflV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScoreV3` | `sports_data_io/models/box_score_v3.py` |
| `NflV3StatsBoxScoreLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_scores_by_week_final

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoresFinal/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_box_scores_by_week_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[BoxScoreV3]`
- **Returns (raw)**: `ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresByWeekFinalErrorBody]`
- **Error**: `NflV3StatsBoxScoresByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScoreV3` | `sports_data_io/models/box_score_v3.py` |
| `NflV3StatsBoxScoresByWeekFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_box_scores_by_week_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_scores_delta_by_week

- **Route**: `GET /v3/nfl/stats/{format}/BoxScoresDeltaV3/{season}/{week}/{playerstoinclude}/{minutes}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_box_scores_delta_by_week(season: str, week: str, minutes: str, *, format_: FormatOrStr = Format.JSON, playerstoinclude: PlayerstoincludeOrStr = Playerstoinclude.ALL, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `minutes`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `playerstoinclude` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScoreV3]`
- **Returns (raw)**: `ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresDeltaByWeekErrorBody]`
- **Error**: `NflV3StatsBoxScoresDeltaByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerstoincludeOrStr` | `sports_data_io/models/enums/playerstoinclude.py` |
| `BoxScoreV3` | `sports_data_io/models/box_score_v3.py` |
| `NflV3StatsBoxScoresDeltaByWeekErrorBody` | `sports_data_io/errors/nfl_v3_stats_box_scores_delta_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_box_scores_simulation

- **Route**: `GET /v3/nfl/stats/{format}/SimulatedBoxScoresV3/{numberofplays}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_box_scores_simulation(numberofplays: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `numberofplays`
- **Params**: `format_` — path `format` · `numberofplays` — path
- **Returns (parsed)**: `list[BoxScoreV3]`
- **Returns (raw)**: `ApiResult[list[BoxScoreV3], NflV3StatsBoxScoresSimulationErrorBody]`
- **Error**: `NflV3StatsBoxScoresSimulationErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScoreV3` | `sports_data_io/models/box_score_v3.py` |
| `NflV3StatsBoxScoresSimulationErrorBody` | `sports_data_io/errors/nfl_v3_stats_box_scores_simulation_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_defense_game_stats_all

- **Route**: `GET /v3/nfl/stats/{format}/FantasyDefenseByGame/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_fantasy_defense_game_stats_all(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[FantasyDefenseGame]`
- **Returns (raw)**: `ApiResult[list[FantasyDefenseGame], NflV3StatsFantasyDefenseGameStatsAllErrorBody]`
- **Error**: `NflV3StatsFantasyDefenseGameStatsAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FantasyDefenseGame` | `sports_data_io/models/fantasy_defense_game.py` |
| `NflV3StatsFantasyDefenseGameStatsAllErrorBody` | `sports_data_io/errors/nfl_v3_stats_fantasy_defense_game_stats_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_defense_game_stats_by_team

- **Route**: `GET /v3/nfl/stats/{format}/FantasyDefenseByGameByTeam/{season}/{week}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_fantasy_defense_game_stats_by_team(season: str, week: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `team`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `team` — path
- **Returns (parsed)**: `FantasyDefenseGame`
- **Returns (raw)**: `ApiResult[FantasyDefenseGame, NflV3StatsFantasyDefenseGameStatsByTeamErrorBody]`
- **Error**: `NflV3StatsFantasyDefenseGameStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FantasyDefenseGame` | `sports_data_io/models/fantasy_defense_game.py` |
| `NflV3StatsFantasyDefenseGameStatsByTeamErrorBody` | `sports_data_io/errors/nfl_v3_stats_fantasy_defense_game_stats_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_defense_season_stats_all

- **Route**: `GET /v3/nfl/stats/{format}/FantasyDefenseBySeason/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_fantasy_defense_season_stats_all(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[FantasyDefenseSeason]`
- **Returns (raw)**: `ApiResult[list[FantasyDefenseSeason], NflV3StatsFantasyDefenseSeasonStatsAllErrorBody]`
- **Error**: `NflV3StatsFantasyDefenseSeasonStatsAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FantasyDefenseSeason` | `sports_data_io/models/fantasy_defense_season.py` |
| `NflV3StatsFantasyDefenseSeasonStatsAllErrorBody` | `sports_data_io/errors/nfl_v3_stats_fantasy_defense_season_stats_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_defense_season_stats_by_team

- **Route**: `GET /v3/nfl/stats/{format}/FantasyDefenseBySeasonByTeam/{season}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_fantasy_defense_season_stats_by_team(season: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `team`
- **Params**: `format_` — path `format` · `season` — path · `team` — path
- **Returns (parsed)**: `FantasyDefenseSeason`
- **Returns (raw)**: `ApiResult[FantasyDefenseSeason, NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody]`
- **Error**: `NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FantasyDefenseSeason` | `sports_data_io/models/fantasy_defense_season.py` |
| `NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody` | `sports_data_io/errors/nfl_v3_stats_fantasy_defense_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week

- **Route**: `GET /v3/nfl/stats/{format}/PlayerOwnership/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerOwnership]`
- **Returns (raw)**: `ApiResult[list[PlayerOwnership], NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody]`
- **Error**: `NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerOwnership` | `sports_data_io/models/player_ownership.py` |
| `NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody` | `sports_data_io/errors/nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_fantasy_points_by_week

- **Route**: `GET /v3/nfl/stats/{format}/FantasyGameStatsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_fantasy_points_by_week(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[FantasyGame]`
- **Returns (raw)**: `ApiResult[list[FantasyGame], NflV3StatsFantasyPointsByWeekErrorBody]`
- **Error**: `NflV3StatsFantasyPointsByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FantasyGame` | `sports_data_io/models/fantasy_game.py` |
| `NflV3StatsFantasyPointsByWeekErrorBody` | `sports_data_io/errors/nfl_v3_stats_fantasy_points_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_games_by_season_final

- **Route**: `GET /v3/nfl/stats/{format}/ScoresFinal/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_games_by_season_final(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[Score]`
- **Returns (raw)**: `ApiResult[list[Score], NflV3StatsGamesBySeasonFinalErrorBody]`
- **Error**: `NflV3StatsGamesBySeasonFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Score` | `sports_data_io/models/score.py` |
| `NflV3StatsGamesBySeasonFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_games_by_season_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_injuries_all

- **Route**: `GET /v3/nfl/stats/{format}/Injuries/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_injuries_all(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[Injury]`
- **Returns (raw)**: `ApiResult[list[Injury], NflV3StatsInjuriesAllErrorBody]`
- **Error**: `NflV3StatsInjuriesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Injury` | `sports_data_io/models/injury.py` |
| `NflV3StatsInjuriesAllErrorBody` | `sports_data_io/errors/nfl_v3_stats_injuries_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_injuries_by_team

- **Route**: `GET /v3/nfl/stats/{format}/Injuries/{season}/{week}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_injuries_by_team(season: str, week: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `team`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `team` — path
- **Returns (parsed)**: `list[Injury]`
- **Returns (raw)**: `ApiResult[list[Injury], NflV3StatsInjuriesByTeamErrorBody]`
- **Error**: `NflV3StatsInjuriesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Injury` | `sports_data_io/models/injury.py` |
| `NflV3StatsInjuriesByTeamErrorBody` | `sports_data_io/errors/nfl_v3_stats_injuries_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_game_logs_by_season(season: str, playerid: str, numberofgames: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `playerid`, `numberofgames`
- **Params**: `format_` — path `format` · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame]`
- **Returns (raw)**: `ApiResult[list[PlayerGame], NflV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `NflV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame` | `sports_data_io/models/player_game.py` |
| `NflV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_red_zone_stats

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameRedZoneStats/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_game_red_zone_stats(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGameRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsErrorBody]`
- **Error**: `NflV3StatsPlayerGameRedZoneStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGameRedZone` | `sports_data_io/models/player_game_red_zone.py` |
| `NflV3StatsPlayerGameRedZoneStatsErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_game_red_zone_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_red_zone_stats_inside_five

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameRedZoneInsideFiveStats/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_game_red_zone_stats_inside_five(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGameRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsInsideFiveErrorBody]`
- **Error**: `NflV3StatsPlayerGameRedZoneStatsInsideFiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGameRedZone` | `sports_data_io/models/player_game_red_zone.py` |
| `NflV3StatsPlayerGameRedZoneStatsInsideFiveErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_game_red_zone_stats_inside_five_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_red_zone_stats_inside_ten

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameRedZoneInsideTenStats/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_game_red_zone_stats_inside_ten(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGameRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerGameRedZone], NflV3StatsPlayerGameRedZoneStatsInsideTenErrorBody]`
- **Error**: `NflV3StatsPlayerGameRedZoneStatsInsideTenErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGameRedZone` | `sports_data_io/models/player_game_red_zone.py` |
| `NflV3StatsPlayerGameRedZoneStatsInsideTenErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_game_red_zone_stats_inside_ten_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_by_team_final

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsByTeamFinal/{season}/{week}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_game_stats_by_team_final(season: str, week: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `team`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `team` — path
- **Returns (parsed)**: `list[PlayerGame]`
- **Returns (raw)**: `ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByTeamFinalErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsByTeamFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame` | `sports_data_io/models/player_game.py` |
| `NflV3StatsPlayerGameStatsByTeamFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_game_stats_by_team_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_by_team_live_final

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsByTeam/{season}/{week}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_game_stats_by_team_live_final(season: str, week: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `team`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `team` — path
- **Returns (parsed)**: `list[PlayerGame]`
- **Returns (raw)**: `ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByTeamLiveFinalErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsByTeamLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame` | `sports_data_io/models/player_game.py` |
| `NflV3StatsPlayerGameStatsByTeamLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_game_stats_by_team_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_by_week_final

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsByWeekFinal/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_game_stats_by_week_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGame]`
- **Returns (raw)**: `ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByWeekFinalErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsByWeekFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame` | `sports_data_io/models/player_game.py` |
| `NflV3StatsPlayerGameStatsByWeekFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_game_stats_by_week_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_by_week_live_final

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsByWeek/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_game_stats_by_week_live_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[PlayerGame]`
- **Returns (raw)**: `ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsByWeekLiveFinalErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsByWeekLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame` | `sports_data_io/models/player_game.py` |
| `NflV3StatsPlayerGameStatsByWeekLiveFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_game_stats_by_week_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_delta

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsDelta/{minutes}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_game_stats_delta(minutes: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `minutes`
- **Params**: `format_` — path `format` · `minutes` — path
- **Returns (parsed)**: `list[PlayerGame]`
- **Returns (raw)**: `ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsDeltaErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsDeltaErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame` | `sports_data_io/models/player_game.py` |
| `NflV3StatsPlayerGameStatsDeltaErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_game_stats_delta_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_game_stats_delta_by_week

- **Route**: `GET /v3/nfl/stats/{format}/PlayerGameStatsByWeekDelta/{season}/{week}/{minutes}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_game_stats_delta_by_week(season: str, week: str, minutes: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`, `minutes`
- **Params**: `format_` — path `format` · `season` — path · `week` — path · `minutes` — path
- **Returns (parsed)**: `list[PlayerGame]`
- **Returns (raw)**: `ApiResult[list[PlayerGame], NflV3StatsPlayerGameStatsDeltaByWeekErrorBody]`
- **Error**: `NflV3StatsPlayerGameStatsDeltaByWeekErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame` | `sports_data_io/models/player_game.py` |
| `NflV3StatsPlayerGameStatsDeltaByWeekErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_game_stats_delta_by_week_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_red_zone_stats

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonRedZoneStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_season_red_zone_stats(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonRedZoneStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeasonRedZone` | `sports_data_io/models/player_season_red_zone.py` |
| `NflV3StatsPlayerSeasonRedZoneStatsErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_season_red_zone_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_red_zone_stats_inside_five

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonRedZoneInsideFiveStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_season_red_zone_stats_inside_five(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsInsideFiveErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonRedZoneStatsInsideFiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeasonRedZone` | `sports_data_io/models/player_season_red_zone.py` |
| `NflV3StatsPlayerSeasonRedZoneStatsInsideFiveErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_season_red_zone_stats_inside_five_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_red_zone_stats_inside_ten

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonRedZoneInsideTenStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_season_red_zone_stats_inside_ten(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonRedZone]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonRedZone], NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeasonRedZone` | `sports_data_io/models/player_season_red_zone.py` |
| `NflV3StatsPlayerSeasonRedZoneStatsInsideTenErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_season_red_zone_stats_inside_ten_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_stats

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_season_stats(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerSeason]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason], NflV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason` | `sports_data_io/models/player_season.py` |
| `NflV3StatsPlayerSeasonStatsErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_season_stats_by_team(season: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `team`
- **Params**: `format_` — path `format` · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason], NflV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason` | `sports_data_io/models/player_season.py` |
| `NflV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_player_season_third_down_stats

- **Route**: `GET /v3/nfl/stats/{format}/PlayerSeasonThirdDownStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_player_season_third_down_stats(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerSeasonThirdDown]`
- **Returns (raw)**: `ApiResult[list[PlayerSeasonThirdDown], NflV3StatsPlayerSeasonThirdDownStatsErrorBody]`
- **Error**: `NflV3StatsPlayerSeasonThirdDownStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeasonThirdDown` | `sports_data_io/models/player_season_third_down.py` |
| `NflV3StatsPlayerSeasonThirdDownStatsErrorBody` | `sports_data_io/errors/nfl_v3_stats_player_season_third_down_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_pro_bowlers

- **Route**: `GET /v3/nfl/stats/{format}/ProBowlers/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_pro_bowlers(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerInfo]`
- **Returns (raw)**: `ApiResult[list[PlayerInfo], NflV3StatsProBowlersErrorBody]`
- **Error**: `NflV3StatsProBowlersErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerInfo` | `sports_data_io/models/player_info.py` |
| `NflV3StatsProBowlersErrorBody` | `sports_data_io/errors/nfl_v3_stats_pro_bowlers_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_stats.nfl_v3_stats_team_game_stats_by_game_final

- **Route**: `GET /v3/nfl/stats/{format}/TeamGameStatsFinal/{season}/{week}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_stats_team_game_stats_by_game_final(season: str, week: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `week`
- **Params**: `format_` — path `format` · `season` — path · `week` — path
- **Returns (parsed)**: `list[TeamGame]`
- **Returns (raw)**: `ApiResult[list[TeamGame], NflV3StatsTeamGameStatsByGameFinalErrorBody]`
- **Error**: `NflV3StatsTeamGameStatsByGameFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame` | `sports_data_io/models/team_game.py` |
| `NflV3StatsTeamGameStatsByGameFinalErrorBody` | `sports_data_io/errors/nfl_v3_stats_team_game_stats_by_game_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

