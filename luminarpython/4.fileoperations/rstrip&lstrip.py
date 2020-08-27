#rstrip is used to remove a character from the end whereas lstrip is used to remove a character from the beginning.
f=open("data","r")
lst=[]
for lines in f:
    print(lines)#my name is sandra
    lst.append(lines)
    print(lines.rstrip("ra"))#my name is sand
    print(lines.lstrip("m"))#y nameis sandra
    print(lst)