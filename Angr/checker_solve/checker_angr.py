from pwn import *
import angr
from binascii import b2a_uu

e = ELF("checker")

main = e.symbols['main']
give_flag = e.symbols['give_flag']
check = e.symbols['check']

def checker():
    proj = angr.Project("./checker")
    
    find = [
        0x8048713, #end of check
        give_flag
    ]

    avoid = [
        0x804879c, #bad switch case
    ]

    state = proj.factory.blank_state(addr=main)
    sm = proj.factory.simulation_manager(state)
    
    ex = sm.explore(find = find, avoid = avoid)
    
    final = ex.found[0]
    flag = final.posix.dumps(0)
    print(flag.rstrip('\x00'))
    

if __name__ == "__main__":
    checker()
