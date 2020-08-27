f=open("covid19cases","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[0]
    total=data[1]
    cured=data[2]
    death=data[3]
    print(state,"have",death," death cases")
    if(state not in dict):
        dict[state]=total
for k,v in dict.items():
    print(k,"total cases:",v)
    confirmed+=int(v)
    if(int(v)>max):
         max=int(v)
         maxstate=k
    print("state death cases:")
    for k,v in dict2.items():
        print(k,"",v)
        totaldeath



