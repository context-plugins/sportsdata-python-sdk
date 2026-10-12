<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — SportsDataIO (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | SportsDataIO |
| Root package | `sports_data_io` |
| Distribution name | `sports-data-io` |
| Requires | Python 3.10 or later |
| API spec version | `1.0` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from sports_data_io import SportsDataIoClient

client = SportsDataIoClient(api_key_header="YOUR_API_KEY", api_key_query="YOUR_API_KEY")

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with SportsDataIoClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run

from sports_data_io import AsyncSportsDataIoClient


async def main() -> None:
    client = AsyncSportsDataIoClient(api_key_header="YOUR_API_KEY", api_key_query="YOUR_API_KEY")
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncSportsDataIoClient(...) as client:` closes the pool on exit.

`AsyncClient` (`sports_data_io/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `SportsDataIoClient` and `AsyncSportsDataIoClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.cbb_v3_odds`). Every constructor argument is optional and keyword-only. Sources: `sports_data_io/client.py`, `sports_data_io/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `base_url` | `str \| None` | `str \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `retry_options` | `int \| RetryOptionsOrDict \| None` | `int \| RetryOptionsOrDict \| None` | `None` |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `api_key_header` | `str \| None` | `str \| None` | `None` |
| `api_key_query` | `str \| None` | `str \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `RetryOptionsOrDict` | `sports_data_io.core` | a retry count, `RetryOptions`, or a dict: `max_retries: int` · `initial_delay: float` · `backoff_factor: float` · `max_delay: float` · `max_jitter: float` · `status_codes_to_retry: frozenset[int]` · `http_methods_to_retry: frozenset[HttpMethod]` |
| `HttpClient` | `sports_data_io.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()`; `send` returns once the head has arrived and never reads the body, and raises `TransportError` (from `core`) when no response arrives — anything else it raises is never retried |
| `AsyncHttpClient` | `sports_data_io.core` | protocol — `async send(request: HttpRequest) -> AsyncHttpResponse` · `async aclose()`; the same obligation, awaited |

### Retries — on by default

`retry_options` left at `None` applies the default `RetryOptions` policy below, so an unconfigured client **retries**: a request whose method is in `http_methods_to_retry` is sent again when it gets a status in `status_codes_to_retry`, or no response at all, and the last outcome reaches you only once its retries are spent. A body that cannot be re-sent byte for byte — a streamed file upload — is never retried. `retry_options=0` (or `{"max_retries": 0}`) turns retrying off; a bare count sets `max_retries` and leaves every other field at its default.

`RetryOptions` fields (source: `sports_data_io/core/retries.py`). Pass only the fields you change; each one left out takes its default:

| Field | Type | Default |
| --- | --- | --- |
| `max_retries` | `int` | `3` |
| `initial_delay` | `float` (seconds) | `1.0` |
| `backoff_factor` | `float` | `2.0` |
| `max_delay` | `float` (seconds) | `60.0` |
| `max_jitter` | `float` (seconds) | `0.5` |
| `status_codes_to_retry` | `frozenset[int]` | `frozenset({408, 429, 500, 502, 503, 504})` |
| `http_methods_to_retry` | `frozenset[HttpMethod]` | `frozenset({"GET", "HEAD", "PUT", "OPTIONS"})` |

The wait before retry *n* is `initial_delay × backoff_factor^(n−1)` plus up to `max_jitter` of random delay, the sum capped at `max_delay`; a `Retry-After` header replaces it, trimmed to `max_delay`.

A single call overrides two of these through `request_options` (`sports_data_io/core/request_options.py`): `max_retries` and `status_codes_to_retry`, each merged over the client's policy field by field — `request_options={"max_retries": 0}` turns retrying off for that one call and leaves every other call alone.

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.status_code` and `.headers`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `sports_data_io/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`sports_data_io/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any`.

Core runtime types (`sports_data_io/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `sports_data_io/errors/` or `RawError` | `error: E` · `status_code: int` · `headers: Mapping[str, str]` | `sports_data_io/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `status_code: int` · `headers: Mapping[str, str]` (both on either) | `sports_data_io/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` | `sports_data_io/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
try:
    response = client.cbb_v3_odds.cbb_v3_odds_alternate_market_pre_game_odds_by_date(
        "some example string", format_=Format.JSON
    )
except ApiError as e:
    # Case A — typed error: e.error is CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody
    if isinstance(e.error, Unauthorized):
        # Handle 401
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **741 operations**, **741 are Case A (typed)** and **0 are Case B (raw)**.

---

## Operations — by controller (50 pages, 741 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every *generated* type it names, with the module that declares it. A runtime type — a file alias, a date/time or byte converter — is not listed there.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout, extra headers, `max_retries` or `status_codes_to_retry`; every signature ends with it | here (`sports_data_io/core/request_options.py`), Retries |
| **Base URL `https://api.sportsdata.io`** — this SDK's only server; override it with `base_url="https://…"` | Servers & auth |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.cbb_v3_odds` | 34 | [map/operations/cbb_v3_odds.md](map/operations/cbb_v3_odds.md) |
| `client.cbb_v3_scores` | 22 | [map/operations/cbb_v3_scores.md](map/operations/cbb_v3_scores.md) |
| `client.cbb_v3_stats` | 11 | [map/operations/cbb_v3_stats.md](map/operations/cbb_v3_stats.md) |
| `client.cfb_v3_odds` | 34 | [map/operations/cfb_v3_odds.md](map/operations/cfb_v3_odds.md) |
| `client.cfb_v3_scores` | 26 | [map/operations/cfb_v3_scores.md](map/operations/cfb_v3_scores.md) |
| `client.cfb_v3_stats` | 13 | [map/operations/cfb_v3_stats.md](map/operations/cfb_v3_stats.md) |
| `client.cwbb_v3_scores` | 8 | [map/operations/cwbb_v3_scores.md](map/operations/cwbb_v3_scores.md) |
| `client.golf_v2` | 23 | [map/operations/golf_v2.md](map/operations/golf_v2.md) |
| `client.golf_v3_headshots` | 1 | [map/operations/golf_v3_headshots.md](map/operations/golf_v3_headshots.md) |
| `client.golf_v3_odds` | 21 | [map/operations/golf_v3_odds.md](map/operations/golf_v3_odds.md) |
| `client.golf_v3_roto_baller_premium_news` | 2 | [map/operations/golf_v3_roto_baller_premium_news.md](map/operations/golf_v3_roto_baller_premium_news.md) |
| `client.mlb_v3_headshots` | 1 | [map/operations/mlb_v3_headshots.md](map/operations/mlb_v3_headshots.md) |
| `client.mlb_v3_odds` | 34 | [map/operations/mlb_v3_odds.md](map/operations/mlb_v3_odds.md) |
| `client.mlb_v3_play_by_play` | 3 | [map/operations/mlb_v3_play_by_play.md](map/operations/mlb_v3_play_by_play.md) |
| `client.mlb_v3_projections` | 8 | [map/operations/mlb_v3_projections.md](map/operations/mlb_v3_projections.md) |
| `client.mlb_v3_roto_baller_premium_news` | 2 | [map/operations/mlb_v3_roto_baller_premium_news.md](map/operations/mlb_v3_roto_baller_premium_news.md) |
| `client.mlb_v3_scores` | 26 | [map/operations/mlb_v3_scores.md](map/operations/mlb_v3_scores.md) |
| `client.mlb_v3_stats` | 17 | [map/operations/mlb_v3_stats.md](map/operations/mlb_v3_stats.md) |
| `client.mma_v3_odds` | 10 | [map/operations/mma_v3_odds.md](map/operations/mma_v3_odds.md) |
| `client.mma_v3_scores` | 6 | [map/operations/mma_v3_scores.md](map/operations/mma_v3_scores.md) |
| `client.mma_v3_stats` | 4 | [map/operations/mma_v3_stats.md](map/operations/mma_v3_stats.md) |
| `client.nascar_v2` | 13 | [map/operations/nascar_v2.md](map/operations/nascar_v2.md) |
| `client.nascar_v3_odds` | 10 | [map/operations/nascar_v3_odds.md](map/operations/nascar_v3_odds.md) |
| `client.nba_v3_headshots` | 1 | [map/operations/nba_v3_headshots.md](map/operations/nba_v3_headshots.md) |
| `client.nba_v3_odds` | 34 | [map/operations/nba_v3_odds.md](map/operations/nba_v3_odds.md) |
| `client.nba_v3_play_by_play` | 3 | [map/operations/nba_v3_play_by_play.md](map/operations/nba_v3_play_by_play.md) |
| `client.nba_v3_projections` | 6 | [map/operations/nba_v3_projections.md](map/operations/nba_v3_projections.md) |
| `client.nba_v3_roto_baller_premium_news` | 2 | [map/operations/nba_v3_roto_baller_premium_news.md](map/operations/nba_v3_roto_baller_premium_news.md) |
| `client.nba_v3_scores` | 27 | [map/operations/nba_v3_scores.md](map/operations/nba_v3_scores.md) |
| `client.nba_v3_stats` | 14 | [map/operations/nba_v3_stats.md](map/operations/nba_v3_stats.md) |
| `client.nfl_v3_headshots` | 1 | [map/operations/nfl_v3_headshots.md](map/operations/nfl_v3_headshots.md) |
| `client.nfl_v3_odds` | 34 | [map/operations/nfl_v3_odds.md](map/operations/nfl_v3_odds.md) |
| `client.nfl_v3_play_by_play` | 6 | [map/operations/nfl_v3_play_by_play.md](map/operations/nfl_v3_play_by_play.md) |
| `client.nfl_v3_projections` | 13 | [map/operations/nfl_v3_projections.md](map/operations/nfl_v3_projections.md) |
| `client.nfl_v3_roto_baller_premium_news` | 3 | [map/operations/nfl_v3_roto_baller_premium_news.md](map/operations/nfl_v3_roto_baller_premium_news.md) |
| `client.nfl_v3_scores` | 44 | [map/operations/nfl_v3_scores.md](map/operations/nfl_v3_scores.md) |
| `client.nfl_v3_stats` | 34 | [map/operations/nfl_v3_stats.md](map/operations/nfl_v3_stats.md) |
| `client.nhl_v3_headshots` | 1 | [map/operations/nhl_v3_headshots.md](map/operations/nhl_v3_headshots.md) |
| `client.nhl_v3_odds` | 34 | [map/operations/nhl_v3_odds.md](map/operations/nhl_v3_odds.md) |
| `client.nhl_v3_play_by_play` | 3 | [map/operations/nhl_v3_play_by_play.md](map/operations/nhl_v3_play_by_play.md) |
| `client.nhl_v3_projections` | 4 | [map/operations/nhl_v3_projections.md](map/operations/nhl_v3_projections.md) |
| `client.nhl_v3_roto_baller_premium_news` | 2 | [map/operations/nhl_v3_roto_baller_premium_news.md](map/operations/nhl_v3_roto_baller_premium_news.md) |
| `client.nhl_v3_scores` | 27 | [map/operations/nhl_v3_scores.md](map/operations/nhl_v3_scores.md) |
| `client.nhl_v3_stats` | 14 | [map/operations/nhl_v3_stats.md](map/operations/nhl_v3_stats.md) |
| `client.soccer_v4_headshots` | 1 | [map/operations/soccer_v4_headshots.md](map/operations/soccer_v4_headshots.md) |
| `client.soccer_v4_odds` | 28 | [map/operations/soccer_v4_odds.md](map/operations/soccer_v4_odds.md) |
| `client.soccer_v4_projections` | 4 | [map/operations/soccer_v4_projections.md](map/operations/soccer_v4_projections.md) |
| `client.soccer_v4_scores` | 21 | [map/operations/soccer_v4_scores.md](map/operations/soccer_v4_scores.md) |
| `client.soccer_v4_stats` | 11 | [map/operations/soccer_v4_stats.md](map/operations/soccer_v4_stats.md) |
| `client.wnba_v3_scores` | 40 | [map/operations/wnba_v3_scores.md](map/operations/wnba_v3_scores.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `sports_data_io/models/` declares one type plus its input companion, and every module under `sports_data_io/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`Area` ↔ `area.py`; an error alias drops its `Body` suffix: `CbbV3OddsAlternateMarketPreGameOddsByDateErrorBody` ↔ `cbb_v3_odds_alternate_market_pre_game_odds_by_date_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 406 | `sports_data_io/models/` |
| Enums (`Enum` over `str`) — Python member names + wire values | 5 | `sports_data_io/models/enums/` |
| Error aliases (one per Case A operation) | 741 | `sports_data_io/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`area_id` ↔ `"AreaId"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model and enum also has an **input companion**, exported beside it from the same package (`Area` ↔ `AreaDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`Format` ↔ `FormatOrStr`) and additionally accepts a wire value this SDK version does not know.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `sports_data_io` |
| Operation controllers | `sports_data_io.apis` |
| Models | `sports_data_io.models` |
| Enums | `sports_data_io.models.enums` |
| Error aliases | `sports_data_io.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `sports_data_io.core` |

---

## Servers & auth

**API key (header `Ocp-Apim-Subscription-Key`).** Pass `api_key_header="<api_key>"`; sent as the `Ocp-Apim-Subscription-Key` request header.

**API key (query `key`).** Pass `api_key_query="<api_key>"`; sent as the `key` query parameter.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**One environment, one server** (`sports_data_io/server/server_config.py`). The spec declares a single environment, so no `environment` keyword exists; the base URL and its override point:

| Base URL | Override point |
| --- | --- |
| `https://api.sportsdata.io` | `base_url="https://…"` |

