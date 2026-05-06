N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
L= []
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if k==i and l==j:
                        continue
                    if k>=0 and k <=N-1 and l>=0 and l<=M-1:
                        if arr[k][l] == 'E':
                            for m in range(k-1,k+2):
                                for n in range(l-1,l+2):
                                    if m==k and n==l:
                                        continue
                                    if m>=0 and m<=N-1 and n>=0 and n<=M-1:
                                        if arr[m][n]=='E':
                                            L.append([(i,j),(k,l),(m,n)])

cnt = 0
for l in L:
    result = True
    if (l[1][0]-l[0][0]) != (l[2][0]-l[1][0]) or (l[1][1]-l[0][1]) != (l[2][1]-l[1][1]):
        result = False
    
    if result:
        cnt+=1

print(cnt)

        
        
        
        

