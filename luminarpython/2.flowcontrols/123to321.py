rem=0
res=0
num=int(input("enter a number"))
while(num!=0):
    rem=num%10#123%10=3,12%10=2,1%10=1
    res=(res*10)+rem#0*10+3=3,0+2=2,0+1
    num=num//10#123/10=12,12//10=1,1//10=0
print(res)#3 2 1