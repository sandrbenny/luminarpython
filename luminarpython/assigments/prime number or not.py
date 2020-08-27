#PRIME NUMBER OR NOT
num=int(input("enter a numbr:"))
flag=0
for i  in range(2,num):
    if((num%i)==0):
        flag=1
    else:
        flag=0
if(flag==0):
    print("given number is prime......")
else:
    print("given number is not prime......")

