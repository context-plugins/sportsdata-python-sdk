<!-- Generated file — do not edit; regenerated with the SDK. -->

# SoccerV4Scores — operations

Accessor: `client.soccer_v4_scores` · Source: `sports_data/apis/soccer_v4_scores.py` · 21 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.soccer_v4_scores.soccer_v4_scores_areas_countries

- **Route**: `GET /v4/soccer/scores/{format}/Areas`
- **Signature**: `def soccer_v4_scores_areas_countries(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Area]`
- **Returns (raw)**: `ApiResult[list[Area], SoccerV4ScoresAreasCountriesErrorBody]`
- **Error**: `SoccerV4ScoresAreasCountriesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Area` | `sports_data/models/area.py` |
| `SoccerV4ScoresAreasCountriesErrorBody` | `sports_data/errors/soccer_v4_scores_areas_countries_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_competitions_leagues

- **Route**: `GET /v4/soccer/scores/{format}/Competitions`
- **Signature**: `def soccer_v4_scores_competitions_leagues(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Competition]`
- **Returns (raw)**: `ApiResult[list[Competition], SoccerV4ScoresCompetitionsLeaguesErrorBody]`
- **Error**: `SoccerV4ScoresCompetitionsLeaguesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Competition` | `sports_data/models/competition.py` |
| `SoccerV4ScoresCompetitionsLeaguesErrorBody` | `sports_data/errors/soccer_v4_scores_competitions_leagues_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_games_by_competition_live_final

- **Route**: `GET /v4/soccer/scores/{format}/CompetitionDetails/{competition}`
- **Signature**: `def soccer_v4_scores_games_by_competition_live_final(format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`
- **Params**: `format` — path · `competition` — path
- **Returns (parsed)**: `CompetitionDetail`
- **Returns (raw)**: `ApiResult[CompetitionDetail, SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody]`
- **Error**: `SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `CompetitionDetail` | `sports_data/models/competition_detail.py` |
| `SoccerV4ScoresGamesByCompetitionLiveFinalErrorBody` | `sports_data/errors/soccer_v4_scores_games_by_competition_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_games_by_date_final

- **Route**: `GET /v4/soccer/scores/{format}/GamesByDateFinal/{competition}/{date}`
- **Signature**: `def soccer_v4_scores_games_by_date_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[Game9]`
- **Returns (raw)**: `ApiResult[list[Game9], SoccerV4ScoresGamesByDateFinalErrorBody]`
- **Error**: `SoccerV4ScoresGamesByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game9` | `sports_data/models/game9.py` |
| `SoccerV4ScoresGamesByDateFinalErrorBody` | `sports_data/errors/soccer_v4_scores_games_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_games_by_date_live_final

- **Route**: `GET /v4/soccer/scores/{format}/GamesByDate/{competition}/{date}`
- **Signature**: `def soccer_v4_scores_games_by_date_live_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[Game9]`
- **Returns (raw)**: `ApiResult[list[Game9], SoccerV4ScoresGamesByDateLiveFinalErrorBody]`
- **Error**: `SoccerV4ScoresGamesByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Game9` | `sports_data/models/game9.py` |
| `SoccerV4ScoresGamesByDateLiveFinalErrorBody` | `sports_data/errors/soccer_v4_scores_games_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_games_basic_by_date_final

- **Route**: `GET /v4/soccer/scores/{format}/ScoresBasicFinal/{competition}/{date}`
- **Signature**: `def soccer_v4_scores_games_basic_by_date_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic6]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic6], SoccerV4ScoresGamesBasicByDateFinalErrorBody]`
- **Error**: `SoccerV4ScoresGamesBasicByDateFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic6` | `sports_data/models/score_basic6.py` |
| `SoccerV4ScoresGamesBasicByDateFinalErrorBody` | `sports_data/errors/soccer_v4_scores_games_basic_by_date_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_games_basic_by_date_live_final

- **Route**: `GET /v4/soccer/scores/{format}/ScoresBasic/{competition}/{date}`
- **Signature**: `def soccer_v4_scores_games_basic_by_date_live_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[ScoreBasic6]`
- **Returns (raw)**: `ApiResult[list[ScoreBasic6], SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody]`
- **Error**: `SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScoreBasic6` | `sports_data/models/score_basic6.py` |
| `SoccerV4ScoresGamesBasicByDateLiveFinalErrorBody` | `sports_data/errors/soccer_v4_scores_games_basic_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_memberships_by_active

- **Route**: `GET /v4/soccer/scores/{format}/ActiveMemberships/{competition}`
- **Signature**: `def soccer_v4_scores_memberships_by_active(format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`
- **Params**: `format` — path · `competition` — path
- **Returns (parsed)**: `list[Membership]`
- **Returns (raw)**: `ApiResult[list[Membership], SoccerV4ScoresMembershipsByActiveErrorBody]`
- **Error**: `SoccerV4ScoresMembershipsByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Membership` | `sports_data/models/membership.py` |
| `SoccerV4ScoresMembershipsByActiveErrorBody` | `sports_data/errors/soccer_v4_scores_memberships_by_active_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_memberships_by_canceled

- **Route**: `GET /v4/soccer/scores/{format}/CanceledMemberships`
- **Signature**: `def soccer_v4_scores_memberships_by_canceled(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `CanceledMembership`
- **Returns (raw)**: `ApiResult[CanceledMembership, SoccerV4ScoresMembershipsByCanceledErrorBody]`
- **Error**: `SoccerV4ScoresMembershipsByCanceledErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `CanceledMembership` | `sports_data/models/canceled_membership.py` |
| `SoccerV4ScoresMembershipsByCanceledErrorBody` | `sports_data/errors/soccer_v4_scores_memberships_by_canceled_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_memberships_by_recently_changed

- **Route**: `GET /v4/soccer/scores/{format}/RecentlyChangedMemberships/{competition}/{days}`
- **Signature**: `def soccer_v4_scores_memberships_by_recently_changed(format: FormatOrStr, competition: str, days: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `days`
- **Params**: `format` — path · `competition` — path · `days` — path
- **Returns (parsed)**: `list[Membership]`
- **Returns (raw)**: `ApiResult[list[Membership], SoccerV4ScoresMembershipsByRecentlyChangedErrorBody]`
- **Error**: `SoccerV4ScoresMembershipsByRecentlyChangedErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Membership` | `sports_data/models/membership.py` |
| `SoccerV4ScoresMembershipsByRecentlyChangedErrorBody` | `sports_data/errors/soccer_v4_scores_memberships_by_recently_changed_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_memberships_historical_by_team

- **Route**: `GET /v4/soccer/scores/{format}/HistoricalMembershipsByTeam/{competition}/{teamid}`
- **Signature**: `def soccer_v4_scores_memberships_historical_by_team(format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `teamid`
- **Params**: `format` — path · `competition` — path · `teamid` — path
- **Returns (parsed)**: `list[Membership]`
- **Returns (raw)**: `ApiResult[list[Membership], SoccerV4ScoresMembershipsHistoricalByTeamErrorBody]`
- **Error**: `SoccerV4ScoresMembershipsHistoricalByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Membership` | `sports_data/models/membership.py` |
| `SoccerV4ScoresMembershipsHistoricalByTeamErrorBody` | `sports_data/errors/soccer_v4_scores_memberships_historical_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_player_details_by_team

- **Route**: `GET /v4/soccer/scores/{format}/PlayersByTeam/{competition}/{teamid}`
- **Signature**: `def soccer_v4_scores_player_details_by_team(format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `teamid`
- **Params**: `format` — path · `competition` — path · `teamid` — path
- **Returns (parsed)**: `list[Player7]`
- **Returns (raw)**: `ApiResult[list[Player7], SoccerV4ScoresPlayerDetailsByTeamErrorBody]`
- **Error**: `SoccerV4ScoresPlayerDetailsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Player7` | `sports_data/models/player7.py` |
| `SoccerV4ScoresPlayerDetailsByTeamErrorBody` | `sports_data/errors/soccer_v4_scores_player_details_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_player_profiles_by_team

- **Route**: `GET /v4/soccer/scores/{format}/PlayersByTeamBasic/{competition}/{teamid}`
- **Signature**: `def soccer_v4_scores_player_profiles_by_team(format: FormatOrStr, competition: str, teamid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `teamid`
- **Params**: `format` — path · `competition` — path · `teamid` — path
- **Returns (parsed)**: `list[PlayerBasic6]`
- **Returns (raw)**: `ApiResult[list[PlayerBasic6], SoccerV4ScoresPlayerProfilesByTeamErrorBody]`
- **Error**: `SoccerV4ScoresPlayerProfilesByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `PlayerBasic6` | `sports_data/models/player_basic6.py` |
| `SoccerV4ScoresPlayerProfilesByTeamErrorBody` | `sports_data/errors/soccer_v4_scores_player_profiles_by_team_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_schedules

- **Route**: `GET /v4/soccer/scores/{format}/Schedule/{competition}/{season}`
- **Signature**: `def soccer_v4_scores_schedules(format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `season`
- **Params**: `format` — path · `competition` — path · `season` — path
- **Returns (parsed)**: `list[Round1]`
- **Returns (raw)**: `ApiResult[list[Round1], SoccerV4ScoresSchedulesErrorBody]`
- **Error**: `SoccerV4ScoresSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Round1` | `sports_data/models/round1.py` |
| `SoccerV4ScoresSchedulesErrorBody` | `sports_data/errors/soccer_v4_scores_schedules_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_schedules_basic

- **Route**: `GET /v4/soccer/scores/{format}/SchedulesBasic/{competition}/{season}`
- **Signature**: `def soccer_v4_scores_schedules_basic(format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `season`
- **Params**: `format` — path · `competition` — path · `season` — path
- **Returns (parsed)**: `list[ScheduleBasic7]`
- **Returns (raw)**: `ApiResult[list[ScheduleBasic7], SoccerV4ScoresSchedulesBasicErrorBody]`
- **Error**: `SoccerV4ScoresSchedulesBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `ScheduleBasic7` | `sports_data/models/schedule_basic7.py` |
| `SoccerV4ScoresSchedulesBasicErrorBody` | `sports_data/errors/soccer_v4_scores_schedules_basic_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_standings

- **Route**: `GET /v4/soccer/scores/{format}/Standings/{competition}/{season}`
- **Signature**: `def soccer_v4_scores_standings(format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `season`
- **Params**: `format` — path · `competition` — path · `season` — path
- **Returns (parsed)**: `list[Round1]`
- **Returns (raw)**: `ApiResult[list[Round1], SoccerV4ScoresStandingsErrorBody]`
- **Error**: `SoccerV4ScoresStandingsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Round1` | `sports_data/models/round1.py` |
| `SoccerV4ScoresStandingsErrorBody` | `sports_data/errors/soccer_v4_scores_standings_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_team_game_stats_by_date_live_final

- **Route**: `GET /v4/soccer/scores/{format}/TeamGameStatsByDate/{competition}/{date}`
- **Signature**: `def soccer_v4_scores_team_game_stats_by_date_live_final(format: FormatOrStr, competition: str, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `date`
- **Params**: `format` — path · `competition` — path · `date` — path
- **Returns (parsed)**: `list[TeamGame6]`
- **Returns (raw)**: `ApiResult[list[TeamGame6], SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody]`
- **Error**: `SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `TeamGame6` | `sports_data/models/team_game6.py` |
| `SoccerV4ScoresTeamGameStatsByDateLiveFinalErrorBody` | `sports_data/errors/soccer_v4_scores_team_game_stats_by_date_live_final_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_team_profiles_by_competition

- **Route**: `GET /v4/soccer/scores/{format}/Teams/{competition}`
- **Signature**: `def soccer_v4_scores_team_profiles_by_competition(format: FormatOrStr, competition: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`
- **Params**: `format` — path · `competition` — path
- **Returns (parsed)**: `list[Team7]`
- **Returns (raw)**: `ApiResult[list[Team7], SoccerV4ScoresTeamProfilesByCompetitionErrorBody]`
- **Error**: `SoccerV4ScoresTeamProfilesByCompetitionErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Team7` | `sports_data/models/team7.py` |
| `SoccerV4ScoresTeamProfilesByCompetitionErrorBody` | `sports_data/errors/soccer_v4_scores_team_profiles_by_competition_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_team_profiles_by_season

- **Route**: `GET /v4/soccer/scores/{format}/SeasonTeams/{competition}/{seasonid}`
- **Signature**: `def soccer_v4_scores_team_profiles_by_season(format: FormatOrStr, competition: str, seasonid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `seasonid`
- **Params**: `format` — path · `competition` — path · `seasonid` — path
- **Returns (parsed)**: `list[SeasonTeam]`
- **Returns (raw)**: `ApiResult[list[SeasonTeam], SoccerV4ScoresTeamProfilesBySeasonErrorBody]`
- **Error**: `SoccerV4ScoresTeamProfilesBySeasonErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `SeasonTeam` | `sports_data/models/season_team.py` |
| `SoccerV4ScoresTeamProfilesBySeasonErrorBody` | `sports_data/errors/soccer_v4_scores_team_profiles_by_season_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_team_season_stats

- **Route**: `GET /v4/soccer/scores/{format}/TeamSeasonStats/{competition}/{season}`
- **Signature**: `def soccer_v4_scores_team_season_stats(format: FormatOrStr, competition: str, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `competition`, `season`
- **Params**: `format` — path · `competition` — path · `season` — path
- **Returns (parsed)**: `list[Round1]`
- **Returns (raw)**: `ApiResult[list[Round1], SoccerV4ScoresTeamSeasonStatsErrorBody]`
- **Error**: `SoccerV4ScoresTeamSeasonStatsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Round1` | `sports_data/models/round1.py` |
| `SoccerV4ScoresTeamSeasonStatsErrorBody` | `sports_data/errors/soccer_v4_scores_team_season_stats_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.soccer_v4_scores.soccer_v4_scores_venues

- **Route**: `GET /v4/soccer/scores/{format}/Venues`
- **Signature**: `def soccer_v4_scores_venues(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Venue]`
- **Returns (raw)**: `ApiResult[list[Venue], SoccerV4ScoresVenuesErrorBody]`
- **Error**: `SoccerV4ScoresVenuesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `Venue` | `sports_data/models/venue.py` |
| `SoccerV4ScoresVenuesErrorBody` | `sports_data/errors/soccer_v4_scores_venues_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

