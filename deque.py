from collections import deque

dq = deque()
dq.append(123)
dq.appendleft(456)
dq.appendleft(789)

print(dq)
print(dq.pop())
print(dq.popleft())
print(dq)

