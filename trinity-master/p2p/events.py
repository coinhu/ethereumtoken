from dataclasses import (
    dataclass,
)
from typing import (
    Tuple,
    Type,
)

from lahja import (
    BaseEvent,
    BaseRequestResponseEvent,
)

from p2p.abc import NodeAPI


class BaseDiscoveryServiceResponse(BaseEvent):
    pass


@dataclass
class PeerCandidatesResponse(BaseDiscoveryServiceResponse):

    candidates: Tuple[NodeAPI, ...]


@dataclass
class PeerCandidatesRequest(BaseRequestResponseEvent[PeerCandidatesResponse]):

    max_candidates: int

    @staticmethod
    def expected_response_type() -> Type[PeerCandidatesResponse]:
        return PeerCandidatesResponse


class RandomBootnodeRequest(BaseRequestResponseEvent[PeerCandidatesResponse]):

    @staticmethod
    def expected_response_type() -> Type[PeerCandidatesResponse]:
        return PeerCandidatesResponse
