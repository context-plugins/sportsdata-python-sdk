from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsFantasyDefenseSeasonStatsByTeamError:
    def map(self, status_code: int, content: bytes) -> NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_stats_fantasy_defense_season_stats_by_team_error_mapper: Final[
    ErrorMapper[NflV3StatsFantasyDefenseSeasonStatsByTeamErrorBody]
] = _NflV3StatsFantasyDefenseSeasonStatsByTeamError()
