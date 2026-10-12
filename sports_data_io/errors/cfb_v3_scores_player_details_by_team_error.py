from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

CfbV3ScoresPlayerDetailsByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _CfbV3ScoresPlayerDetailsByTeamError:
    def map(self, status_code: int, content: bytes) -> CfbV3ScoresPlayerDetailsByTeamErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


cfb_v3_scores_player_details_by_team_error_mapper: Final[
    ErrorMapper[CfbV3ScoresPlayerDetailsByTeamErrorBody]
] = _CfbV3ScoresPlayerDetailsByTeamError()
