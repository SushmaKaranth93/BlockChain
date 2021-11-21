import hashlib
import json
from time import time
class BlockChain:
    def __init__(self):
        self.chain=[]
        self.pending_transaction = []
        self.new_block(previous_hash="Some message",proof=100)

    def new_block(self,proof,previous_hash=None):
        block={
            'index':len(self.chain)+1,
            'timestamp':time(),
            'transaction':self.pending_transaction,
            'proof':proof,
            'previous_hash':previous_hash or self.hash(self.chain[-1])
        }
        self.pending_transaction = []
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transactions(self,sender,recipient,amount):
        transaction={
            'sender':sender,
            'recipient':recipient,
            'amount':amount
        }
        self.pending_transaction.append(transaction)
        return self.last_block['index']+1

    def hash(self,block):
        string_object=json.dumps(block,sort_keys=True)
        block_string=string_object.encode()
        raw_hash=hashlib.sha256(block_string)
        hex_hash=raw_hash.hexdigest()
        return hex_hash

block_chain=BlockChain()
t1=block_chain.new_transactions("A","B",'5 BTC')
t2=block_chain.new_transactions("B","A","2 BTC")
t3=block_chain.new_transactions("A","C","5 BTC")
block_chain.new_block(12345)

t4 = block_chain.new_transactions("B", "D", '1 BTC')
t5 = block_chain.new_transactions("D", "E", '0.5 BTC')
t6 = block_chain.new_transactions("E", "A", '0.5 BTC')
block_chain.new_block(6789)

print("new",block_chain.chain)




