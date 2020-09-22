#alpha = [chr(i+65) for i in range(26)]

alphabet = input()

time = []
for x in alphabet:
    if x == "A" or x == "B" or x == "C":
        time.append(3)
    elif x == "D" or x == "E" or x == "F":
        time.append(4)
    elif x == "G" or x == "H" or x == "I":
        time.append(5)
    elif x == "J" or x == "K" or x == "L":
        time.append(6)
    elif x == "M" or x == "N" or x == "O":
        time.append(7)
    elif x == "P" or x == "Q" or x == "R" or x == "S":
        time.append(8)
    elif x == "T" or x == "U" or x == "V":
        time.append(9)
    elif x == "W" or x == "X" or x == "Y" or x == "Z":
        time.append(10)

print(sum(time))


"""
dial_str = input()
dial_alphabet = [2,2,2, 3,3,3, 4,4,4, 5,5,5, 6,6,6, 7,7,7,7, 8,8,8, 9,9,9,9]

time = 0
for chr in dial_str:
    i = ord(chr) - ord("A") # U = 20
    time += dial_alphabet[i] + 1
print(time)
"""
