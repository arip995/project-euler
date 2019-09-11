def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime(n):
    x = 0
    prime = 1

    while x < n:
        prime += 1
        if isPrime(prime):
            x += 1
    return prime

print(prime(10001))
