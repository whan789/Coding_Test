n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(0, len(arr)-1):
    for j in range(0, len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for num in arr:
    print(num, end=' ')