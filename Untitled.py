#!/usr/bin/env python
# coding: utf-8

# In[1]:


# version: '2020zfs'
# index: 0
# timestamp: date.datetime.now()
# data: say what you want to say
# target: 10**74


# 分叉问题：我和韩阳，谁先发布谁是最长串。不会产生分叉。
# 记账权的问题：在我和韩阳的聊天记录中发布，即会被认可，掌握记账权。
# 身份认证问题：韩阳就是hanyang，我就是zfs

# In[2]:


import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, version, index, timestamp, data, previous_hash, nonce, target):
        self.version = version
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = nonce
        self.target = target
        self.hash = self.hash_block()

    def __str__(self):
        return 'version: ' + str(self.version) + '\n' + 'index: '+str(self.index)+ '\n' + 'timestamp: ' + str(self.timestamp) + '\n' + 'data: '+ str(self.data)+ '\n' + 'previous_hash: '+ str(self.previous_hash)+ '\n' + 'nonce: ' + str(self.nonce) + '\n' + 'target: ' + str(self.target) + '\n' + 'hash: ' + str(self.hash)
        
    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)+ str(self.nonce)).encode("utf8"))
        return sha.hexdigest()

## function
def create_genesis_block():
    return Block('2020zfs',0, date.datetime.now(),"Genesis Block","0" ,1, 10**74)

def find_block(version, index, timestamp, data, previous_hash, nonce, target):
    sha = hasher.sha256()
    sha.update((str(index) + str(timestamp) + str(data) + str(previous_hash)+ str(nonce)).encode("utf8"))
    return int(sha.hexdigest(),16)<target

def next_block(version, index, timestamp, data, previous_hash, nonce, target):
    return Block(this_index,this_timestamp,this_data,this_hash)


# In[3]:


blockchain=[create_genesis_block()]
print(blockchain[0],end='\n')
num_of_blocks_to_add=1

# version: 2020zfs
# index: 0
# timestamp: 2020-11-14 11:18:45.121418
# data: Genesis Block
# previous_hash: 0
# nonce: 1
# target: 100000000000000000000000000000000000000000000000000000000000000000000000000
# hash: fe715d25a6ef82c9f8c18cb35d925801be5e2f0dd25fe388fd82e20ab4a24a5e


# In[6]:


# for i in range(0,num_of_blocks_to_add):
previous_block=blockchain[-1]

version = previous_block.version
index = previous_block.index + 1
timestamp = date.datetime.now()
data = 'hanyang has 50 coins'
target = previous_block.target
previous_hash = previous_block.hash

for i in range(10000):
    nonce = i
    if find_block(version, index, timestamp, data, previous_hash, nonce, target):
        block_to_add = Block(version, index, timestamp, data, previous_hash, nonce, target)
        blockchain.append(block_to_add)
        print(blockchain[-1])
        break


# In[7]:


# for i in range(0,num_of_blocks_to_add):
previous_block=blockchain[-1]

version = previous_block.version
index = previous_block.index + 1
timestamp = date.datetime.now()
data = 'zfs has 50 coins'
target = previous_block.target
previous_hash = previous_block.hash

for i in range(10000):
    nonce = i
    if find_block(version, index, timestamp, data, previous_hash, nonce, target):
        block_to_add = Block(version, index, timestamp, data, previous_hash, nonce, target)
        blockchain.append(block_to_add)
        print(blockchain[-1])
        break

