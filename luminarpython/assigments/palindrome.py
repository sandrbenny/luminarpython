rem=0
res=0
num=int(input("enter a number"))
temp=num
while(num>0):
    rem=num%10
    res=(res*10)+rem
    num=num//10
print("reverse is:")
print(res)
if(res==temp):
    print("number is palindrome")
else:
    print("number is not palindrome")