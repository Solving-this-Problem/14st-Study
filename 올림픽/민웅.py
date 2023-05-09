# 8979_올림픽_Olympics
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

q = []
for i in range(1, N+1):
    medal = list(map(int, input().split()))
    q.append(medal)
    if medal[0] == K:
        my_medal = medal


q.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

rank = 1
for i in range(N):
    if q[i][1] > my_medal[1]:
        rank += 1
    elif q[i][1] == my_medal[1] and q[i][2] > my_medal[2]:
        rank += 1
    elif q[i][1] == my_medal[1] and q[i][2] == my_medal[2] and q[i][3]>my_medal[3]:
        rank += 1

print(rank)