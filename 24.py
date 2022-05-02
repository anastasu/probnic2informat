f = open ('24-179.txt')
s = f.read()

#f = open ('24-179.txt')
#f_c = f.read()
#s = f_c.split('\n')
k1 =0
k2 =0
k3= 0
for i in range(len(s)-4):
    sk = s[i]+ s[i+1] + s[i+2] +s[i+3] +s[i+4]
    if sk == 'CBCBC': k1+=1
    if sk == 'CBDBC': k2+=1
    if sk == 'CBEBC': k3+=1
print(k1,k2,k3,k1+k2+k3)