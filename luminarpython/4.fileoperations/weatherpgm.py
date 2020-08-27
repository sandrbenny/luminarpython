#compare temperature in two days in kerala
f=open("temperture","r")
dict={}
for lines in f:
    data=lines.rstrip("/n").split(",")
    district=data[0]
    temp=data[1]
    if(district not in dict):
        #print("not available")
        dict[district]=temp
    else:
        old=dict[district]
        if(temp>old):
            dict[district]=temp
for k,v in dict.items():
    print(k,v)

print(dict.items())





