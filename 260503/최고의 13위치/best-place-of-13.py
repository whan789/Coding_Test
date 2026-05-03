n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max = 0
cnt = 0
for i in range(n):
    for j in range(n-2):
        for k in range(3):
            if grid[i][j+k]==1:
                cnt+=1
        if cnt > max:
            max = cnt
        cnt=0

print(max)
        
        
        