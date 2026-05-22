n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(n):
    for j in range(i, n):
        sum_val = 0
        cnt_interval = 0
        for k in range(i, j+1):
            sum_val += arr[k]
            cnt_interval+=1
        
        avg_val = sum_val / cnt_interval
        if avg_val in arr[i:j+1]:
            cnt+=1
print(cnt)