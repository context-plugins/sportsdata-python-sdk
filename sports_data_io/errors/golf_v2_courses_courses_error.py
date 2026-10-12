from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unauthorized import Unauthorized

GolfV2CoursesCoursesErrorBody: TypeAlias = Unauthorized | RawError


@dataclass(frozen=True, slots=True)
class _GolfV2CoursesCoursesError:
    def map(self, status_code: int, content: bytes) -> GolfV2CoursesCoursesErrorBody:
        match status_code:
            case 401:
                return decode_json[Unauthorized](content)
            case _:
                return RawError(status_code, content)


golf_v2_courses_courses_error_mapper: Final[ErrorMapper[GolfV2CoursesCoursesErrorBody]] = _GolfV2CoursesCoursesError()
