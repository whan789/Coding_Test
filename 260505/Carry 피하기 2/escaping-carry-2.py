import sys

n = int(input())
arr = [int(input()) for _ in range(n)]

max_len = len(str(max(arr)))

l = []
for num in arr:
    num = (max_len - len(str(num))) * '0' + str(num)
    l.append(num)

max_val = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            carry = False

            for h in range(max_len):
                if int(l[i][h]) + int(l[j][h]) + int(l[k][h]) >= 10:
                    carry = True
                    break

            if not carry:
                hap = arr[i] + arr[j] + arr[k]
                max_val = max(max_val, hap)

print(max_val)