from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalError:
    def map(self, response: HttpResponse) -> GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v2_playertournamentroundscores_scores_by_tournament_live_final_error_mapper: Final[
    ErrorMapper[GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalErrorBody]
] = _GolfV2PlayertournamentroundscoresScoresByTournamentLiveFinalError()
