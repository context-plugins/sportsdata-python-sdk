from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3OddsBettingPlayerPropsByGameSportsbookGroupError:
    def map(self, response: HttpResponse) -> CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


cfb_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper: Final[
    ErrorMapper[CfbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]
] = _CfbV3OddsBettingPlayerPropsByGameSportsbookGroupError()
