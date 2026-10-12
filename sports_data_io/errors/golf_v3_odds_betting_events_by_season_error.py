from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3OddsBettingEventsBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3OddsBettingEventsBySeasonError:
    def map(self, status_code: int, content: bytes) -> GolfV3OddsBettingEventsBySeasonErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v3_odds_betting_events_by_season_error_mapper: Final[
    ErrorMapper[GolfV3OddsBettingEventsBySeasonErrorBody]
] = _GolfV3OddsBettingEventsBySeasonError()
