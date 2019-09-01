x=0
z=0
for i in range(1,101):
    z=(i**2)+z
    x+=i
diff=(x**2)-z
print(diff)
