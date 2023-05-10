
N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

sorted_arr = sorted(arr, key=lambda x: (x[1], x[2], x[3]))  # 0번 인덱스 빼고 정렬


for i in range(N):
    if sorted_arr[i][0] == K:   
         print(N - i)   # 등수는 거꾸로
         break
    
    