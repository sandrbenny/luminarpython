n1=int(input("n1"))
n2=int(input("n2"))
n3=int(input("n3"))
if((n1>n2)&n1>n3):
    if(n2>n3):
        print("secnd is",n2)
    else:
        print("secnd largest",n3)
elif((n2>n1)&(n2>n3)):
    if (n1 > n3):
        print("secnd is", n1)
    else:
        print("secnd largest", n3)
elif((n3>n1)&(n3>n2)):
    if (n1 > n2):
        print("secnd is", n1)
    else:
        print("secnd largest", n2)
else:
    print("numbers are equal")
