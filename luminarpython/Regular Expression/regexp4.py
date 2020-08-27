from re import *
pattern='[A-Z]'
matcher=finditer(pattern,"abc234AXv")
for match in matcher:
    print(match.start())
    print(match.group())