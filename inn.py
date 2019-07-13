#Nithya
n=input().split()
a=input().split()
b=input().split()
l=[]
for i in a:
    if i in b:
        l.append(i)
if(len(b)==len(l)):
    print('YES')
else:
    print('NO')
