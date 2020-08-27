from re import *
f=open('mobno','r')
lst=[]
rule='\d{10}'
for lines in f:
    mobno=lines.rstrip("\n")
    matcher=fullmatch(rule,mobno)
    if(matcher!=None):


        lst.append(mobno)

    else:
        pass
f1=open('mobno1','w')
for item in lst:
    f1.write("%s\n" % item)
    #f1.write(item)
f1=open('mobno1','r')
print("output file...........")
for data in f1:
    print(data)




