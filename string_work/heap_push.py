from heapq import heappush as insert, heappop as extract_maximum
pq = []

insert(pq, 4)

insert(pq, 2)
insert(pq, 3)
insert(pq, 1)

print(extract_maximum(pq))
print(extract_maximum(pq))
print(extract_maximum(pq))
print(extract_maximum(pq))

