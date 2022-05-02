f = open('26-59.txt')
colstr = int(f.readline())
numb = 0
for i in range(colstr):
    busy = list(f.readline())
    numb += busy
print (numb)