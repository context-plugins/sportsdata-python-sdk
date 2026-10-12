from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

NflV3ScoresAreGamesInProgressErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NflV3ScoresAreGamesInProgressError:
    def map(self, status_code: int, content: bytes) -> NflV3ScoresAreGamesInProgressErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


nfl_v3_scores_are_games_in_progress_error_mapper: Final[
    ErrorMapper[NflV3ScoresAreGamesInProgressErrorBody]
] = _NflV3ScoresAreGamesInProgressError()
