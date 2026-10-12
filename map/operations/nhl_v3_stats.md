<!-- Generated file — do not edit; regenerated with the SDK. -->

# NhlV3Stats — operations

Accessor: `client.nhl_v3_stats` · Source: `sports_data_io/apis/nhl_v3_stats.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nhl_v3_stats.nhl_v3_stats_box_score_final

- **Route**: `GET /v3/nhl/stats/{format}/BoxScoreFinal/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_box_score_final(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `BoxScore2`
- **Returns (raw)**: `ApiResult[BoxScore2, NhlV3StatsBoxScoreFinalErrorBody]`
- **Error**: `NhlV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore2` | `sports_data_io/models/box_score2.py` |
| `NhlV3StatsBoxScoreFinalErrorBody` | `sports_data_io/errors/nhl_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_box_score_live_final

- **Route**: `GET /v3/nhl/stats/{format}/BoxScore/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_box_score_live_final(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `BoxScore2`
- **Returns (raw)**: `ApiResult[BoxScore2, NhlV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `NhlV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore2` | `sports_data_io/models/box_score2.py` |
| `NhlV3StatsBoxScoreLiveFinalErrorBody` | `sports_data_io/errors/nhl_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_box_scores_by_date_final

- **Route**: `GET /v3/nhl/stats/{format}/BoxScoresFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_box_scores_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[BoxScore2]`
- **Returns (raw)**: `ApiResult[list[BoxScore2], NhlV3StatsBoxScoresByDateFinalErrorBody]`
- **Error**: `NhlV3StatsBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore2` | `sports_data_io/models/box_score2.py` |
| `NhlV3StatsBoxScoresByDateFinalErrorBody` | `sports_data_io/errors/nhl_v3_stats_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_box_scores_by_date_live_final

- **Route**: `GET /v3/nhl/stats/{format}/BoxScores/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_box_scores_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[BoxScore2]`
- **Returns (raw)**: `ApiResult[list[BoxScore2], NhlV3StatsBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `NhlV3StatsBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore2` | `sports_data_io/models/box_score2.py` |
| `NhlV3StatsBoxScoresByDateLiveFinalErrorBody` | `sports_data_io/errors/nhl_v3_stats_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_box_scores_delta_by_date

- **Route**: `GET /v3/nhl/stats/{format}/BoxScoresDelta/{date}/{minutes}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_box_scores_delta_by_date(date: str, minutes: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`, `minutes`
- **Params**: `format_` — path `format` · `date` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScore2]`
- **Returns (raw)**: `ApiResult[list[BoxScore2], NhlV3StatsBoxScoresDeltaByDateErrorBody]`
- **Error**: `NhlV3StatsBoxScoresDeltaByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore2` | `sports_data_io/models/box_score2.py` |
| `NhlV3StatsBoxScoresDeltaByDateErrorBody` | `sports_data_io/errors/nhl_v3_stats_box_scores_delta_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_fantasy_points_by_date

- **Route**: `GET /v3/nhl/stats/{format}/FantasyGameStatsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_fantasy_points_by_date(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[FantasyGame3]`
- **Returns (raw)**: `ApiResult[list[FantasyGame3], NhlV3StatsFantasyPointsByDateErrorBody]`
- **Error**: `NhlV3StatsFantasyPointsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FantasyGame3` | `sports_data_io/models/fantasy_game3.py` |
| `NhlV3StatsFantasyPointsByDateErrorBody` | `sports_data_io/errors/nhl_v3_stats_fantasy_points_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_line_combinations_by_season

- **Route**: `GET /v3/nhl/stats/{format}/LinesBySeason/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_line_combinations_by_season(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[TeamLine]`
- **Returns (raw)**: `ApiResult[list[TeamLine], NhlV3StatsLineCombinationsBySeasonErrorBody]`
- **Error**: `NhlV3StatsLineCombinationsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamLine` | `sports_data_io/models/team_line.py` |
| `NhlV3StatsLineCombinationsBySeasonErrorBody` | `sports_data_io/errors/nhl_v3_stats_line_combinations_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/nhl/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_player_game_logs_by_season(season: str, playerid: str, numberofgames: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `playerid`, `numberofgames`
- **Params**: `format_` — path `format` · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame3]`
- **Returns (raw)**: `ApiResult[list[PlayerGame3], NhlV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `NhlV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame3` | `sports_data_io/models/player_game3.py` |
| `NhlV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data_io/errors/nhl_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_player_game_stats_by_date_final

- **Route**: `GET /v3/nhl/stats/{format}/PlayerGameStatsByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_player_game_stats_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[PlayerGame3]`
- **Returns (raw)**: `ApiResult[list[PlayerGame3], NhlV3StatsPlayerGameStatsByDateFinalErrorBody]`
- **Error**: `NhlV3StatsPlayerGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame3` | `sports_data_io/models/player_game3.py` |
| `NhlV3StatsPlayerGameStatsByDateFinalErrorBody` | `sports_data_io/errors/nhl_v3_stats_player_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_player_game_stats_by_date_live_final

- **Route**: `GET /v3/nhl/stats/{format}/PlayerGameStatsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_player_game_stats_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[PlayerGame3]`
- **Returns (raw)**: `ApiResult[list[PlayerGame3], NhlV3StatsPlayerGameStatsByDateLiveFinalErrorBody]`
- **Error**: `NhlV3StatsPlayerGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame3` | `sports_data_io/models/player_game3.py` |
| `NhlV3StatsPlayerGameStatsByDateLiveFinalErrorBody` | `sports_data_io/errors/nhl_v3_stats_player_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_player_season_stats

- **Route**: `GET /v3/nhl/stats/{format}/PlayerSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_player_season_stats(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerSeason4]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason4], NhlV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `NhlV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason4` | `sports_data_io/models/player_season4.py` |
| `NhlV3StatsPlayerSeasonStatsErrorBody` | `sports_data_io/errors/nhl_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/nhl/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_player_season_stats_by_team(season: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `team`
- **Params**: `format_` — path `format` · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason4]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason4], NhlV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `NhlV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason4` | `sports_data_io/models/player_season4.py` |
| `NhlV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data_io/errors/nhl_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_team_game_stats_by_date_final

- **Route**: `GET /v3/nhl/stats/{format}/TeamGameStatsByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_team_game_stats_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[TeamGame3]`
- **Returns (raw)**: `ApiResult[list[TeamGame3], NhlV3StatsTeamGameStatsByDateFinalErrorBody]`
- **Error**: `NhlV3StatsTeamGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame3` | `sports_data_io/models/team_game3.py` |
| `NhlV3StatsTeamGameStatsByDateFinalErrorBody` | `sports_data_io/errors/nhl_v3_stats_team_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_stats.nhl_v3_stats_team_stats_allowed_by_position

- **Route**: `GET /v3/nhl/stats/{format}/TeamStatsAllowedByPosition/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_stats_team_stats_allowed_by_position(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[TeamSeason3]`
- **Returns (raw)**: `ApiResult[list[TeamSeason3], NhlV3StatsTeamStatsAllowedByPositionErrorBody]`
- **Error**: `NhlV3StatsTeamStatsAllowedByPositionErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamSeason3` | `sports_data_io/models/team_season3.py` |
| `NhlV3StatsTeamStatsAllowedByPositionErrorBody` | `sports_data_io/errors/nhl_v3_stats_team_stats_allowed_by_position_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

