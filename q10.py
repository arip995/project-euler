def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
for i in range(3, 2000000,2):
    if isPrime(i):
        sum += i

print (sum+2)
