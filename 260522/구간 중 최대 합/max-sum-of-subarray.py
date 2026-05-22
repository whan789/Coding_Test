n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_hap = 0
for i in range(n-k+1):
    hap = 0
    for j in range(i, i+k):
        hap += arr[j]
    max_hap = max(max_hap, hap)

print(max_hap)