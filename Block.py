import json
from txGenerator import generate_hash
from Transaction import Transaction
import random


class Block:
    def __init__(self, tx: Transaction, prev: str, node):
        self.tx = tx
        self.prev = prev
        self.nonce = self.generate_nonce(64)
        self.block_reward = 25
        self.node = node
        self.pow = self.generate_pow()
        try:
            self.generate_cbtx(node)
        except:
            print("genesis")

    @staticmethod
    def generate_nonce(length):
        """Generate pseudorandom number."""
        return ''.join([str(random.randint(0, 9)) for i in range(length)])

    def generate_pow(self):
        return generate_hash([str(self.tx).encode('utf-8'), self.prev.encode('utf-8'), self.nonce.encode('utf-8')])

    def hash(self):
        return self.pow

    def asTx(self):
        try:
            return json.dumps({'tx': {'number': self.tx.number, 'output': self.tx.output, 'input': self.tx.input, 'sig': self.tx.sig}, 'prev': self.prev, 'nonce': self.nonce, 'pow': self.pow, 'cb_tx': {'miner': self.node, 'tx_fee': self.tx.tx_fee, 'reward': self.block_reward}})
        except:
            return json.dumps({'tx': {'number': self.tx.number, 'output': self.tx.output, 'input': self.tx.input, 'sig': self.tx.sig}, 'prev': self.prev, 'nonce': self.nonce, 'pow': self.pow})
        # return json.dumps({'tx':{'number':self.tx.number, 'output':self.tx.output, 'input':self.tx.input, 'sig':self.tx.sig}})

    def asBlock(self):
        try:
            return json.dumps({'tx': {'number': self.tx.number, 'output': self.tx.output, 'input': self.tx.input, 'sig': self.tx.sig}, 'prev': self.prev, 'nonce': self.nonce, 'pow': self.pow, 'cb_tx': {'miner': self.node, 'tx_fee': self.tx.tx_fee, 'reward': self.block_reward}})
        except:
            return json.dumps({'tx': {'number': self.tx.number, 'output': self.tx.output, 'input': self.tx.input, 'sig': self.tx.sig}, 'prev': self.prev, 'nonce': self.nonce, 'pow': self.pow})
        # return json.dumps({'tx':{'number':self.tx.number, 'output':self.tx.output, 'input':self.tx.input, 'sig':self.tx.sig}})

    def generate_cbtx(self, node):
        print('\n' + node + '\nTransaction fee: ' + str(self.tx.tx_fee) +
              '\nBlock reward: ' + str(self.block_reward) + '\n')
