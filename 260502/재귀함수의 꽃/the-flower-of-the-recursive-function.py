N = int(input())

# Please write your code here.
def f(l, t, n):
    if t >= n:
        return
    
    print(l[t], end=' ')
    f(l, t+1, n)
    print(l[t], end=' ')



l = [i for i in range(N, 0, -1)]
f(l, 0, N)


    