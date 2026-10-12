from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalError:
    def map(
        self, status_code: int, content: bytes
    ) -> GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v2_playertournamentroundscores_scores_by_tournament_live_final_error_mapper: Final[
    ErrorMapper[GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody]
] = _GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalError()
