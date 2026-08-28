from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NbaV3OddsBettingPlayerPropsByGameErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NbaV3OddsBettingPlayerPropsByGameError:
    def map(self, response: HttpResponse) -> NbaV3OddsBettingPlayerPropsByGameErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nba_v3_odds_betting_player_props_by_game_error_mapper: Final[
    ErrorMapper[NbaV3OddsBettingPlayerPropsByGameErrorBody]
] = _NbaV3OddsBettingPlayerPropsByGameError()
