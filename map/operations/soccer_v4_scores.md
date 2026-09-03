<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoccerV4Scores — operations

Accessor: `client.soccer_v4_scores` · Source: `sports_data_io/apis/soccer_v4_scores.py` · 21 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.soccer_v4_scores.soccer_v4_scores_areas_countries

- **Route**: `GET /v4/soccer/scores/{format}/Areas`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_areas_countries(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Area]`
- **Returns (raw)**: `ApiResult[list[Area], SoccerV4ScoresAreasCountriesErrorBody]`
- **Error**: `SoccerV4ScoresAreasCountriesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Area` | `sports_data_io/models/area.py` |
| `SoccerV4ScoresAreasCountriesErrorBody` | `sports_data_io/errors/soccer_v4_scores_areas_countries_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_competitions_leagues

- **Route**: `GET /v4/soccer/scores/{format}/Competitions`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_competitions_leagues(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Competition]`
- **Returns (raw)**: `ApiResult[list[Competition], SoccerV4ScoresCompetitionsLeaguesErrorBody]`
- **Error**: `SoccerV4ScoresCompetitionsLeaguesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Competition` | `sports_data_io/models/competition.py` |
| `SoccerV4ScoresCompetitionsLeaguesErrorBody` | `sports_data_io/errors/soccer_v4_scores_competitions_leagues_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_games_by_competition_live_final

- **Route**: `GET /v4/soccer/scores/{format}/CompetitionDetails/{competition}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_games_by_competition_live_final(format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`
- **Params**: `format` — path · `competition` — path
- **Returns (parsed)**: `CompetitionDetail`
- **Returns (raw)**: `ApiResult[CompetitionDetail, SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody]`
- **Error**: `SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `CompetitionDetail` | `sports_data_io/models/competition_detail.py` |
| `SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody` | `sports_data_io/errors/soccer_v4_scores_games_by_competition_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_games_by_date_final

- **Route**: `GET /v4/soccer/scores/{format}/GamesByDateFinal/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_games_by_date_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[Game17]`
- **Returns (raw)**: `ApiResult[list[Game17], SoccerV4ScoresGamesByDateFinalErrorBody]`
- **Error**: `SoccerV4ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game17` | `sports_data_io/models/game17.py` |
| `SoccerV4ScoresGamesByDateFinalErrorBody` | `sports_data_io/errors/soccer_v4_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_games_by_date_live_final

- **Route**: `GET /v4/soccer/scores/{format}/GamesByDate/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_games_by_date_live_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[Game17]`
- **Returns (raw)**: `ApiResult[list[Game17], SoccerV4ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `SoccerV4ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Game17` | `sports_data_io/models/game17.py` |
| `SoccerV4ScoresGamesByDateLiveFinalErrorBody` | `sports_data_io/errors/soccer_v4_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_games_basic_by_date_final

- **Route**: `GET /v4/soccer/scores/{format}/ScoresBasicFinal/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_games_basic_by_date_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic7]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic7], SoccerV4ScoresGamesBasicByDateFinalErrorBody]`
- **Error**: `SoccerV4ScoresGamesBasicByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic7` | `sports_data_io/models/score_basic7.py` |
| `SoccerV4ScoresGamesBasicByDateFinalErrorBody` | `sports_data_io/errors/soccer_v4_scores_games_basic_by_date_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_games_basic_by_date_live_final

- **Route**: `GET /v4/soccer/scores/{format}/ScoresBasic/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_games_basic_by_date_live_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic7]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic7], SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody]`
- **Error**: `SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScoreBasic7` | `sports_data_io/models/score_basic7.py` |
| `SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody` | `sports_data_io/errors/soccer_v4_scores_games_basic_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_memberships_by_active

- **Route**: `GET /v4/soccer/scores/{format}/ActiveMemberships/{competition}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_memberships_by_active(format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`
- **Params**: `format` — path · `competition` — path
- **Returns (parsed)**: `list[Membership]`
- **Returns (raw)**: `ApiResult[list[Membership], SoccerV4ScoresMembershipsByActiveErrorBody]`
- **Error**: `SoccerV4ScoresMembershipsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Membership` | `sports_data_io/models/membership.py` |
| `SoccerV4ScoresMembershipsByActiveErrorBody` | `sports_data_io/errors/soccer_v4_scores_memberships_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_memberships_by_canceled

- **Route**: `GET /v4/soccer/scores/{format}/CanceledMemberships`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_memberships_by_canceled(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `CanceledMembership`
- **Returns (raw)**: `ApiResult[CanceledMembership, SoccerV4ScoresMembershipsByCanceledErrorBody]`
- **Error**: `SoccerV4ScoresMembershipsByCanceledErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `CanceledMembership` | `sports_data_io/models/canceled_membership.py` |
| `SoccerV4ScoresMembershipsByCanceledErrorBody` | `sports_data_io/errors/soccer_v4_scores_memberships_by_canceled_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_memberships_by_recently_changed

- **Route**: `GET /v4/soccer/scores/{format}/RecentlyChangedMemberships/{competition}/{days}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_memberships_by_recently_changed(format: FormatOrStr, competition: str, days: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `days`
- **Params**: `format` — path · `competition` — path · `days` — path
- **Returns (parsed)**: `list[Membership]`
- **Returns (raw)**: `ApiResult[list[Membership], SoccerV4ScoresMembershipsByRecentlyChangedErrorBody]`
- **Error**: `SoccerV4ScoresMembershipsByRecentlyChangedErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Membership` | `sports_data_io/models/membership.py` |
| `SoccerV4ScoresMembershipsByRecentlyChangedErrorBody` | `sports_data_io/errors/soccer_v4_scores_memberships_by_recently_changed_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_memberships_historical_by_team

- **Route**: `GET /v4/soccer/scores/{format}/HistoricalMembershipsByTeam/{competition}/{teamid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_memberships_historical_by_team(format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `teamid`
- **Params**: `format` — path · `competition` — path · `teamid` — path
- **Returns (parsed)**: `list[Membership]`
- **Returns (raw)**: `ApiResult[list[Membership], SoccerV4ScoresMembershipsHistoricalByTeamErrorBody]`
- **Error**: `SoccerV4ScoresMembershipsHistoricalByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Membership` | `sports_data_io/models/membership.py` |
| `SoccerV4ScoresMembershipsHistoricalByTeamErrorBody` | `sports_data_io/errors/soccer_v4_scores_memberships_historical_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_player_details_by_team

- **Route**: `GET /v4/soccer/scores/{format}/PlayersByTeam/{competition}/{teamid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_player_details_by_team(format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `teamid`
- **Params**: `format` — path · `competition` — path · `teamid` — path
- **Returns (parsed)**: `list[Player7]`
- **Returns (raw)**: `ApiResult[list[Player7], SoccerV4ScoresPlayerDetailsByTeamErrorBody]`
- **Error**: `SoccerV4ScoresPlayerDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Player7` | `sports_data_io/models/player7.py` |
| `SoccerV4ScoresPlayerDetailsByTeamErrorBody` | `sports_data_io/errors/soccer_v4_scores_player_details_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_player_profiles_by_team

- **Route**: `GET /v4/soccer/scores/{format}/PlayersByTeamBasic/{competition}/{teamid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_player_profiles_by_team(format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `teamid`
- **Params**: `format` — path · `competition` — path · `teamid` — path
- **Returns (parsed)**: `list[PlayerBasic6]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic6], SoccerV4ScoresPlayerProfilesByTeamErrorBody]`
- **Error**: `SoccerV4ScoresPlayerProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `PlayerBasic6` | `sports_data_io/models/player_basic6.py` |
| `SoccerV4ScoresPlayerProfilesByTeamErrorBody` | `sports_data_io/errors/soccer_v4_scores_player_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_schedules

- **Route**: `GET /v4/soccer/scores/{format}/Schedule/{competition}/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_schedules(format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `season`
- **Params**: `format` — path · `competition` — path · `season` — path
- **Returns (parsed)**: `list[Round]`
- **Returns (raw)**: `ApiResult[list[Round], SoccerV4ScoresSchedulesErrorBody]`
- **Error**: `SoccerV4ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Round` | `sports_data_io/models/round.py` |
| `SoccerV4ScoresSchedulesErrorBody` | `sports_data_io/errors/soccer_v4_scores_schedules_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_schedules_basic

- **Route**: `GET /v4/soccer/scores/{format}/SchedulesBasic/{competition}/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_schedules_basic(format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `season`
- **Params**: `format` — path · `competition` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic7]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic7], SoccerV4ScoresSchedulesBasicErrorBody]`
- **Error**: `SoccerV4ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `ScheduleBasic7` | `sports_data_io/models/schedule_basic7.py` |
| `SoccerV4ScoresSchedulesBasicErrorBody` | `sports_data_io/errors/soccer_v4_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_standings

- **Route**: `GET /v4/soccer/scores/{format}/Standings/{competition}/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_standings(format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `season`
- **Params**: `format` — path · `competition` — path · `season` — path
- **Returns (parsed)**: `list[Round]`
- **Returns (raw)**: `ApiResult[list[Round], SoccerV4ScoresStandingsErrorBody]`
- **Error**: `SoccerV4ScoresStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Round` | `sports_data_io/models/round.py` |
| `SoccerV4ScoresStandingsErrorBody` | `sports_data_io/errors/soccer_v4_scores_standings_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_team_game_stats_by_date_live_final

- **Route**: `GET /v4/soccer/scores/{format}/TeamGameStatsByDate/{competition}/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_team_game_stats_by_date_live_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame7]`
- **Returns (raw)**: `ApiResult[list[TeamGame7], SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody]`
- **Error**: `SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `TeamGame7` | `sports_data_io/models/team_game7.py` |
| `SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody` | `sports_data_io/errors/soccer_v4_scores_team_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_team_profiles_by_competition

- **Route**: `GET /v4/soccer/scores/{format}/Teams/{competition}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_team_profiles_by_competition(format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`
- **Params**: `format` — path · `competition` — path
- **Returns (parsed)**: `list[Team8]`
- **Returns (raw)**: `ApiResult[list[Team8], SoccerV4ScoresTeamProfilesByCompetitionErrorBody]`
- **Error**: `SoccerV4ScoresTeamProfilesByCompetitionErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Team8` | `sports_data_io/models/team8.py` |
| `SoccerV4ScoresTeamProfilesByCompetitionErrorBody` | `sports_data_io/errors/soccer_v4_scores_team_profiles_by_competition_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_team_profiles_by_season

- **Route**: `GET /v4/soccer/scores/{format}/SeasonTeams/{competition}/{seasonid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_team_profiles_by_season(format: FormatOrStr, competition: str, seasonid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `seasonid`
- **Params**: `format` — path · `competition` — path · `seasonid` — path
- **Returns (parsed)**: `list[SeasonTeam]`
- **Returns (raw)**: `ApiResult[list[SeasonTeam], SoccerV4ScoresTeamProfilesBySeasonErrorBody]`
- **Error**: `SoccerV4ScoresTeamProfilesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `SeasonTeam` | `sports_data_io/models/season_team.py` |
| `SoccerV4ScoresTeamProfilesBySeasonErrorBody` | `sports_data_io/errors/soccer_v4_scores_team_profiles_by_season_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_team_season_stats

- **Route**: `GET /v4/soccer/scores/{format}/TeamSeasonStats/{competition}/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_team_season_stats(format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `season`
- **Params**: `format` — path · `competition` — path · `season` — path
- **Returns (parsed)**: `list[Round]`
- **Returns (raw)**: `ApiResult[list[Round], SoccerV4ScoresTeamSeasonStatsErrorBody]`
- **Error**: `SoccerV4ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Round` | `sports_data_io/models/round.py` |
| `SoccerV4ScoresTeamSeasonStatsErrorBody` | `sports_data_io/errors/soccer_v4_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_venues

- **Route**: `GET /v4/soccer/scores/{format}/Venues`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def soccer_v4_scores_venues(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Venue]`
- **Returns (raw)**: `ApiResult[list[Venue], SoccerV4ScoresVenuesErrorBody]`
- **Error**: `SoccerV4ScoresVenuesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Venue` | `sports_data_io/models/venue.py` |
| `SoccerV4ScoresVenuesErrorBody` | `sports_data_io/errors/soccer_v4_scores_venues_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

