lst=[1,2,7,3,2]
list=[]
lst.sort()
print(lst)
for i in lst:
    list.append(i)
print(list)
l=len(list)
print(l)
flag=0
for i in lst:
    if i  not in lst :
            flag=1
            break
    else:
        flag=0
if(flag==0):
            print("duplicate not found")
else:
    print("found")

