# Find runner-up from given list
n = int(input())
arr =list(map(int,input().split()))
    
a=max(arr) 
b=arr.count(a)
    
for i in range(b):
    arr.remove(a)
print(max(arr))
