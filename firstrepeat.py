#Nithya
n=int(input())
a=input().split()
l=[]
for i in range(0,len(a)):
    if a[i] not in l:
        l.append(a[i])
    else:
        r=a[i]
        break
if r==0:
    print('unique')
else:
    print(r)

