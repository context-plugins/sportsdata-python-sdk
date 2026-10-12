from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.cbb_v3_odds import AsyncCbbV3Odds
from .apis.cbb_v3_scores import AsyncCbbV3Scores
from .apis.cbb_v3_stats import AsyncCbbV3Stats
from .apis.cfb_v3_odds import AsyncCfbV3Odds
from .apis.cfb_v3_scores import AsyncCfbV3Scores
from .apis.cfb_v3_stats import AsyncCfbV3Stats
from .apis.cwbb_v3_scores import AsyncCwbbV3Scores
from .apis.golf_v2 import AsyncGolfV2
from .apis.golf_v3_headshots import AsyncGolfV3Headshots
from .apis.golf_v3_odds import AsyncGolfV3Odds
from .apis.golf_v3_roto_baller_premium_news import AsyncGolfV3RotoBallerPremiumNews
from .apis.mlb_v3_headshots import AsyncMlbV3Headshots
from .apis.mlb_v3_odds import AsyncMlbV3Odds
from .apis.mlb_v3_play_by_play import AsyncMlbV3PlayByPlay
from .apis.mlb_v3_projections import AsyncMlbV3Projections
from .apis.mlb_v3_roto_baller_premium_news import AsyncMlbV3RotoBallerPremiumNews
from .apis.mlb_v3_scores import AsyncMlbV3Scores
from .apis.mlb_v3_stats import AsyncMlbV3Stats
from .apis.mma_v3_odds import AsyncMmaV3Odds
from .apis.mma_v3_scores import AsyncMmaV3Scores
from .apis.mma_v3_stats import AsyncMmaV3Stats
from .apis.nascar_v2 import AsyncNascarV2
from .apis.nascar_v3_odds import AsyncNascarV3Odds
from .apis.nba_v3_headshots import AsyncNbaV3Headshots
from .apis.nba_v3_odds import AsyncNbaV3Odds
from .apis.nba_v3_play_by_play import AsyncNbaV3PlayByPlay
from .apis.nba_v3_projections import AsyncNbaV3Projections
from .apis.nba_v3_roto_baller_premium_news import AsyncNbaV3RotoBallerPremiumNews
from .apis.nba_v3_scores import AsyncNbaV3Scores
from .apis.nba_v3_stats import AsyncNbaV3Stats
from .apis.nfl_v3_headshots import AsyncNflV3Headshots
from .apis.nfl_v3_odds import AsyncNflV3Odds
from .apis.nfl_v3_play_by_play import AsyncNflV3PlayByPlay
from .apis.nfl_v3_projections import AsyncNflV3Projections
from .apis.nfl_v3_roto_baller_premium_news import AsyncNflV3RotoBallerPremiumNews
from .apis.nfl_v3_scores import AsyncNflV3Scores
from .apis.nfl_v3_stats import AsyncNflV3Stats
from .apis.nhl_v3_headshots import AsyncNhlV3Headshots
from .apis.nhl_v3_odds import AsyncNhlV3Odds
from .apis.nhl_v3_play_by_play import AsyncNhlV3PlayByPlay
from .apis.nhl_v3_projections import AsyncNhlV3Projections
from .apis.nhl_v3_roto_baller_premium_news import AsyncNhlV3RotoBallerPremiumNews
from .apis.nhl_v3_scores import AsyncNhlV3Scores
from .apis.nhl_v3_stats import AsyncNhlV3Stats
from .apis.soccer_v4_headshots import AsyncSoccerV4Headshots
from .apis.soccer_v4_odds import AsyncSoccerV4Odds
from .apis.soccer_v4_projections import AsyncSoccerV4Projections
from .apis.soccer_v4_scores import AsyncSoccerV4Scores
from .apis.soccer_v4_stats import AsyncSoccerV4Stats
from .apis.wnba_v3_scores import AsyncWnbaV3Scores
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseSportsDataIoClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    ApiKeyQueryScheme,
    AsyncHttpClient,
    AsyncHttpx2Client,
    AsyncRawClient,
    RetryOptionsOrDict,
    no_auth,
    param,
)


class AsyncSportsDataIoClient(BaseSportsDataIoClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
        api_key_header: str | None = None,
        api_key_query: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout, retry_options=retry_options)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpx2Client(timeout=timeout)
            ),
            retry_options=self._retry_options,
            global_headers=[
                param[str]("User-Agent", "SportsDataIoClient/1.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
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

    @cached_property
    def cfb_v3_odds(self) -> AsyncCfbV3Odds:
        return AsyncCfbV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def cfb_v3_scores(self) -> AsyncCfbV3Scores:
        return AsyncCfbV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def cfb_v3_stats(self) -> AsyncCfbV3Stats:
        return AsyncCfbV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def cwbb_v3_scores(self) -> AsyncCwbbV3Scores:
        return AsyncCwbbV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def golf_v2(self) -> AsyncGolfV2:
        return AsyncGolfV2(self._raw_client, self._server, self._auth)

    @cached_property
    def golf_v3_headshots(self) -> AsyncGolfV3Headshots:
        return AsyncGolfV3Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def golf_v3_odds(self) -> AsyncGolfV3Odds:
        return AsyncGolfV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def golf_v3_roto_baller_premium_news(self) -> AsyncGolfV3RotoBallerPremiumNews:
        return AsyncGolfV3RotoBallerPremiumNews(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_headshots(self) -> AsyncMlbV3Headshots:
        return AsyncMlbV3Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_odds(self) -> AsyncMlbV3Odds:
        return AsyncMlbV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_play_by_play(self) -> AsyncMlbV3PlayByPlay:
        return AsyncMlbV3PlayByPlay(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_projections(self) -> AsyncMlbV3Projections:
        return AsyncMlbV3Projections(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_roto_baller_premium_news(self) -> AsyncMlbV3RotoBallerPremiumNews:
        return AsyncMlbV3RotoBallerPremiumNews(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_scores(self) -> AsyncMlbV3Scores:
        return AsyncMlbV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_stats(self) -> AsyncMlbV3Stats:
        return AsyncMlbV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def mma_v3_odds(self) -> AsyncMmaV3Odds:
        return AsyncMmaV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def mma_v3_scores(self) -> AsyncMmaV3Scores:
        return AsyncMmaV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def mma_v3_stats(self) -> AsyncMmaV3Stats:
        return AsyncMmaV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def nascar_v2(self) -> AsyncNascarV2:
        return AsyncNascarV2(self._raw_client, self._server, self._auth)

    @cached_property
    def nascar_v3_odds(self) -> AsyncNascarV3Odds:
        return AsyncNascarV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_headshots(self) -> AsyncNbaV3Headshots:
        return AsyncNbaV3Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_odds(self) -> AsyncNbaV3Odds:
        return AsyncNbaV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_play_by_play(self) -> AsyncNbaV3PlayByPlay:
        return AsyncNbaV3PlayByPlay(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_projections(self) -> AsyncNbaV3Projections:
        return AsyncNbaV3Projections(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_roto_baller_premium_news(self) -> AsyncNbaV3RotoBallerPremiumNews:
        return AsyncNbaV3RotoBallerPremiumNews(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_scores(self) -> AsyncNbaV3Scores:
        return AsyncNbaV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_stats(self) -> AsyncNbaV3Stats:
        return AsyncNbaV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_headshots(self) -> AsyncNflV3Headshots:
        return AsyncNflV3Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_odds(self) -> AsyncNflV3Odds:
        return AsyncNflV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_play_by_play(self) -> AsyncNflV3PlayByPlay:
        return AsyncNflV3PlayByPlay(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_projections(self) -> AsyncNflV3Projections:
        return AsyncNflV3Projections(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_roto_baller_premium_news(self) -> AsyncNflV3RotoBallerPremiumNews:
        return AsyncNflV3RotoBallerPremiumNews(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_scores(self) -> AsyncNflV3Scores:
        return AsyncNflV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_stats(self) -> AsyncNflV3Stats:
        return AsyncNflV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_headshots(self) -> AsyncNhlV3Headshots:
        return AsyncNhlV3Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_odds(self) -> AsyncNhlV3Odds:
        return AsyncNhlV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_play_by_play(self) -> AsyncNhlV3PlayByPlay:
        return AsyncNhlV3PlayByPlay(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_projections(self) -> AsyncNhlV3Projections:
        return AsyncNhlV3Projections(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_roto_baller_premium_news(self) -> AsyncNhlV3RotoBallerPremiumNews:
        return AsyncNhlV3RotoBallerPremiumNews(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_scores(self) -> AsyncNhlV3Scores:
        return AsyncNhlV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_stats(self) -> AsyncNhlV3Stats:
        return AsyncNhlV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def soccer_v4_headshots(self) -> AsyncSoccerV4Headshots:
        return AsyncSoccerV4Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def soccer_v4_odds(self) -> AsyncSoccerV4Odds:
        return AsyncSoccerV4Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def soccer_v4_projections(self) -> AsyncSoccerV4Projections:
        return AsyncSoccerV4Projections(self._raw_client, self._server, self._auth)

    @cached_property
    def soccer_v4_scores(self) -> AsyncSoccerV4Scores:
        return AsyncSoccerV4Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def soccer_v4_stats(self) -> AsyncSoccerV4Stats:
        return AsyncSoccerV4Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def wnba_v3_scores(self) -> AsyncWnbaV3Scores:
        return AsyncWnbaV3Scores(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncSportsDataIoClient
