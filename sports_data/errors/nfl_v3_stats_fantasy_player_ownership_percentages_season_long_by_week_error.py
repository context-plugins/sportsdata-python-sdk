from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekError:
    def map(self, response: HttpResponse) -> NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_stats_fantasy_player_ownership_percentages_season_long_by_week_error_mapper: Final[
    ErrorMapper[NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekErrorBody]
] = _NflV3StatsFantasyPlayerOwnershipPercentagesSeasonLongByWeekError()
