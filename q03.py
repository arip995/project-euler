import math

factors = []
n = 600851475143

for i in range(2, math.ceil(math.sqrt(n))):
    while n % i == 0:
        factors.append(i)
        n = n / i

print(factors[-1])