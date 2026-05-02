N = int(input())

# Please write your code here.
def f(cnt, n):
    if n == 1:
        return cnt
    
    if n % 2 ==0:
        cnt +=1
        return f(cnt,n//2)
    if n % 2 !=0:
        cnt+=1 
        return f(cnt, n//3)

print(f(0, N))
        