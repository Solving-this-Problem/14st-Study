p, m = map(int, input().split())
room = [[] for _ in range(p)]
i = 0
for k in range(p):      
    arr = input().split()
    level, n = int(arr[0]), arr[1]  
    if k == 0:                      # 처음에는 무조건 넣어주고 시작
        room[0].append((level, n))
    else:
        while room[i]:  
            # 레벨 +- 10 사이이고, m보다 작은 방이면 검사하고 추가
            if room[i][0][0] - 10 <= level <= room[i][0][0] + 10 and len(room[i]) < m:
                room[i].append((level, n))
                break
            else: 
                i += 1
        else:           # 채워져있는 room 다 돌았는데 들어가지 못했으면 빈 방에 바로 추가
            room[i].append((level, n))
        i = 0


for i in range(p):
    if room[i]:
        sorted_room = sorted(room[i], key=lambda x: x[1])   # 닉네임 기준으로 정렬
        if len(sorted_room) == m:
            print('Started!')
        else:
            print('Waiting!')
        for x in sorted_room:
                print(*x)