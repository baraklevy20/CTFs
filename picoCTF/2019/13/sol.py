crypt = 'cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}'
x = []
y = []
for i in range(26):
    x.append(chr(ord('A') + i))
    x.append(chr(ord('a') + i))
    y.append(chr(ord('A') + ((i + 13) % 26)))
    y.append(chr(ord('a') + ((i + 13) % 26)))
rot13 = str.maketrans(str(x), str(y))
flag = str.translate(crypt, rot13)
print(flag)
