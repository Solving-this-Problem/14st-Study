# 20006_랭킹전대기열_RankingWaiting
import sys
input = sys.stdin.readline

p, m = map(int, input().split())

room = []

for _ in range(p):
    level, name = input().split()
    level = int(level)
    for i in range(len(room)):
        if level-10 <= room[i][0] <= level+10:
            if len(room[i]) < m+1:
                room[i].append((level, name))
                break
    else:
        room.append([level, (level, name)])

# print(room)
for v in room:
    player = v[1:]
    player.sort(key=lambda x: x[1])
    if len(v) == m+1:
        print('Started!')
    else:
        print('Waiting!')
    for p in player:
        print(*p)