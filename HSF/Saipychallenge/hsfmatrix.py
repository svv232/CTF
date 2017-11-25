import itertools
import operator

def get_nums(n):
    nums = [1003743029632021475054785701632993352910831886148576467954531360117818347389,
    1477134929459533177408445750577886266346773423039665589711234610192826751773,
    1529844325207399430703055056106613335406599034453232660337748296761783699013,
    1464201100094878403593181244147905338741412374963703679650470582110217016993,
    1698577018739898181381710607774133693555362166938752343027068031503907298837,
    204452034550701700896591797901001229264169037855943032823555994466328271689,
    1348061227068297354580336610751811894886573502374152776822693313583804360857,
    1640447383859648731354733208856214809899082172302060649487472131149843094197,
    1034610819274482257381853466037279717672856447414311501596397634284691172097,
    1366311494551162483027542583769516928255225569186547990671378784607187917081,
    1123331076771048395927467886981459432782440745196992419051302424585299723851]
    return nums[hash(


def get_flag():
    x = input("Please give me the password:  ");
    if len(x) == 0:
        return "NOOOOOOOOOOOOO"
        quit()
    return x

def matrixify(string):
    primes = get_primes(len(string)*9)
    ordify = lambda x: (ord(x), primes[len(primes)-2])
    row = zip(*[x for x in map(ordify,[i for i in string])])
    matrix = list(row) * len(string)
    return matrix    

def super_cool_matrix_operations(matrix):
    matrix.reverse()
    transpose = zip(*matrix)
    compressed = set(matrix)
    print(compressed);
    special_sum = lambda x: operator.mul(*(map(sum,x))) #operator.mul takes 2 arguments
    x = special_sum(compressed)
    print(x)
    return(x)

def NOOOOOO():
    print("N00000000000000000")
    print("HAHAHAHAHA")
    return 

def YEEEEEEEE():
    print("YEEE DIGGITY YOU GOT THE PASSWORD!!!")

    print("ENTER THE PASSWORD IN FLAG FORMAT!!!!!")
    print("EX: flag{PASSWORD}")
    return 

def main():
    flag = get_flag()
    matrix = matrixify(flag)
    print(super_cool_matrix_operations(matrix))
    print("".join(sorted(list(flag)))) 
    if super_cool_matrix_operations(matrix) == 34968 and "".join(sorted(list(flag))) == flag and len(flag) == 4 and len(set(flag)) == 4:
        return YEEEEEEEE()
    else:
        return NOOOOOO()

if __name__ == '__main__':
    main()
