#Nithya
n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,len(a)):
    if(i%2==0 and a[i]%2!=0):
        l.append(a[i])
    elif(i%2!=0 and a[i]%2==0):
        l.append(a[i])
print(" ".join(map(str,l)))
