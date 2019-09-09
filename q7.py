th=1
i=3
while True:
    if i/2!=0:
        c=1
        k=int(i/2+1)
        for j in range(1,k):
            if i%j==0:
                c+=1
        
        if c==2:
            th+=1
        if th==10001:
            print(i)
            break
        i+=2   


