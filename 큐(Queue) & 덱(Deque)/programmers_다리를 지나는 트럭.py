from collections import deque

# 특정케이스에서 시간초과
def solution(bridge_length, weight, truck_weights):
    time = 0
    crossing_q = deque([0 for _ in range(bridge_length)])
    wating_q = deque(truck_weights)

    while crossing_q:
        time += 1
        crossing_q.popleft()

        if wating_q:
            # 내장함수 sum()의 시간복잡도는 O(n)
            # list.pop(0)의 시간복잡도는 O(n)인 반면 deque.popleft()의 시간복잡도는 O(1)
            if sum(crossing_q) + wating_q[0] <= weight:
                crossing_q.append(wating_q.popleft())
            else:
                crossing_q.append(0)

    return time


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))


##### Class #####
# 위의 코드보다 수행속도가 50배 빠르다
from collections import deque


class Bridge(object):
    DUMMY_TRUCK = 0 # 클래스 변수

    def __init__(self, bridge_length, weight):
        self._bridge_length = bridge_length
        self._max_weight = weight
        self._queue = deque([self.DUMMY_TRUCK for _ in range(bridge_length)])
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._bridge_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def popleft(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution2(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = deque(truck_weights)

    time = 0
    # 대기중인 트럭
    while trucks:
        bridge.popleft()

        if bridge.push(trucks[0]) == True:
            trucks.popleft()
        else:
            bridge.push(0) # DUMMY_TRUCK

        time += 1

    # 다리 위 트럭
    while bridge:
        bridge.popleft()
        time += 1

    return time


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution2(bridge_length, weight, truck_weights))