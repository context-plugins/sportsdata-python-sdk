<!-- Generated file — do not edit; regenerated with the SDK. -->

# NascarV2 — operations

Accessor: `client.nascar_v2` · Source: `sports_data_io/apis/nascar_v2.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nascar_v2.nascar_v2_driver_driver_profiles_by_driver

- **Route**: `GET /nascar/v2/{format}/driver/{driverid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_driver_driver_profiles_by_driver(format: FormatOrStr, driverid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `driverid`
- **Params**: `format` — path · `driverid` — path
- **Returns (parsed)**: `Driver`
- **Returns (raw)**: `ApiResult[Driver, NascarV2DriverDriverProfilesByDriverErrorBody]`
- **Error**: `NascarV2DriverDriverProfilesByDriverErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Driver` | `sports_data_io/models/driver.py` |
| `NascarV2DriverDriverProfilesByDriverErrorBody` | `sports_data_io/errors/nascar_v2_driver_driver_profiles_by_driver_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_driverraceprojections_projected_player_race_stats_by_race

- **Route**: `GET /nascar/v2/{format}/DriverRaceProjections/{raceid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_driverraceprojections_projected_player_race_stats_by_race(format: FormatOrStr, raceid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `raceid`
- **Params**: `format` — path · `raceid` — path
- **Returns (parsed)**: `list[DriverRaceProjection]`
- **Returns (raw)**: `ApiResult[list[DriverRaceProjection], NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceErrorBody]`
- **Error**: `NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DriverRaceProjection` | `sports_data_io/models/driver_race_projection.py` |
| `NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceErrorBody` | `sports_data_io/errors/nascar_v2_driverraceprojections_projected_player_race_stats_by_race_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_drivers_driver_profiles_all

- **Route**: `GET /nascar/v2/{format}/drivers`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_drivers_driver_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Driver]`
- **Returns (raw)**: `ApiResult[list[Driver], NascarV2DriversDriverProfilesAllErrorBody]`
- **Error**: `NascarV2DriversDriverProfilesAllErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Driver` | `sports_data_io/models/driver.py` |
| `NascarV2DriversDriverProfilesAllErrorBody` | `sports_data_io/errors/nascar_v2_drivers_driver_profiles_all_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_driversbyactive_drivers_by_active

- **Route**: `GET /nascar/v2/{format}/driversbyactive`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_driversbyactive_drivers_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[DriverBasic]`
- **Returns (raw)**: `ApiResult[list[DriverBasic], NascarV2DriversbyactiveDriversByActiveErrorBody]`
- **Error**: `NascarV2DriversbyactiveDriversByActiveErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DriverBasic` | `sports_data_io/models/driver_basic.py` |
| `NascarV2DriversbyactiveDriversByActiveErrorBody` | `sports_data_io/errors/nascar_v2_driversbyactive_drivers_by_active_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_entrylistbyrace_entry_list_by_race

- **Route**: `GET /nascar/v2/{format}/EntryListbyRace/{raceid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_entrylistbyrace_entry_list_by_race(format: FormatOrStr, raceid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `raceid`
- **Params**: `format` — path · `raceid` — path
- **Returns (parsed)**: `list[DriverRaceBasic]`
- **Returns (raw)**: `ApiResult[list[DriverRaceBasic], NascarV2EntrylistbyraceEntryListByRaceErrorBody]`
- **Error**: `NascarV2EntrylistbyraceEntryListByRaceErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `DriverRaceBasic` | `sports_data_io/models/driver_race_basic.py` |
| `NascarV2EntrylistbyraceEntryListByRaceErrorBody` | `sports_data_io/errors/nascar_v2_entrylistbyrace_entry_list_by_race_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race

- **Route**: `GET /nascar/v2/{format}/FantasyGameStatsByRace/{raceid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race(format: FormatOrStr, raceid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `raceid`
- **Params**: `format` — path · `raceid` — path
- **Returns (parsed)**: `FantasyRace`
- **Returns (raw)**: `ApiResult[FantasyRace, NascarV2FantasygamestatsbyraceFantasyPointsByRaceErrorBody]`
- **Error**: `NascarV2FantasygamestatsbyraceFantasyPointsByRaceErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `FantasyRace` | `sports_data_io/models/fantasy_race.py` |
| `NascarV2FantasygamestatsbyraceFantasyPointsByRaceErrorBody` | `sports_data_io/errors/nascar_v2_fantasygamestatsbyrace_fantasy_points_by_race_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_leaderboardbasic_leaderboard_basic

- **Route**: `GET /nascar/v2/{format}/LeaderboardBasic/{raceid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_leaderboardbasic_leaderboard_basic(format: FormatOrStr, raceid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `raceid`
- **Params**: `format` — path · `raceid` — path
- **Returns (parsed)**: `RaceResultBasic`
- **Returns (raw)**: `ApiResult[RaceResultBasic, NascarV2LeaderboardbasicLeaderboardBasicErrorBody]`
- **Error**: `NascarV2LeaderboardbasicLeaderboardBasicErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `RaceResultBasic` | `sports_data_io/models/race_result_basic.py` |
| `NascarV2LeaderboardbasicLeaderboardBasicErrorBody` | `sports_data_io/errors/nascar_v2_leaderboardbasic_leaderboard_basic_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_leaderboardbasicfinal_leaderboard_basic_final

- **Route**: `GET /nascar/v2/{format}/LeaderboardBasicFinal/{raceid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_leaderboardbasicfinal_leaderboard_basic_final(format: FormatOrStr, raceid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `raceid`
- **Params**: `format` — path · `raceid` — path
- **Returns (parsed)**: `RaceResultBasic`
- **Returns (raw)**: `ApiResult[RaceResultBasic, NascarV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody]`
- **Error**: `NascarV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `RaceResultBasic` | `sports_data_io/models/race_result_basic.py` |
| `NascarV2LeaderboardbasicfinalLeaderboardBasicFinalErrorBody` | `sports_data_io/errors/nascar_v2_leaderboardbasicfinal_leaderboard_basic_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_raceresult_leaderboard_live_final

- **Route**: `GET /nascar/v2/{format}/raceresult/{raceid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_raceresult_leaderboard_live_final(format: FormatOrStr, raceid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `raceid`
- **Params**: `format` — path · `raceid` — path
- **Returns (parsed)**: `RaceResult`
- **Returns (raw)**: `ApiResult[RaceResult, NascarV2RaceresultLeaderboardLiveFinalErrorBody]`
- **Error**: `NascarV2RaceresultLeaderboardLiveFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `RaceResult` | `sports_data_io/models/race_result.py` |
| `NascarV2RaceresultLeaderboardLiveFinalErrorBody` | `sports_data_io/errors/nascar_v2_raceresult_leaderboard_live_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_raceresultfinal_leaderboard_final

- **Route**: `GET /nascar/v2/{format}/raceresultfinal/{raceid}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_raceresultfinal_leaderboard_final(format: FormatOrStr, raceid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `raceid`
- **Params**: `format` — path · `raceid` — path
- **Returns (parsed)**: `RaceResult`
- **Returns (raw)**: `ApiResult[RaceResult, NascarV2RaceresultfinalLeaderboardFinalErrorBody]`
- **Error**: `NascarV2RaceresultfinalLeaderboardFinalErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `RaceResult` | `sports_data_io/models/race_result.py` |
| `NascarV2RaceresultfinalLeaderboardFinalErrorBody` | `sports_data_io/errors/nascar_v2_raceresultfinal_leaderboard_final_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_races_schedules

- **Route**: `GET /nascar/v2/{format}/races/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_races_schedules(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Race]`
- **Returns (raw)**: `ApiResult[list[Race], NascarV2RacesSchedulesErrorBody]`
- **Error**: `NascarV2RacesSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Race` | `sports_data_io/models/race.py` |
| `NascarV2RacesSchedulesErrorBody` | `sports_data_io/errors/nascar_v2_races_schedules_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_series_series

- **Route**: `GET /nascar/v2/{format}/series`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_series_series(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[Series1]`
- **Returns (raw)**: `ApiResult[list[Series1], NascarV2SeriesSeriesErrorBody]`
- **Error**: `NascarV2SeriesSeriesErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Series1` | `sports_data_io/models/series1.py` |
| `NascarV2SeriesSeriesErrorBody` | `sports_data_io/errors/nascar_v2_series_series_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nascar_v2.nascar_v2_tracks_tracks

- **Route**: `GET /nascar/v2/{format}/tracks/{season}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nascar_v2_tracks_tracks(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `season`
- **Params**: `format` — path · `season` — path
- **Returns (parsed)**: `list[Tracks]`
- **Returns (raw)**: `ApiResult[list[Tracks], NascarV2TracksTracksErrorBody]`
- **Error**: `NascarV2TracksTracksErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `Tracks` | `sports_data_io/models/tracks.py` |
| `NascarV2TracksTracksErrorBody` | `sports_data_io/errors/nascar_v2_tracks_tracks_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

