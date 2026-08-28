from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.cbb_v3_odds import CbbV3Odds
from .apis.cbb_v3_scores import CbbV3Scores
from .apis.cbb_v3_stats import CbbV3Stats
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseCbbApiClient
from .core import ApiKeyHeaderScheme, ApiKeyQueryScheme, HttpClient, HttpxClient, RawClient, no_auth


class CbbApiClient(BaseCbbApiClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout)
        )
        self._auth = AuthSchemes(
            api_key_header=(
                ApiKeyHeaderScheme("Ocp-Apim-Subscription-Key", api_key_header)
                if api_key_header is not None
                else no_auth
            ),
            api_key_query=ApiKeyQueryScheme("key", api_key_query) if api_key_query is not None else no_auth,
        )

    @cached_property
    def cbb_v3_odds(self) -> CbbV3Odds:
        return CbbV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def cbb_v3_scores(self) -> CbbV3Scores:
        return CbbV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def cbb_v3_stats(self) -> CbbV3Stats:
        return CbbV3Stats(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = CbbApiClient
