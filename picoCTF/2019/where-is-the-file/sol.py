from pwn import *
import os
import sys
sys.path.append(os.path.abspath("../../.."))
import credentials

sh = ssh(host='2019shell1.picoctf.com',
         user=credentials.username, password=credentials.password).run('sh')
sh.sendline(
    'cd /problems/where-is-the-file_6_8eae99761e71a8a21d3b82ac6cf2a7d0')
sh.interactive()
sh.close()
