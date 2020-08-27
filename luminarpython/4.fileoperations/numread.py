f=open("numbers","r")
#for lines in f:
    #print(lines)

lst=[]
for lines in f:
    lst.append(int(lines.rstrip("\n")))
    #lst.append(int(lines.rstrip("/n")))#rstrip is used to remove a character from the end .
print(lst)