#1806 부분합
import sys
input = sys.stdin.readline
N, S = map(int, input().strip().split())
arr = list(map(int,input().strip().split()))
# 투 포인터 설정
left = right = 0
# 최소값 설정
minV = 100001
# 누적 합
total = arr[0]

while right<= N:
    # 누적 합이 작으면 오른쪽 수를 더함
    if total < S:
        right += 1
        # 인덱스를 넘어가면 멈춤
        if right == N: break
        total += arr[right]
        # print(total, minV)
    # 누적합이 크거나 같으면 왼쪽 수를 빼서 다른 경우의 수도 확인
    else:
        minV = min(minV, right-left+1)
        total -= arr[left]
        left += 1
    #     print(total, minV)
    # print('left = ', left, 'right = ', right)
# 최소값 갱신이 안 되어있으면 0
print(minV if minV != 100001 else 0) 
