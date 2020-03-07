import base64

flag = base64.b64decode("bDNhcm5fdGgzX3IwcDM1").decode('UTF-8')
print(f'picoCTF{{{flag}}}')
