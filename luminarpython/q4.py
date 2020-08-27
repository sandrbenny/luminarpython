string="hello hai hello hai"
word=string.split()
print(word)
dict={}
for words in word:
    #dict[words] = 0
    if(words not in dict):
        dict[words]=1
    else:
        dict[words]+=1
for key,value in dict.items():
    print(key,":",value)