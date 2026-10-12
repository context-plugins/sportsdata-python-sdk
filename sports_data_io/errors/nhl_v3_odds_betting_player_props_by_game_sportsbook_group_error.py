from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3OddsBettingPlayerPropsByGameSportsbookGroupError:
    def map(self, status_code: int, content: bytes) -> NhlV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nhl_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper: Final[
    ErrorMapper[NhlV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]
] = _NhlV3OddsBettingPlayerPropsByGameSportsbookGroupError()
