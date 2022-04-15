# Find Captain Room Number
k=int(input())
list1=list(map(int,input().split()))

a1=set()
a2=set()
for i in list1:
    if i in a1:
        a2.add(i)
    else:
        a1.add(i)
        
x=a1.difference(a2)
print(*x)
