l=int(input("enter limit:"))

for i in range(0,l):
    for j in range(0,l):
        print(end=" ")
    l=l-1
    for j in range(0,i+1):
        #print(end=" ")
        print("*",end="")
    print()

