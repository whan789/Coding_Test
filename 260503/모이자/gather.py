n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
result = []
total = 0
for i in range(n):
    for j in range(n):
        total += A[j]*abs(i-j)
    result.append(total)
    total = 0
print(min(result))
