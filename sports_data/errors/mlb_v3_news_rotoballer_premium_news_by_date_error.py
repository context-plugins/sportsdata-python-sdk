from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3NewsRotoballerPremiumNewsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3NewsRotoballerPremiumNewsByDateError:
    def map(self, response: HttpResponse) -> MlbV3NewsRotoballerPremiumNewsByDateErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_news_rotoballer_premium_news_by_date_error_mapper: Final[
    ErrorMapper[MlbV3NewsRotoballerPremiumNewsByDateErrorBody]
] = _MlbV3NewsRotoballerPremiumNewsByDateError()
