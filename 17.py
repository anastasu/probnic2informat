f = open ('17-204.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))
k = 0
m = 0
for i in range (len(a)-3):
    if (a[i]<0 and a[i]%10!=9 ) and (a[i+1 >0 and a[i+1]%10 == 9]) and (a[i+3]<0 and a[i+3]%10!=9 ):
        k +=1
        if (a[i]+a[i+1]+a[i+3])>m:
            m = a[i]+a[i+1]+a[i+3]
print (k,m)
