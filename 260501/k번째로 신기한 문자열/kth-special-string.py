n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
l = []
for word in str:
    if word[:len(t)] == t:
        l.append(word)

l.sort()
print(l[k-1])
        