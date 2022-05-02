n = 1
for i in range (1,10000):
    s=i
    while s > 200:
        s = s - 15
        n = n + 3
    if n == 46:
        print (i)