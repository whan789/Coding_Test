n = int(input())

# Please write your code here.
def sol(n):
    return 'Yes' if n%2==0 and (int(str(n)[0]) + int(str(n)[1])) % 5==0 else 'No'

print(sol(n))