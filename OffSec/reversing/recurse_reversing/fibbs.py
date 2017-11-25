from pwn import *
context.log_level = "DEBUG"

r = remote('offsec-chalbroker.osiris.cyber.nyu.edu',1249)

def fibbs(a,b):
    c = a+b
    for i in range(16):
        a = b
        b = c
        c = a+b
    return 116369 == c


def solver():
    for i in range(100):
        for j in range(100):
            if fibbs(i,j):
                return str(i) + " " + str(j)

def main():
    r.sendline("svv232");
    r.recvline()
    r.sendline(solver())
    r.recvline()

main()
