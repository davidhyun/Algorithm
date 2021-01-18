import heapq


operations = ['I 16', 'D 1']
heap = []

for command in operations:
    com, num = command.split()
    if com == "I":
        heapq.heappush(heap, (-int(num), int(num))) # max heap

    elif com == "D":
        if num == '1':
            heapq.heappop(heap)
        elif num == '-1':
            ''

test = [1,2,3]
max_heap = []
for n in test:
    heapq.heappush(max_heap, (-n, n))
print(max_heap)
print(heapq.heappop(max_heap))
print(heapq.heappop(max_heap))
print(heapq.heappop(max_heap))