# 탐욕 알고리즘(Greedy)

### (0) 정의

> 탐욕 알고리즘은 **최적해에 가까운 값을 구하기 위해 사용**되는 근사적인 방법으로, 여러 경우 중 하나를 결정해야할 때마다 **그 순간에 최적이라고 생각되는 것을 선택**해나가서 최종적인 해답에 도달하는 알고리즘.

<br>

### (1) 탐욕 알고리즘 예

#### (i) 동전문제

> 지불해야하는 값이 4720원일 때 1원/50원/100원/500원 동전으로 동전의 수가 가장 적게 지불하시오.
>
> - 가장 큰 동전부터 최대한 지불해야 하는 값을 채우는 방식으로 구현 가능
> - 탐욕 알고리즘으로 매순간 최적이라고 생각되는 경우를 선택하면됨

```python
def min_coin_count(cost, coin_list):
    total_coin_count = 0
    details = []
    coin_list.sort(reverse=True)


    for coin in coin_list:
        coin_num = cost // coin
        total_coin_count += coin_num
        cost %= coin
        details.append([coin, coin_num])

    return total_coin_count, details


coin_list = [1, 50, 100, 500]
total_coin_count, details = min_coin_count(4720, coin_list)
```

<br>

#### (ii) 부분 배낭 문제 (Fractional Knapsack Problem)

> 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
>
> - 각 물건은 무게(w)와 가치(v)로 표현될 수 있음
> - 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음(Fractional Knapsack Problem)
>   - 반대로 물건을 쪼개서 넣을 수 없는 배낭 문제도 존재함(0/1 Knapsack Problem)

|         | 물건1 | 물건2 | 물건3 | 물건4 | 물건5 |
| ------- | ----- | ----- | ----- | ----- | ----- |
| 무게(w) | 10    | 15    | 20    | 25    | 30    |
| 가치(v) | 10    | 12    | 10    | 8     | 5     |

```python
def get_max_value(data_list, capacity):
    # 무게당 가치(1000원/1kg)가 큰 순으로 정렬
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = []

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]  # 무게당 가치가 가장 큰 물건을 쪼개 넣음
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break

    return total_value, details


data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
total_value, details = get_max_value(data_list, 30)
```

<br>

### (2) 탐욕 알고리즘의 한계

- 탐욕 알고리즘은 **근사치 추정**에 활용
- **반드시 최적의 해를 구할 수 있는 것은 아님**
- 최적해에 가까운 값을 구하는 방법 중 하나일 뿐