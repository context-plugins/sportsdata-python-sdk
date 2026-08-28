from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekError:
    def map(self, response: HttpResponse) -> NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nfl_v3_projections_idp_projected_player_game_stats_by_week_error_mapper: Final[
    ErrorMapper[NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekErrorBody]
] = _NflV3ProjectionsIdpProjectedPlayerGameStatsByWeekError()
