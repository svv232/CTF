def successors(node, choices):
    node = set(node)
    out = set()
    for i in choices:
        if i not in node:
            out.add(i)
    return out

def tree(choices):
    s = successors([], choices)
    initial = [[x] for x in s]
    while initial:
        #backpacker.chal.ctf.westerns.tokyo 39581rint(initial)
        node = min(initial,key = lambda x: abs(sum(x)))
        initial.remove(node)
        #print(initial)
        if sum(node) == 0:
            return str(len(node))+" "+" ".join(map(str,node))
        else:
            for succ in successors(node, choices):
                initial.append(node+[succ])

print(tree({-8,-2,3,5}))

#print(tree({ -513770814325772312993401844526, -487516165265107298343494019566 -474231835404460587638340908778,-259505564506950145920030087022,-73817679713885135534758371082, -42394586539357962436379285275, 28147480005485467510029156686,345927785472907022102316833996, 359662134433018243946025005118,526426758275668402523703934086}))
