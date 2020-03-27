import pwn

with open("whitepages.txt", "rb") as file:
    data = file.read()
    data = data.replace(b'\xe2\x80\x83', b'0')
    data = data.replace(b'\x20', b'1')
    data = data.decode("ascii")
    print(pwn.unbits(data).decode("ascii"))