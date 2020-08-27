def division(num1, num2):
    if (num1 == 0):
        return 0
    if (num2 == 0):
        return INT_MAX
    negresult=0

    if (num1 < 0):
        num1=-num1

        if (num2 < 0):
            num2 = - num2
        else:
            negResult = true

    elif (num2 < 0):
        num2 = - num2
        negResult = true
        quotient = 0

        while (num1 >= num2):
            num1 = num1 - num2
            quotient += 1
        if (negResult):
            quotient = - quotient
            return quotient
num1 = 10;
num2 = 3
print(division(num1, num2))