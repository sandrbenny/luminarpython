lst=[x,y,z]


dict={}
for letter in lst:
    data=letter.split(",")
    print(int(data))
    x=x
    y=y
    z=z

dict[x]=y
dict[y]=z
dict[z]=x
print(dict.items())

    #print(key)