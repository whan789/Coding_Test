n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
def sol(A,B):
    A.sort()
    B.sort()
    cnt = 0
    for a,b in zip(A,B):
        if a!=b:
            cnt+=1
    
    return 'Yes' if cnt==0 else 'No'

print(sol(A,B))