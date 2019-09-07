sguare=0
sum=0
result=0
n=101
for i in range(1,n):
    sum = n * (n+1)/ 2
    square = (n * (n + 1) * (2 * n + 1)) / 6
    
    result = sum * sum - square
print(result)
