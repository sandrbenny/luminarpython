num=int(input("enter a number"))
a=0
res=0
temp=num
while(num!=0):
    a=num%10#123%10=3,12%10=2,1%10=1
    res=res+(a**3)#3*3*3=27,2*2*2=8,1*1*1=1
    num=num//10#123//10=12,12//10=1,1//10=0
print(res)
if(temp==res):
    print(res,"is amstrong")
else:
    print("not")

