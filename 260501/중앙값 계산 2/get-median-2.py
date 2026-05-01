n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
l = []

for i in range(0,len(arr),2):
    a = sorted(arr[:i+1])
    l.append(a[len(a)//2])

for num in l:
    print(num, end=' ')
    

    
