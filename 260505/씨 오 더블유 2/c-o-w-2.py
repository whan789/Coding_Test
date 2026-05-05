n = int(input())
S = input()

# Please write your code here.
cnt = 0
for i in range(0,n):
    if S[i] == 'C':
        for j in range(i+1, n):
            if S[j] == 'O':
                for h in range(j+1,n):
                    if S[h] == 'W':
                        cnt+=1
print(cnt)
