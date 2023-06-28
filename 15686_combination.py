from itertools import combinations

N, M = map(int, input().split())
# 좌표의 쌍들을 리스트로 넣어줌
houses = []
chickens = []

for i in range(N):
    # enumerate: 한줄 통째로 입력받음, index & value를 한번에 가져올수 있음
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        if v == 2:
            chickens.append((i, j))


# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|
def get_dist(a, b):
    return abs(a[0] - b[0] + abs(a[1] - b[1]))


# 도시의 치킨 거리의 최솟값
ans = 2 * N * len(houses)

for combi in combinations(chickens, M):
    # 도시 치킨의 거리
    total = 0
    for house in houses:
        total = total + min(get_dist(house, chicken) for chicken in combi)
    ans = min(ans, total)

print(ans)