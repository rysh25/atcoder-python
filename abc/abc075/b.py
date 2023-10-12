H, W = map(int, input().split())

S: list[str] = []
for _ in range(H):
    S.append(input())

ans: list[list[int]] = [[0] * W for _ in range(H)]

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]



for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue

        for i in range(8):
            nh = h + dy[i]
            nw = w + dx[i]

            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue

            if S[nh][nw] == '#':
                ans[h][w] += 1

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            print('#', end='')
        else:
            print(ans[h][w], end='')
    print()

