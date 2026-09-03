<!-- Generated file — do not edit; regenerated with the SDK. -->

# NflV3RotoBallerPremiumNews — operations

Accessor: `client.nfl_v3_roto_baller_premium_news` · Source: `sports_data_io/apis/nfl_v3_roto_baller_premium_news.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.nfl_v3_roto_baller_premium_news.nfl_v3_news_rotoballer_premium_news

- **Route**: `GET /v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNews`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_news_rotoballer_premium_news(format: FormatOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`
- **Params**: `format` — path
- **Returns (parsed)**: `list[News]`
- **Returns (raw)**: `ApiResult[list[News], NflV3NewsRotoballerPremiumNewsErrorBody]`
- **Error**: `NflV3NewsRotoballerPremiumNewsErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News` | `sports_data_io/models/news.py` |
| `NflV3NewsRotoballerPremiumNewsErrorBody` | `sports_data_io/errors/nfl_v3_news_rotoballer_premium_news_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_roto_baller_premium_news.nfl_v3_news_rotoballer_premium_news_by_date

- **Route**: `GET /v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{date}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_news_rotoballer_premium_news_by_date(format: FormatOrStr, date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `date`
- **Params**: `format` — path · `date` — path
- **Returns (parsed)**: `list[News]`
- **Returns (raw)**: `ApiResult[list[News], NflV3NewsRotoballerPremiumNewsByDateErrorBody]`
- **Error**: `NflV3NewsRotoballerPremiumNewsByDateErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News` | `sports_data_io/models/news.py` |
| `NflV3NewsRotoballerPremiumNewsByDateErrorBody` | `sports_data_io/errors/nfl_v3_news_rotoballer_premium_news_by_date_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

### client.nfl_v3_roto_baller_premium_news.nfl_v3_news_rotoballer_premium_news_by_team

- **Route**: `GET /v3/nfl/news-rotoballer/{format}/RotoBallerPremiumNewsByTeam/{team}`
- **Auth**: `api_key_header` OR `api_key_query`
- **Signature**: `def nfl_v3_news_rotoballer_premium_news_by_team(format: FormatOrStr, team: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `format`, `team`
- **Params**: `format` — path · `team` — path
- **Returns (parsed)**: `list[News]`
- **Returns (raw)**: `ApiResult[list[News], NflV3NewsRotoballerPremiumNewsByTeamErrorBody]`
- **Error**: `NflV3NewsRotoballerPremiumNewsByTeamErrorBody` — **Case A (typed)**
- **Error arms**: `Unauthorized` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `sports_data_io/models/enums/format.py` |
| `News` | `sports_data_io/models/news.py` |
| `NflV3NewsRotoballerPremiumNewsByTeamErrorBody` | `sports_data_io/errors/nfl_v3_news_rotoballer_premium_news_by_team_error.py` |
| `Unauthorized` | `sports_data_io/models/unauthorized.py` |

