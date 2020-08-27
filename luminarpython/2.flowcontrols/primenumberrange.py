lowlimit=int(input("enter a number"))
uplimit=int(input("enter a number"))
for i in range(lowlimit,uplimit+1):
    for j in (2,i):
        if(i%j==0):
            break
        else:
            print(i,end="\n")