import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
INT_MAX = sys.maxsize
min_dis = INT_MAX
total_dis = 0
L = []
for i in range(1, len(points)-1):
    for j in range(len(points)):
        if j !=i:
            L.append((x[j],y[j]))
    
    for k in range(len(L)-1):
        total_dis += abs(L[k+1][0]-L[k][0]) + abs(L[k+1][1]-L[k][1])
    
    if min_dis > total_dis:
        min_dis = total_dis

    L = []
    total_dis = 0
print(min_dis)




    