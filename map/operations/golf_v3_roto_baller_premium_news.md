<!-- Generated file — do not edit; regenerated with the SDK. -->

# GolfV3RotoBallerPremiumNews — operations

Accessor: `client.golf_v3_roto_baller_premium_news` · Source: `sports_data/apis/golf_v3_roto_baller_premium_news.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.golf_v3_roto_baller_premium_news.golf_v3_news_rotoballer_premium_news

- **Route**: `GET /v3/golf/news-rotoballer/{format}/RotoBallerPremiumNews`
- **Signature**: `def golf_v3_news_rotoballer_premium_news(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[News]`
- **Returns (raw)**: `ApiResult[list[News], GolfV3NewsRotoballerPremiumNewsErrorBody]`
- **Error**: `GolfV3NewsRotoballerPremiumNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News` | `sports_data/models/news.py` |
| `GolfV3NewsRotoballerPremiumNewsErrorBody` | `sports_data/errors/golf_v3_news_rotoballer_premium_news_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

### client.golf_v3_roto_baller_premium_news.golf_v3_news_rotoballer_premium_news_by_date

- **Route**: `GET /v3/golf/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}`
- **Signature**: `def golf_v3_news_rotoballer_premium_news_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[News]`
- **Returns (raw)**: `ApiResult[list[News], GolfV3NewsRotoballerPremiumNewsByDateErrorBody]`
- **Error**: `GolfV3NewsRotoballerPremiumNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data/models/enums/format.py` |
| `News` | `sports_data/models/news.py` |
| `GolfV3NewsRotoballerPremiumNewsByDateErrorBody` | `sports_data/errors/golf_v3_news_rotoballer_premium_news_by_date_error.py` |
| `Unauthorized` | `sports_data/models/unauthorized.py` |

