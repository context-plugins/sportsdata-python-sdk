from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3NewsRotoballerPremiumNewsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3NewsRotoballerPremiumNewsByDateError:
    def map(self, response: HttpResponse) -> GolfV3NewsRotoballerPremiumNewsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v3_news_rotoballer_premium_news_by_date_error_mapper: Final[
    ErrorMapper[GolfV3NewsRotoballerPremiumNewsByDateErrorBody]
] = _GolfV3NewsRotoballerPremiumNewsByDateError()
