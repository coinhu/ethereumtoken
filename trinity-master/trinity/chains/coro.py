from typing import Type

from eth.abc import ChainDatabaseAPI
from eth.chains import Chain

from trinity._utils.async_dispatch import async_method
from trinity.db.eth1.chain import AsyncChainDB

from .base import AsyncChainAPI


class AsyncChainMixin(AsyncChainAPI):
    chaindb_class: Type[ChainDatabaseAPI] = AsyncChainDB

    coro_get_ancestors = async_method(Chain.get_ancestors)
    coro_get_block_by_hash = async_method(Chain.get_block_by_hash)
    coro_get_block_by_header = async_method(Chain.get_block_by_header)
    coro_get_block_header_by_hash = async_method(Chain.get_block_header_by_hash)
    coro_get_canonical_block_by_number = async_method(Chain.get_canonical_block_by_number)
    coro_get_canonical_head = async_method(Chain.get_canonical_head)
    coro_get_canonical_block_header_by_number = async_method(
        Chain.get_canonical_block_header_by_number
    )
    coro_get_canonical_transaction_index = async_method(Chain.get_canonical_transaction_index)
    coro_get_canonical_transaction = async_method(Chain.get_canonical_transaction)
    coro_get_canonical_transaction_by_index = async_method(Chain.get_canonical_transaction_by_index)
    coro_get_transaction_receipt = async_method(Chain.get_transaction_receipt)
    coro_get_transaction_receipt_by_index = async_method(Chain.get_transaction_receipt_by_index)
    coro_import_block = async_method(Chain.import_block)
    coro_validate_chain = async_method(Chain.validate_chain)
    coro_validate_receipt = async_method(Chain.validate_receipt)
