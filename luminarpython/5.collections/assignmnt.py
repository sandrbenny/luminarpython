#list=[3,5,8]output should be[13,11,8]
lst=[3,5,8]
outlist=[]
F=0
for i in lst:
    index=lst.index(i)#i=0
    if(index==0):
        f=lst[1]+lst[2]#5+8=13
        outlist.append(f)8,
    elif (index==1):#i=1
        f = lst[0]+lst[2]#3+5=8
        outlist.append(f)
    elif (index==2):
        f = lst[0]+lst[1]
        outlist.append(f)
    else:
        break
print(outlist)



