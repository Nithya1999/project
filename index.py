#Nithya
n=int(input())
a=input().split()
a=[int(i) for i in a]
l=[]
for i in range(0,len(a)):
    if i==a[i]:
        l.append(i)
if(len(l)>0):
    re=" ".join(map(str,l))
    print(re)
else:
    print(-1)
