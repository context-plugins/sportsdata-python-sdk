<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoccerV4Stats — operations

Accessor: `client.soccer_v4_stats` · Source: `sports_data/apis/soccer_v4_stats.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.soccer_v4_stats.soccer_v4_stats_box_score_final

- **Route**: `GET /v4/soccer/stats/{format}/BoxScoreFinal/{competition}/{gameid}`
- **Signature**: `def soccer_v4_stats_box_score_final(format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `gameid`
- **Params**: `format` — path · `competition` — path · `gameid` — path
- **Returns (parsed)**: `list[BoxScore5]`
- **Returns (raw)**: `ApiResult[list[BoxScore5], SoccerV4StatsBoxScoreFinalErrorBody]`
- **Error**: `SoccerV4StatsBoxScoreFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore5` | `sports_data/models/box_score5.py` |
| `SoccerV4StatsBoxScoreFinalErrorBody` | `sports_data/errors/soccer_v4_stats_box_score_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_stats.soccer_v4_stats_box_score_live_final

- **Route**: `GET /v4/soccer/stats/{format}/BoxScore/{competition}/{gameid}`
- **Signature**: `def soccer_v4_stats_box_score_live_final(format: FormatOrStr, competition: str, gameid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `gameid`
- **Params**: `format` — path · `competition` — path · `gameid` — path
- **Returns (parsed)**: `list[BoxScore5]`
- **Returns (raw)**: `ApiResult[list[BoxScore5], SoccerV4StatsBoxScoreLiveFinalErrorBody]`
- **Error**: `SoccerV4StatsBoxScoreLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore5` | `sports_data/models/box_score5.py` |
| `SoccerV4StatsBoxScoreLiveFinalErrorBody` | `sports_data/errors/soccer_v4_stats_box_score_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_stats.soccer_v4_stats_box_scores_by_date_final

- **Route**: `GET /v4/soccer/stats/{format}/BoxScoresFinal/{competition}/{date}`
- **Signature**: `def soccer_v4_stats_box_scores_by_date_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore5]`
- **Returns (raw)**: `ApiResult[list[BoxScore5], SoccerV4StatsBoxScoresByDateFinalErrorBody]`
- **Error**: `SoccerV4StatsBoxScoresByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore5` | `sports_data/models/box_score5.py` |
| `SoccerV4StatsBoxScoresByDateFinalErrorBody` | `sports_data/errors/soccer_v4_stats_box_scores_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_stats.soccer_v4_stats_box_scores_by_date_live_final

- **Route**: `GET /v4/soccer/stats/{format}/BoxScoresByDate/{competition}/{date}`
- **Signature**: `def soccer_v4_stats_box_scores_by_date_live_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[BoxScore5]`
- **Returns (raw)**: `ApiResult[list[BoxScore5], SoccerV4StatsBoxScoresByDateLiveFinalErrorBody]`
- **Error**: `SoccerV4StatsBoxScoresByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore5` | `sports_data/models/box_score5.py` |
| `SoccerV4StatsBoxScoresByDateLiveFinalErrorBody` | `sports_data/errors/soccer_v4_stats_box_scores_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_stats.soccer_v4_stats_box_scores_delta_by_date

- **Route**: `GET /v4/soccer/stats/{format}/BoxScoresDeltaByDate/{competition}/{date}/{minutes}`
- **Signature**: `def soccer_v4_stats_box_scores_delta_by_date(format: FormatOrStr, competition: str, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`, `minutes`
- **Params**: `format` — path · `competition` — path · `date` — path · `minutes` — path
- **Returns (parsed)**: `list[BoxScore5]`
- **Returns (raw)**: `ApiResult[list[BoxScore5], SoccerV4StatsBoxScoresDeltaByDateErrorBody]`
- **Error**: `SoccerV4StatsBoxScoresDeltaByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `BoxScore5` | `sports_data/models/box_score5.py` |
| `SoccerV4StatsBoxScoresDeltaByDateErrorBody` | `sports_data/errors/soccer_v4_stats_box_scores_delta_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_stats.soccer_v4_stats_fantasy_points_by_date

- **Route**: `GET /v4/soccer/stats/{format}/FantasyGameStatsByDate/{competition}/{date}`
- **Signature**: `def soccer_v4_stats_fantasy_points_by_date(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[FantasyGame4]`
- **Returns (raw)**: `ApiResult[list[FantasyGame4], SoccerV4StatsFantasyPointsByDateErrorBody]`
- **Error**: `SoccerV4StatsFantasyPointsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `FantasyGame4` | `sports_data/models/fantasy_game4.py` |
| `SoccerV4StatsFantasyPointsByDateErrorBody` | `sports_data/errors/soccer_v4_stats_fantasy_points_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_stats.soccer_v4_stats_lineups_by_date

- **Route**: `GET /v4/soccer/stats/{format}/LineupsByDate/{competition}/{date}`
- **Signature**: `def soccer_v4_stats_lineups_by_date(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGameBasic]`
- **Returns (raw)**: `ApiResult[list[PlayerGameBasic], SoccerV4StatsLineupsByDateErrorBody]`
- **Error**: `SoccerV4StatsLineupsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGameBasic` | `sports_data/models/player_game_basic.py` |
| `SoccerV4StatsLineupsByDateErrorBody` | `sports_data/errors/soccer_v4_stats_lineups_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_stats.soccer_v4_stats_player_game_stats_by_date_final

- **Route**: `GET /v4/soccer/stats/{format}/PlayerGameStatsByDateFinal/{competition}/{date}`
- **Signature**: `def soccer_v4_stats_player_game_stats_by_date_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGame6]`
- **Returns (raw)**: `ApiResult[list[PlayerGame6], SoccerV4StatsPlayerGameStatsByDateFinalErrorBody]`
- **Error**: `SoccerV4StatsPlayerGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame6` | `sports_data/models/player_game6.py` |
| `SoccerV4StatsPlayerGameStatsByDateFinalErrorBody` | `sports_data/errors/soccer_v4_stats_player_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_stats.soccer_v4_stats_player_game_stats_by_date_live_final

- **Route**: `GET /v4/soccer/stats/{format}/PlayerGameStatsByDate/{competition}/{date}`
- **Signature**: `def soccer_v4_stats_player_game_stats_by_date_live_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[PlayerGame6]`
- **Returns (raw)**: `ApiResult[list[PlayerGame6], SoccerV4StatsPlayerGameStatsByDateLiveFinalErrorBody]`
- **Error**: `SoccerV4StatsPlayerGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerGame6` | `sports_data/models/player_game6.py` |
| `SoccerV4StatsPlayerGameStatsByDateLiveFinalErrorBody` | `sports_data/errors/soccer_v4_stats_player_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_stats.soccer_v4_stats_player_season_stats

- **Route**: `GET /v4/soccer/stats/{format}/PlayerSeasonStats/{competition}/{season}`
- **Signature**: `def soccer_v4_stats_player_season_stats(format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `season`
- **Params**: `format` — path · `competition` — path · `season` — path
- **Returns (parsed)**: `list[Round1]`
- **Returns (raw)**: `ApiResult[list[Round1], SoccerV4StatsPlayerSeasonStatsErrorBody]`
- **Error**: `SoccerV4StatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Round1` | `sports_data/models/round1.py` |
| `SoccerV4StatsPlayerSeasonStatsErrorBody` | `sports_data/errors/soccer_v4_stats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_stats.soccer_v4_stats_team_game_stats_by_date_final

- **Route**: `GET /v4/soccer/stats/{format}/TeamGameStatsByDateFinal/{competition}/{date}`
- **Signature**: `def soccer_v4_stats_team_game_stats_by_date_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame6]`
- **Returns (raw)**: `ApiResult[list[TeamGame6], SoccerV4StatsTeamGameStatsByDateFinalErrorBody]`
- **Error**: `SoccerV4StatsTeamGameStatsByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame6` | `sports_data/models/team_game6.py` |
| `SoccerV4StatsTeamGameStatsByDateFinalErrorBody` | `sports_data/errors/soccer_v4_stats_team_game_stats_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

