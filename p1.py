Factorial = int(input('Enter your number ? '))

Sum1 = 1
Sum2 = 0

for i in range(Factorial, 0, -1):
    Sum1 *= i
    Sum2 += i

print(Sum1, Sum2)