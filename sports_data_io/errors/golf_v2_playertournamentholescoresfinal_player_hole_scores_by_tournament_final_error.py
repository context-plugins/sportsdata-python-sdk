from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalError:
    def map(
        self, response: HttpResponse
    ) -> GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v2_playertournamentholescoresfinal_player_hole_scores_by_tournament_final_error_mapper: Final[
    ErrorMapper[GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalErrorBody]
] = _GolfV2PlayertournamentholescoresfinalPlayerHoleScoresByTournamentFinalError()
