#function with return value
def fact(i):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    return fact
data=fact(5)
print(data)

