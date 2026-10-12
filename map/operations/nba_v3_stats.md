<!-- Generated file — do not edit; regenerated with the SDK. -->

# NbaV3Stats — operations

Accessor: `client.nba_v3_stats` · Source: `sports_data_io/apis/nba_v3_stats.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nba_v3_stats.nba_v3_stats_all_stars

- **Route**: `GET /v3/nba/stats/{format}/AllStars/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_all_stars(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerInfo]`
- **Returns (raw)**: `ApiResult[list[PlayerInfo], NbaV3StatsAllStarsErrorBody]`
- **Error**: `NbaV3StatsAllStarsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerInfo` | `sports_data_io/models/player_info.py` |
| `NbaV3StatsAllStarsErrorBody` | `sports_data_io/errors/nba_v3_stats_all_stars_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_box_score_final

- **Route**: `GET /v3/nba/stats/{format}/BoxScoreFinal/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_box_score_final(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `BoxScore`
- **Returns (raw)**: `ApiResult[BoxScore, NbaV3StatsBoxScoreFinalErrorBody]`
- **Error**: `NbaV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore` | `sports_data_io/models/box_score.py` |
| `NbaV3StatsBoxScoreFinalErrorBody` | `sports_data_io/errors/nba_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_box_score_live_final

- **Route**: `GET /v3/nba/stats/{format}/BoxScore/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_box_score_live_final(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `BoxScore`
- **Returns (raw)**: `ApiResult[BoxScore, NbaV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `NbaV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore` | `sports_data_io/models/box_score.py` |
| `NbaV3StatsBoxScoreLiveFinalErrorBody` | `sports_data_io/errors/nba_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_box_scores_by_date_final

- **Route**: `GET /v3/nba/stats/{format}/BoxScoresFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_box_scores_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[BoxScore]`
- **Returns (raw)**: `ApiResult[list[BoxScore], NbaV3StatsBoxScoresByDateFinalErrorBody]`
- **Error**: `NbaV3StatsBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore` | `sports_data_io/models/box_score.py` |
| `NbaV3StatsBoxScoresByDateFinalErrorBody` | `sports_data_io/errors/nba_v3_stats_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_box_scores_by_date_live_final

- **Route**: `GET /v3/nba/stats/{format}/BoxScores/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_box_scores_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[BoxScore]`
- **Returns (raw)**: `ApiResult[list[BoxScore], NbaV3StatsBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `NbaV3StatsBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore` | `sports_data_io/models/box_score.py` |
| `NbaV3StatsBoxScoresByDateLiveFinalErrorBody` | `sports_data_io/errors/nba_v3_stats_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_box_scores_delta_by_date

- **Route**: `GET /v3/nba/stats/{format}/BoxScoresDelta/{date}/{minutes}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_box_scores_delta_by_date(date: str, minutes: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`, `minutes`
- **Params**: `format_` — path `format` · `date` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScore]`
- **Returns (raw)**: `ApiResult[list[BoxScore], NbaV3StatsBoxScoresDeltaByDateErrorBody]`
- **Error**: `NbaV3StatsBoxScoresDeltaByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore` | `sports_data_io/models/box_score.py` |
| `NbaV3StatsBoxScoresDeltaByDateErrorBody` | `sports_data_io/errors/nba_v3_stats_box_scores_delta_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_fantasy_points_by_date

- **Route**: `GET /v3/nba/stats/{format}/FantasyGameStatsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_fantasy_points_by_date(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[FantasyGame1]`
- **Returns (raw)**: `ApiResult[list[FantasyGame1], NbaV3StatsFantasyPointsByDateErrorBody]`
- **Error**: `NbaV3StatsFantasyPointsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FantasyGame1` | `sports_data_io/models/fantasy_game1.py` |
| `NbaV3StatsFantasyPointsByDateErrorBody` | `sports_data_io/errors/nba_v3_stats_fantasy_points_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/nba/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_player_game_logs_by_season(season: str, playerid: str, numberofgames: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `playerid`, `numberofgames`
- **Params**: `format_` — path `format` · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame1]`
- **Returns (raw)**: `ApiResult[list[PlayerGame1], NbaV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `NbaV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame1` | `sports_data_io/models/player_game1.py` |
| `NbaV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data_io/errors/nba_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_player_game_stats_by_date_final

- **Route**: `GET /v3/nba/stats/{format}/PlayerGameStatsByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_player_game_stats_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[PlayerGame1]`
- **Returns (raw)**: `ApiResult[list[PlayerGame1], NbaV3StatsPlayerGameStatsByDateFinalErrorBody]`
- **Error**: `NbaV3StatsPlayerGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame1` | `sports_data_io/models/player_game1.py` |
| `NbaV3StatsPlayerGameStatsByDateFinalErrorBody` | `sports_data_io/errors/nba_v3_stats_player_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_player_game_stats_by_date_live_final

- **Route**: `GET /v3/nba/stats/{format}/PlayerGameStatsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_player_game_stats_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[PlayerGame1]`
- **Returns (raw)**: `ApiResult[list[PlayerGame1], NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody]`
- **Error**: `NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame1` | `sports_data_io/models/player_game1.py` |
| `NbaV3StatsPlayerGameStatsByDateLiveFinalErrorBody` | `sports_data_io/errors/nba_v3_stats_player_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_player_season_stats

- **Route**: `GET /v3/nba/stats/{format}/PlayerSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_player_season_stats(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerSeason1]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason1], NbaV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `NbaV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason1` | `sports_data_io/models/player_season1.py` |
| `NbaV3StatsPlayerSeasonStatsErrorBody` | `sports_data_io/errors/nba_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/nba/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_player_season_stats_by_team(season: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `team`
- **Params**: `format_` — path `format` · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason1]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason1], NbaV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `NbaV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason1` | `sports_data_io/models/player_season1.py` |
| `NbaV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data_io/errors/nba_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_team_game_stats_by_date_final

- **Route**: `GET /v3/nba/stats/{format}/TeamGameStatsByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_team_game_stats_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[TeamGame1]`
- **Returns (raw)**: `ApiResult[list[TeamGame1], NbaV3StatsTeamGameStatsByDateFinalErrorBody]`
- **Error**: `NbaV3StatsTeamGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame1` | `sports_data_io/models/team_game1.py` |
| `NbaV3StatsTeamGameStatsByDateFinalErrorBody` | `sports_data_io/errors/nba_v3_stats_team_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nba_v3_stats.nba_v3_stats_team_stats_allowed_by_position

- **Route**: `GET /v3/nba/stats/{format}/TeamStatsAllowedByPosition/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nba_v3_stats_team_stats_allowed_by_position(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[TeamSeason1]`
- **Returns (raw)**: `ApiResult[list[TeamSeason1], NbaV3StatsTeamStatsAllowedByPositionErrorBody]`
- **Error**: `NbaV3StatsTeamStatsAllowedByPositionErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamSeason1` | `sports_data_io/models/team_season1.py` |
| `NbaV3StatsTeamStatsAllowedByPositionErrorBody` | `sports_data_io/errors/nba_v3_stats_team_stats_allowed_by_position_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

