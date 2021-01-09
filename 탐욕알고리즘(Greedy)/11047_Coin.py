import sys


def min_coin_count(coin_list, cost):
    # 동전가치가 큰 순으로 정렬
    coin_list = sorted(coin_list, reverse=True)
    total_coin_num = 0
    details = []

    for coin in coin_list:
        coin_num = cost // coin             # 해당 동전 개수
        total_coin_num += coin_num          # 총 동전 개수
        cost %= coin                        # 남은 금액
        details.append([coin, coin_num])    # 동전 명세서

    return total_coin_num


N, K = map(int, sys.stdin.readline().split())
coin_list = []
for _ in range(N):
    coin = int(sys.stdin.readline())
    coin_list.append(coin)

print(min_coin_count(coin_list, K))