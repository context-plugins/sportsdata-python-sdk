from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3ProjectionsDepthChartsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3ProjectionsDepthChartsError:
    def map(self, response: HttpResponse) -> MlbV3ProjectionsDepthChartsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_projections_depth_charts_error_mapper: Final[
    ErrorMapper[MlbV3ProjectionsDepthChartsErrorBody]
] = _MlbV3ProjectionsDepthChartsError()
