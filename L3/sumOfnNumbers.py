def sumOfNumber(n):
    if n == 1 or n == 0:
        return n
    else:
        return n + sumOfNumber(n-1)

print(sumOfNumber(6))
# print(sumOfNumber(9))