# 10 15
# 5 1 3 5 10 7 4 9 2 8


N, S = map(int, input().split())
arr = list(map(int, input().split()))

head = 0
min = N + 1

for x in arr:
    if x >= S:
        print(1)
        break
else:
    while head < N:
        # if arr[head] >= S:   # 처음부터 넘어가면 1 출력하고 
        #     print(1)
        #     break
        # else:
            tail = head + 1
            sum = arr[head]
            while tail < N:
                sum += arr[tail]
                tail += 1
                if sum >= S:
                    if min > (tail - head):
                        min = (tail - head)
                    break
            if min == 2:
                break
            head += 1
    
        
    
    if min == N + 1:
        print(0)
    else:
        print(min)

