import heapq as hq

pq = []
hq.heappush(pq,6)
hq.heappush(pq,12)
hq.heappush(pq,0)
hq.heappush(pq,-5)
hq.heappush(pq,8)

print(pq)
while pq:
    print(pq[0])
    hq.heappop(pq)
