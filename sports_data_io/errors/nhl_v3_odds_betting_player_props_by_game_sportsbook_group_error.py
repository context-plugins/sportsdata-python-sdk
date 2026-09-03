from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3OddsBettingPlayerPropsByGameSportsbookGroupError:
    def map(self, response: HttpResponse) -> NhlV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper: Final[
    ErrorMapper[NhlV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]
] = _NhlV3OddsBettingPlayerPropsByGameSportsbookGroupError()
