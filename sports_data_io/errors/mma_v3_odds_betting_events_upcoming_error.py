from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

MmaV3OddsBettingEventsUpcomingErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MmaV3OddsBettingEventsUpcomingError:
    def map(self, status_code: int, content: bytes) -> MmaV3OddsBettingEventsUpcomingErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


mma_v3_odds_betting_events_upcoming_error_mapper: Final[
    ErrorMapper[MmaV3OddsBettingEventsUpcomingErrorBody]
] = _MmaV3OddsBettingEventsUpcomingError()
