from pwn import *
import angr

e = ELF("./larrycrypt")

encrypt = e.symbols['encrypt']
main = e.symbols['main']

def larrydecrypt():
    proj = angr.Project("./larrycrypt -R 4 -K 'V3c70R' -m '' ")

    find = [
        0x3e46,
    ]

    avoid = [
        0x3dbe,
    ]

    state = proj.factory.blank_state(addr=main)
    sm = proj.factory.simulation_manager(state)
    ex = sm.explore(find = find, avoid = avoid)

    final = ex.found[0]
    flag = final.posix.dumps(0)
    print(flag.rstrip("\x00"))
    return flag


if "__main__" == __name__:
    larrydecrypt()
