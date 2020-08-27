liness="ABABABCAAA"
dict={}            #created a dictionary
for lines in liness:
    if(lines not in dict): #check whether dictionary contains the word
        dict[lines]=1   #if no such word in dict set dict[words]as 1
    else:
        dict[lines]+=1  #if yes increase count
for key,value in dict.items():#take items from dictionary print as key value pair
    print(key,":",value)

