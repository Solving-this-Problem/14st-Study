
N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

sorted_arr = sorted(arr, key=lambda x: (x[1], x[2], x[3]))


for i in range(N):
    if sorted_arr[i][0] == K:
         print(N - i)
         break
    
    