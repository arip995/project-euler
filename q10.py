
sum = 0
for i in range(2, 10):
    c=1
    for j in range(2, int(i/2) + 1):
        if i % j == 0:
            c+=1
            if c==2:
                sum += i

print (sum)