board = [list(map(int, input().split())) for _ in range(19)]

dxs = [0, 1, 1, 1]
dys = [1, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

def win(n):
    for i in range(19):
        for j in range(19):

            if board[i][j] != n:
                continue

            for dx, dy in zip(dxs, dys):
                cnt = 1
                stones = [(i, j)]

                curx = i
                cury = j

                while True:
                    nx = curx + dx
                    ny = cury + dy

                    if not in_range(nx, ny):
                        break

                    if board[nx][ny] != n:
                        break

                    cnt += 1
                    stones.append((nx, ny))

                    curx = nx
                    cury = ny

                if cnt == 5:
                    return n, stones

    return None

res1 = win(1)
res2 = win(2)

if res1:
    print(res1[0])
    print(res1[1][2][0] + 1, res1[1][2][1] + 1)
elif res2:
    print(res2[0])
    print(res2[1][2][0] + 1, res2[1][2][1] + 1)
else:
    print(0)