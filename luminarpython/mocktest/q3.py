def divide(dividend, divisor):

  if ((dividend < 0)^(divisor < 0)):
    sign=-1
  else:
    sign=1
    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1

    return sign * quotient
a = 10
b = 3
answer=divide(a, b)
print("10/3=",answer)