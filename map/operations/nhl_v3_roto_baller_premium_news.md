<!-- Generated file — do not edit; regenerated with the SDK. -->

# NhlV3RotoBallerPremiumNews — operations

Accessor: `client.nhl_v3_roto_baller_premium_news` · Source: `sports_data_io/apis/nhl_v3_roto_baller_premium_news.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nhl_v3_roto_baller_premium_news.nhl_v3_news_rotoballer_premium_news

- **Route**: `GET /v3/nhl/news-rotoballer/{format}/RotoBallerPremiumNews`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_news_rotoballer_premium_news(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], NhlV3NewsRotoballerPremiumNewsErrorBody]`
- **Error**: `NhlV3NewsRotoballerPremiumNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News1` | `sports_data_io/models/news1.py` |
| `NhlV3NewsRotoballerPremiumNewsErrorBody` | `sports_data_io/errors/nhl_v3_news_rotoballer_premium_news_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nhl_v3_roto_baller_premium_news.nhl_v3_news_rotoballer_premium_news_by_date

- **Route**: `GET /v3/nhl/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nhl_v3_news_rotoballer_premium_news_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[News1]`
- **Returns (raw)**: `ApiResult[list[News1], NhlV3NewsRotoballerPremiumNewsByDateErrorBody]`
- **Error**: `NhlV3NewsRotoballerPremiumNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News1` | `sports_data_io/models/news1.py` |
| `NhlV3NewsRotoballerPremiumNewsByDateErrorBody` | `sports_data_io/errors/nhl_v3_news_rotoballer_premium_news_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

