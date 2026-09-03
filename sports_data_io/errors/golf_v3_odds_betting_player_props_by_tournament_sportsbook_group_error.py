from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupError:
    def map(self, response: HttpResponse) -> GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v3_odds_betting_player_props_by_tournament_sportsbook_group_error_mapper: Final[
    ErrorMapper[GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupErrorBody]
] = _GolfV3OddsBettingPlayerPropsByTournamentSportsbookGroupError()
