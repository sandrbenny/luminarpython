#print all even numbers fromgiven limit
low=int(input("enterlowerlimit"))
limit=int(input("enter limit"))
while(low<=limit):
    if((low%2)==0):
        print(low)
    low+=1
