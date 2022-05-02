for i in range (1,10000):
    x = i
    s = 0
    while x > 0:
        s = s + x % 9
        x = x // 3
    if s == 17:
        print (i)