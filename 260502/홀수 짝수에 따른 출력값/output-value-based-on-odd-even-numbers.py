N = int(input())

# Please write your code here.
def f(n):
    if n==1:
        return 1
    if n==2:
        return 2

    if n%2!=0:
        return f(n-2) + n
    else:
        return f(n-2) + n

print(f(N))
