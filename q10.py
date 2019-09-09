
sum = 0
for i in range(2,2000000):
    c=1
    if i/2!=0:
        for j in range(2, int(i/2) + 1):
            if j/2!=0:
                if i % j == 0:
                    c+=1
                    if c==2:
                        sum += i

print (sum)
