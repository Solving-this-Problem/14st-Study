# 20006번 랭킹 대기열

import sys
input = sys.stdin.readline

p, m = map(int, input().strip().split())
# 방 리스트
rooms = []
# 방별 레벨 제한(인덱스 활용)
level_range = []
# 방별 인원수
room_count = []
for _ in range(p):
    l, n = input().strip().split()
    l = int(l)
    # 생성된 방이 있으면
    if rooms:
        # 레벨 제한에 안 걸리면서 만원 방이 아니면 들어가기
        for room_id in range(len(level_range)):
            if room_count[room_id] < m and level_range[room_id][0] <= l <=level_range[room_id][1]:
                rooms[room_id] += [(l, n)]
                room_count[room_id] += 1
                break
        else:
            # 알맞는 방이 없으면 생성
            rooms.append([(l, n)])
            level_range.append((l-10, l+10))
            room_count.append(1)
    # 생성된 방이 없으면 생성
    else:
        rooms.append([(l, n)])
        level_range.append((l-10, l+10))
        room_count.append(1)
# 출력
for cnt in range(len(room_count)):
    # 만원이면 Started!
    if room_count[cnt] == m:
        print('Started!')
    # 이 외는 Waiting!
    else:
        print('Waiting!')
    # 닉네임 사전순으로 정렬
    rooms[cnt].sort(key=lambda x:x[1])
    # 방에 있는 인원 리스트 출력
    [print(*room) for room in rooms[cnt]]