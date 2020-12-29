# 축구 경기장안에서 가장 가까운 터치라인까지의 거리를 구하기
x, y, w, h = map(int, input().split())
distance = [x, y, w-x, h-y]
print(min(distance))