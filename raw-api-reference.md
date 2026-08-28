# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [CbbApiClient](cbb_api/client.py)

## CbbV3Odds

> Source: [CbbV3Odds](cbb_api/apis/cbb_v3_odds.py)

<details>
<summary><code>def cbb_v3_odds_alternate_market_pre_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfo], CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the non-full-game odds for games on a given date. This means odds such as 1st-half, rather than full game. Only returns the most recently seen odds, not-including line movement.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_alternate_market_pre_game_odds_by_date(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_alternate_market_pre_game_odds_by_date(
    format, date
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s). <br>Examples: <code>2018-11-20</code>, <code>2018-11-23</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;, [CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody](cbb_api/errors/cbb_v3_odds_alternate_market_pre_game_odds_by_date_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody](cbb_api/errors/cbb_v3_odds_alternate_market_pre_game_odds_by_date_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_alternate_market_pre_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfo], CbbV3OddsAlternateMarketPreGameOddsLineMovementErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the non-full-game odds for games in a given GameID. This means odds such as 1st-half, rather than full game. Returns the full line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the second line.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_alternate_market_pre_game_odds_line_movement(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsAlternateMarketPreGameOddsLineMovementErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_alternate_market_pre_game_odds_line_movement(
    format, gameid
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsAlternateMarketPreGameOddsLineMovementErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are <code>17775</code> or <code>17776</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;, [CbbV3OddsAlternateMarketPreGameOddsLineMovementErrorBody](cbb_api/errors/cbb_v3_odds_alternate_market_pre_game_odds_line_movement_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsAlternateMarketPreGameOddsLineMovementErrorBody](cbb_api/errors/cbb_v3_odds_alternate_market_pre_game_odds_line_movement_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_events_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingEvent], CbbV3OddsBettingEventsByDateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The list of current BettingEvents for the given date, from which Betting Market data can be gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_events_by_date(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingEvent]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingEventsByDateErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_events_by_date(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingEvent]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingEventsByDateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s). <br>Examples: <code>2018-11-20</code>, <code>2018-11-23</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingEvent](cbb_api/models/betting_event.py)&#93;, [CbbV3OddsBettingEventsByDateErrorBody](cbb_api/errors/cbb_v3_odds_betting_events_by_date_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingEvent](cbb_api/models/betting_event.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingEventsByDateErrorBody](cbb_api/errors/cbb_v3_odds_betting_events_by_date_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_events_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingEvent], CbbV3OddsBettingEventsBySeasonErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The list of current BettingEvents for the given season, from which Betting Market data can be gathered via the Betting Markets by Event endpoint, for all available Betting Market types (e.g. Player Props, Team Props.)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_events_by_season(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingEvent]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingEventsBySeasonErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_events_by_season(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingEvent]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingEventsBySeasonErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingEvent](cbb_api/models/betting_event.py)&#93;, [CbbV3OddsBettingEventsBySeasonErrorBody](cbb_api/errors/cbb_v3_odds_betting_events_by_season_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingEvent](cbb_api/models/betting_event.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingEventsBySeasonErrorBody](cbb_api/errors/cbb_v3_odds_betting_events_by_season_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_futures_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingEvent], CbbV3OddsBettingFuturesBySeasonErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns available Futures markets for the given season. Does not include line movement.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_futures_by_season(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingEvent]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingFuturesBySeasonErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_futures_by_season(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingEvent]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingFuturesBySeasonErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingEvent](cbb_api/models/betting_event.py)&#93;, [CbbV3OddsBettingFuturesBySeasonErrorBody](cbb_api/errors/cbb_v3_odds_betting_futures_by_season_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingEvent](cbb_api/models/betting_event.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingFuturesBySeasonErrorBody](cbb_api/errors/cbb_v3_odds_betting_futures_by_season_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_futures_by_season_sportsbook_group(format: FormatOrStr, season: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingEvent], CbbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns available Futures markets for the given season. Does not include line movement. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_futures_by_season_sportsbook_group(
    format, season, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingEvent]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_futures_by_season_sportsbook_group(
    format, season, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingEvent]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season<br>Examples: <code>2020</code>, <code>2021</code>, etc. |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingEvent](cbb_api/models/betting_event.py)&#93;, [CbbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_futures_by_season_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingEvent](cbb_api/models/betting_event.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingFuturesBySeasonSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_futures_by_season_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BettingMarket, CbbV3OddsBettingMarketErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of detail, it is intended for historical data purposes and not for the most up-to-the-second lines.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_market(format, market_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingMarket
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_market(format, market_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingMarket
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>market_id</code> | <code>str</code> | The MarketId of the desired market for which to pull all outcomes/bets. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[BettingMarket](cbb_api/models/betting_market.py), [CbbV3OddsBettingMarketErrorBody](cbb_api/errors/cbb_v3_odds_betting_market_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BettingMarket](cbb_api/models/betting_market.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingMarketErrorBody](cbb_api/errors/cbb_v3_odds_betting_market_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BettingMarket, CbbV3OddsBettingMarketSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns full line movement for a given BettingMarket. Due to the sheer size of the output and the level of detail, it is intended for historical data purposes and not for the most up-to-the-second lines. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_market_sportsbook_group(
    format, market_id, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingMarket
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_market_sportsbook_group(
    format, market_id, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingMarket
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>market_id</code> | <code>str</code> | The MarketId of the desired market for which to pull all outcomes/bets. |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[BettingMarket](cbb_api/models/betting_market.py), [CbbV3OddsBettingMarketSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_market_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BettingMarket](cbb_api/models/betting_market.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingMarketSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_market_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_markets_by_event(format: FormatOrStr, event_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByEventErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given BettingEventID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_event(format, event_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByEventErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_event(format, event_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByEventErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>event_id</code> | <code>str</code> | The EventId of the desired event/game for which to pull all betting markets (includes outcomes/bets). |
| <code>include</code> | <code>[IncludeOrStr](cbb_api/models/enums/include.py) \| None</code> | This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br><br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be several minutes old. For best performance, the default parameter is highly recommended. <br><br><br><br>Possible values include: <br><br><br><code>available</code> - excludes any betting outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster than using unlisted. <br><br><br><code>unlisted</code> - includes the most recently available betting outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much longer than available. <br><br><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;, [CbbV3OddsBettingMarketsByEventErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_event_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingMarketsByEventErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_event_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_markets_by_event_sportsbook_group(format: FormatOrStr, event_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByEventSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the markets and available outcomes for a given BettingEventID. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_event_sportsbook_group(
    format, event_id, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByEventSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_event_sportsbook_group(
    format, event_id, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByEventSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>event_id</code> | <code>str</code> | The EventId of the desired event/game for which to pull all betting markets (includes outcomes/bets). |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>include</code> | <code>[IncludeOrStr](cbb_api/models/enums/include.py) \| None</code> | This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be several minutes old. For best performance, the default parameter is highly recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most recently available betting outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much longer than available. <br><br><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;, [CbbV3OddsBettingMarketsByEventSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_event_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingMarketsByEventSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_event_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_markets_by_game(format: FormatOrStr, gameid: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByGameErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given GameID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_game(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByGameErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_game(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByGameErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of the desired game for which to pull all betting markets (includes outcomes/bets). |
| <code>include</code> | <code>[IncludeOrStr](cbb_api/models/enums/include.py) \| None</code> | This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be several minutes old. For best performance, the default parameter is highly recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most recently available betting outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much longer than available. <br><br><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;, [CbbV3OddsBettingMarketsByGameErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_game_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingMarketsByGameErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_game_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_markets_by_game_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByGameSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the markets of all available types (e.g. Player Props, Team Props) and available outcomes for a given GameID. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_game_sportsbook_group(
    format, gameid, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByGameSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_game_sportsbook_group(
    format, gameid, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByGameSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of the desired game for which to pull all betting markets (includes outcomes/bets). |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>include</code> | <code>[IncludeOrStr](cbb_api/models/enums/include.py) \| None</code> | This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be several minutes old. For best performance, the default parameter is highly recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most recently available betting outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much longer than available. <br><br><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;, [CbbV3OddsBettingMarketsByGameSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_game_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingMarketsByGameSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_game_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_markets_by_market_type(format: FormatOrStr, event_id: str, market_type_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByMarketTypeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns Markets and available outcomes for a given event and market type requested. A lighter call than by BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is available for each sport in its Betting Metadata endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_market_type(
    format, event_id, market_type_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByMarketTypeErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_market_type(
    format, event_id, market_type_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByMarketTypeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>event_id</code> | <code>str</code> | The EventId of the desired event/game for which to pull all betting markets (includes outcomes/bets). |
| <code>market_type_id</code> | <code>str</code> | The Market Type ID of the desired MarketTypes to pull. Some common types include: <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props, <code>6</code> for Game Props |
| <code>include</code> | <code>[IncludeOrStr](cbb_api/models/enums/include.py) \| None</code> | This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be several minutes old. For best performance, the default parameter is highly recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most recently available betting outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much longer than available. <br><br><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;, [CbbV3OddsBettingMarketsByMarketTypeErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_market_type_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingMarketsByMarketTypeErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_market_type_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_markets_by_market_type_sportsbook_group(format: FormatOrStr, event_id: str, market_type_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingMarket], CbbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns Markets and available outcomes for a given event and market type requested. A lighter call than by BettingEventID as it only includes markets tagged with the specific MarketType, a full list of which is available for each sport in its Betting Metadata endpoint. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_market_type_sportsbook_group(
    format, event_id, market_type_id, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_markets_by_market_type_sportsbook_group(
    format, event_id, market_type_id, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>event_id</code> | <code>str</code> | The EventId of the desired event/game for which to pull all betting markets (includes outcomes/bets). |
| <code>market_type_id</code> | <code>str</code> | The Market Type ID of the desired MarketTypes to pull. Some common types include: <code>1</code> for Game Lines, <code>2</code> for Player Props, <code>3</code> for Team Props, <code>6</code> for Game Props |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>include</code> | <code>[IncludeOrStr](cbb_api/models/enums/include.py) \| None</code> | This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br><b>Important Note:</b> the default parameter of <code>available</code> is much faster and provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be several minutes old. For best performance, the default parameter is highly recommended. <br><br>Possible values include: <br><br><code>available</code> - excludes any betting outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster than using unlisted. <br><br><code>unlisted</code> - includes the most recently available betting outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much longer than available. <br><br><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;, [CbbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingMarketsByMarketTypeSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_markets_by_market_type_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_metadata(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BettingEntityMetadataCollection, CbbV3OddsBettingMetadataErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the list of MarketTypes, BetTypes, PeriodTypes, OutcomeTypes, and ResultTypes to map the IDs to descriptive names. Also includes a list of the MarketType, BetType & PeriodType combinations which we will have resulting for.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_metadata(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingEntityMetadataCollection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMetadataErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_metadata(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingEntityMetadataCollection
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingMetadataErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[BettingEntityMetadataCollection](cbb_api/models/betting_entity_metadata_collection.py), [CbbV3OddsBettingMetadataErrorBody](cbb_api/errors/cbb_v3_odds_betting_metadata_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BettingEntityMetadataCollection](cbb_api/models/betting_entity_metadata_collection.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingMetadataErrorBody](cbb_api/errors/cbb_v3_odds_betting_metadata_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_player_props_by_game(format: FormatOrStr, game_id: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingMarket], CbbV3OddsBettingPlayerPropsByGameErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is recommended to use the by Market Type endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_player_props_by_game(format, game_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingPlayerPropsByGameErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_player_props_by_game(format, game_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingPlayerPropsByGameErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>game_id</code> | <code>str</code> | The unique GameID of the game in question. |
| <code>include</code> | <code>[IncludeOrStr](cbb_api/models/enums/include.py) \| None</code> | This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br><br><br><b>Important Note:</b> the default parameter of available is much faster and provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be several minutes old. For best performance, the default parameter is highly recommended. <br><br><br><br>Possible values include: <br><br><br><code>available</code> - excludes any betting outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster than using unlisted. <br><br><br><code>unlisted</code> - includes the most recently available betting outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much longer than available. <br><br><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;, [CbbV3OddsBettingPlayerPropsByGameErrorBody](cbb_api/errors/cbb_v3_odds_betting_player_props_by_game_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingPlayerPropsByGameErrorBody](cbb_api/errors/cbb_v3_odds_betting_player_props_by_game_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_player_props_by_game_sportsbook_group(format: FormatOrStr, game_id: str, sportsbookgroup: str, *, include: IncludeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BettingMarket], CbbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This works in the same way as Betting Markets by Market Type but is prefiltered to the Player Props type only. Ideal if your application will only ever require Player Props, but if you also want Team Props etc. it is recommended to use the by Market Type endpoint. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_player_props_by_game_sportsbook_group(
    format, game_id, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_player_props_by_game_sportsbook_group(
    format, game_id, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BettingMarket]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>game_id</code> | <code>str</code> | The unique GameID of the game in question. |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>include</code> | <code>[IncludeOrStr](cbb_api/models/enums/include.py) \| None</code> | This parameter indicates which <code>BettingOutcome</code> records to return in the payload. By default, this endpoint only returns available outcomes, excluding the unlisted bets. <br><br><br><br><b>Important Note:</b> the default parameter of available is much faster and provides the best performance. Passing unlisted will return unlisted odds, but these are cached for much longer and may be several minutes old. For best performance, the default parameter is highly recommended. <br><br><br><br>Possible values include: <br><br><br><code>available</code> - excludes any betting outcomes that have been removed/unlisted by the respective sportsbook. This is more lightweight and delivers odds much faster than using unlisted. <br><br><br><code>unlisted</code> - includes the most recently available betting outcome per sportsbook, for each listed market, even those outcomes are expired/unlisted or otherwise unavailable from the respective sportsbook. This is a far heavier payload, and it's cached for much longer than available. <br><br><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;, [CbbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_player_props_by_game_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BettingMarket](cbb_api/models/betting_market.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_player_props_by_game_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_results_by_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BettingMarketResult, CbbV3OddsBettingResultsByMarketErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result: for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won or lost.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_results_by_market(format, market_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingMarketResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingResultsByMarketErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_results_by_market(format, market_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingMarketResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingResultsByMarketErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>market_id</code> | <code>str</code> | BettingMarketID of the market for which you would like to see resulted outcomes. Valid example ID <code>96401</code>, <code>93518</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[BettingMarketResult](cbb_api/models/betting_market_result.py), [CbbV3OddsBettingResultsByMarketErrorBody](cbb_api/errors/cbb_v3_odds_betting_results_by_market_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BettingMarketResult](cbb_api/models/betting_market_result.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingResultsByMarketErrorBody](cbb_api/errors/cbb_v3_odds_betting_results_by_market_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_results_by_market_sportsbook_group(format: FormatOrStr, market_id: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BettingMarketResult, CbbV3OddsBettingResultsByMarketSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provide a market ID that supports resulting (i.e. has a ResultType) and this endpoint will return a result: for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won or lost. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_results_by_market_sportsbook_group(
    format, market_id, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingMarketResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingResultsByMarketSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_results_by_market_sportsbook_group(
    format, market_id, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingMarketResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingResultsByMarketSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>market_id</code> | <code>str</code> | BettingMarketID of the market for which you would like to see resulted outcomes. Valid example ID <code>96401</code>, <code>93518</code> |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[BettingMarketResult](cbb_api/models/betting_market_result.py), [CbbV3OddsBettingResultsByMarketSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_results_by_market_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BettingMarketResult](cbb_api/models/betting_market_result.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingResultsByMarketSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_betting_results_by_market_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_splits_by_betting_market(format: FormatOrStr, market_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BettingMarketSplit, CbbV3OddsBettingSplitsByBettingMarketErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List of Money and Bet Percentage splits for each outcome type available in this market. This specific endpoint will return the movement from this market as well as the most recent.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_splits_by_betting_market(format, market_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingMarketSplit
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingSplitsByBettingMarketErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_splits_by_betting_market(
    format, market_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BettingMarketSplit
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingSplitsByBettingMarketErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>market_id</code> | <code>str</code> | The MarketId of the desired market for which to pull splits. MarketIds are pulled from the Betting Markets endpoints. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[BettingMarketSplit](cbb_api/models/betting_market_split.py), [CbbV3OddsBettingSplitsByBettingMarketErrorBody](cbb_api/errors/cbb_v3_odds_betting_splits_by_betting_market_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BettingMarketSplit](cbb_api/models/betting_market_split.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingSplitsByBettingMarketErrorBody](cbb_api/errors/cbb_v3_odds_betting_splits_by_betting_market_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_splits_by_game(format: FormatOrStr, game_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GameBettingSplit, CbbV3OddsBettingSplitsByGameErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List of Money and Bet Percentage splits for each market and their respective outcome types available in this game. This specific endpoint will return current splits for each available market and no line movement.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_splits_by_game(format, game_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GameBettingSplit
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingSplitsByGameErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_splits_by_game(format, game_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GameBettingSplit
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingSplitsByGameErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>game_id</code> | <code>str</code> | The ID of the game for which you want to receive splits for. GameIds are pulled from the Schedules and Games by Date endpoints. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[GameBettingSplit](cbb_api/models/game_betting_split.py), [CbbV3OddsBettingSplitsByGameErrorBody](cbb_api/errors/cbb_v3_odds_betting_splits_by_game_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GameBettingSplit](cbb_api/models/game_betting_split.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingSplitsByGameErrorBody](cbb_api/errors/cbb_v3_odds_betting_splits_by_game_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_trends_by_matchup(format: FormatOrStr, team: str, opponent: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MatchupTrends, CbbV3OddsBettingTrendsByMatchupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns trends data for a given pairing of teams. Will return data even if the teams are not set to play this season. Intended for use on a specific game though it will work for other comparisons if applicable.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_trends_by_matchup(format, team, opponent)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MatchupTrends
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingTrendsByMatchupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_trends_by_matchup(format, team, opponent)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MatchupTrends
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingTrendsByMatchupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>team</code> | <code>str</code> | The abbreviation of the requested team.<br><br>Examples: <code>OU</code>, <code>UK</code>. |
| <code>opponent</code> | <code>str</code> | The abbreviation of the requested opponent.<br><br>Examples: <code>OU</code>, <code>UK</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[MatchupTrends](cbb_api/models/matchup_trends.py), [CbbV3OddsBettingTrendsByMatchupErrorBody](cbb_api/errors/cbb_v3_odds_betting_trends_by_matchup_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[MatchupTrends](cbb_api/models/matchup_trends.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingTrendsByMatchupErrorBody](cbb_api/errors/cbb_v3_odds_betting_trends_by_matchup_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_betting_trends_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TeamTrends, CbbV3OddsBettingTrendsByTeamErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Describes recent team trends and performance against betting data in recent sets of games

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_trends_by_team(format, team)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamTrends
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingTrendsByTeamErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_betting_trends_by_team(format, team)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TeamTrends
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsBettingTrendsByTeamErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>team</code> | <code>str</code> | The abbreviation of the requested team.<br><br>Examples: <code>OU</code>, <code>UK</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[TeamTrends](cbb_api/models/team_trends.py), [CbbV3OddsBettingTrendsByTeamErrorBody](cbb_api/errors/cbb_v3_odds_betting_trends_by_team_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TeamTrends](cbb_api/models/team_trends.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsBettingTrendsByTeamErrorBody](cbb_api/errors/cbb_v3_odds_betting_trends_by_team_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_in_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfo], CbbV3OddsInGameOddsByDateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides in-play odds data for a given date. This means odds for games which are in-progress. Only serves the most recently seen data & does not include line movement.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_in_game_odds_by_date(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsInGameOddsByDateErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_in_game_odds_by_date(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsInGameOddsByDateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s). <br>Examples: <code>2018-11-20</code>, <code>2018-11-23</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;, [CbbV3OddsInGameOddsByDateErrorBody](cbb_api/errors/cbb_v3_odds_in_game_odds_by_date_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsInGameOddsByDateErrorBody](cbb_api/errors/cbb_v3_odds_in_game_odds_by_date_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_in_game_odds_by_date_sportsbook_group(format: FormatOrStr, date: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfo], CbbV3OddsInGameOddsByDateSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns in-play game odds (spread, moneyline, total) for games on a given date. Only returns the most recently seen odds, not inclusive of line movement. As this is in-game, it will only return results while the game is in progress. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_in_game_odds_by_date_sportsbook_group(
    format, date, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsInGameOddsByDateSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_in_game_odds_by_date_sportsbook_group(
    format, date, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsInGameOddsByDateSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s). <br>Examples: <code>2018-11-20</code>, <code>2018-11-23</code>. |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;, [CbbV3OddsInGameOddsByDateSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_in_game_odds_by_date_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsInGameOddsByDateSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_in_game_odds_by_date_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_in_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfo], CbbV3OddsInGameOddsLineMovementErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns in-play game odds (spread, moneyline, total) for games on a given date. Returns the full line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the second line.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_in_game_odds_line_movement(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsInGameOddsLineMovementErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_in_game_odds_line_movement(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsInGameOddsLineMovementErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are <code>17775</code> or <code>17776</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;, [CbbV3OddsInGameOddsLineMovementErrorBody](cbb_api/errors/cbb_v3_odds_in_game_odds_line_movement_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsInGameOddsLineMovementErrorBody](cbb_api/errors/cbb_v3_odds_in_game_odds_line_movement_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_in_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfo], CbbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns in-play game odds (spread, moneyline, total) for games on a given date. Returns the full line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_in_game_odds_line_movement_sportsbook_group(
    format, gameid, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_in_game_odds_line_movement_sportsbook_group(
    format, gameid, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are <code>17775</code> or <code>17776</code> |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;, [CbbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_in_game_odds_line_movement_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsInGameOddsLineMovementSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_in_game_odds_line_movement_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfoResult], CbbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns in-play game odds (spread, moneyline, total) for games on a given date. This also includes Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
    format, gameid, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfoResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group(
    format, gameid, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfoResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are <code>17775</code> or <code>17776</code> |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfoResult](cbb_api/models/game_info_result.py)&#93;, [CbbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfoResult](cbb_api/models/game_info_result.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsInGameOddsLineMovementWithResultingSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_in_game_odds_line_movement_with_resulting_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(format: FormatOrStr, date: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfo], CbbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the full-game and non-full-game odds (spread, moneyline, total) for games in a given week and season. Only returns the most recently seen odds, not inclusive of line movement. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
    format, date, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group(
    format, date, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s). <br>Examples: <code>2018-11-20</code>, <code>2018-11-23</code>. |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;, [CbbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsPreGameAndPeriodGameOddsByDateSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_pre_game_and_period_game_odds_by_date_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfo], CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the game odds ( for games on a given date. In this endpoint both full-game and partial-game odds are included. Returns the full line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
    format, gameid, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group(
    format, gameid, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are <code>17775</code> or <code>17776</code> |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;, [CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsPreGameAndPeriodGameOddsLineMovementSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_pre_game_and_period_game_odds_line_movement_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(format: FormatOrStr, gameid: str, sportsbookgroup: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfoResult], CbbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the game odds ( for games on a given date. In this endpoint both full-game and partial-game odds are included. This also includes Resulting: for markets with a ResultType, each line will be graded and it will be determined whether the bet would have won or lost. Returns the full line movement for the given game. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the second line. A Sportsbook Group must be specified as a URL parameter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
    format, gameid, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfoResult]
    case Failure(error=error):
        # TODO: Handle 'error' of type
        # CbbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody
        ...
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group(
    format, gameid, sportsbookgroup
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfoResult]
    case Failure(error=error):
        # TODO: Handle 'error' of type
        # CbbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody
        ...
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are <code>17775</code> or <code>17776</code> |
| <code>sportsbookgroup</code> | <code>str</code> | The name of the Sportsbook grouping.<br><br>Examples: <code>G1100</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfoResult](cbb_api/models/game_info_result.py)&#93;, [CbbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfoResult](cbb_api/models/game_info_result.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsPreGameAndPeriodGameOddsLineMovementWithResultingSportsbookGroupErrorBody](cbb_api/errors/cbb_v3_odds_pre_game_and_period_game_odds_line_movement_with_resulting_sportsbook_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_pre_game_odds_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfo], CbbV3OddsPreGameOddsByDateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the full-game core odds for games in a given date. This means moneyline, spread, and total. Only returns the most recently seen odds, not-including line movement.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_pre_game_odds_by_date(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsPreGameOddsByDateErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_pre_game_odds_by_date(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsPreGameOddsByDateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s). <br>Examples: <code>2018-11-20</code>, <code>2018-11-23</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;, [CbbV3OddsPreGameOddsByDateErrorBody](cbb_api/errors/cbb_v3_odds_pre_game_odds_by_date_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsPreGameOddsByDateErrorBody](cbb_api/errors/cbb_v3_odds_pre_game_odds_by_date_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_pre_game_odds_line_movement(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GameInfo], CbbV3OddsPreGameOddsLineMovementErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the full-game core odds for a given GameID. This means moneyline, spread, and total. Only returns the most recently seen odds, not-including line movement. This endpoint has a longer cache as it is meant for historical data/line movement rather than the most up to the second line.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_pre_game_odds_line_movement(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsPreGameOddsLineMovementErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_pre_game_odds_line_movement(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GameInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsPreGameOddsLineMovementErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are <code>17775</code> or <code>17776</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;, [CbbV3OddsPreGameOddsLineMovementErrorBody](cbb_api/errors/cbb_v3_odds_pre_game_odds_line_movement_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GameInfo](cbb_api/models/game_info.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsPreGameOddsLineMovementErrorBody](cbb_api/errors/cbb_v3_odds_pre_game_odds_line_movement_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_odds_sportsbooks_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Sportsbook], CbbV3OddsSportsbooksByActiveErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

A list of all available sportsbooks with their associated unique IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_odds.with_raw_response.cbb_v3_odds_sportsbooks_by_active(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Sportsbook]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsSportsbooksByActiveErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_odds.with_raw_response.cbb_v3_odds_sportsbooks_by_active(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Sportsbook]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3OddsSportsbooksByActiveErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Sportsbook](cbb_api/models/sportsbook.py)&#93;, [CbbV3OddsSportsbooksByActiveErrorBody](cbb_api/errors/cbb_v3_odds_sportsbooks_by_active_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Sportsbook](cbb_api/models/sportsbook.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3OddsSportsbooksByActiveErrorBody](cbb_api/errors/cbb_v3_odds_sportsbooks_by_active_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## CbbV3Scores

> Source: [CbbV3Scores](cbb_api/apis/cbb_v3_scores.py)

<details>
<summary><code>def cbb_v3_scores_are_games_in_progress(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[bool, CbbV3ScoresAreGamesInProgressErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns <code>true</code> if there is at least one game being played at the time of the request or <code>false</code> if there are none.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_are_games_in_progress(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type bool
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresAreGamesInProgressErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_are_games_in_progress(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type bool
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresAreGamesInProgressErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;bool, [CbbV3ScoresAreGamesInProgressErrorBody](cbb_api/errors/cbb_v3_scores_are_games_in_progress_error.py)&#93;</code>

**On `Success`**: `payload` is <code>bool</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresAreGamesInProgressErrorBody](cbb_api/errors/cbb_v3_scores_are_games_in_progress_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_games_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Game], CbbV3ScoresGamesByDateFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full scores and gameday info, including half scores, delivered after the game ends.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_games_by_date_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Game]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresGamesByDateFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_games_by_date_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Game]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresGamesByDateFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s).<br><br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Game](cbb_api/models/game.py)&#93;, [CbbV3ScoresGamesByDateFinalErrorBody](cbb_api/errors/cbb_v3_scores_games_by_date_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Game](cbb_api/models/game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresGamesByDateFinalErrorBody](cbb_api/errors/cbb_v3_scores_games_by_date_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_games_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Game], CbbV3ScoresGamesByDateLiveFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full scores and gameday info delivered live and post-game. Live data includes half and score info. Gameday info includes weather, TV channel etc

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_games_by_date_live_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Game]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresGamesByDateLiveFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_games_by_date_live_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Game]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresGamesByDateLiveFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s).<br><br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Game](cbb_api/models/game.py)&#93;, [CbbV3ScoresGamesByDateLiveFinalErrorBody](cbb_api/errors/cbb_v3_scores_games_by_date_live_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Game](cbb_api/models/game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresGamesByDateLiveFinalErrorBody](cbb_api/errors/cbb_v3_scores_games_by_date_live_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_games_by_season(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Game], CbbV3ScoresGamesBySeasonErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

A full schedule of games for a given season.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_games_by_season(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Game]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresGamesBySeasonErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_games_by_season(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Game]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresGamesBySeasonErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Game](cbb_api/models/game.py)&#93;, [CbbV3ScoresGamesBySeasonErrorBody](cbb_api/errors/cbb_v3_scores_games_by_season_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Game](cbb_api/models/game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresGamesBySeasonErrorBody](cbb_api/errors/cbb_v3_scores_games_by_season_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_games_by_season_final(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Game], CbbV3ScoresGamesBySeasonFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full scores and gameday info, including half scores, for all games of a given season, delivered after each game ends

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_games_by_season_final(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Game]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresGamesBySeasonFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_games_by_season_final(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Game]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresGamesBySeasonFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Game](cbb_api/models/game.py)&#93;, [CbbV3ScoresGamesBySeasonFinalErrorBody](cbb_api/errors/cbb_v3_scores_games_by_season_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Game](cbb_api/models/game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresGamesBySeasonFinalErrorBody](cbb_api/errors/cbb_v3_scores_games_by_season_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_games_basic_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[ScoreBasic], CbbV3ScoresGamesBasicByDateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

A slimmed-down score endpoint, giving just the quarter scores and final score, for simple applications.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_games_basic_by_date(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ScoreBasic]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresGamesBasicByDateErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_games_basic_by_date(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ScoreBasic]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresGamesBasicByDateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s).<br><br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[ScoreBasic](cbb_api/models/score_basic.py)&#93;, [CbbV3ScoresGamesBasicByDateErrorBody](cbb_api/errors/cbb_v3_scores_games_basic_by_date_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[ScoreBasic](cbb_api/models/score_basic.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresGamesBasicByDateErrorBody](cbb_api/errors/cbb_v3_scores_games_basic_by_date_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_league_hierarchy(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Conference], CbbV3ScoresLeagueHierarchyErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the list of conferences, their teams, and standings.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_league_hierarchy(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Conference]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresLeagueHierarchyErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_league_hierarchy(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Conference]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresLeagueHierarchyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Conference](cbb_api/models/conference.py)&#93;, [CbbV3ScoresLeagueHierarchyErrorBody](cbb_api/errors/cbb_v3_scores_league_hierarchy_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Conference](cbb_api/models/conference.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresLeagueHierarchyErrorBody](cbb_api/errors/cbb_v3_scores_league_hierarchy_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_player_details_by_active(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Player], CbbV3ScoresPlayerDetailsByActiveErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full player bio and details, including injury notes, for all active players.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_player_details_by_active(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Player]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresPlayerDetailsByActiveErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_player_details_by_active(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Player]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresPlayerDetailsByActiveErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Player](cbb_api/models/player.py)&#93;, [CbbV3ScoresPlayerDetailsByActiveErrorBody](cbb_api/errors/cbb_v3_scores_player_details_by_active_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Player](cbb_api/models/player.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresPlayerDetailsByActiveErrorBody](cbb_api/errors/cbb_v3_scores_player_details_by_active_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_player_details_by_active2(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[PlayerBasic], CbbV3ScoresPlayerDetailsByActive2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full player bio and details, including injury notes, for all active players.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_player_details_by_active2(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerBasic]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresPlayerDetailsByActive2ErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_player_details_by_active2(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerBasic]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresPlayerDetailsByActive2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[PlayerBasic](cbb_api/models/player_basic.py)&#93;, [CbbV3ScoresPlayerDetailsByActive2ErrorBody](cbb_api/errors/cbb_v3_scores_player_details_by_active2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[PlayerBasic](cbb_api/models/player_basic.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresPlayerDetailsByActive2ErrorBody](cbb_api/errors/cbb_v3_scores_player_details_by_active2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_player_details_by_injured(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Player], CbbV3ScoresPlayerDetailsByInjuredErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint provides all currently injured college basketball players, along with injury details.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_player_details_by_injured(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Player]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresPlayerDetailsByInjuredErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_player_details_by_injured(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Player]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresPlayerDetailsByInjuredErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Player](cbb_api/models/player.py)&#93;, [CbbV3ScoresPlayerDetailsByInjuredErrorBody](cbb_api/errors/cbb_v3_scores_player_details_by_injured_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Player](cbb_api/models/player.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresPlayerDetailsByInjuredErrorBody](cbb_api/errors/cbb_v3_scores_player_details_by_injured_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_player_details_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Player], CbbV3ScoresPlayerDetailsByTeamErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full player bio and details, including injury notes, for all available players by team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_player_details_by_team(format, team)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Player]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresPlayerDetailsByTeamErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_player_details_by_team(format, team)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Player]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresPlayerDetailsByTeamErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>team</code> | <code>str</code> | The abbreviation of the requested team.<br><br>Examples: <code>SF</code>, <code>NYY</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Player](cbb_api/models/player.py)&#93;, [CbbV3ScoresPlayerDetailsByTeamErrorBody](cbb_api/errors/cbb_v3_scores_player_details_by_team_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Player](cbb_api/models/player.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresPlayerDetailsByTeamErrorBody](cbb_api/errors/cbb_v3_scores_player_details_by_team_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_player_profiles_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[PlayerBasic], CbbV3ScoresPlayerProfilesByTeamErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Roster information for a given team. Player profiles include basic biographical information, position, etc. Specify a team code parameter to receive all players currently on that team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_player_profiles_by_team(format, team)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerBasic]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresPlayerProfilesByTeamErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_player_profiles_by_team(format, team)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerBasic]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresPlayerProfilesByTeamErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>team</code> | <code>str</code> | The abbreviation of the requested team.<br><br>Examples: <code>SMU</code>, <code>UCLA</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[PlayerBasic](cbb_api/models/player_basic.py)&#93;, [CbbV3ScoresPlayerProfilesByTeamErrorBody](cbb_api/errors/cbb_v3_scores_player_profiles_by_team_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[PlayerBasic](cbb_api/models/player_basic.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresPlayerProfilesByTeamErrorBody](cbb_api/errors/cbb_v3_scores_player_profiles_by_team_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_schedules_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Game], CbbV3ScoresSchedulesByTeamErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

A list of all a team's games for a given season.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_schedules_by_team(format, season, team)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Game]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresSchedulesByTeamErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_schedules_by_team(format, season, team)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Game]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresSchedulesByTeamErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc. |
| <code>team</code> | <code>str</code> | The abbreviation of the requested team.<br>Examples: <code>SF</code>, <code>NYY</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Game](cbb_api/models/game.py)&#93;, [CbbV3ScoresSchedulesByTeamErrorBody](cbb_api/errors/cbb_v3_scores_schedules_by_team_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Game](cbb_api/models/game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresSchedulesByTeamErrorBody](cbb_api/errors/cbb_v3_scores_schedules_by_team_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_schedules_basic(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[ScheduleBasic], CbbV3ScoresSchedulesBasicErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

A lightweight schedule endpoint without gameday information. Home and away teams, the date and time of the game, and season type etc. are included. Ideal for the most basic information required to build a schedule.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_schedules_basic(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ScheduleBasic]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresSchedulesBasicErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_schedules_basic(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ScheduleBasic]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresSchedulesBasicErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018PRE</code>, <code>2018POST</code>, <code>2018STAR</code>, <code>2019</code>, etc. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[ScheduleBasic](cbb_api/models/schedule_basic.py)&#93;, [CbbV3ScoresSchedulesBasicErrorBody](cbb_api/errors/cbb_v3_scores_schedules_basic_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[ScheduleBasic](cbb_api/models/schedule_basic.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresSchedulesBasicErrorBody](cbb_api/errors/cbb_v3_scores_schedules_basic_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_season_current(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Season, CbbV3ScoresSeasonCurrentErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Year of the current season. This value changes at the start of the new league year. For leagues that run over two years, this is the year the season starts, not ends.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_season_current(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Season
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresSeasonCurrentErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_season_current(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Season
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresSeasonCurrentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[Season](cbb_api/models/season.py), [CbbV3ScoresSeasonCurrentErrorBody](cbb_api/errors/cbb_v3_scores_season_current_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Season](cbb_api/models/season.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresSeasonCurrentErrorBody](cbb_api/errors/cbb_v3_scores_season_current_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_stadiums(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Stadium], CbbV3ScoresStadiumsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns all stadiums in CBB with school, capacity, latitude/longitude, city and state (and where applicable country.)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_stadiums(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Stadium]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresStadiumsErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_stadiums(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Stadium]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresStadiumsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Stadium](cbb_api/models/stadium.py)&#93;, [CbbV3ScoresStadiumsErrorBody](cbb_api/errors/cbb_v3_scores_stadiums_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Stadium](cbb_api/models/stadium.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresStadiumsErrorBody](cbb_api/errors/cbb_v3_scores_stadiums_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_team_game_logs_by_season(format: FormatOrStr, season: str, teamid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[TeamGame], CbbV3ScoresTeamGameLogsBySeasonErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Game by game log of total team statistics.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_team_game_logs_by_season(
    format, season, teamid, numberofgames
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[TeamGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTeamGameLogsBySeasonErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_team_game_logs_by_season(
    format, season, teamid, numberofgames
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[TeamGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTeamGameLogsBySeasonErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Season to get games from. Example <code>2019POST</code>, <code>2020</code> |
| <code>teamid</code> | <code>str</code> | Unique ID of team.  Example <code> 1 </code> |
| <code>numberofgames</code> | <code>str</code> | How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[TeamGame](cbb_api/models/team_game.py)&#93;, [CbbV3ScoresTeamGameLogsBySeasonErrorBody](cbb_api/errors/cbb_v3_scores_team_game_logs_by_season_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[TeamGame](cbb_api/models/team_game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresTeamGameLogsBySeasonErrorBody](cbb_api/errors/cbb_v3_scores_team_game_logs_by_season_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_team_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[TeamGame], CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the box score statistical record team-wide (aggregated from all players) for teams playing on a given date, both live and post-game.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_team_game_stats_by_date_live_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[TeamGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_team_game_stats_by_date_live_final(
    format, date
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[TeamGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s).<br><br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[TeamGame](cbb_api/models/team_game.py)&#93;, [CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody](cbb_api/errors/cbb_v3_scores_team_game_stats_by_date_live_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[TeamGame](cbb_api/models/team_game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresTeamGameStatsByDateLiveFinalErrorBody](cbb_api/errors/cbb_v3_scores_team_game_stats_by_date_live_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_team_profiles_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Team], CbbV3ScoresTeamProfilesAllErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full team information: team name and city, school, conference, and colors. Also contains full stadium data. This endpoint returns all teams regardless of current active status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_team_profiles_all(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Team]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTeamProfilesAllErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_team_profiles_all(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Team]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTeamProfilesAllErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[Team](cbb_api/models/team.py)&#93;, [CbbV3ScoresTeamProfilesAllErrorBody](cbb_api/errors/cbb_v3_scores_team_profiles_all_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Team](cbb_api/models/team.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresTeamProfilesAllErrorBody](cbb_api/errors/cbb_v3_scores_team_profiles_all_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_team_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[TeamSeason], CbbV3ScoresTeamSeasonStatsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns all season-long stats (i.e. the season total, not each individual game record) for all teams (aggregated from all players) for a given season.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_team_season_stats(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[TeamSeason]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTeamSeasonStatsErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_team_season_stats(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[TeamSeason]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTeamSeasonStatsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018POST</code>, <code>2019</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[TeamSeason](cbb_api/models/team_season.py)&#93;, [CbbV3ScoresTeamSeasonStatsErrorBody](cbb_api/errors/cbb_v3_scores_team_season_stats_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[TeamSeason](cbb_api/models/team_season.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresTeamSeasonStatsErrorBody](cbb_api/errors/cbb_v3_scores_team_season_stats_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_teams_basic_all(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[TeamBasic], CbbV3ScoresTeamsBasicAllErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The most basic top-line team information, such as team name, school and city, conference and division, stadium ID, and team colors. Returns all teams regardless of current active status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_teams_basic_all(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[TeamBasic]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTeamsBasicAllErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_teams_basic_all(format)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[TeamBasic]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTeamsBasicAllErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[TeamBasic](cbb_api/models/team_basic.py)&#93;, [CbbV3ScoresTeamsBasicAllErrorBody](cbb_api/errors/cbb_v3_scores_teams_basic_all_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[TeamBasic](cbb_api/models/team_basic.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresTeamsBasicAllErrorBody](cbb_api/errors/cbb_v3_scores_teams_basic_all_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_scores_tournament_hierarchy(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Tournament, CbbV3ScoresTournamentHierarchyErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns tournament info and games associated with the NCAA Tournament for the given season.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_scores.with_raw_response.cbb_v3_scores_tournament_hierarchy(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Tournament
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTournamentHierarchyErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_scores.with_raw_response.cbb_v3_scores_tournament_hierarchy(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Tournament
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3ScoresTournamentHierarchyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season.<br>Examples: <code>2018</code>, <code>2019</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[Tournament](cbb_api/models/tournament.py), [CbbV3ScoresTournamentHierarchyErrorBody](cbb_api/errors/cbb_v3_scores_tournament_hierarchy_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Tournament](cbb_api/models/tournament.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3ScoresTournamentHierarchyErrorBody](cbb_api/errors/cbb_v3_scores_tournament_hierarchy_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## CbbV3Stats

> Source: [CbbV3Stats](cbb_api/apis/cbb_v3_stats.py)

<details>
<summary><code>def cbb_v3_stats_box_score_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BoxScore, CbbV3StatsBoxScoreFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full statistical information for a specified game, down to the team and player stat level, delivered after the game is complete.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_box_score_final(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BoxScore
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsBoxScoreFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_box_score_final(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BoxScore
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsBoxScoreFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are <code>14620</code> or <code>16905</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[BoxScore](cbb_api/models/box_score.py), [CbbV3StatsBoxScoreFinalErrorBody](cbb_api/errors/cbb_v3_stats_box_score_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BoxScore](cbb_api/models/box_score.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsBoxScoreFinalErrorBody](cbb_api/errors/cbb_v3_stats_box_score_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_stats_box_score_live_final(format: FormatOrStr, gameid: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BoxScore, CbbV3StatsBoxScoreLiveFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full statistical information for a specified game, down to the team and player stat level, delivered live during the game, called per individual game.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_box_score_live_final(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BoxScore
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsBoxScoreLiveFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_box_score_live_final(format, gameid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BoxScore
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsBoxScoreLiveFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>gameid</code> | <code>str</code> | The GameID of an CBB game.  GameIDs can be found in the Games API.  Valid entries are <code>14620</code> or <code>16905</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;[BoxScore](cbb_api/models/box_score.py), [CbbV3StatsBoxScoreLiveFinalErrorBody](cbb_api/errors/cbb_v3_stats_box_score_live_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BoxScore](cbb_api/models/box_score.py)</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsBoxScoreLiveFinalErrorBody](cbb_api/errors/cbb_v3_stats_box_score_live_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_stats_box_scores_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BoxScore], CbbV3StatsBoxScoresByDateFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full statistical information for all games on a given date, down to the team and player stat level, delivered after the game is complete.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_box_scores_by_date_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BoxScore]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsBoxScoresByDateFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_box_scores_by_date_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BoxScore]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsBoxScoresByDateFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s).<br><br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BoxScore](cbb_api/models/box_score.py)&#93;, [CbbV3StatsBoxScoresByDateFinalErrorBody](cbb_api/errors/cbb_v3_stats_box_scores_by_date_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BoxScore](cbb_api/models/box_score.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsBoxScoresByDateFinalErrorBody](cbb_api/errors/cbb_v3_stats_box_scores_by_date_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_stats_box_scores_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BoxScore], CbbV3StatsBoxScoresByDateLiveFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Full statistical information for games, down to the team and player stat level, delivered live during the game, called for a given date (returns all games on that date.)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_box_scores_by_date_live_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BoxScore]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsBoxScoresByDateLiveFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_box_scores_by_date_live_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BoxScore]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsBoxScoresByDateLiveFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s).<br><br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BoxScore](cbb_api/models/box_score.py)&#93;, [CbbV3StatsBoxScoresByDateLiveFinalErrorBody](cbb_api/errors/cbb_v3_stats_box_scores_by_date_live_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BoxScore](cbb_api/models/box_score.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsBoxScoresByDateLiveFinalErrorBody](cbb_api/errors/cbb_v3_stats_box_scores_by_date_live_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_stats_box_scores_delta_by_date(format: FormatOrStr, date: str, minutes: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[BoxScore], CbbV3StatsBoxScoresDeltaByDateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This method returns all box scores for a given season and week, but only returns player stats that have changed in the last X minutes as specified in your API call. By definition this is a live endpoint, not final.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_box_scores_delta_by_date(format, date, minutes)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BoxScore]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsBoxScoresDeltaByDateErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_box_scores_delta_by_date(format, date, minutes)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[BoxScore]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsBoxScoresDeltaByDateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s).<br><br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>. |
| <code>minutes</code> | <code>str</code> | Only returns player statistics that have changed in the last X minutes.  You specify how many minutes in time to go back.  Valid entries are:<br><code>1</code> or <code>2</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[BoxScore](cbb_api/models/box_score.py)&#93;, [CbbV3StatsBoxScoresDeltaByDateErrorBody](cbb_api/errors/cbb_v3_stats_box_scores_delta_by_date_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[BoxScore](cbb_api/models/box_score.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsBoxScoresDeltaByDateErrorBody](cbb_api/errors/cbb_v3_stats_box_scores_delta_by_date_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_stats_player_game_logs_by_season(format: FormatOrStr, season: str, playerid: str, numberofgames: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[PlayerGame], CbbV3StatsPlayerGameLogsBySeasonErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Specify a season, a player, and number of games (either an integer or <code>all</code>) to see all of their box score logs. Refreshed after their most recent game is complete.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_player_game_logs_by_season(
    format, season, playerid, numberofgames
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsPlayerGameLogsBySeasonErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_player_game_logs_by_season(
    format, season, playerid, numberofgames
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsPlayerGameLogsBySeasonErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Season to get games from. Example <code>2019POST</code>, <code>2020</code> |
| <code>playerid</code> | <code>str</code> | Unique SportsDataIO Player ID.Example:<code>60008094</code>. |
| <code>numberofgames</code> | <code>str</code> | How many games to return. Example <code>all</code>, <code>10</code>, <code>25</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[PlayerGame](cbb_api/models/player_game.py)&#93;, [CbbV3StatsPlayerGameLogsBySeasonErrorBody](cbb_api/errors/cbb_v3_stats_player_game_logs_by_season_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[PlayerGame](cbb_api/models/player_game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsPlayerGameLogsBySeasonErrorBody](cbb_api/errors/cbb_v3_stats_player_game_logs_by_season_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_stats_player_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[PlayerGame], CbbV3StatsPlayerGameStatsByDateFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the box score statistical record for all involved players across all teams' games on a given date. After each game has concluded its players' records are added.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_player_game_stats_by_date_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsPlayerGameStatsByDateFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_player_game_stats_by_date_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsPlayerGameStatsByDateFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s).<br><br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[PlayerGame](cbb_api/models/player_game.py)&#93;, [CbbV3StatsPlayerGameStatsByDateFinalErrorBody](cbb_api/errors/cbb_v3_stats_player_game_stats_by_date_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[PlayerGame](cbb_api/models/player_game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsPlayerGameStatsByDateFinalErrorBody](cbb_api/errors/cbb_v3_stats_player_game_stats_by_date_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_stats_player_game_stats_by_date_live_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[PlayerGame], CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the box score statistical record for all involved players across a given date, updated live as the game takes place.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_player_game_stats_by_date_live_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_player_game_stats_by_date_live_final(
    format, date
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s).<br><br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[PlayerGame](cbb_api/models/player_game.py)&#93;, [CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody](cbb_api/errors/cbb_v3_stats_player_game_stats_by_date_live_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[PlayerGame](cbb_api/models/player_game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsPlayerGameStatsByDateLiveFinalErrorBody](cbb_api/errors/cbb_v3_stats_player_game_stats_by_date_live_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_stats_player_season_stats(format: FormatOrStr, season: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[PlayerSeason], CbbV3StatsPlayerSeasonStatsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns all season-long stats (i.e. the season total, not each individual game record) for all players for a given season.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_player_season_stats(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerSeason]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsPlayerSeasonStatsErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_player_season_stats(format, season)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerSeason]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsPlayerSeasonStatsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018POST</code>, <code>2019</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[PlayerSeason](cbb_api/models/player_season.py)&#93;, [CbbV3StatsPlayerSeasonStatsErrorBody](cbb_api/errors/cbb_v3_stats_player_season_stats_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[PlayerSeason](cbb_api/models/player_season.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsPlayerSeasonStatsErrorBody](cbb_api/errors/cbb_v3_stats_player_season_stats_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_stats_player_season_stats_by_team(format: FormatOrStr, season: str, team: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[PlayerSeason], CbbV3StatsPlayerSeasonStatsByTeamErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns all season-long stats (i.e. the season total, not each individual game record) for a given team's players in a given season.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_player_season_stats_by_team(format, season, team)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerSeason]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsPlayerSeasonStatsByTeamErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_player_season_stats_by_team(
    format, season, team
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[PlayerSeason]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsPlayerSeasonStatsByTeamErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>season</code> | <code>str</code> | Year of the season (with optional season type).<br>Examples: <code>2018</code>, <code>2018POST</code>, <code>2019</code>. |
| <code>team</code> | <code>str</code> | The abbreviation of the requested team.<br><br>Examples: <code>SF</code>, <code>NYY</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[PlayerSeason](cbb_api/models/player_season.py)&#93;, [CbbV3StatsPlayerSeasonStatsByTeamErrorBody](cbb_api/errors/cbb_v3_stats_player_season_stats_by_team_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[PlayerSeason](cbb_api/models/player_season.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsPlayerSeasonStatsByTeamErrorBody](cbb_api/errors/cbb_v3_stats_player_season_stats_by_team_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cbb_v3_stats_team_game_stats_by_date_final(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[TeamGame], CbbV3StatsTeamGameStatsByDateFinalErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the box score statistical record team-wide (aggregated from all players) for all games on a given date, updated as each game concludes.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cbb_v3_stats.with_raw_response.cbb_v3_stats_team_game_stats_by_date_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[TeamGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsTeamGameStatsByDateFinalErrorBody
```

**Async**

```python
result = await async_client.cbb_v3_stats.with_raw_response.cbb_v3_stats_team_game_stats_by_date_final(format, date)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[TeamGame]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CbbV3StatsTeamGameStatsByDateFinalErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>format</code> | <code>[FormatOrStr](cbb_api/models/enums/format.py)</code> | Desired response format. Valid entries are <code>JSON</code> or <code>XML</code>. |
| <code>date</code> | <code>str</code> | The date of the game(s).<br><br>Examples: <code>2018-FEB-27</code>, <code>2017-DEC-01</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](cbb_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](cbb_api/core/results.py)&#91;list&#91;[TeamGame](cbb_api/models/team_game.py)&#93;, [CbbV3StatsTeamGameStatsByDateFinalErrorBody](cbb_api/errors/cbb_v3_stats_team_game_stats_by_date_final_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[TeamGame](cbb_api/models/team_game.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[CbbV3StatsTeamGameStatsByDateFinalErrorBody](cbb_api/errors/cbb_v3_stats_team_game_stats_by_date_final_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[Unauthorized](cbb_api/models/unauthorized.py)</code> |
| anything unmapped | <code>[RawError](cbb_api/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

