import sys

min_dis = sys.maxsize

n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
for i in range(0, n):
    dis = 0
    idx = 0
    
    for j in range(i, n+i):
        dis = dis + a[j%n] * idx
        idx +=1

    
    min_dis = min(dis, min_dis)

print(min_dis)
        
        
        