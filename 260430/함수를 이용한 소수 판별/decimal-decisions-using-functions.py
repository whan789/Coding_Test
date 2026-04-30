a, b = map(int, input().split())

# Please write your code here.
def prime(N):
    for i in range(2,N-1):
        if N % i == 0:
            return False
    return True

total = 0

for i in range(a, b+1):
    if prime(i):
        total +=i
    
print(total)