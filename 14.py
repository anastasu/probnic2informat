x = (64** 25 + 4**10) - (16**20 + 32**3)
s = ''
while x>0:
    s = str(x%4) + s
    x //= 4
print (s)