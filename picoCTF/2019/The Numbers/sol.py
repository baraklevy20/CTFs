numbers = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

flag = ''
for number in numbers:
    flag += chr(number + ord('A') - 1)

print(f'PICOCTF{{{flag}}}')
