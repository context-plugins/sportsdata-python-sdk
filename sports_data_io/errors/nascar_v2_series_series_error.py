from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV2SeriesSeriesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV2SeriesSeriesError:
    def map(self, response: HttpResponse) -> NascarV2SeriesSeriesErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nascar_v2_series_series_error_mapper: Final[ErrorMapper[NascarV2SeriesSeriesErrorBody]] = _NascarV2SeriesSeriesError()
