#Nithya
from itertools import combinations
n=int(input())
a=list(map(int,input().split()))
c=combinations(a,3)
l=[]
for i in list(c):
    l.append(i)
for i in range(0,len(l)):
    l[i]=list(l[i])
for i in range(0,len(l)):
    if(l[i][0]+l[i][1]==l[i][-1]):
        print(" ".join(map(str,l[i])))
