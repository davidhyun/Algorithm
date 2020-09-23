S = input()
string = S.upper()

ALPHABET = [chr(i+65) for i in range(26)]
cnt_alphabet = []
for X in ALPHABET:
    cnt_alphabet.append(string.count(X))
#print(cnt_alphabet)

if cnt_alphabet.count(max(cnt_alphabet)) >= 2:
    print("?")
else:
    print(ALPHABET[cnt_alphabet.index(max(cnt_alphabet))])

"""
# Count 함수기능
for s in S:
    alpha[ord(s) - ord("A")] += 1
"""

