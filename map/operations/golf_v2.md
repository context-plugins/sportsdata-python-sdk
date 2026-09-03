<!-- Generated file — do not edit; regenerated with the SDK. -->

# GolfV2 — operations

Accessor: `client.golf_v2` · Source: `sports_data_io/apis/golf_v2.py` · 23 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.golf_v2.golf_v2_courses_courses

- **Route**: `GET /golf/v2/{format}/Courses`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_courses_courses(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Courses]`
- **Returns (raw)**: `ApiResult[list[Courses], GolfV2CoursesCoursesErrorBody]`
- **Error**: `GolfV2CoursesCoursesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Courses` | `sports_data_io/models/courses.py` |
| `GolfV2CoursesCoursesErrorBody` | `sports_data_io/errors/golf_v2_courses_courses_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_currentseason_season_current

- **Route**: `GET /golf/v2/{format}/CurrentSeason`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_currentseason_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `Season7`
- **Returns (raw)**: `ApiResult[Season7, GolfV2CurrentseasonSeasonCurrentErrorBody]`
- **Error**: `GolfV2CurrentseasonSeasonCurrentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Season7` | `sports_data_io/models/season7.py` |
| `GolfV2CurrentseasonSeasonCurrentErrorBody` | `sports_data_io/errors/golf_v2_currentseason_season_current_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate

- **Route**: `GET /golf/v2/{format}/DfsSlateOwnershipProjectionsBySlateID/{slateId}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate(format: FormatOrStr, slate_id: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `slate_id`
- **Params**: `format` — path · `slate_id` — path `slateId`
- **Returns (parsed)**: `DfsSlateWithOwnershipProjection`
- **Returns (raw)**: `ApiResult[DfsSlateWithOwnershipProjection, GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateErrorBody]`
- **Error**: `GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DfsSlateWithOwnershipProjection` | `sports_data_io/models/dfs_slate_with_ownership_projection.py` |
| `GolfV2DfsslateownershipprojectionsbyslateidDfsSlateOwnershipProjectionsBySlateErrorBody` | `sports_data_io/errors/golf_v2_dfsslateownershipprojectionsbyslateid_dfs_slate_ownership_projections_by_slate_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_dfsslatesbytournament_dfs_slates_by_tournament

- **Route**: `GET /golf/v2/{format}/DfsSlatesByTournament/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_dfsslatesbytournament_dfs_slates_by_tournament(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `list[DfsSlate2]`
- **Returns (raw)**: `ApiResult[list[DfsSlate2], GolfV2DfsslatesbytournamentDfsSlatesByTournamentErrorBody]`
- **Error**: `GolfV2DfsslatesbytournamentDfsSlatesByTournamentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DfsSlate2` | `sports_data_io/models/dfs_slate2.py` |
| `GolfV2DfsslatesbytournamentDfsSlatesByTournamentErrorBody` | `sports_data_io/errors/golf_v2_dfsslatesbytournament_dfs_slates_by_tournament_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament

- **Route**: `GET /golf/v2/{format}/FantasyGameStatsByTournament/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `FantasyTournament`
- **Returns (raw)**: `ApiResult[FantasyTournament, GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentErrorBody]`
- **Error**: `GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FantasyTournament` | `sports_data_io/models/fantasy_tournament.py` |
| `GolfV2FantasygamestatsbytournamentFantasyPointsByTournamentErrorBody` | `sports_data_io/errors/golf_v2_fantasygamestatsbytournament_fantasy_points_by_tournament_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_leaderboard_leaderboard_live_final

- **Route**: `GET /golf/v2/{format}/Leaderboard/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_leaderboard_leaderboard_live_final(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `Leaderboard`
- **Returns (raw)**: `ApiResult[Leaderboard, GolfV2LeaderboardLeaderboardLiveFinalErrorBody]`
- **Error**: `GolfV2LeaderboardLeaderboardLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Leaderboard` | `sports_data_io/models/leaderboard.py` |
| `GolfV2LeaderboardLeaderboardLiveFinalErrorBody` | `sports_data_io/errors/golf_v2_leaderboard_leaderboard_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_leaderboardbasic_leaderboard_basic

- **Route**: `GET /golf/v2/{format}/LeaderboardBasic/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_leaderboardbasic_leaderboard_basic(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `LeaderboardBasic`
- **Returns (raw)**: `ApiResult[LeaderboardBasic, GolfV2LeaderboardbasicLeaderboardBasicErrorBody]`
- **Error**: `GolfV2LeaderboardbasicLeaderboardBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `LeaderboardBasic` | `sports_data_io/models/leaderboard_basic.py` |
| `GolfV2LeaderboardbasicLeaderboardBasicErrorBody` | `sports_data_io/errors/golf_v2_leaderboardbasic_leaderboard_basic_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_leaderboardbasicfinal_leaderboard_basic_final

- **Route**: `GET /golf/v2/{format}/LeaderboardBasicFinal/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_leaderboardbasicfinal_leaderboard_basic_final(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `LeaderboardBasic`
- **Returns (raw)**: `ApiResult[LeaderboardBasic, GolfV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody]`
- **Error**: `GolfV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `LeaderboardBasic` | `sports_data_io/models/leaderboard_basic.py` |
| `GolfV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody` | `sports_data_io/errors/golf_v2_leaderboardbasicfinal_leaderboard_basic_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_leaderboardfinal_leaderboard_final

- **Route**: `GET /golf/v2/{format}/LeaderboardFinal/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_leaderboardfinal_leaderboard_final(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `Leaderboard`
- **Returns (raw)**: `ApiResult[Leaderboard, GolfV2LeaderboardfinalLeaderboardFinalErrorBody]`
- **Error**: `GolfV2LeaderboardfinalLeaderboardFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Leaderboard` | `sports_data_io/models/leaderboard.py` |
| `GolfV2LeaderboardfinalLeaderboardFinalErrorBody` | `sports_data_io/errors/golf_v2_leaderboardfinal_leaderboard_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_news_news

- **Route**: `GET /golf/v2/{format}/News`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_news_news(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[News2]`
- **Returns (raw)**: `ApiResult[list[News2], GolfV2NewsNewsErrorBody]`
- **Error**: `GolfV2NewsNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News2` | `sports_data_io/models/news2.py` |
| `GolfV2NewsNewsErrorBody` | `sports_data_io/errors/golf_v2_news_news_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_newsbydate_news_by_date

- **Route**: `GET /golf/v2/{format}/NewsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_newsbydate_news_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[News2]`
- **Returns (raw)**: `ApiResult[list[News2], GolfV2NewsbydateNewsByDateErrorBody]`
- **Error**: `GolfV2NewsbydateNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News2` | `sports_data_io/models/news2.py` |
| `GolfV2NewsbydateNewsByDateErrorBody` | `sports_data_io/errors/golf_v2_newsbydate_news_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_player_player

- **Route**: `GET /golf/v2/{format}/Player/{playerid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_player_player(format: FormatOrStr, playerid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `playerid`
- **Params**: `format` — path · `playerid` — path
- **Returns (parsed)**: `Player8`
- **Returns (raw)**: `ApiResult[Player8, GolfV2PlayerPlayerErrorBody]`
- **Error**: `GolfV2PlayerPlayerErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player8` | `sports_data_io/models/player8.py` |
| `GolfV2PlayerPlayerErrorBody` | `sports_data_io/errors/golf_v2_player_player_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_players_player_profiles_all

- **Route**: `GET /golf/v2/{format}/Players`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_players_player_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Player8]`
- **Returns (raw)**: `ApiResult[list[Player8], GolfV2PlayersPlayerProfilesAllErrorBody]`
- **Error**: `GolfV2PlayersPlayerProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player8` | `sports_data_io/models/player8.py` |
| `GolfV2PlayersPlayerProfilesAllErrorBody` | `sports_data_io/errors/golf_v2_players_player_profiles_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_playerseasonstats_player_season_stats

- **Route**: `GET /golf/v2/{format}/PlayerSeasonStats/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_playerseasonstats_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason9]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason9], GolfV2PlayerseasonstatsPlayerSeasonStatsErrorBody]`
- **Error**: `GolfV2PlayerseasonstatsPlayerSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason9` | `sports_data_io/models/player_season9.py` |
| `GolfV2PlayerseasonstatsPlayerSeasonStatsErrorBody` | `sports_data_io/errors/golf_v2_playerseasonstats_player_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final

- **Route**: `GET /golf/v2/{format}/PlayerTournamentHoleScores/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `list[PlayerTournamentBasic]`
- **Returns (raw)**: `ApiResult[list[PlayerTournamentBasic], GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalErrorBody]`
- **Error**: `GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerTournamentBasic` | `sports_data_io/models/player_tournament_basic.py` |
| `GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalErrorBody` | `sports_data_io/errors/golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final

- **Route**: `GET /golf/v2/{format}/PlayerTournamentHoleScoresFinal/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `list[PlayerTournamentBasic]`
- **Returns (raw)**: `ApiResult[list[PlayerTournamentBasic], GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalErrorBody]`
- **Error**: `GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerTournamentBasic` | `sports_data_io/models/player_tournament_basic.py` |
| `GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalErrorBody` | `sports_data_io/errors/golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament

- **Route**: `GET /golf/v2/{format}/PlayerTournamentProjectionStats/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `list[PlayerTournamentProjection]`
- **Returns (raw)**: `ApiResult[list[PlayerTournamentProjection], GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentErrorBody]`
- **Error**: `GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerTournamentProjection` | `sports_data_io/models/player_tournament_projection.py` |
| `GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentErrorBody` | `sports_data_io/errors/golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_playertournamentroundscores_scores_by_tournament_live_final

- **Route**: `GET /golf/v2/{format}/PlayerTournamentRoundScores/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_playertournamentroundscores_scores_by_tournament_live_final(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `list[TournamentRound]`
- **Returns (raw)**: `ApiResult[list[TournamentRound], GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody]`
- **Error**: `GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TournamentRound` | `sports_data_io/models/tournament_round.py` |
| `GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody` | `sports_data_io/errors/golf_v2_playertournamentroundscores_scores_by_tournament_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final

- **Route**: `GET /golf/v2/{format}/PlayerTournamentRoundScoresFinal/{tournamentid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final(format: FormatOrStr, tournamentid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `tournamentid`
- **Params**: `format` — path · `tournamentid` — path
- **Returns (parsed)**: `list[TournamentRound]`
- **Returns (raw)**: `ApiResult[list[TournamentRound], GolfV2PlayertournamentroundscoresfinalScoresByTournamentFinalErrorBody]`
- **Error**: `GolfV2PlayertournamentroundscoresfinalScoresByTournamentFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TournamentRound` | `sports_data_io/models/tournament_round.py` |
| `GolfV2PlayertournamentroundscoresfinalScoresByTournamentFinalErrorBody` | `sports_data_io/errors/golf_v2_playertournamentroundscoresfinal_scores_by_tournament_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_rankings_rankings

- **Route**: `GET /golf/v2/{format}/Rankings/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_rankings_rankings(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[PlayerSeason9]`
- **Returns (raw)**: `ApiResult[list[PlayerSeason9], GolfV2RankingsRankingsErrorBody]`
- **Error**: `GolfV2RankingsRankingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerSeason9` | `sports_data_io/models/player_season9.py` |
| `GolfV2RankingsRankingsErrorBody` | `sports_data_io/errors/golf_v2_rankings_rankings_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_tournaments_schedule_by_season

- **Route**: `GET /golf/v2/{format}/Tournaments/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_tournaments_schedule_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Tournament1]`
- **Returns (raw)**: `ApiResult[list[Tournament1], GolfV2TournamentsScheduleBySeasonErrorBody]`
- **Error**: `GolfV2TournamentsScheduleBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Tournament1` | `sports_data_io/models/tournament1.py` |
| `GolfV2TournamentsScheduleBySeasonErrorBody` | `sports_data_io/errors/golf_v2_tournaments_schedule_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_tournaments_schedules

- **Route**: `GET /golf/v2/{format}/Tournaments`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_tournaments_schedules(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Tournament1]`
- **Returns (raw)**: `ApiResult[list[Tournament1], GolfV2TournamentsSchedulesErrorBody]`
- **Error**: `GolfV2TournamentsSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Tournament1` | `sports_data_io/models/tournament1.py` |
| `GolfV2TournamentsSchedulesErrorBody` | `sports_data_io/errors/golf_v2_tournaments_schedules_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.golf_v2.golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming

- **Route**: `GET /golf/v2/{format}/UpcomingDfsSlateOwnershipProjections`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[DfsSlateWithOwnershipProjection]`
- **Returns (raw)**: `ApiResult[list[DfsSlateWithOwnershipProjection], GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingErrorBody]`
- **Error**: `GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DfsSlateWithOwnershipProjection` | `sports_data_io/models/dfs_slate_with_ownership_projection.py` |
| `GolfV2UpcomingdfsslateownershipprojectionsDfsSlateOwnershipProjectionsUpcomingErrorBody` | `sports_data_io/errors/golf_v2_upcomingdfsslateownershipprojections_dfs_slate_ownership_projections_upcoming_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

