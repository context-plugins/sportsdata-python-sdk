from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

MlbV3StatsBatterVsPitcherStatsErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _MlbV3StatsBatterVsPitcherStatsError:
    def map(self, response: HttpResponse) -> MlbV3StatsBatterVsPitcherStatsErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


mlb_v3_stats_batter_vs_pitcher_stats_error_mapper: Final[
    ErrorMapper[MlbV3StatsBatterVsPitcherStatsErrorBody]
] = _MlbV3StatsBatterVsPitcherStatsError()
