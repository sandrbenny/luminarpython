#find count of each word in a file.how muny repetitions.
f=open("word","r")#open file word
dict={}            #created a dictionary
for lines in f:
    print(lines)    #print file data
    word=lines.split(" ")#split sentence where there is a space
    print(word)      #print after splitting
    break
for words in word:  #from that sentence or data
    #dict[words] = 0
    if(words not in dict): #check whether dictionary contains the word
        dict[words]=1   #if no such word in dict set dict[words]as 1
    else:
        dict[words]+=1  #if yes increase count
for key,value in dict.items():#take items from dictionary print as key value pair
    print(key,":",value)

