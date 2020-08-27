from re import *
f=open('regno','r')
lst=[]
rule='[Kk][Ll][0-9]{2}[a-z]{1,2}\d{4}'
for lines in f:
    regno=lines.rstrip("\n")
    matcher=fullmatch(rule,regno)
    if(matcher!=None):


        lst.append(regno)

    else:
        pass
#print("lst:",lst)
f1=open('regno1','w')
for item in lst:
    f1.write("%s\n" % item)#line by line output
    #f1.write(item)
f1=open('regno1','r')
print("output file...........")
for data in f1:
    print(data)




