maximum = 0   
    
for i in range(100,1000):
    for j in range(100,1000):
        prod = i*j
        temp = prod
        rev=0
        while(prod!=0):
                r = prod % 10
                rev = rev*10+r
                prod=prod//10
        if (temp == rev):
                if(temp>maximum):
                        maximum=temp
                
                
print(maximum)



