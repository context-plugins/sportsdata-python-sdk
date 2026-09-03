from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2CoursesCoursesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2CoursesCoursesError:
    def map(self, response: HttpResponse) -> GolfV2CoursesCoursesErrorBody:
        match response.status_code:
            case 401:
                return decode_json[Unauthorized](response)
            case _:
                return RawError(response)


golf_v2_courses_courses_error_mapper: Final[ErrorMapper[GolfV2CoursesCoursesErrorBody]] = _GolfV2CoursesCoursesError()
