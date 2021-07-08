# Made by Ross Nkama
from collections import deque
from datetime import datetime
from hashlib import sha256


class Blockchain:
    """Blockchain
    This is a generic multi-purpose blockchain.

    ...

    :var self.blockchain: The linked list containing blocks.
    """

    def __init__(self):
        self.blockchain = deque([])

    def create_block(self, data: object, prev_hash: str, nonce: int) -> None:
        """

        :param nonce: For proof of work.
        :param prev_hash: The hash of the previous block.
        :param data: The data that the new block will contain.
        :return: None
        """
        block = {
            'index': len(self.blockchain) + 1,
            'timestamp': datetime.now(),
            'data': data,
            'nonce': nonce,
            'prev_hash': prev_hash,
        }
        self.blockchain.append(block)
        return block
