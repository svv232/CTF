from pwn import *
import angr
from struct import unpack

e = ELF("./numerix")

main = e.symbols['main']
print_flag = e.symbols['print_flag']


def numerix_smash(start = main, goal = 0x4008ed):
    proj = angr.Project("numerix")

    find = [
        goal,
    ]

    avoid = [
        0x4008d9,
        0x400c07,
        0x40098b,
    ]

    state = proj.factory.blank_state(addr = start)
    sm = proj.factory.simulation_manager(state)
    ex = sm.explore(find = find, avoid = avoid)

    final = ex.found[0]
    flag = final.posix.dumps(0)
    print(flag.rstrip('\x00'))

if __name__ == "__main__":
    
    args = [
        (main, 0x4008ed),
        (0x4008ed, 0x400924),
        (0x400924, 0x400967), 
        (0x400967, print_flag),
    ]

    for i in range(4):
        try:
            numerix_smash(*args[i])
        except:
            pass
