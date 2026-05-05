A = input()

# Please write your code here.
cnt = 0

for i in range(0,len(A)):
    if A[i:i+2] == '((':
        
        for j in range(i+2, len(A)):
            if A[j:j+2]=='))':
                cnt+=1

print(cnt)
            
        