p, m = map(int, input().split())
room = [[] for _ in range(p)]
i = 0
for k in range(p):
    arr = input().split()
    level, n = int(arr[0]), arr[1]
    if k == 0:
        room[0].append((level, n))
    else:
        while room[i]: 
            if room[i][0][0] - 10 <= level <= room[i][0][0] + 10 and len(room[i]) < m:
                room[i].append((level, n))
                break
            else: 
                i += 1
        else:
            room[i].append((level, n))
        i = 0


for i in range(p):
    if room[i]:
        sorted_room = sorted(room[i], key=lambda x: x[1])
        if len(sorted_room) == m:
            print('Started!')
        else:
            print('Waiting!')
        for x in sorted_room:
                print(*x)