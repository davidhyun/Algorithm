# (1) 1
# (6) 2 3 4 5 6 7
# (12) 8 9 10 11 12 13 14 15 16 17 18 19
# (18) 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
# (24) 38 39 40 41 ...

N = int(input())

i = 1
room_last_num = 1
room_size = 6
if N == 1:
    print(1)
else:
    while True:
        i += 1
        room_last_num += room_size
        if N <= room_last_num:
            print(i)
            break
        room_size += 6
