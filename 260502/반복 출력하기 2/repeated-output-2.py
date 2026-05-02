n = int(input())

# Please write your code here.
def sol(n):
    if n==0:
        return
    sol(n-1)
    print('HelloWorld')

sol(n)