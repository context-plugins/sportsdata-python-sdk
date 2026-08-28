from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentError:
    def map(
        self, response: HttpResponse
    ) -> GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v2_playertournamentprojectionstats_player_projected_stats_by_tournament_error_mapper: Final[
    ErrorMapper[GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentErrorBody]
] = _GolfV2PlayertournamentprojectionstatsPlayerProjectedStatsByTournamentError()
