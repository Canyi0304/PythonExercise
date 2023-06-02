N = int(input())
req = list(map(int,input().split()))
M = int(input())

# lo : 작은값 hi: 높은값 mid: 중간값

lo = 0
hi = max(req)
mid = (lo + hi) // 2
answer = 0


def is_possible(mid):
    return sum(min(r, mid) for r in req) <= M


# 탐색 범위 반복
while lo <= hi:
    # print(f'lo: {lo}, mid: {mid}, hi: {hi}, answer: {answer}')
    # 국가 총 예산 으로 감당이 가능 한지?
    if is_possible(mid):
        # mid 로 가능할 경우 mid 불포함
        lo = mid + 1
        answer = mid
    # 그렇지 않을 경우 상한선 을 낮은 쪽으로 탐색
    else:
        hi = mid - 1

    mid = (lo + hi) // 2
print(answer)
