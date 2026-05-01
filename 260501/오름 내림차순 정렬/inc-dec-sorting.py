n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums_o = sorted(nums)
nums_n = sorted(nums, reverse=True)

for n in nums_o:
    print(n, end=' ')

print('')

for n in nums_n:
    print(n, end=' ')