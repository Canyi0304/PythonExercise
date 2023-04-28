# import time
#
# # 첫 번째 코드
# start_time = time.time()
#
# num = int(input())
# cards = list(range(1, num+1))
#
# while len(cards) > 1:
#     cards.pop(0)
#     cards.append(cards.pop(0))
#
# print(cards[0])
#
# end_time = time.time()
#
# print("첫 번째 코드 실행 시간: ", end_time - start_time)

from collections import deque
import time
# 두 번째 코드
start_time = time.time()

num = int(input())
cards = range(1, num + 1)
dq = deque(cards)

while len(dq) > 1:
    dq. popleft()
    dq.append(dq.popleft())

print(dq.popleft())

end_time = time.time()
print("두 번째 코드 실행 시간: ", end_time - start_time)
