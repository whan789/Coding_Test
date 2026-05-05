import sys
n = int(input())
numbers = list(map(int, input().split()))

max_val = -sys.maxsize-1


# Please write your code here.
for i in range(n):
    total = 0
    for j in range(i+1,n):
        if j == i+1:
            continue
        
        total = numbers[i] + numbers[j]

        max_val = max(total, max_val)

print(max_val)
        