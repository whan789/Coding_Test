n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(1, len(arr)):
    key = arr[i]
    for j in range(i-1, -1, -1):
        if key < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = key

for num in arr:
    print(num, end=' ')