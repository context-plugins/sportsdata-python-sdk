from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3NewsRotoballerPremiumNewsByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3NewsRotoballerPremiumNewsByTeamError:
    def map(self, response: HttpResponse) -> NflV3NewsRotoballerPremiumNewsByTeamErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_news_rotoballer_premium_news_by_team_error_mapper: Final[
    ErrorMapper[NflV3NewsRotoballerPremiumNewsByTeamErrorBody]
] = _NflV3NewsRotoballerPremiumNewsByTeamError()
