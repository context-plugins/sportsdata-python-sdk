from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4OddsBettingEventsBySeasonErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4OddsBettingEventsBySeasonError:
    def map(self, status_code: int, content: bytes) -> SoccerV4OddsBettingEventsBySeasonErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


soccer_v4_odds_betting_events_by_season_error_mapper: Final[
    ErrorMapper[SoccerV4OddsBettingEventsBySeasonErrorBody]
] = _SoccerV4OddsBettingEventsBySeasonError()
