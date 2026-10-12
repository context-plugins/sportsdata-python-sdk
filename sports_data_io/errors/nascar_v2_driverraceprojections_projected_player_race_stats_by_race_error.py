from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceError:
    def map(
        self, status_code: int, content: bytes
    ) -> NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nascar_v2_driverraceprojections_projected_player_race_stats_by_race_error_mapper: Final[
    ErrorMapper[NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceErrorBody]
] = _NascarV2DriverraceprojectionsProjectedPlayerRaceStatsByRaceError()
