import heapq as hq
import sys

num = sys.stdin.readline
pq = []
for _ in range(int(num())):
    x = int(num())
    if x:
        hq.heappush(pq, (abs(x), x))
    else:
        print(hq.heappop(pq)[1] if pq else 0)


