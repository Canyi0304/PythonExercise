N, L = map(int, input().split())
# 크기 1001 짜리 좌표 리스트 False 로 만들기
coord = [False] * 1001

for i in map(int, input().split()):
    # 구멍이 난 값만 True
    coord[i] = True

answer = 0
x = 0
while x < 1001:
    # coord[x] 가 True 인지 판단
    if coord[x]:
        # 테이프 쓸 경우 answer 에 1추가
        answer += 1
        # 테이프 를 쓸 경우 x 좌표도 L 길이 만큼 점프
        x += L
    else:
        # 구멍이 안난 경우 그냥 1 늘리기
        x += 1

print(answer)


# 좌표 압축
# N, L = map(int, input().split())
# coord = list(map(int, input().split()))
# print(coord)