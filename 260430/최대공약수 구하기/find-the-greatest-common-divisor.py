n, m = map(int, input().split())

# Please write your code here.
def solution(n, m):
    while n > 0:
        m, n = n, m % n
    print(m)

solution(n, m)