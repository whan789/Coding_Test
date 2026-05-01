n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()

# 1 2 3 5 7 8
m = 0
for i in range(len(nums)):
    l = []
    l.append(nums[i])
    l.append(nums[len(nums)-1-i])
    total = sum(l)
    if total >= m:
        m = total

print(m)
    



