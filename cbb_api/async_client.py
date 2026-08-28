from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.cbb_v3_odds import AsyncCbbV3Odds
from .apis.cbb_v3_scores import AsyncCbbV3Scores
from .apis.cbb_v3_stats import AsyncCbbV3Stats
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseCbbApiClient
from .core import ApiKeyHeaderScheme, ApiKeyQueryScheme, AsyncHttpClient, AsyncHttpxClient, AsyncRawClient, no_auth


class AsyncCbbApiClient(BaseCbbApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
        )
        self._auth = AsyncAuthSchemes(
            api_key_header=(
                ApiKeyHeaderScheme("Ocp-Apim-Subscription-Key", api_key_header)
                if api_key_header is not None
                else no_auth
            ),
            api_key_query=ApiKeyQueryScheme("key", api_key_query) if api_key_query is not None else no_auth,
        )

    @cached_property
    def cbb_v3_odds(self) -> AsyncCbbV3Odds:
        return AsyncCbbV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def cbb_v3_scores(self) -> AsyncCbbV3Scores:
        return AsyncCbbV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def cbb_v3_stats(self) -> AsyncCbbV3Stats:
        return AsyncCbbV3Stats(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncCbbApiClient
