from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

SoccerV4OddsBettingPlayerPropsByGameErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _SoccerV4OddsBettingPlayerPropsByGameError:
    def map(self, response: HttpResponse) -> SoccerV4OddsBettingPlayerPropsByGameErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


soccer_v4_odds_betting_player_props_by_game_error_mapper: Final[
    ErrorMapper[SoccerV4OddsBettingPlayerPropsByGameErrorBody]
] = _SoccerV4OddsBettingPlayerPropsByGameError()
