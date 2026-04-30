n, m = map(int, input().split())

# Please write your code here.
def LCM(n,m):
    mul = m * n
    
    while n > 0:
        m, n = n, m%n
    
    lcm = mul // m
    print(lcm)

LCM(n,m)