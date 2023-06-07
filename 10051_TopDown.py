import sys

MOD = 10007
# Traceback (most recent call last):
sys.setrecursionlimit((10 ** 7))

cache = [[0] * 1001 for _ in range(1001)]
N, K = map(int, input().split())


def bino(n, k):
    if cache[n][k]:
        return cache[n][k]

    if k == 0 or k == n:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n - 1, k - 1) + bino(n - 1, k)
        # cache[n][k]의 값이 10007미만 초과 방지
        cache[n][k] %= MOD
    return cache[n][k]


print(bino(N, K))
