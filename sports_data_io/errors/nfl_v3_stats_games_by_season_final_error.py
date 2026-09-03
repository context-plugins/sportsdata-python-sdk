from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3StatsGamesBySeasonFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3StatsGamesBySeasonFinalError:
    def map(self, response: HttpResponse) -> NflV3StatsGamesBySeasonFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_stats_games_by_season_final_error_mapper: Final[
    ErrorMapper[NflV3StatsGamesBySeasonFinalErrorBody]
] = _NflV3StatsGamesBySeasonFinalError()
