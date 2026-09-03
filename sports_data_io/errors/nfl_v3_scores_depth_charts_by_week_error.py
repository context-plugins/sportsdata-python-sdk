from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ScoresDepthChartsByWeekErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ScoresDepthChartsByWeekError:
    def map(self, response: HttpResponse) -> NflV3ScoresDepthChartsByWeekErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_scores_depth_charts_by_week_error_mapper: Final[
    ErrorMapper[NflV3ScoresDepthChartsByWeekErrorBody]
] = _NflV3ScoresDepthChartsByWeekError()
