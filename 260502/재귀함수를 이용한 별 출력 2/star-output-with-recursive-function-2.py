n = int(input())

# Please write your code here.
def f(s, n):
    if s >= n:
        return

    print('* ' * (n-s), end = ' ')
    print()
    f(s+1, n)
    print('* ' * (n-s), end=' ')
    print()
    
f(0, n)
