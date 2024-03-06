Factorial = int(input('Enter your number ? '))

Sum1 = 1
Sum2 = 0

for i in range(Factorial, 0, -1):
    Sum1 *= i
    Sum2 += i

print(Sum1, Sum2)

Sum1 = 1
if Factorial % 2 == 0:
    Sum1 += (Factorial - 1) // 2
    print(Sum1)
