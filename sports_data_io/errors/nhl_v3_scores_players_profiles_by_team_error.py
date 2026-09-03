from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NhlV3ScoresPlayersProfilesByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NhlV3ScoresPlayersProfilesByTeamError:
    def map(self, response: HttpResponse) -> NhlV3ScoresPlayersProfilesByTeamErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nhl_v3_scores_players_profiles_by_team_error_mapper: Final[
    ErrorMapper[NhlV3ScoresPlayersProfilesByTeamErrorBody]
] = _NhlV3ScoresPlayersProfilesByTeamError()
