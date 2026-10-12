from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV3OddsRaceOddsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV3OddsRaceOddsError:
    def map(self, status_code: int, content: bytes) -> NascarV3OddsRaceOddsErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nascar_v3_odds_race_odds_error_mapper: Final[ErrorMapper[NascarV3OddsRaceOddsErrorBody]] = _NascarV3OddsRaceOddsError()
