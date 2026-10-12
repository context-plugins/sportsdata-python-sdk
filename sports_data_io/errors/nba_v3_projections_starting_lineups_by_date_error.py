from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3ProjectionsStartingLineupsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3ProjectionsStartingLineupsByDateError:
    def map(self, status_code: int, content: bytes) -> NbaV3ProjectionsStartingLineupsByDateErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nba_v3_projections_starting_lineups_by_date_error_mapper: Final[
    ErrorMapper[NbaV3ProjectionsStartingLineupsByDateErrorBody]
] = _NbaV3ProjectionsStartingLineupsByDateError()
