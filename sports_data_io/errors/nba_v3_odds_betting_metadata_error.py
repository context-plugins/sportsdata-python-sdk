from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3OddsBettingMetadataErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3OddsBettingMetadataError:
    def map(self, response: HttpResponse) -> NbaV3OddsBettingMetadataErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_odds_betting_metadata_error_mapper: Final[
    ErrorMapper[NbaV3OddsBettingMetadataErrorBody]
] = _NbaV3OddsBettingMetadataError()
