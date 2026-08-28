from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsFantasyDefenseGameStatsByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsFantasyDefenseGameStatsByTeamError:
    def map(self, response: HttpResponse) -> NflV3StatsFantasyDefenseGameStatsByTeamErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_stats_fantasy_defense_game_stats_by_team_error_mapper: Final[
    ErrorMapper[NflV3StatsFantasyDefenseGameStatsByTeamErrorBody]
] = _NflV3StatsFantasyDefenseGameStatsByTeamError()
