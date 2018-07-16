#99乘法表
def list(n1=10,n2=10):
   for n1 in range(1,10):
    for n2 in range(1,10):
        print(n1,"*",n2,"=",n1*n2)
list()


#四則運算
def op(n1,n2,op):
    if op=='+':
        print(int(n1+n2))
    elif op=='-':
        print(int(n1-n2))
    elif op=='*':
        print(int(n1*n2))
    elif op=='/':
        print(n1/n2)
    else :
        print("您輸入錯誤唷!")
op(3,4,"+")