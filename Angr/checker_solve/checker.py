fom pwn import *

item = "aquaaaaaaaaaaaaaaauqa"
print(item)
print(len(item))
#p = process("./checker")
p = remote("recruit.isis.poly.edu",1234)
p.recvuntil(":")
#pause()
p.sendline(item)
print p.recvall()
