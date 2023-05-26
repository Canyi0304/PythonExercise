import sys

# 재귀가 1000이상 걸리거 같음 sys.setrecursionlimit 사용
sys.setrecursionlimit(10 ** 6)
# 빠른 input 함수 만들기
input = sys.stdin.readline

N, M = map(int, input().split())

# 인접 행렬 adj
adj = [[0] * N for _ in range(N)]

# M개 만큼 M줄 간선 정보 입력됨
for _ in range(M):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

# for row in adj:
#     print(row)

ans = 0
check = [False] * N


def dfs(now):
    for nxt in range(N):
        # 방문 체크
        if adj[now][nxt] and not check[nxt]:
            check[nxt] = True
            dfs(nxt)


# 배열  True / False 체크
for i in range(N):
    if not check[i]:
        ans += 1
        check[i] = True
        dfs(i)


print(ans)


