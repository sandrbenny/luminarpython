from re import *
#pattern='a+'only checks a's occurance
pattern='a*'#checks all occurances
#pattern='a?'# check a and non a.non a position prints
#pattern='a{2}'#two a varunna occurance
#pattern='a{2,3}'  #minimum 2and max 3 occurances of a
count=0
matcher=finditer(pattern,"aaaabbaaabbaab")
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)