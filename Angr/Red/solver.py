from pwn import *
import angr

e = ELF("RedVelvet")
main = e.symbols["main"]
exit = e.symbols["exit"]

def VelvetBash(start_addr, func):
    proj = angr.Project("RedVelvet")

    find = [func,]
    
    avoid = [exit,]
    
    st = proj.factory.blank_state(addr=start_addr)
    
    known =  ["W","h","a","t","_",]
    for i in known:
        k = st.posix.files[0].read_from(1)
        st.solver.add(k == ord(i))
        
    sm = proj.factory.simulation_manager(st)
    ex = sm.explore(find=find, avoid=avoid)
    final = ex.found[0]
    flag = final.posix.dumps(0)
    print(flag[len(known):].rstrip("\x00"))
    return flag

if __name__ == "__main__":
    VelvetBash(main, 0x401534)
