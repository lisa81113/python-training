#作業1：四則運算式
print("======作業1：四則運算式======")
n1=int(input("Enter a Number1："))
n2=int(input("Enter a Number2："))
op=input("請擇一運算符號輸入:+,-,*,/：")

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


#作業2：算整數平方根
print("======作業2：算整數平方根======")
n=int(input("請輸入一個正整數："))
for a in range(int(n)):
    a=a+1
    if n==a*a:
        print('該數值平方根為：',a)
        break
else :
    print('沒有整數的平方根!')

#作業3：99乘法表
print("======作業3：99乘法表======")
for x in range(1,10):
    for y in range(1,10):
        print(x,"*",y,"=",x*y)
