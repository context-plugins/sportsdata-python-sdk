from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV2DriverDriverProfilesByDriverErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV2DriverDriverProfilesByDriverError:
    def map(self, response: HttpResponse) -> NascarV2DriverDriverProfilesByDriverErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nascar_v2_driver_driver_profiles_by_driver_error_mapper: Final[
    ErrorMapper[NascarV2DriverDriverProfilesByDriverErrorBody]
] = _NascarV2DriverDriverProfilesByDriverError()
