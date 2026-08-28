from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ScoresScoresByWeekSimulationErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ScoresScoresByWeekSimulationError:
    def map(self, response: HttpResponse) -> NflV3ScoresScoresByWeekSimulationErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_scores_scores_by_week_simulation_error_mapper: Final[
    ErrorMapper[NflV3ScoresScoresByWeekSimulationErrorBody]
] = _NflV3ScoresScoresByWeekSimulationError()
