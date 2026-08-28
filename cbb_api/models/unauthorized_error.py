from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UnauthorizedError(SdkBaseModel):
    http_status_code: Optional[int] = Field(default=UNSET, alias="HttpStatusCode")
    code: Optional[int] = Field(default=UNSET, alias="Code")
    description: Optional[str] = Field(default=UNSET, alias="Description")
    help: Optional[str] = Field(default=UNSET, alias="Help")


class UnauthorizedErrorDict(TypedDict):
    http_status_code: NotRequired[int]
    code: NotRequired[int]
    description: NotRequired[str]
    help: NotRequired[str]
