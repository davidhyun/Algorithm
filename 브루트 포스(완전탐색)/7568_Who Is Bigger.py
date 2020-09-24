N = int(input())

wh = []
for _ in range(N):
    x, y = map(int, input().split())
    wh.append((x,y))


rank_list = []; rank=1
for i in range(len(wh)):
    rank=1
    for j in range(len(wh)):
        if wh[i][0] < wh[j][0] and wh[i][1] < wh[j][1]:
            rank += 1
    rank_list.append(rank)
print(*rank_list)
