from pwn import *
import angr

e = ELF("RedVelvet")

main = e.symbols["main"]
exit = e.symbols["exit"]

funcs = {}
for i in range(1,16):
    symbol = "func" + str(i)
    funcs[symbol] = e.symbols[symbol]

def VelvetBash(start_addr = main, func = funcs["func3"]):
    proj = angr.Project("RedVelvet")
    
    find = [
        func,
    ]
    
    avoid = [
        exit,
    ]
    
    st = proj.factory.blank_state(addr=start_addr)
    
    for i in ["W","h","a","t","_","A"]:
        k = st.posix.files[0].read_from(1)
        st.solver.add(k == ord(i))
        
    sm = proj.factory.simulation_manager(st)
    ex = sm.explore(find=find, avoid=avoid)

    final = ex.found[0]
    flag = final.posix.dumps(0)
    print(flag.rstrip("\x00"))
    return flag

if __name__ == "__main__":
    VelvetBash(main, funcs['func5'])
