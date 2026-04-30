n = int(input())

# Please write your code here.
def sol(N):
    sum = 0
    for i in range(1, N+1):
        sum += i

    return sum // 10

print(sol(n))