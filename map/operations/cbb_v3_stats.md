<!-- Generated file — do not edit; regenerated with the SDK. -->

# CbbV3Stats — operations

Accessor: `client.cbb_v3_stats` · Source: `sports_data_io/apis/cbb_v3_stats.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cbb_v3_stats.cbb_v3_stats_box_score_final

- **Route**: `GET /v3/cbb/stats/{format}/BoxScoreFinal/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_box_score_final(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `BoxScore4`
- **Returns (raw)**: `ApiResult[BoxScore4, CbbV3StatsBoxScoreFinalErrorBody]`
- **Error**: `CbbV3StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore4` | `sports_data_io/models/box_score4.py` |
| `CbbV3StatsBoxScoreFinalErrorBody` | `sports_data_io/errors/cbb_v3_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_box_score_live_final

- **Route**: `GET /v3/cbb/stats/{format}/BoxScore/{gameid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_box_score_live_final(gameid: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gameid`
- **Params**: `format_` — path `format` · `gameid` — path
- **Returns (parsed)**: `BoxScore4`
- **Returns (raw)**: `ApiResult[BoxScore4, CbbV3StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `CbbV3StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore4` | `sports_data_io/models/box_score4.py` |
| `CbbV3StatsBoxScoreLiveFinalErrorBody` | `sports_data_io/errors/cbb_v3_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_box_scores_by_date_final

- **Route**: `GET /v3/cbb/stats/{format}/BoxScoresFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_box_scores_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[BoxScore4]`
- **Returns (raw)**: `ApiResult[list[BoxScore4], CbbV3StatsBoxScoresByDateFinalErrorBody]`
- **Error**: `CbbV3StatsBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore4` | `sports_data_io/models/box_score4.py` |
| `CbbV3StatsBoxScoresByDateFinalErrorBody` | `sports_data_io/errors/cbb_v3_stats_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_box_scores_by_date_live_final

- **Route**: `GET /v3/cbb/stats/{format}/BoxScores/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_box_scores_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[BoxScore4]`
- **Returns (raw)**: `ApiResult[list[BoxScore4], CbbV3StatsBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `CbbV3StatsBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore4` | `sports_data_io/models/box_score4.py` |
| `CbbV3StatsBoxScoresByDateLiveFinalErrorBody` | `sports_data_io/errors/cbb_v3_stats_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_box_scores_delta_by_date

- **Route**: `GET /v3/cbb/stats/{format}/BoxScoresDelta/{date}/{minutes}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_box_scores_delta_by_date(date: str, minutes: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`, `minutes`
- **Params**: `format_` — path `format` · `date` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScore4]`
- **Returns (raw)**: `ApiResult[list[BoxScore4], CbbV3StatsBoxScoresDeltaByDateErrorBody]`
- **Error**: `CbbV3StatsBoxScoresDeltaByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `BoxScore4` | `sports_data_io/models/box_score4.py` |
| `CbbV3StatsBoxScoresDeltaByDateErrorBody` | `sports_data_io/errors/cbb_v3_stats_box_scores_delta_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_player_game_logs_by_season

- **Route**: `GET /v3/cbb/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_player_game_logs_by_season(season: str, playerid: str, numberofgames: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `playerid`, `numberofgames`
- **Params**: `format_` — path `format` · `season` — path · `playerid` — path · `numberofgames` — path
- **Returns (parsed)**: `list[PlayerGame5]`
- **Returns (raw)**: `ApiResult[list[PlayerGame5], CbbV3StatsPlayerGameLogsBySeasonErrorBody]`
- **Error**: `CbbV3StatsPlayerGameLogsBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame5` | `sports_data_io/models/player_game5.py` |
| `CbbV3StatsPlayerGameLogsBySeasonErrorBody` | `sports_data_io/errors/cbb_v3_stats_player_game_logs_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_player_game_stats_by_date_final

- **Route**: `GET /v3/cbb/stats/{format}/PlayerGameStatsByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_player_game_stats_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[PlayerGame5]`
- **Returns (raw)**: `ApiResult[list[PlayerGame5], CbbV3StatsPlayerGameStatsByDateFinalErrorBody]`
- **Error**: `CbbV3StatsPlayerGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame5` | `sports_data_io/models/player_game5.py` |
| `CbbV3StatsPlayerGameStatsByDateFinalErrorBody` | `sports_data_io/errors/cbb_v3_stats_player_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_player_game_stats_by_date_live_final

- **Route**: `GET /v3/cbb/stats/{format}/PlayerGameStatsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_player_game_stats_by_date_live_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[PlayerGame5]`
- **Returns (raw)**: `ApiResult[list[PlayerGame5], CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody]`
- **Error**: `CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerGame5` | `sports_data_io/models/player_game5.py` |
| `CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody` | `sports_data_io/errors/cbb_v3_stats_player_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_player_season_stats

- **Route**: `GET /v3/cbb/stats/{format}/PlayerSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_player_season_stats(season: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`
- **Params**: `format_` — path `format` · `season` — path
- **Returns (parsed)**: `list[PlayerSeason6]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason6], CbbV3StatsPlayerSeasonStatsErrorBody]`
- **Error**: `CbbV3StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason6` | `sports_data_io/models/player_season6.py` |
| `CbbV3StatsPlayerSeasonStatsErrorBody` | `sports_data_io/errors/cbb_v3_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_player_season_stats_by_team

- **Route**: `GET /v3/cbb/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_player_season_stats_by_team(season: str, team: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `season`, `team`
- **Params**: `format_` — path `format` · `season` — path · `team` — path
- **Returns (parsed)**: `list[PlayerSeason6]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason6], CbbV3StatsPlayerSeasonStatsByTeamErrorBody]`
- **Error**: `CbbV3StatsPlayerSeasonStatsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason6` | `sports_data_io/models/player_season6.py` |
| `CbbV3StatsPlayerSeasonStatsByTeamErrorBody` | `sports_data_io/errors/cbb_v3_stats_player_season_stats_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.cbb_v3_stats.cbb_v3_stats_team_game_stats_by_date_final

- **Route**: `GET /v3/cbb/stats/{format}/TeamGameStatsByDateFinal/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def cbb_v3_stats_team_game_stats_by_date_final(date: str, *, format_: FormatOrStr = Format.JSON, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`
- **Params**: `format_` — path `format` · `date` — path
- **Returns (parsed)**: `list[TeamGame5]`
- **Returns (raw)**: `ApiResult[list[TeamGame5], CbbV3StatsTeamGameStatsByDateFinalErrorBody]`
- **Error**: `CbbV3StatsTeamGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame5` | `sports_data_io/models/team_game5.py` |
| `CbbV3StatsTeamGameStatsByDateFinalErrorBody` | `sports_data_io/errors/cbb_v3_stats_team_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

