#Nithya
n=input().split()
a=int(n[0])
b=int(n[1])
arr=list(map(int,input().split()))
arr.sort(reverse=True)
i=b-1
print(arr[i])
