from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3StatsTeamHittingVsStartingPitcherErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3StatsTeamHittingVsStartingPitcherError:
    def map(self, status_code: int, content: bytes) -> MlbV3StatsTeamHittingVsStartingPitcherErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


mlb_v3_stats_team_hitting_vs_starting_pitcher_error_mapper: Final[
    ErrorMapper[MlbV3StatsTeamHittingVsStartingPitcherErrorBody]
] = _MlbV3StatsTeamHittingVsStartingPitcherError()
