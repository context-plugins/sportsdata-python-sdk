from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalError:
    def map(
        self, status_code: int, content: bytes
    ) -> GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v2_playertournamentholescores_player_hole_scores_by_tournament_live_final_error_mapper: Final[
    ErrorMapper[GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalErrorBody]
] = _GolfV2PlayertournamentholescoresPlayerHoleScoresByTournamentLiveFinalError()
