a = input()
A = list(a)
max_num = 0
total = 0
# Please write your code here.
for i in range(len(A)):
    if A[i]== "1":
        A[i] = "0"
    else:
        A[i] = "1"

    for j in range(len(A)):
        total = total * 2 + int(A[j])
    
    if total > max_num:
        max_num = total
    A = list(a)
    total = 0

print(max_num)


