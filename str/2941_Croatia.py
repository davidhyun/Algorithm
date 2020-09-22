S = input()

Croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# a = 'ljes=njak'
for x in Croatia_alphabet:
    S = S.replace(x, "A")
print(len(S))