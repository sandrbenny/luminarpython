#used for pattern matching
#step 1 to import re module
import re#or from re import *
#finditer is the function to find how  many ab pattern is there in ababababbbbbaaaaabbbbb
pattern=re.finditer("ab","ababababbbbbbaaaaabababbbb")
count=0
for match in pattern:
    print(match.start())#which position
    print(match.group())#match with which object
    count+=1
print(count)