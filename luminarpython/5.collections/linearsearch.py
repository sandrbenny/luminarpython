#lst=(lst[1:])#slicing
lst=[1,2,3,4,5]
element=int(input("enter a element"))
for i in lst:
    if(element==i):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("element found")
else:
    print("element not found")
