#Nithya
n=int(input())
a=input().split()
a=[int(i) for i in a]
for i in a:
    if(a.count(i)==1):
        r=i
print(r)
