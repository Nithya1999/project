#Nithya
n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]+a[j]==0):
            l.append(a[i])
            l.append(a[j])
            break
        else:
            if(a[i]+a[j]==1):
                l.append(a[i])
                l.append(a[j])
                break
print(" ".join(map(str,l)))
