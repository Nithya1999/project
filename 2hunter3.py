#Nithya
from itertools import permutations
s=input()
p=permutations(s,len(s))
for i in list(p):
    print("".join(i))
