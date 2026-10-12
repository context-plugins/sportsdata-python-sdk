from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3OddsBettingPlayerPropsByGameErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3OddsBettingPlayerPropsByGameError:
    def map(self, status_code: int, content: bytes) -> CfbV3OddsBettingPlayerPropsByGameErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cfb_v3_odds_betting_player_props_by_game_error_mapper: Final[
    ErrorMapper[CfbV3OddsBettingPlayerPropsByGameErrorBody]
] = _CfbV3OddsBettingPlayerPropsByGameError()
