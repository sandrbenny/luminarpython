from re import *
pattern='[a-z]'
matcher=finditer(pattern,"abc234AXv")
for match in matcher:
    print(match.start())
    print(match.group())