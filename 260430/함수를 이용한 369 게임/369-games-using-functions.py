a, b = map(int, input().split())

# Please write your code here.
def sol1(N):
    return any(char in str(N) for char in '369')
    

def sol2(N):
    return N % 3 ==0 or sol1(N)

cnt = 0
for i in range(a, b+1):
    if sol2(i):
        cnt+=1
print(cnt)



        