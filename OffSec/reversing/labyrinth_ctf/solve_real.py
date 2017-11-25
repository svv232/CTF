from pwn import *
context.log_level = "DEBUG"

class Node:
    def __init__(self,left=None,right=None,data=None):
        self._left, self._right, self._data = left,right,data
    
Graph = {}

Graph['a'] = Node('c','g',0xe3)
Graph['b'] = Node('e','d',0x1f9)
Graph['c'] = Node('d','g',0x468)
Graph['d'] = Node('i','d',0x213)
Graph['e'] = Node('f','h',0x121)
Graph['f'] = Node('a','f',0x3a9)
Graph['g'] = Node('j','a',0x19a)
Graph['h'] = Node('a','j',0x13a)
Graph['i'] = Node('j','b',0x362)
Graph['j'] = Node('j','d',0x2c6)

magic_number = 9595

def traverse(node = 'a',total=0,path=""):
    current = total + Graph[node]._data
    if current <= magic_number:
        r,rsum = traverse(Graph[node]._right,current,path + 'R')
        l,lsum = traverse(Graph[node]._left,current,path + 'L')
        return (r,rsum) if rsum == magic_number else (l,lsum)
    return path,total

r = remote('offsec-chalbroker.osiris.cyber.nyu.edu',1253)
r.sendline('svv232')
r.recvline()
r.recvline()
r.sendline(traverse()[0])
r.recvline()
r.recvline()
