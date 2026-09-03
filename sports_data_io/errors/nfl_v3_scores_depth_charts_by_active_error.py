from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ScoresDepthChartsByActiveErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ScoresDepthChartsByActiveError:
    def map(self, response: HttpResponse) -> NflV3ScoresDepthChartsByActiveErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_scores_depth_charts_by_active_error_mapper: Final[
    ErrorMapper[NflV3ScoresDepthChartsByActiveErrorBody]
] = _NflV3ScoresDepthChartsByActiveError()
