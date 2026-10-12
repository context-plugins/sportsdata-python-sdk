from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekError:
    def map(
        self, status_code: int, content: bytes
    ) -> NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week_error_mapper: Final[
    ErrorMapper[NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody]
] = _NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekError()
