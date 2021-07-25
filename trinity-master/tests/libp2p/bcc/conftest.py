import asyncio
import time

import pytest

from eth2.beacon.state_machines.forks.serenity.blocks import SerenityBeaconBlock
from eth2.beacon.state_machines.forks.skeleton_lake.config import (
    MINIMAL_SERENITY_CONFIG,
)
from eth2.beacon.tools.builder.initializer import create_mock_genesis
from eth2.beacon.tools.builder.validator import mk_keymap_of_size
from eth2.beacon.typing import Timestamp
from trinity.protocol.bcc_libp2p import servers, utils
from trinity.tools.bcc_factories import NodeFactory

MOCK_TIME = 0.01
MOCK_PROCESS_ORPHAN_BLOCKS_PERIOD = 0.1


@pytest.fixture
def mock_process_orphan_blocks_period(monkeypatch):
    monkeypatch.setattr(
        servers, "PROCESS_ORPHAN_BLOCKS_PERIOD", MOCK_PROCESS_ORPHAN_BLOCKS_PERIOD
    )


@pytest.fixture
def mock_timeout(monkeypatch):
    monkeypatch.setattr(utils, "TTFB_TIMEOUT", MOCK_TIME)
    monkeypatch.setattr(utils, "RESP_TIMEOUT", MOCK_TIME * 2)


@pytest.fixture
def num_nodes():
    return 3


@pytest.fixture
async def nodes(num_nodes):
    async for _nodes in make_nodes(num_nodes, None):
        yield _nodes


async def make_nodes(num_nodes, chains=None):
    if chains is None:
        _nodes = NodeFactory.create_batch(num_nodes)
    else:
        assert num_nodes == len(chains)
        _nodes = tuple(NodeFactory(chain=chain) for chain in chains)
    for n in _nodes:
        asyncio.ensure_future(n.run())
        await n.events.started.wait()
    try:
        yield _nodes
    finally:
        for n in _nodes:
            await n.close()
            await n.cancel()


@pytest.fixture
def config():
    return MINIMAL_SERENITY_CONFIG


@pytest.fixture
def number_of_validators():
    return 8


@pytest.fixture
def genesis_state(number_of_validators, config):
    keymap = mk_keymap_of_size(number_of_validators)
    genesis_state, _ = create_mock_genesis(
        config=config,
        pubkeys=tuple(keymap.keys()),
        keymap=keymap,
        genesis_block_class=SerenityBeaconBlock,
        genesis_time=Timestamp(int(time.time())),
    )
    return genesis_state
