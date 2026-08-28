from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ScoresPlayerDetailsByRookieDraftYearError:
    def map(self, response: HttpResponse) -> NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_scores_player_details_by_rookie_draft_year_error_mapper: Final[
    ErrorMapper[NflV3ScoresPlayerDetailsByRookieDraftYearErrorBody]
] = _NflV3ScoresPlayerDetailsByRookieDraftYearError()
