# 완!
max_score = 1
lion = [0] * 11
visited = [0] * 11
ans = []

def backtracking(arrow, N, score, info, count):
    global max_score, lion, ans
    if arrow == N:
        apeach = 0
        for i in range(11):
            if info[i] and info[i] >= lion[i]:
                apeach += (10-i)
        if max_score < score-apeach:
            max_score = score-apeach
            ans = lion.copy()
        elif max_score == score-apeach:
            ans = lion.copy()
        return
    if count == 11:
        return 
    for i in range(11):
        if not visited[i]:
            if N-arrow > info[i]:
                visited[i] = 1
                lion[i] = info[i] + 1
                backtracking(arrow+lion[i], N, score+(10-i), info, count + 1)
                lion[i] = 0
                visited[i] = 0
            else:
                visited[i] = 1
                lion[i] = N-arrow
                backtracking(arrow+lion[i], N, score, info, i)
                lion[i] = 0
                visited[i] = 0


def solution(n, info):
    global max_score, lion, ans
    if n == 1 and info[0]:
        return [-1]

    
    backtracking(0, n, 0, info, 0)
    if max_score == 1:
        ans =[-1]
    return ans