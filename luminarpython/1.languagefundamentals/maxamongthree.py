n1=int(input("n1"))
n2=int(input("n2"))
n3=int(input("n3"))
if((n1>n2)&n1>n3):
    print(" max is",n1)
elif((n2>n1)&(n2>n3)):
    print("max",n2)
elif((n3>n1)&(n3>n2)):
    print("max",n3)
else:
    print("numbers are equal")
