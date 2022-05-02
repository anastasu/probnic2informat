s = 20 * '2' + 15 * '3' + 10 *'4'
max = 0
for i in s:
   while '42' in s or '32' in s:
      if '42' in s:
         s = s.replace('42','51',1)
      else:
         s = s.replace('32', '61', 1)
a = [int (i) for i in s]
if sum(a) > max: max = sum (a)
print (max)