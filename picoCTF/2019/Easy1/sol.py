key = 'SOLVECRYPTO'
crypt = 'UFJKXQZQUNB'

flag = ''
for i in range(len(crypt)):
    flag += (chr((ord(crypt[i]) - ord(key[i])) % 26 + ord('A')))

print(f'picoCTF{{{flag}}}')
