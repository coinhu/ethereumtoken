from abc import abstractmethod
from typing import Tuple

from eth_typing import BlockNumber, Hash32

from eth.abc import (
    BlockAPI,
    ChainAPI,
    BlockHeaderAPI,
    ReceiptAPI,
    SignedTransactionAPI,
)


# This class is a work in progress; its main purpose is to define the API of an asyncio-compatible
# Chain implementation.
class AsyncChainAPI(ChainAPI):
    @abstractmethod
    async def coro_import_block(self,
                                block: BlockHeaderAPI,
                                perform_validation: bool = True,
                                ) -> Tuple[BlockAPI, Tuple[BlockAPI, ...], Tuple[BlockAPI, ...]]:
        ...

    @abstractmethod
    async def coro_validate_chain(
            self,
            parent: BlockHeaderAPI,
            chain: Tuple[BlockHeaderAPI, ...],
            seal_check_random_sample_rate: int = 1) -> None:
        ...

    @abstractmethod
    async def coro_validate_receipt(self,
                                    receipt: ReceiptAPI,
                                    at_header: BlockHeaderAPI) -> None:
        ...

    @abstractmethod
    async def coro_get_ancestors(self, limit: int, header: BlockHeaderAPI) -> Tuple[BlockAPI, ...]:
        ...

    @abstractmethod
    async def coro_get_block_by_hash(self,
                                     block_hash: Hash32) -> BlockAPI:
        ...

    @abstractmethod
    async def coro_get_block_by_header(self,
                                       header: BlockHeaderAPI) -> BlockAPI:
        ...

    @abstractmethod
    async def coro_get_block_header_by_hash(self, block_hash: Hash32) -> BlockHeaderAPI:
        ...

    @abstractmethod
    async def coro_get_canonical_block_by_number(self,
                                                 block_number: BlockNumber) -> BlockAPI:
        ...

    @abstractmethod
    async def coro_get_canonical_head(self) -> BlockHeaderAPI:
        ...

    @abstractmethod
    async def coro_get_canonical_block_header_by_number(
            self,
            block_number: BlockNumber) -> BlockHeaderAPI:
        ...

    @abstractmethod
    async def coro_get_canonical_transaction_index(
            self,
            transaction_hash: Hash32) -> Tuple[BlockNumber, int]:
        ...

    @abstractmethod
    async def coro_get_canonical_transaction(self,
                                             transaction_hash: Hash32) -> SignedTransactionAPI:
        ...

    @abstractmethod
    async def coro_get_canonical_transaction_by_index(
            self,
            block_number: BlockNumber,
            index: int) -> SignedTransactionAPI:
        ...

    @abstractmethod
    async def coro_get_transaction_receipt(self, transaction_hash: Hash32) -> ReceiptAPI:
        ...

    @abstractmethod
    async def coro_get_transaction_receipt_by_index(self,
                                                    block_number: BlockNumber,
                                                    index: int) -> ReceiptAPI:
        ...
