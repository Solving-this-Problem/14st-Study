# 정렬 오
p, m = map(int, input().split())

rooms = [set() for _ in range(p//2+1)]
rooms[0].add(tuple(input().split())) # 맨 처음친구 첫번째 방에 넣기

for i in range(1, p):
    level, nick = input().split()
    for j in range(len(rooms)):
        # 해당 방에 인원이 존재하지 않는 경우
        if not rooms[j]:
            rooms[j].add((level, nick))
            break
        # 해당 방의 첫 번째 인원과 level 차이가 10 이하인 경우
        else:
            first_player = sorted(list(rooms[j]), key=lambda x: int(x[0]))[0]
            if abs(int(level)-int(first_player[0])) <= 10:
                # 해당 방의 인원이 m명 이하인 경우
                if len(rooms[j]) < m:
                    rooms[j].add((level, nick))
                    break
    # 모든 방에 인원이 m명 있는 경우
    else:
        rooms.append(set())
        # rooms[-1] -> 방 목록에서 가장 최근에 추가된 방
        rooms[-1].add((level, nick))

for i in range(len(rooms)):
    players = sorted(list(rooms[i]), key=lambda x: int(x[0]))
    if len(players) == 0:  # 방이 비어있는 경우 출력하지 않음
        continue
    print('Started!' if len(rooms[i]) == m else 'Waiting!')
    for player in players:
        print(player[0], player[1]) # player[0]은 레벨을 나타내고, player[1]은 아이디