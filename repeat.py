#Nithya
n=int(input())
a=input().split()
a=[int(i) for i in a]
l=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            l.append(a[i])
        else:
            continue
r=[]
for i in range(0,len(l)):
    if i not in r:
        r.append(l[i])
print(sorted(r))
