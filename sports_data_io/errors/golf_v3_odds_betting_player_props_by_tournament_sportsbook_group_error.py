from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupError:
    def map(self, status_code: int, content: bytes) -> GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v3_odds_betting_player_props_by_tournament_sportsbook_group_error_mapper: Final[
    ErrorMapper[GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody]
] = _GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupError()
