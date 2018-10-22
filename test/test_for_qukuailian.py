# encoding=utf-8
import hashlib
from datetime import datetime
#定义区块类
class Block(object):

    def __init__(self, index, time, data, pre_hash):
        self.index = index
        self.time = time
        self.data = data
        self.pre_hash = pre_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update("{}{}{}{}".format(self.index, self.time, self.data, self.pre_hash))
        return sha.hexdigest()

#创建初始区块
def head_block_create():
    return Block(0, datetime.now(), "Head Block", "0")

#创建新的区块
def new_block(last_block):
    _index = last_block.index + 1
    _time = datetime.now()
    _data = "block{}".format(_index)
    _hash = last_block.hash
    return Block(_index, _time, _data, _hash)


if __name__ == '__main__':
    blockchain = [head_block_create()]
    pre_block = blockchain[0]
    print "Block id:0 Hash value:{}".format(blockchain[0].hash)
    #待测新增区块的数量
    num_block = 10
    for i in range(num_block):
        one_block = new_block(pre_block)
        blockchain.append(one_block)
        pre_block = one_block
        print "Block id:{} Hash value:{}".format(one_block.index, one_block.hash)
