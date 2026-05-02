n = int(input())

# Please write your code here.
def O(n):
    if n==0:
        return
    O(n-1)
    print(n, end = ' ')

def N(n):
    if n==0:
        return
    print(n, end = ' ')
    N(n-1)

O(n)
print()
N(n)