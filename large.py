#Nithya
n=int(input())
a=input().split()
a=[int(i) for i in a]
a.sort(reverse=True)
b=int("".join(map(str, a))) 
print(b)
