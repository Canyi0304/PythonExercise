# 메모리 2초 초과
# num = int(input())
# cards = list(range(1, num+1))
#
# while len(cards) > 1:
#     cards.pop(0)
#
#     cards.append(cards.pop(0))
#
# print(cards[0])

# 메모리 초과
# from collections import deque
#
# num = int(input())
# cards = range(1, num+1)
# dq = deque(cards)
#
# # 카드가 1장 이상일 경우 첫번째 배열 삭제 & 삭제후 첫번째 배열을 마지막 배열에 추가
# while len(dq) > 1:
#     dq.popleft()
#     dq.append(dq.popleft())
#     # print(dq)
#
# card_string = ' '.join(map(str, dq))
# print(card_string[0])

from collections import deque

# 카드 갯수 입력 > 입력한 카드 세트 만들기 > 카드 세트 deque 에 추가
num = int(input())
cards = range(1, num + 1)
dq = deque(cards)

# 카드가 1장 이상일 경우 >  첫번째 배열 삭제 > 삭제후 첫번째 배열을 마지막 배열에 추가
while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
    # print(dq)

# dq 마지막 값 출력
print(dq.popleft())








