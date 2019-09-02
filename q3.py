maximum=0
def maxa(a):
    if (a>maximum):
        maximum=a
    
    
def primea(b):
    c=1
    for x in range(1,int((b/2)+1)):
        if b%x==0:
            c+=1
    if c==2:
        maxa(b)
        
for i in range(2,int((13195/2+1))):
    if 13195%i==0:
        primea(i)

print(maximum)