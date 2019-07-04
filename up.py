n=input().split()
x=n[0]
y=n[1]
if len(y)>=len(x):
    c=len(y)-len(x)
for i in range(0,len(x)):
        if y in x:
            break
        elif(x[i]!=y[i]):
            c=c+1
            break        
print(c)
        
        
