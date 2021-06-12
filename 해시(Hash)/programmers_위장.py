clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

from collections import Counter


clothes_dict = {}
for value, key in clothes:
    clothes_dict.setdefault(key, []).append(value)

print(clothes_dict)
print([category for _, category in clothes])

print('*' * 20)


counter_each_category = Counter([category for _, category in clothes])
print(counter_each_category)
all_possible = 1

for key in counter_each_category:
    all_possible *= (counter_each_category[key] + 1)

print(all_possible - 1)