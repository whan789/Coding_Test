n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# 1. 사진 크기(k)와 상관없이, 안쪽 j 루프가 사람의 최대 위치까지 안전하게 접근할 수 있도록
# 배열 크기를 넉넉하게 '최대 위치 + k' 만큼 잡아줍니다.
max_x = max(x)
placed = [0] * (max_x + k + 1)

for pos, char in zip(x, c):
    placed[pos] = char

max_score = 0

# 2. 사진의 시작점 i를 0번(또는 1번)부터 '사람이 존재하는 마지막 위치'까지 전부 이동시킵니다.
# 이렇게 하면 시작점이 어디든, 그 지점부터 k칸을 정상적으로 탐색합니다.
for i in range(0, max_x + 1):
    hap = 0
    for j in range(i, i + k + 1):
        if placed[j] == 'G':
            hap += 1
        elif placed[j] == 'H':
            hap += 2

    max_score = max(hap, max_score)

print(max_score)