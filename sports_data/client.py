from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.cbb_v3_odds import CbbV3Odds
from .apis.cbb_v3_scores import CbbV3Scores
from .apis.cbb_v3_stats import CbbV3Stats
from .apis.cfb_v3_odds import CfbV3Odds
from .apis.cfb_v3_scores import CfbV3Scores
from .apis.cfb_v3_stats import CfbV3Stats
from .apis.cwbb_v3_scores import CwbbV3Scores
from .apis.golf_v2 import GolfV2
from .apis.golf_v3_headshots import GolfV3Headshots
from .apis.golf_v3_odds import GolfV3Odds
from .apis.golf_v3_roto_baller_premium_news import GolfV3RotoBallerPremiumNews
from .apis.mlb_v3_headshots import MlbV3Headshots
from .apis.mlb_v3_odds import MlbV3Odds
from .apis.mlb_v3_play_by_play import MlbV3PlayByPlay
from .apis.mlb_v3_projections import MlbV3Projections
from .apis.mlb_v3_roto_baller_premium_news import MlbV3RotoBallerPremiumNews
from .apis.mlb_v3_scores import MlbV3Scores
from .apis.mlb_v3_stats import MlbV3Stats
from .apis.mma_v3_odds import MmaV3Odds
from .apis.mma_v3_scores import MmaV3Scores
from .apis.mma_v3_stats import MmaV3Stats
from .apis.nascar_v2 import NascarV2
from .apis.nascar_v3_odds import NascarV3Odds
from .apis.nba_v3_headshots import NbaV3Headshots
from .apis.nba_v3_odds import NbaV3Odds
from .apis.nba_v3_play_by_play import NbaV3PlayByPlay
from .apis.nba_v3_projections import NbaV3Projections
from .apis.nba_v3_roto_baller_premium_news import NbaV3RotoBallerPremiumNews
from .apis.nba_v3_scores import NbaV3Scores
from .apis.nba_v3_stats import NbaV3Stats
from .apis.nfl_v3_headshots import NflV3Headshots
from .apis.nfl_v3_odds import NflV3Odds
from .apis.nfl_v3_play_by_play import NflV3PlayByPlay
from .apis.nfl_v3_projections import NflV3Projections
from .apis.nfl_v3_roto_baller_premium_news import NflV3RotoBallerPremiumNews
from .apis.nfl_v3_scores import NflV3Scores
from .apis.nfl_v3_stats import NflV3Stats
from .apis.nhl_v3_headshots import NhlV3Headshots
from .apis.nhl_v3_odds import NhlV3Odds
from .apis.nhl_v3_play_by_play import NhlV3PlayByPlay
from .apis.nhl_v3_projections import NhlV3Projections
from .apis.nhl_v3_roto_baller_premium_news import NhlV3RotoBallerPremiumNews
from .apis.nhl_v3_scores import NhlV3Scores
from .apis.nhl_v3_stats import NhlV3Stats
from .apis.soccer_v4_headshots import SoccerV4Headshots
from .apis.soccer_v4_odds import SoccerV4Odds
from .apis.soccer_v4_projections import SoccerV4Projections
from .apis.soccer_v4_scores import SoccerV4Scores
from .apis.soccer_v4_stats import SoccerV4Stats
from .apis.wnba_v3_scores import WnbaV3Scores
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseSportsDataClient
from .core import ApiKeyHeaderScheme, ApiKeyQueryScheme, HttpClient, HttpxClient, RawClient, no_auth


class SportsDataClient(BaseSportsDataClient[RawClient]):
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

    @cached_property
    def cfb_v3_odds(self) -> CfbV3Odds:
        return CfbV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def cfb_v3_scores(self) -> CfbV3Scores:
        return CfbV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def cfb_v3_stats(self) -> CfbV3Stats:
        return CfbV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def cwbb_v3_scores(self) -> CwbbV3Scores:
        return CwbbV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def golf_v2(self) -> GolfV2:
        return GolfV2(self._raw_client, self._server, self._auth)

    @cached_property
    def golf_v3_headshots(self) -> GolfV3Headshots:
        return GolfV3Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def golf_v3_odds(self) -> GolfV3Odds:
        return GolfV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def golf_v3_roto_baller_premium_news(self) -> GolfV3RotoBallerPremiumNews:
        return GolfV3RotoBallerPremiumNews(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_headshots(self) -> MlbV3Headshots:
        return MlbV3Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_odds(self) -> MlbV3Odds:
        return MlbV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_play_by_play(self) -> MlbV3PlayByPlay:
        return MlbV3PlayByPlay(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_projections(self) -> MlbV3Projections:
        return MlbV3Projections(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_roto_baller_premium_news(self) -> MlbV3RotoBallerPremiumNews:
        return MlbV3RotoBallerPremiumNews(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_scores(self) -> MlbV3Scores:
        return MlbV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def mlb_v3_stats(self) -> MlbV3Stats:
        return MlbV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def mma_v3_odds(self) -> MmaV3Odds:
        return MmaV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def mma_v3_scores(self) -> MmaV3Scores:
        return MmaV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def mma_v3_stats(self) -> MmaV3Stats:
        return MmaV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def nascar_v2(self) -> NascarV2:
        return NascarV2(self._raw_client, self._server, self._auth)

    @cached_property
    def nascar_v3_odds(self) -> NascarV3Odds:
        return NascarV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_headshots(self) -> NbaV3Headshots:
        return NbaV3Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_odds(self) -> NbaV3Odds:
        return NbaV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_play_by_play(self) -> NbaV3PlayByPlay:
        return NbaV3PlayByPlay(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_projections(self) -> NbaV3Projections:
        return NbaV3Projections(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_roto_baller_premium_news(self) -> NbaV3RotoBallerPremiumNews:
        return NbaV3RotoBallerPremiumNews(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_scores(self) -> NbaV3Scores:
        return NbaV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def nba_v3_stats(self) -> NbaV3Stats:
        return NbaV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_headshots(self) -> NflV3Headshots:
        return NflV3Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_odds(self) -> NflV3Odds:
        return NflV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_play_by_play(self) -> NflV3PlayByPlay:
        return NflV3PlayByPlay(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_projections(self) -> NflV3Projections:
        return NflV3Projections(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_roto_baller_premium_news(self) -> NflV3RotoBallerPremiumNews:
        return NflV3RotoBallerPremiumNews(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_scores(self) -> NflV3Scores:
        return NflV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def nfl_v3_stats(self) -> NflV3Stats:
        return NflV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_headshots(self) -> NhlV3Headshots:
        return NhlV3Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_odds(self) -> NhlV3Odds:
        return NhlV3Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_play_by_play(self) -> NhlV3PlayByPlay:
        return NhlV3PlayByPlay(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_projections(self) -> NhlV3Projections:
        return NhlV3Projections(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_roto_baller_premium_news(self) -> NhlV3RotoBallerPremiumNews:
        return NhlV3RotoBallerPremiumNews(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_scores(self) -> NhlV3Scores:
        return NhlV3Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def nhl_v3_stats(self) -> NhlV3Stats:
        return NhlV3Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def soccer_v4_headshots(self) -> SoccerV4Headshots:
        return SoccerV4Headshots(self._raw_client, self._server, self._auth)

    @cached_property
    def soccer_v4_odds(self) -> SoccerV4Odds:
        return SoccerV4Odds(self._raw_client, self._server, self._auth)

    @cached_property
    def soccer_v4_projections(self) -> SoccerV4Projections:
        return SoccerV4Projections(self._raw_client, self._server, self._auth)

    @cached_property
    def soccer_v4_scores(self) -> SoccerV4Scores:
        return SoccerV4Scores(self._raw_client, self._server, self._auth)

    @cached_property
    def soccer_v4_stats(self) -> SoccerV4Stats:
        return SoccerV4Stats(self._raw_client, self._server, self._auth)

    @cached_property
    def wnba_v3_scores(self) -> WnbaV3Scores:
        return WnbaV3Scores(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = SportsDataClient
