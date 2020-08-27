num=int(input("enter limit:"))
f1=0
f2=1
print(f1)
print(f2)
for i in range(0,num-2):
    f=f1+f2
    print(f)
    f1=f2
    f2=f
    i+=1