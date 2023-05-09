def ranking(n, k, medals):
    target_country_medals = medals[k - 1]
    rank = 1

    for i in range(n):
        if i == k - 1:  # target_country가 자기 자신인 경우
            continue
        if medals[i][0] > target_country_medals[0]:
            rank += 1
        elif medals[i][0] == target_country_medals[0]:
            if medals[i][1] > target_country_medals[1]:
                rank += 1
            elif medals[i][1] == target_country_medals[1]:
                if medals[i][2] > target_country_medals[2]:
                    rank += 1

    return rank


n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]

print(ranking(n, k, medals))