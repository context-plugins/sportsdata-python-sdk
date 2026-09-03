from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

NascarV2EntrylistbyraceEntryListByRaceErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _NascarV2EntrylistbyraceEntryListByRaceError:
    def map(self, response: HttpResponse) -> NascarV2EntrylistbyraceEntryListByRaceErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


nascar_v2_entrylistbyrace_entry_list_by_race_error_mapper: Final[
    ErrorMapper[NascarV2EntrylistbyraceEntryListByRaceErrorBody]
] = _NascarV2EntrylistbyraceEntryListByRaceError()
