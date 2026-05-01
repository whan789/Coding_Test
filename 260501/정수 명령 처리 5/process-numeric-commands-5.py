N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
l = []
for c, n in zip(command, num):
    if c == 'push_back':
        l.append(n)
    elif c == 'pop_back':
        l = l[:-1]
    elif c == 'get':
        print(l[n-1])
    else:
        print(len(l))


