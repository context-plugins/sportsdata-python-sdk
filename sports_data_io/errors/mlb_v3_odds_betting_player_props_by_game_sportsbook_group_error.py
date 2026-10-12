from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3OddsBettingPlayerPropsByGameSportsbookGroupError:
    def map(self, status_code: int, content: bytes) -> MlbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


mlb_v3_odds_betting_player_props_by_game_sportsbook_group_error_mapper: Final[
    ErrorMapper[MlbV3OddsBettingPlayerPropsByGameSportsbookGroupErrorBody]
] = _MlbV3OddsBettingPlayerPropsByGameSportsbookGroupError()
