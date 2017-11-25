from pwn import *
context.log_level = "DEBUG"

r = remote('offsec-chalbroker.osiris.cyber.nyu.edu',1236)
r.sendline("svv232")

for i in range(4):
    r.recvline() # eat interstitial

def sign(num1,sign,num2):

    D = {"ONE":'1',"TWO" :'2',"THREE":'3',"FOUR":'4',"FIVE":'5'
        ,"SIX":'6',"SEVEN":'7',"EIGHT":'8', "NINE":'9',"ZERO":'0'}

    if '0x' in num1:
        num1 = str(int(num1,16))
        print(num1)
    if '0x' in num2:
        num2 = str(int(num2,16))
        print(num2)
 
    if '0b' in num1:
        num1 = str(int(num1,2))
        print(num1)
    if '0b' in num2:
        num2 = str(int(num2,2))
        print(num2)
    
    if num1.split('-')[0] in D:
        num1 =  "".join(map(lambda x:D[x],num1.split('-')))
        print("poop1")
    
    if num2.split('-')[0] in D:
        num2 = "".join(map(lambda x:D[x],num2.split('-')))
        print("poop2")

    if sign == '+':
        return int(num1)+int(num2)
    
    elif sign == '-':
        return int(num1)-int(num2)
    elif sign == '*':
        return int(num1)* int(num2)
    else:
        return int(num1)/int(num2)

def mathsolver(math_array):
    return str(sign(math_array[0],math_array[1],math_array[2]))

while 1:
    line_array = r.recvline("=?\n").split(' ')
    print(line_array,"--------------------------")
    r.sendline(mathsolver(line_array))
    r.recvline()
