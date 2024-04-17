#Secret Santa problem

import random
P = ['Fred','Wilma','Barney','Betty','Pebbles','Bam Bam']
ans = []

a = len(P)/2
for i in range(int(a)):
    if len(P) != 2:
        t_1 = P.pop(i)
        t_2 = P.pop(random.randint(0,len(P)-1))
        ans.append([t_1,t_2])
    else:
        ans.append(P)

print(ans)
