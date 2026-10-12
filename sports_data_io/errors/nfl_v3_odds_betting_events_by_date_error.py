from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3OddsBettingEventsByDateErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3OddsBettingEventsByDateError:
    def map(self, status_code: int, content: bytes) -> NflV3OddsBettingEventsByDateErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_odds_betting_events_by_date_error_mapper: Final[
    ErrorMapper[NflV3OddsBettingEventsByDateErrorBody]
] = _NflV3OddsBettingEventsByDateError()
