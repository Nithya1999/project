#Nithya
n=input().split()
x=n[0]
y=n[1]
u=0
if len(y)>len(x):
    c=len(y)-len(x)
for i in range(0,len(x)):
        if(len(y)==1 and y[i] in x):
            break
        else:
            u=u+1
            break        
print(c+u)
        
        
