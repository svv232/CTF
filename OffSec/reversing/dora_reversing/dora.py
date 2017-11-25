from pwn import *
context.log_level = "DEBUG"

success = []
for i in range(1,256):
    #r = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1250)
    r = process('./dora',raw=False)
    #r.sendline('svv232')
    r.sendline(str(i))
    l = r.recvline()
