from re import *
pattern='[abc]'
matcher=finditer(pattern,"abcpattern")
for match in matcher:
    print(match.start())
    print(match.group())